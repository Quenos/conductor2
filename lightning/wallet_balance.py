from lightning import lndAL


class WalletBalance(object):
    def __init__(self):
        wallet_balance = lndAL.LndAL.wallet_balance()
        self.total_balance = wallet_balance.total_balance
        self.confirmed_balance = wallet_balance.confirmed_balance
        self.unconfirmed_balance = wallet_balance.unconfirmed_balance