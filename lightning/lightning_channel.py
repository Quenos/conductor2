# Copyright 2018 <Quenos Blockchain R&D KFT>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from lightning import lndAL
from collections import defaultdict
from enum import Enum


class HTLC(object):
    def __init__(self, channel_htlc):
        self.incoming = channel_htlc.incoming
        self.amount = channel_htlc.amount
        self.hash_lock = channel_htlc.hash_lock
        self.expiration_height = channel_htlc.expiration_height


class Channel(object):

    class ChannelState(Enum):
        ACTIVE = 1
        INACTIVE = 2
        CLOSED = 3

        def __str__(self):
            return self.name

    def __init__(self, channel=None):
        self.remote_pubkey = channel.remote_pubkey
        self.channel_point = Channel.create_channel_point(channel.channel_point)
        self.chan_id = channel.chan_id
        self.capacity = channel.capacity
        try:
            remote_node_info = lndAL.LndAL.get_node_info(self.remote_pubkey)
            self.remote_node_alias = remote_node_info.node.alias
            self.remote_node_colour = remote_node_info.node.color
            self.remote_uri = "Unknown"
            for x in remote_node_info.node.addresses:
                self.remote_uri = x.addr
        except Exception as ex:
            if ex.__str__()[:12] == "<_Rendezvous":
                self.remote_node_alias = "Unknown"
                self.remote_node_colour = 0x000000
            else:
                raise ex
        self.channel_type = ""

    def __eq__(self, other):
        return self.chan_id == other.chan_id

    def update_channel(self, channel):
        self.remote_pubkey = channel.remote_pubkey
        self.channel_point = Channel.create_channel_point(channel.channel_point)
        self.chan_id = channel.chan_id
        self.capacity = channel.capacity
        self.remote_node_alias = lndAL.LndAL.get_node_info(self.remote_pubkey).node.alias

    @staticmethod
    def create_channel_point(channel_point):
        cp = {'funding_txid_str': channel_point[:channel_point.find(':')],
              'output_index': int(channel_point[channel_point.find(':')+1:])}
        return cp

    @staticmethod
    def factory(channel_type, channel):
        if channel_type == "open_channel":
            return OpenChannel(channel)
        if channel_type == "closed_channel":
            return ClosedChannel(channel)
        assert 0, "Bad channel creation: " + channel_type


class OpenChannel(Channel):
    def __init__(self, channel):
        super(OpenChannel, self).__init__(channel)
        self.channel_type = "open_channel"
        if channel.active:
            self.channel_state = self.ChannelState.ACTIVE
        else:
            self.channel_state = self.ChannelState.INACTIVE
        self.local_balance = channel.local_balance
        self.remote_balance = channel.remote_balance
        self.commit_fee = channel.commit_fee
        self.commit_weight = channel.commit_weight
        self.fee_per_kw = channel.fee_per_kw
        self.unsettled_balance = channel.unsettled_balance
        self.total_satoshis_sent = channel.total_satoshis_sent
        self.total_satoshis_received = channel.total_satoshis_received
        self.num_updates = channel.num_updates
        self.pending_htlcs = []
        for htlc in channel.pending_htlcs:
            self.pending_htlcs.append(htlc)
        self.csv_delay = channel.csv_delay
        self.private = channel.private

    def update_channel(self, channel):
        super(OpenChannel, self).update_channel(channel)
        if channel.active:
            self.channel_state = self.ChannelState.ACTIVE
        else:
            self.channel_state = self.ChannelState.INACTIVE
        self.local_balance = channel.local_balance
        self.remote_balance = channel.remote_balance
        self.commit_fee = channel.commit_fee
        self.commit_weight = channel.commit_weight
        self.fee_per_kw = channel.fee_per_kw
        self.unsettled_balance = channel.unsettled_balance
        self.total_satoshis_sent = channel.total_satoshis_sent
        self.total_satoshis_received = channel.total_satoshis_received
        self.num_updates = channel.num_updates
        self.pending_htlcs = []
        for htlc in channel.pending_htlcs:
            self.pending_htlcs.append(htlc)
        self.csv_delay = channel.csv_delay
        self.private = channel.private

    def reconnect(self):
        lndAL.LndAL.connect({'pubkey': self.remote_pubkey, 'host': self.remote_uri}, True)

    def close_channel(self):
        force = self.channel_state == Channel.ChannelState.INACTIVE
        response = lndAL.LndAL.close_channel(self.channel_point, force=force)
        for r in response:
            x = r['close_pending']
            print(x)

