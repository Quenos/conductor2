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

from lightning import lndAL, hop, rpc_pb2


class Route:

    def __init__(
            self,
            total_time_lock=0,
            total_fees=0,
            total_amt=0,
            hops=None,
            total_fees_msat=0,
            total_amt_msat=0):

        self.total_time_lock = total_time_lock
        self.total_fees = total_fees
        self.total_amt = total_amt
        if hops is None:
            self.hops = []
        else:
            self.hops = hops
        self.total_fees_msat = total_fees_msat
        self.total_amt_msat = total_amt_msat

    def add_hop(self, hop):
        self.hops.append(hop)

    def __contains__(self, item):
        # returns True if item == chan_id of one of the hops, otherwise False

        for hop in self.hops:
            if hop.chan_id == item:
                return True
        return False

    def __eq__(self, other):
        # route is equal if all the hops are equal

        equal_tot = True
        for hop_self in self.hops:
            eq_local = False
            for hop_other in other.hops:
                if hop_other == hop_self:
                    eq_local = True
            if not eq_local:
                equal_tot = False
        return equal_tot

    def __ne__(self, other):
        return not(self == other)

    def __str__(self):
        ret_val = str(self.total_time_lock) + "\n" \
            + str(self.total_fees) + "\n" \
            + str(self.total_amt) + "\n"
        for hop in self.hops:
            ret_val += str(hop)
        ret_val += '\n' \
            + str(self.total_fees_msat) + "\n" \
            + str(self.total_amt_msat)
        return ret_val

