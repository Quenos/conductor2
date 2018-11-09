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

class Hop:

    def __init__(
            self,
            chan_id=0,
            chan_capacity=0,
            amt_to_forward=0,
            fee=0,
            expiry=0,
            fee_msat=0
            ):
        self.chan_id = chan_id
        self.chan_capacity = chan_capacity
        self.amt_to_forward = amt_to_forward
        self.fee = fee
        self.expiry = expiry
        self.fee_msat = fee_msat

    def __eq__(self, other):
        return self.chan_id == other.chan_id

    def __ne__(self, other):
        return not(self == other)

    def __str__(self):
        return str(self.chan_id) + '\n' \
            + str(self.chan_capacity) + '\n' \
            + str(self.amt_to_forward) + '\n' \
            + str(self.fee) + '\n' \
            + str(self.expiry) + '\n' \
            + str(self. fee_msat)