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

import time
from lightning.lndAL import LndAL


class FwdingEvent(object):
    def __init__(self, fwding_event=None):
        if fwding_event:
            self.timestamp = fwding_event.timestamp
            self.chan_id_in = fwding_event.chan_id_in
            self.chan_id_out = fwding_event.chan_id_out
            self.amt_in = fwding_event.amt_in
            self.amt_out = fwding_event.amt_out
            self.fee = fwding_event.fee


class FwdingEvents(object):

    def __init__(self):
        self.forwarding_events = []
        self.time_last_fwd = 0
        self.update_forwarding_events()

    def update_forwarding_events(self):
        forwarding_history = LndAL.forwarding_history(start_time=self.time_last_fwd + 1,
                                                      end_time=int(time.time()),
                                                      num_max_events=9999999)
        for fwding_event in forwarding_history.forwarding_events:
            e = FwdingEvent(fwding_event)
            self.forwarding_events.append(e)
        if self.forwarding_events:
            self.time_last_fwd = self.forwarding_events[len(self.forwarding_events) - 1].timestamp
        else:
            self.time_last_fwd = 0

    def reverse_fwd_events(self):
        return self.forwarding_events[::-1]

    def get_total_in_out_fee_amount(self, chan_id):
        in_amt = 0
        out_amt = 0
        fee_amt = 0
        for forwarding_event in self.forwarding_events:
            if forwarding_event.chan_id_in == chan_id:
                in_amt += forwarding_event.amt_in
                fee_amt += forwarding_event.fee
            elif forwarding_event.chan_id_out == chan_id:
                out_amt += forwarding_event.amt_out
                fee_amt += forwarding_event.fee
        return in_amt, out_amt, fee_amt

    def get_date_last_forward(self, chan_id):
        timestamp = 0
        for forwarding_event in self.forwarding_events:
            if (chan_id == forwarding_event.chan_id_in or chan_id == forwarding_event.chan_id_out) \
                    and timestamp < forwarding_event.timestamp:
                timestamp = forwarding_event.timestamp
        return timestamp

    def total_amt_forwarded(self):
        tot_amt_fwd = 0
        for fwe in self.forwarding_events:
            tot_amt_fwd += fwe.amt_in
        return tot_amt_fwd

    def total_fees_received(self):
        tot_fees_received = 0
        for fwe in self.forwarding_events:
            tot_fees_received += fwe.amt_in
            tot_fees_received -= fwe.amt_out
        return tot_fees_received
