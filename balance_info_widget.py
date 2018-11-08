from lightning import wallet_balance, channel_balance
from PyQt5 import QtCore, QtWidgets, QtGui


class BalanceInfoWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 0, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("channel_name_label")
        self.label.setText("Wallet balance:")

        wb = wallet_balance.WalletBalance()
        self.wallet_balance_label = QtWidgets.QLabel(self)
        self.wallet_balance_label.setGeometry(QtCore.QRect(350, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wallet_balance_label.setFont(font)
        self.wallet_balance_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wallet_balance_label.setObjectName("wallet_balance_label")
        self.wallet_balance_label.setText(str(wb.total_balance) + " sat")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("wallet_balance_unconf_label")
        self.label_2.setText("Unconf:")

        self.unconf_wallet_balance_label = QtWidgets.QLabel(self)
        self.unconf_wallet_balance_label.setGeometry(QtCore.QRect(130, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.unconf_wallet_balance_label.setFont(font)
        self.unconf_wallet_balance_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.unconf_wallet_balance_label.setObjectName("channel_name_label")
        self.unconf_wallet_balance_label.setText(str(wb.unconfirmed_balance) + " sat")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(350, 70, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("wallet_balance_conf_label")
        self.label_3.setText("Conf:")

        self.conf_wallet_balance_label = QtWidgets.QLabel(self)
        self.conf_wallet_balance_label.setGeometry(QtCore.QRect(415, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.conf_wallet_balance_label.setFont(font)
        self.conf_wallet_balance_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conf_wallet_balance_label.setObjectName("wallet_balance_conf_label")
        self.conf_wallet_balance_label.setText(str(wb.confirmed_balance) + " sat")

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(600, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("channel_name_label")
        self.label_1.setText("Channel balance:")

        cb = channel_balance.ChannelBalance()
        self.channel_balance_label = QtWidgets.QLabel(self)
        self.channel_balance_label.setGeometry(QtCore.QRect(900, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.channel_balance_label.setFont(font)
        self.channel_balance_label.setObjectName("channel_name_label")
        self.channel_balance_label.setText(str(cb.balance) + " sat")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(600, 70, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("pending_open_balance_label")
        self.label_4.setText("Pending:")

        self.pending_open_balance_label = QtWidgets.QLabel(self)
        self.pending_open_balance_label.setGeometry(QtCore.QRect(700, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.pending_open_balance_label.setFont(font)
        self.pending_open_balance_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pending_open_balance_label.setObjectName("wallet_balance_conf_label")
        self.pending_open_balance_label.setText(str(cb.pending_open_balance) + " sat")

        self.show()