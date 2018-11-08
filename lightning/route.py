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


routes_response = lndAL.LndAL.query_routes('0232e20e7b68b9b673fb25f48322b151a93186bffe4550045040673797ceca43cf', amt=510000, fee_limit=lndAL.LndAL.set_fee_limit(5, 1))
h = rpc_pb2.Route()
h.total_time_lock = 17
print(routes_response.routes[0])
channels = lndAL.LndAL.list_channels(active_only=True)
unbalanced = []
for channel in channels.channels:
    if channel.remote_balance < channel.local_balance / 4:
        unbalanced.append(channel.chan_id)
routes = []
for route in routes_response.routes:
    r = Route()
    r.total_time_lock = route.total_time_lock
    r.total_fees = route.total_fees
    r.total_amt = route.total_amt
    for route_hop in route.hops:
        h = hop.Hop()
        h.chan_id = route_hop.chan_id
        h.fee_msat = route_hop.fee_msat
        h.fee = route_hop.fee
        h.expiry = route_hop.expiry
        h.amt_to_forward = route_hop.amt_to_forward
        h.chan_capacity = route_hop.chan_capacity
        r.add_hop(h)
    r.total_fees_msat = route.total_fees_msat
    r.total_amt_msat = route.total_amt_msat
    routes.append(r)
for route in routes:
    for chan_id in unbalanced:
        if chan_id in route:
            # print(chan_id, " found")
            # print(route.hops[0])
            # print('\n')
            a = str(route)
            # print(a)
