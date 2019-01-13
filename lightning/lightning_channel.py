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
from datetime import datetime
from utils.block_explorer import get_block_data
from lightning import lndAL
from lightning.fee_report import FeeReport
from lightning.routing_policy import RoutingPolicy
from collections import defaultdict
from enum import Enum
from abc import ABC, abstractmethod


# TODO: investigate if the Node class from lightning_node.py can be used


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
                raise
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
        self._creation_date = None

    def update_channel(self, channel):
        self.chan_id = channel.chan_id

    @property
    def creation_date(self):
        if self._creation_date is None:
            channel_id_bytes = hex(self.chan_id)[2:]
            while len(channel_id_bytes) < 16:
                channel_id_bytes = '0' + channel_id_bytes
            data = get_block_data(int(channel_id_bytes[:6], 16))
            self._creation_date = data['timestamp']
        return self._creation_date

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
        self.channel_fee = []
        if self.channel_point:
            self.channel_fee = FeeReport().get_channel_fee(BaseChannel.channel_point_str(self.channel_point))
            self.routing_policy = RoutingPolicy(BaseChannel.channel_point_str(self.channel_point))

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
        if self.channel_point:
            self.channel_fee = BaseChannel.channel_point_str(FeeReport().get_channel_fee(self.channel_point))
            self.routing_policy = RoutingPolicy(BaseChannel.channel_point_str(self.channel_point))

    def reconnect(self):
        try:
            lndAL.LndAL.connect({'pubkey': self.remote_pubkey, 'host': self.remote_uri}, True)
        except:
            pass

    def close_channel(self):
        force = self.channel_state == Channel.ChannelState.INACTIVE
        lndAL.LndAL.close_channel(self.channel_point, force=force)


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
    class ReadMode(Enum):
        OPEN_ONLY = 0
        CLOSED_ONLY = 1
        BOTH = 3

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
    def read_channels(mode=ReadMode.OPEN_ONLY):
        # read channels: Empties the existing channels list,
        #                reads the open and closed channels
        #                re-creates the channel list with the current state
        #                Also the routing policy is cleared
        print('read_channels entry: ' + str(datetime.now()))
        RoutingPolicy.clear_graph()
        Channels.channel_index = defaultdict(list)
        if mode == Channels.ReadMode.OPEN_ONLY or mode == Channels.ReadMode.BOTH:
            Channels._read_open_channels()
        if mode == Channels.ReadMode.CLOSED_ONLY or mode == Channels.ReadMode.BOTH:
            Channels._read_closed_channels()
        print('read_channels exit: ' + str(datetime.now()))

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
            try:
                if isinstance(channel[0], OpenChannel):
                    ret_val += channel[0].local_balance
            except IndexError:
                pass
        return ret_val

    @staticmethod
    def tot_remote_balance():
        ret_val = 0
        for c in Channels.channel_index:
            channel = Channels.find_by_chan_id(c)
            try:
                if isinstance(channel[0], OpenChannel):
                    ret_val += channel[0].remote_balance
            except IndexError:
                pass
        return ret_val

    @staticmethod
    def open_channel(pub_key_str, amount, sat_per_byte=0, address=None):
        try:
            if address:
                lndAL.LndAL.connect({'pubkey': pub_key_str, 'host': address}, True)
        except:
            pass
        try:
            pub_key = bytes.fromhex(pub_key_str)
            response = lndAL.LndAL.open_channel(node_pub_key=pub_key,
                                                node_pub_key_string=pub_key_str,
                                                local_funding_amount=amount,
                                                sat_per_byte=sat_per_byte)
            return response
        except Exception as ex:
            raise ex

    @staticmethod
    def update_channel_policy(chan_point, base_fee_msat=1000, fee_rate=0.000001, time_lock_delta=144):
        lndAL.LndAL.update_channel_policy(chan_point=chan_point,
                                          base_fee_msat=base_fee_msat,
                                          fee_rate=fee_rate,
                                          time_lock_delta=time_lock_delta)

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
