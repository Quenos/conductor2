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


import ipaddress
from config.config import SystemConfiguration
from lightning import lndAL
from collections import defaultdict
from enum import Enum
from abc import ABC, abstractmethod


class BaseChannel(ABC):

    class ChannelState(Enum):
        ACTIVE = 1
        INACTIVE = 2
        CLOSED = 3

        def __str__(self):
            return self.name

    def __init__(self, channel=None):
        if isinstance(self, PendingChannel):
            self.remote_pubkey = channel.remote_node_pub
        else:
            self.remote_pubkey = channel.remote_pubkey
        self.channel_point = Channel.create_channel_point(channel.channel_point)
        self.capacity = channel.capacity
        try:
            remote_node_info = lndAL.LndAL.get_node_info(self.remote_pubkey)
            self.remote_node_alias = remote_node_info.node.alias
            self.remote_node_colour = remote_node_info.node.color
            self.remote_uri = "Unknown"
            for x in remote_node_info.node.addresses:
                self.remote_uri = x.addr
                # test if the uri is IPv4, IPv6 or tor
                if self.remote_uri.split(':')[0][-5:] == 'onion':
                    continue
                if isinstance(ipaddress.ip_address(self.remote_uri.split(':')[0]), ipaddress.IPv4Address):
                    break
        except Exception as ex:
            if ex.__str__()[:12] == "<_Rendezvous":
                self.remote_node_alias = "Unknown"
                self.remote_node_colour = 0x000000
            else:
                raise ex
        self.channel_type = ""

    def update_channel(self, channel):
        self.remote_pubkey = channel.remote_pubkey
        self.channel_point = Channel.create_channel_point(channel.channel_point)
        self.capacity = channel.capacity
        self.remote_node_alias = lndAL.LndAL.get_node_info(self.remote_pubkey).node.alias

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass

    @staticmethod
    def create_channel_point(channel_point):
        cp = {'funding_txid_str': channel_point[:channel_point.find(':')],
              'output_index': int(channel_point[channel_point.find(':')+1:])}
        return cp

    @staticmethod
    def channel_point_str(channel_point):
        return channel_point['funding_txid_str'] + ':' + str(channel_point['output_index'])

    @staticmethod
    def factory(channel_type, channel):
        if channel_type == "open_channel":
            return OpenChannel(channel)
        if channel_type == "closed_channel":
            return ClosedChannel(channel)
        raise ValueError


class Channel(BaseChannel):
    def __init__(self, channel):
        super(Channel, self).__init__(channel)
        self.channel_type = "channel"
        self.chan_id = channel.chan_id

    def update_channel(self, channel):
        self.chan_id = channel.chan_id

    def __eq__(self, other):
        return self.chan_id == other.chan_id

    def __ne__(self, other):
        return not self == other


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


class PendingChannel(BaseChannel):
    def __init__(self, channel):
        super(PendingChannel, self).__init__(channel)
        self.channel_type = 'pending_channel'
        self.local_balance = channel.local_balance
        self.remote_balance = channel.remote_balance

    def update_channel(self, channel):
        self.remote_pubkey = channel.remote_node_pub
        self.channel_point = channel.channel_point
        self.capacity = channel.capacity
        self.channel_type = 'pending_channel'
        self.local_balance = channel.local_balance
        self.remote_balance = channel.remote_balance
        self.remote_node_alias = lndAL.LndAL.get_node_info(self.remote_pubkey).node.alias

    def __eq__(self, other):
        return Channel.channel_point_str(self.channel_point) \
               == Channel.channel_point_str(other.channel_point)

    def __ne__(self, other):
        return not self == other


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
    def tot_local_balance():
        ret_val = 0
        for c in Channels.channel_index:
            channel = Channels.find_by_chan_id(c)
            if isinstance(channel[0], OpenChannel):
                ret_val += channel[0].local_balance
        return ret_val

    @staticmethod
    def tot_remote_balance():
        ret_val = 0
        for c in Channels.channel_index:
            channel = Channels.find_by_chan_id(c)
            if isinstance(channel[0], OpenChannel):
                ret_val += channel[0].remote_balance
        return ret_val

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

    @staticmethod
    def find_by_chan_point(chan_point):
        for c in Channels.channel_index:
            channel = Channels.find_by_chan_id(c)
            if channel[0].channel_point == chan_point:
                return channel[0]
        return None


if __name__ == "__main__":
    sc = SystemConfiguration()
    sc.admin_macaroon_directory = '/home/coen/data'
    sc.tls_cert_directory = '/home/coen/data'
    sc.lnd_rpc_address = '192.168.0.110'
    sc.lnd_rpc_port = '10009'
    channels = Channels()
    channels.read_channels()
    x = channels.find_by_chan_point('689cad04801d33e7a9a2fefacb1208cbf28ddb5daf9e2837b06009827da57930:1')
    print(x)
#    channels.manage_channel_fees()
