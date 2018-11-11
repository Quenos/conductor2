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

from lightning.lndAL import LndAL
from lightning.lightning_channel import PendingChannel
from lightning.htlc import PendingHTLC
from config.config import SystemConfiguration


class PendingOpenChannel(object):
    def __init__(self, open_channel):
        self.channel = PendingChannel(open_channel.channel)
        self.confirmation_height = open_channel.confirmation_height
        self.commit_fee = open_channel.commit_fee
        self.commit_weight = open_channel.commit_weight
        self.fee_per_kw = open_channel.fee_per_kw

    @property
    def channel_point(self):
        return self.channel.channel_point

    @property
    def capacity(self):
        return self.channel.capacity

    @property
    def local_balance(self):
        return self.channel.local_balance

    @property
    def remote_balance(self):
        return self.channel.remote_balance

    @property
    def remote_node_alias(self):
        return self.channel.remote_node_alias


class PendingClosingChannel(object):
    def __init__(self, closing_channel):
        self.channel = PendingChannel(closing_channel.channel)
        self.closing_txid = closing_channel.closing_txid

    @property
    def channel_point(self):
        return self.channel.channel_point

    @property
    def capacity(self):
        return self.channel.capacity

    @property
    def local_balance(self):
        return self.channel.local_balance

    @property
    def remote_balance(self):
        return self.channel.remote_balance

    @property
    def remote_node_alias(self):
        return self.channel.remote_node_alias


class PendingForceClosingChannel(object):
    def __init__(self, force_closing_channel):
        self.channel = PendingChannel(force_closing_channel.channel)
        self.closing_txid = force_closing_channel.closing_txid
        self.limbo_balance = force_closing_channel.limbo_balance
        self.maturity_height = force_closing_channel.maturity_height
        self.blocks_til_maturity = force_closing_channel.blocks_til_maturity
        self.recovered_balance = force_closing_channel.recovered_balance
        self.pending_htlcs = []
        for pending_htlc in force_closing_channel.pending_htlcs:
            self.pending_htlcs.append(PendingHTLC(pending_htlc))

    @property
    def channel_point(self):
        return self.channel.channel_point

    @property
    def capacity(self):
        return self.channel.capacity

    @property
    def local_balance(self):
        return self.channel.local_balance

    @property
    def remote_balance(self):
        return self.channel.remote_balance

    @property
    def remote_node_alias(self):
        return self.channel.remote_node_alias


class WaitingCloseChannel(object):
    def __init__(self, waiting_close_channel):
        self.channel = PendingChannel(waiting_close_channel.channel)
        self.limbo_balance = waiting_close_channel.limbo_balance

    @property
    def channel_point(self):
        return self.channel.channel_point

    @property
    def capacity(self):
        return self.channel.capacity

    @property
    def local_balance(self):
        return self.channel.local_balance

    @property
    def remote_balance(self):
        return self.channel.remote_balance

    @property
    def remote_node_alias(self):
        return self.channel.remote_node_alias


class PendingChannels(object):
    def __init__(self, pending_channels=None):
        if pending_channels:
            self.update(pending_channels)
        else:
            self.total_limbo_balance = 0
            self.pending_open_channels = []
            self.pending_closing_channels = []
            self.pending_force_closing_channels = []
            self.waiting_close_channels = []

    def read_pending_channels(self):
        self.update(LndAL.pending_channels())

    def update(self, pending_channels):
        self.total_limbo_balance = pending_channels.total_limbo_balance
        for pending_open_channel in pending_channels.pending_open_channels:
            self.pending_open_channels.append(PendingOpenChannel(pending_open_channel))
        for pending_closing_channel in pending_channels.pending_closing_channels:
            self.pending_closing_channels.append((PendingClosingChannel(pending_closing_channel)))
        for pending_force_closing_channel in pending_channels.pending_force_closing_channels:
            self.pending_force_closing_channels.append((PendingForceClosingChannel(pending_force_closing_channel)))
        for waiting_close_channel in pending_channels.waiting_close_channels:
            self.waiting_close_channels.append((WaitingCloseChannel(waiting_close_channel)))


if __name__ == "__main__":
    sc = SystemConfiguration()
    sc.admin_macaroon_directory = '/home/coen/data'
    sc.tls_cert_directory = '/home/coen/data'
    sc.lnd_rpc_address = '192.168.0.110'
    sc.lnd_rpc_port = '10009'
    pc = PendingChannels()
    pc.read_pending_channels()
    print(pc)
