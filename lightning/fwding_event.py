import time
from lightning import lndAL
import channel
from collections import defaultdict

class FwdingEvent:
    def __init__(self, fwding_event=None):
        if fwding_event is not None:
            self.timestamp = fwding_event.timestamp
            self.chan_id_in = fwding_event.chan_id_in
            self.chan_id_out = fwding_event.chan_id_out
            self.amt_in = fwding_event.amt_in
            self.amt_out = fwding_event.amt_out
            self.fee = fwding_event.fee
            channel_in = channel.Channels.find_by_chan_id(self.chan_id_in)
            if channel_in:
                self.alias_in = channel_in[0].remote_node_alias
            else:
                self.alias_in = "Unknown"
            channel_out = channel.Channels.find_by_chan_id(self.chan_id_out)
            if channel_out:
                self.alias_out = channel_out[0].remote_node_alias
            else:
                self.alias_out = "Unknown"

class ConsolidatedForwardingEvent(object):

    def __init__(self,
                 total_amt_in=0,
                 total_amt_out=0,
                 alias=""):
        self.total_amt_in = total_amt_in
        self.total_amt_out = total_amt_out
        self.alias = alias

class FwdingEvents:

    def __init__(self, fwding_history=None):
        self.cons_fwd_events_per_node = defaultdict(list)
        self.forwarding_events = []
        if fwding_history is not None:
            for fwding_event in fwding_history:
                e = FwdingEvent(fwding_event)
                self.forwarding_events.append(e)

    def consolidate_per_node(self):
        # creates an overview of the in and out amount per node
        self.cons_fwd_events_per_node = defaultdict(list)
        for fwd_event in self.forwarding_events:
            if self.cons_fwd_events_per_node[fwd_event.alias_in]:
                self.cons_fwd_events_per_node[fwd_event.alias_in][0].total_amt_in += fwd_event.amt_in
            else:
                cons_fwd_event = ConsolidatedForwardingEvent(total_amt_in=fwd_event.amt_in,
                                                             alias=fwd_event.alias_in)
                self.cons_fwd_events_per_node[fwd_event.alias_in].append(cons_fwd_event)
            if self.cons_fwd_events_per_node[fwd_event.alias_out]:
                self.cons_fwd_events_per_node[fwd_event.alias_out][0].total_amt_out += fwd_event.amt_out
            else:
                cons_fwd_event = ConsolidatedForwardingEvent(total_amt_out=fwd_event.amt_out,
                                                             alias=fwd_event.alias_out)
                self.cons_fwd_events_per_node[fwd_event.alias_out].append(cons_fwd_event)


channel.Channels.read_channels()
history = lndAL.LndAL.forwarding_history(end_time=int(time.time()))
fwding_events = FwdingEvents(history.forwarding_events)
fwding_events.consolidate_per_node()
print(fwding_events.cons_fwd_events_per_node)