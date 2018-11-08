import lndAL


class ChannelBalance(object):
    def __init__(self):
        channel_balance = lndAL.LndAL.channel_balance()
        self.balance = channel_balance.balance
        self.pending_open_balance = channel_balance.pending_open_balance
