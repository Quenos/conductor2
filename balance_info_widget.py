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

        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 300, 200))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(25, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.label.setText("Wallet balance:")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.wallet_balance_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.wallet_balance_label.setObjectName("wallet_balance_label")
        self.wallet_balance_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.wallet_balance_label)
        wb = wallet_balance.WalletBalance()
        self.wallet_balance_label.setText(str(wb.total_balance) + " sat")

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("wallet_balance_unconf_label")
        self.label_2.setText("Unconf:")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.unconf_wallet_balance_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.unconf_wallet_balance_label.setObjectName("channel_name_label")
        self.unconf_wallet_balance_label.setText(str(wb.unconfirmed_balance) + " sat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.unconf_wallet_balance_label)

        self.formLayoutWidget_2 = QtWidgets.QWidget(self)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(300, 0, 600, 200))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(25, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("wallet_balance_conf_label")
        self.label_3.setText("Conf:")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.conf_wallet_balance_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.conf_wallet_balance_label.setObjectName("wallet_balance_conf_label")
        self.conf_wallet_balance_label.setText(str(wb.confirmed_balance) + " sat")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.conf_wallet_balance_label)

        # channel balance == local balance + pending balance (?)
        self.label_1 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_1.setObjectName("channel_name_label")
        self.label_1.setText("Channel balance:")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_1)

        cb = channel_balance.ChannelBalance()
        self.channel_balance_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.channel_balance_label.setObjectName("channel_name_label")
        self.channel_balance_label.setText(str(cb.balance) + " sat")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel_balance_label)

        self.formLayoutWidget_3 = QtWidgets.QWidget(self)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(600, 0, 900, 200))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(25, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_4.setObjectName("pending_open_balance_label")
        self.label_4.setText("Pending:")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.pending_open_balance_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.pending_open_balance_label.setObjectName("wallet_balance_conf_label")
        self.pending_open_balance_label.setText(str(cb.pending_open_balance) + " sat")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pending_open_balance_label)

        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName("total_limbo_balance_label")
        self.label_10.setText("Total limbo balance:")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)

        lb = pending_channels.PendingChannels()
        lb.read_pending_channels()
        self.limbo_balance_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.limbo_balance_label.setObjectName("total_limbo_balance_label")
        self.limbo_balance_label.setText(str(lb.total_limbo_balance) + " sat")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.limbo_balance_label)

        self.formLayoutWidget_4 = QtWidgets.QWidget(self)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(900, 0, 1200, 200))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(25, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")

        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.label_11.setText("Total local balance:")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)

        self.tot_local_balance_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.tot_local_balance_label.setObjectName("total_local_balance_label")
        self.tot_local_balance_label.setText(str(lightning_channel.Channels.tot_local_balance()) + " sat")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tot_local_balance_label)

        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_12.setObjectName("total_remote_balance_label")
        self.label_12.setText("Total remote balance:")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)

        self.tot_remote_balance_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.tot_remote_balance_label.setObjectName("channel_name_label")
        self.tot_remote_balance_label.setText(str(lightning_channel.Channels.tot_remote_balance()) + " sat")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tot_remote_balance_label)

        self.formLayoutWidget_5 = QtWidgets.QWidget(self)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(1200, 0, 1250, 200))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(25, 0, 1000, 0)
        self.formLayout_5.setObjectName("formLayout_5")

        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_13.setObjectName("label_13")
        self.label_13.setText("Ratio local/remote:")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)

        ratio = lightning_channel.Channels.tot_local_balance() / lightning_channel.Channels.tot_remote_balance()
        ratio = round(ratio * 100) / 100
        self.ratio_label = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.ratio_label.setAlignment(QtCore.Qt.AlignCenter)
        if ratio < 0.5 or ratio > 1.5:
            self.ratio_label.setStyleSheet("QLabel { background-color : #aa3333; }")
        elif ratio < 0.75 or ratio > 1.25:
            self.ratio_label.setStyleSheet("QLabel { background-color : #aa8000; }")
        else:
            self.ratio_label.setStyleSheet("QLabel { background-color : #33aa33; }")

        self.ratio_label.setObjectName("channel_name_label")
        self.ratio_label.setText(str(ratio))
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ratio_label)

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
