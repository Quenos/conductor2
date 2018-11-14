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

from lightning import wallet_balance, channel_balance, pending_channels, lightning_channel
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
        self.wallet_balance_label.setGeometry(QtCore.QRect(325, 0, 700, 80))
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
        self.label_3.setGeometry(QtCore.QRect(275, 70, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("wallet_balance_conf_label")
        self.label_3.setText("Conf:")

        self.conf_wallet_balance_label = QtWidgets.QLabel(self)
        self.conf_wallet_balance_label.setGeometry(QtCore.QRect(360, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.conf_wallet_balance_label.setFont(font)
        self.conf_wallet_balance_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conf_wallet_balance_label.setObjectName("wallet_balance_conf_label")
        self.conf_wallet_balance_label.setText(str(wb.confirmed_balance) + " sat")

        # channel balance == local balance + pending balance (?)
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

        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(1200, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("total_limbo_balance_label")
        self.label_10.setText("Total limbo balance:")

        lb = pending_channels.PendingChannels()
        lb.read_pending_channels()
        self.limbo_balance_label = QtWidgets.QLabel(self)
        self.limbo_balance_label.setGeometry(QtCore.QRect(1550, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.limbo_balance_label.setFont(font)
        self.limbo_balance_label.setObjectName("total_limbo_balance_label")
        self.limbo_balance_label.setText(str(lb.total_limbo_balance) + " sat")

        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(1200, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_11.setText("Total local balance:")

        self.tot_local_balance_label = QtWidgets.QLabel(self)
        self.tot_local_balance_label.setGeometry(QtCore.QRect(1550, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tot_local_balance_label.setFont(font)
        self.tot_local_balance_label.setObjectName("total_local_balance_label")
        self.tot_local_balance_label.setText(str(lightning_channel.Channels.tot_local_balance()) + " sat")

        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(1800, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("total_remote_balance_label")
        self.label_12.setText("Total remote balance:")

        self.tot_remote_balance_label = QtWidgets.QLabel(self)
        self.tot_remote_balance_label.setGeometry(QtCore.QRect(2155, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tot_remote_balance_label.setFont(font)
        self.tot_remote_balance_label.setObjectName("channel_name_label")
        self.tot_remote_balance_label.setText(str(lightning_channel.Channels.tot_remote_balance()) + " sat")

        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(1800, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_13.setText("Ratio local/remote:")

        ratio = lightning_channel.Channels.tot_local_balance() / lightning_channel.Channels.tot_remote_balance()
        ratio = round(ratio * 100) / 100
        self.ratio_label = QtWidgets.QLabel(self)
        self.ratio_label.setAlignment(QtCore.Qt.AlignCenter)
        if ratio < 0.5 or ratio > 1.5:
            self.ratio_label.setStyleSheet("QLabel { background-color : #aa3333; }")
        elif ratio < 0.75 or ratio > 1.25:
            self.ratio_label.setStyleSheet("QLabel { background-color : #aa8000; }")
        else:
            self.ratio_label.setStyleSheet("QLabel { background-color : #33aa33; }")

        self.ratio_label.setGeometry(QtCore.QRect(2155, 70, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ratio_label.setFont(font)
        self.ratio_label.setObjectName("channel_name_label")
        self.ratio_label.setText(str(ratio))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30000)

        self.show()

    def update(self):
        wb = wallet_balance.WalletBalance()
        self.wallet_balance_label.setText(str(wb.total_balance) + " sat")
        self.unconf_wallet_balance_label.setText(str(wb.unconfirmed_balance) + " sat")
        self.conf_wallet_balance_label.setText(str(wb.confirmed_balance) + " sat")

        cb = channel_balance.ChannelBalance()
        self.channel_balance_label.setText(str(cb.balance) + " sat")
        self.pending_open_balance_label.setText(str(cb.pending_open_balance) + " sat")

        lb = pending_channels.PendingChannels()
        lb.read_pending_channels()
        self.limbo_balance_label.setText(str(lb.total_limbo_balance) + " sat")

        self.tot_local_balance_label.setText(str(lightning_channel.Channels.tot_local_balance()) + " sat")
        self.tot_remote_balance_label.setText(str(lightning_channel.Channels.tot_remote_balance()) + " sat")

        ratio = lightning_channel.Channels.tot_local_balance() / lightning_channel.Channels.tot_remote_balance()
        ratio = round(ratio * 100) / 100
        if ratio < 0.5 or ratio > 1.5:
            self.ratio_label.setStyleSheet("QLabel { background-color : #aa3333; }")
        elif ratio < 0.75 or ratio > 1.25:
            self.ratio_label.setStyleSheet("QLabel { background-color : #aa8000; }")
        else:
            self.ratio_label.setStyleSheet("QLabel { background-color : #33aa33; }")