class ClosedChannel(Channel):
    def __init__(self, channel):
        super(ClosedChannel, self).__init__(channel)
        self.channel_type = "closed_channel"
        self.channel_state = self.ChannelState.CLOSED
        self.chain_hash = channel.chain_hash
        self.closing_tx_hash = channel.closing_tx_hash
        self.close_height = channel.close_height
        self.settled_balance = channel.settled_balance
        self.time_locked_balance = channel.time_locked_balance
        self.close_type = channel.close_type

    def update_channel(self, channel):
        super(ClosedChannel, self).update_channel(channel)
        self.channel_state = self.ChannelState.CLOSED
        self.chain_hash = channel.chain_hash
        self.closing_tx_hash = channel.closing_tx_hash
        self.close_height = channel.close_height
        self.settled_balance = channel.settled_balance
        self.time_locked_balance = channel.time_locked_balance
        self.close_type = channel.close_type


class Channels(object):
    # TODO: make channel_index better iterable
    channel_index = defaultdict(list)
    large_local_amt = 400000
    med_local_amt = 200000
    small_remote_amt = 100000

    @staticmethod
    def add_channel(channel, channel_type):
        c = Channel.factory(channel_type, channel)
        Channels.channel_index[c.chan_id].append(c)

    @staticmethod
    def read_channels():
        # read channels: Empties the existing channels list,
        #                reads the open and closed channels
        #                re-creates the channel list with the current state
        Channels.channel_index = defaultdict(list)
        Channels._read_open_channels()
        Channels._read_closed_channels()

    @staticmethod
    def _read_open_channels():
        response = lndAL.LndAL.list_channels()
        for channel in response.channels:
            Channels.add_channel(channel, "open_channel")

    @staticmethod
    def _read_closed_channels():
        response = lndAL.LndAL.closed_channels()
        for channel in response.channels:
            Channels.add_channel(channel, "closed_channel")

    @staticmethod
    def manage_channel_fees():
        for channel_index in Channels.channel_index:
            channel_list = Channels.find_by_chan_id(channel_index)
            if channel_list:
                channel = channel_list[0]
                if channel.channel_type == "open_channel":
                    if channel.remote_balance < Channels.small_remote_amt:
                        lndAL.LndAL.update_channel_policy(chan_point=channel.channel_point,
                                                          base_fee_msat=-5000,
                                                          fee_rate=0.000001,
                                                          time_lock_delta=10)
                    elif channel.local_balance >= Channels.large_local_amt:
                        lndAL.LndAL.update_channel_policy(chan_point=channel.channel_point,
                                                          base_fee_msat=1000,
                                                          fee_rate=0.000001,
                                                          time_lock_delta=10)
                    elif channel.local_balance >= Channels.med_local_amt:
                        lndAL.LndAL.update_channel_policy(chan_point=channel.channel_point,
                                                          base_fee_msat=2500,
                                                          fee_rate=0.000001,
                                                          time_lock_delta=10)
                    else:
                        lndAL.LndAL.update_channel_policy(chan_point=channel.channel_point,
                                                          base_fee_msat=5000,
                                                          fee_rate=0.000001,
                                                          time_lock_delta=10)

    @staticmethod
    def find_by_chan_id(chan_id):
        return Channels.channel_index[chan_id]


if __name__ == "__main__":
    channels = Channels()
    channels.read_channels()
    channels.manage_channel_fees()