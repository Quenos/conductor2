# Copyright 2018 <Quenos Blockchain R&D KFT>
#
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
from config.config import SystemConfiguration


class FeeReport(object):
    def __init__(self):
        fee_report = lndAL.LndAL.get_fee_report()
        self.channel_fees = []
        for channel_fee in fee_report.channel_fees:
            self.channel_fees.append(ChannelFee(channel_fee))
        self.day_fee_sum = fee_report.day_fee_sum
        self.week_fee_sum = fee_report.week_fee_sum
        self.month_fee_sum = fee_report.month_fee_sum

    def get_channel_fee(self, channel_point):
        for channel_fee in self.channel_fees:
            if channel_fee.chan_point == channel_point:
                return channel_fee
        return None


class ChannelFee(object):
    def __init__(self, channel_fee):
        self.chan_point = channel_fee.chan_point
        self.base_fee_msat = channel_fee.base_fee_msat
        self.fee_per_mil = channel_fee.fee_per_mil
        self.fee_rate = channel_fee.fee_rate

