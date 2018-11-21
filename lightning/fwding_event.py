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
from lightning import lndAL
from collections import defaultdict
from config.config import SystemConfiguration


class FwdingEvent:
    def __init__(self, fwding_event=None):
        if fwding_event:
            self.timestamp = fwding_event.timestamp
            self.chan_id_in = fwding_event.chan_id_in
            self.chan_id_out = fwding_event.chan_id_out
            self.amt_in = fwding_event.amt_in
            self.amt_out = fwding_event.amt_out
            self.fee = fwding_event.fee


class ConsolidatedForwardingEvent(object):

    def __init__(self,
                 total_amt_in=0,
                 total_amt_out=0,
                 alias=""):
        self.total_amt_in = total_amt_in
        self.total_amt_out = total_amt_out
        self.alias = alias


class FwdingEvents(object):

    def __init__(self, fwding_history=None):
        self.cons_fwd_events_per_node = defaultdict(list)
        self.forwarding_events = []
        if fwding_history:
            for fwding_event in fwding_history:
                e = FwdingEvent(fwding_event)
                self.forwarding_events.append(e)

