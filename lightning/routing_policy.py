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

from config.config import SystemConfiguration
from lightning.lndAL import LndAL


class RoutingPolicy(object):
    _graph = None

    def __init__(self, channel_point):
        if not RoutingPolicy._graph:
            RoutingPolicy._graph = LndAL.describe_graph()
        for edge in RoutingPolicy._graph.edges:
            if edge.chan_point == channel_point:
                self.node1_pub = edge.node1_pub
                self.node2_pub = edge.node2_pub
                self.node1_time_lock_delta = edge.node1_policy.time_lock_delta
                self.node2_time_lock_delta = edge.node2_policy.time_lock_delta
                self.node1_min_htlc = edge.node1_policy.min_htlc
                self.node2_min_htlc = edge.node2_policy.min_htlc
                self.node1_fee_base_msat = edge.node1_policy.fee_base_msat
                self.node2_fee_base_msat = edge.node2_policy.fee_base_msat
                self.node1_fee_rate_milli_msat = edge.node1_policy.fee_rate_milli_msat
                self.node2_fee_rate_milli_msat = edge.node2_policy.fee_rate_milli_msat
                self.node1_disabled = edge.node1_policy.disabled
                self.node2_disabled = edge.node2_policy.disabled
                return

    @staticmethod
    def clear_graph():
        RoutingPolicy._graph = None


if __name__ == "__main__":
    sc = SystemConfiguration()
    sc.admin_macaroon_directory = '/home/coen/data'
    sc.tls_cert_directory = '/home/coen/data'
    sc.lnd_rpc_address = '178.164.174.219'
    sc.lnd_rpc_port = '10009'
    rp = RoutingPolicy(True)
