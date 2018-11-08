import lndAL

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