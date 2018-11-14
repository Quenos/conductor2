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

from lightning import lightning_channel
from PyQt5 import QtCore, QtWidgets, QtGui
from stylesheets.dark_theme import DarkTheme


class ChannelInfoWidget(QtWidgets.QWidget):
    class SatPerByte(QtWidgets.QDialog):
        def __init__(self, parent):
            super().__init__()

            self.parent = parent
            self.setObjectName("sat_byte_dialog")
            self.setWindowTitle("Input sat/byte")
            self.resize(650, 180)
            self.formLayoutWidget = QtWidgets.QWidget(self)
            self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 590, 100))
            self.formLayoutWidget.setObjectName("formLayoutWidget")
            self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
            self.formLayout.setContentsMargins(0, 0, 0, 0)
            self.formLayout.setObjectName("formLayout")
            self.label = QtWidgets.QLabel(self.formLayoutWidget)
            self.label.setObjectName("label")
            self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
            self.sat_per_byte_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
            self.sat_per_byte_edit.setObjectName("sat_per_byte_edit")
            self.sat_per_byte_edit.setInputMask('9999')
            self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sat_per_byte_edit)

            self.buttonBox = QtWidgets.QDialogButtonBox(self)
            self.buttonBox.setGeometry(QtCore.QRect(280, 110, 341, 50))
            self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
            self.buttonBox.setObjectName("buttonBox")

            self.setModal(True)
            self.setStyleSheet(DarkTheme.get_style_sheet())
            self.label.setText('Commit fee in sat/byte:')
            self.sat_per_byte_edit.setText('1')

            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)

        def accept(self):
            self.parent.sat_per_byte = int(self.sat_per_byte_edit.text())
            if self.parent.sat_per_byte > 20:
                mb_reply = QtWidgets.QMessageBox.question(self,
                                                          'Are you sure?', "Do you really want to pay "
                                                          + str(self.parent.sat_per_byte) + " sat/byte commit fee",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.No)
                if mb_reply == QtWidgets.QMessageBox.No:
                    # Setting the amount to 0 will effectively cancel the open channel command
                    self.parent.sat_per_byte = 0
            self.hide()

        def reject(self):
            self.parent.sat_per_byte = 0
            self.hide()

    def __init__(self, channel_id=0):
        super().__init__()

        self.sat_per_byte = 0
        self.sat_per_byte_form = None
        # self.resize(600, 600)
        self.channel_id = channel_id
        self.channel_name_label = QtWidgets.QLabel(self)
        self.channel_name_label.setGeometry(QtCore.QRect(200, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.channel_name_label.setFont(font)
        self.channel_name_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.channel_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.channel_name_label.setObjectName("channel_name_label")
        self.channel_name_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 80, 610, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(50, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.active_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.active_label.setObjectName("active_label")
        self.active_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.active_label)

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.channel_id_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.channel_id_label.setObjectName("channel_id_label")
        self.channel_id_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel_id_label)

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.capacity_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.capacity_label.setObjectName("capacity_label")
        self.capacity_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.capacity_label)

        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.local_balance_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.local_balance_label.setObjectName("local_balance_label")
        self.local_balance_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.local_balance_label)

        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.remote_balance_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.remote_balance_label.setObjectName("remote_balance_label")
        self.remote_balance_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.remote_balance_label)

        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)

        self.commit_fee_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.commit_fee_label.setObjectName("commit_fee_label")
        self.commit_fee_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.commit_fee_label)

        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)

        self.commit_weight_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.commit_weight_label.setObjectName("commit_weight_label")
        self.commit_weight_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.commit_weight_label)

        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_17)

        self.fee_per_kw_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.fee_per_kw_label.setObjectName("fee_per_kw_label")
        self.fee_per_kw_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.fee_per_kw_label)

        self.formLayoutWidget_2 = QtWidgets.QWidget(self)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(610, 80, 621, 431))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(50, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)

        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)

        self.unsettled_balance_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.unsettled_balance_label.setObjectName("unsettled_balance_label")
        self.unsettled_balance_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.unsettled_balance_label)

        self.tot_sat_sent_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.tot_sat_sent_label.setObjectName("tot_sat_sent_label")
        self.tot_sat_sent_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tot_sat_sent_label)

        self.tot_sat_received_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.tot_sat_received_label.setObjectName("tot_sat_received_label")
        self.tot_sat_received_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tot_sat_received_label)

        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_20)

        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_21)

        self.num_updates_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.num_updates_label.setObjectName("num_updates_label")
        self.num_updates_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.num_updates_label)

        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_29.setObjectName("label_29")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_29)

        self.pending_htlcs_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.pending_htlcs_label.setObjectName("pending_htlcs_label")
        self.pending_htlcs_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pending_htlcs_label)

        self.label_31 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_31)

        self.csv_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.csv_label.setObjectName("csv_label")
        self.csv_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.csv_label)

        self.label_33 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_33.setObjectName("label_33")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_33)

        self.private_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.private_label.setObjectName("private_label")
        self.private_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.private_label)

        self.formLayoutWidget_3 = QtWidgets.QWidget(self)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 471, 1251, 150))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(50, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.label_42 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_42.setObjectName("label_4")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_42)

        self.channel_point_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.channel_point_label.setObjectName("channel_point_label")
        # self.channel_point_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.channel_point_label.linkActivated.connect(self.open_block_explorer)
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel_point_label)

        self.remote_pubkey_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.remote_pubkey_label.setObjectName("remote_pubkey_label")
        self.remote_pubkey_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.remote_pubkey_label)

        self.uri_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.uri_label.setObjectName("uri_label")
        self.uri_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uri_label)

        self.reconnect_push_button = QtWidgets.QPushButton(self)
        self.reconnect_push_button.setGeometry(QtCore.QRect(900, 690, 250, 48))
        self.reconnect_push_button.setObjectName("reconnect_push_button")
        self.reconnect_push_button.setText("Reconnect")
        self.reconnect_push_button.clicked.connect(self.reconnect_channel)

        self.close_channel_push_button = QtWidgets.QPushButton(self)
        self.close_channel_push_button.setGeometry(QtCore.QRect(50, 690, 250, 48))
        self.close_channel_push_button.setObjectName("close_channel_push_button")
        self.close_channel_push_button.setText("Close Channel")
        self.close_channel_push_button.clicked.connect(self.close_channel)

        self.channel_policy_push_button = QtWidgets.QPushButton(self)
        self.channel_policy_push_button.setGeometry(QtCore.QRect(450, 690, 300, 48))
        self.channel_policy_push_button.setObjectName("channel_policy_push_button")
        self.channel_policy_push_button.setText("Set Channel Policy")
        self.channel_policy_push_button.clicked.connect(self.set_channel_policy)

        self.channel_name_label.setText("TextLabel")
        self.label.setText("Active:")
        self.active_label.setText("TextLabel")
        self.label_2.setText("Remote pubkey:")
        self.remote_pubkey_label.setText("TextLabel")
        self.label_3.setText("Channel point:")
        self.channel_point_label.setText("TextLabel")
        self.label_4.setText("Channel id:")
        self.channel_id_label.setText("TextLabel")
        self.label_5.setText("Capacity:")
        self.capacity_label.setText("TextLabel")
        self.label_6.setText("Local balance:")
        self.local_balance_label.setText("TextLabel")
        self.label_7.setText("Remote balance:")
        self.remote_balance_label.setText("TextLabel")
        self.label_15.setText("Commit fee:")
        self.commit_fee_label.setText("TextLabel")
        self.label_16.setText("Commit weight:")
        self.commit_weight_label.setText("TextLabel")
        self.label_17.setText("Fee per kw:")
        self.fee_per_kw_label.setText("TextLabel")
        self.label_18.setText("Unsettled balance:")
        self.label_19.setText("Total satoshis sent:")
        self.unsettled_balance_label.setText("TextLabel")
        self.tot_sat_sent_label.setText("TextLabel")
        self.tot_sat_received_label.setText("TextLabel")
        self.label_20.setText("Total satoshis received:")
        self.label_21.setText("Number of updates:")
        self.num_updates_label.setText("TextLabel")
        self.label_29.setText("Pending htlcs")
        self.pending_htlcs_label.setText("TextLabel")
        self.label_31.setText("CSV delay")
        self.csv_label.setText("TextLabel")
        self.label_33.setText("Private")
        self.private_label.setText("TextLabel")
        self.label_42.setText("Uri:")
        self.uri_label.setText("TextLabel")

        if self.channel_id != 0:
            self.update(channel_id)
        # don't show the object yet, because it is forward created
        # in order for the channel list to access this object
        # to update info

    def update(self, channel_id):
        self.channel_id = channel_id
        channel = lightning_channel.Channels.channel_index[channel_id][0]
        if channel.channel_state == lightning_channel.Channel.ChannelState.ACTIVE:
            self.reconnect_push_button.hide()
        else:
            self.reconnect_push_button.show()
        self.channel_name_label.setText(channel.remote_node_alias)
        self.active_label.setText(str(channel.channel_state))
        self.remote_pubkey_label.setText(channel.remote_pubkey)

        cp = lightning_channel.Channel.channel_point_str(channel.channel_point)
        self.channel_point_label.setText(
            '<style> a {color:#3daee9;}</style><a href="https://blockstream.info/">' + cp + '</a>')
        self.channel_id_label.setText(str(channel.chan_id))
        self.capacity_label.setText(str(channel.capacity))
        self.local_balance_label.setText(str(channel.local_balance))
        self.remote_balance_label.setText(str(channel.remote_balance))
        self.commit_fee_label.setText(str(channel.commit_fee))
        self.commit_weight_label.setText(str(channel.commit_weight))
        self.fee_per_kw_label.setText(str(channel.fee_per_kw))
        self.unsettled_balance_label.setText(str(channel.unsettled_balance))
        self.tot_sat_sent_label.setText(str(channel.total_satoshis_sent))
        self.tot_sat_received_label.setText(str(channel.total_satoshis_received))
        self.num_updates_label.setText(str(channel.num_updates))
        # TODO: add pending htlcs link
        if not channel.pending_htlcs:
            self.pending_htlcs_label.setText("No pending HTLC")
        self.csv_label.setText(str(channel.csv_delay))
        self.private_label.setText(str(channel.private))
        self.uri_label.setText(channel.remote_uri)

    def reconnect_channel(self, event):
        try:
            channel = lightning_channel.Channels.channel_index[self.channel_id][0]
            channel.reconnect()
            lightning_channel.Channels.read_channels()
            self.update(self.channel_id)
            if self.active_label.text() == 'INACTIVE':
                mb = QtWidgets.QMessageBox()
                mb.about(self, "Reconnect error", "Unable to reconnect with node. Try again later")
        except IOError:
            mb = QtWidgets.QMessageBox()
            mb.about(self, "Reconnect error", "Unable to reconnect with node. Try again later")

    def close_channel(self, event):
        channel = lightning_channel.Channels.channel_index[self.channel_id][0]
        self.sat_per_byte_form = ChannelInfoWidget.SatPerByte(self)
        self.sat_per_byte_form.show()
        self.sat_per_byte_form.exec_()
        if self.sat_per_byte > 0:
            button_reply = QtWidgets.QMessageBox.question(self,
                                                          'Close channel',
                                                          "Do you realy want to close the channel?\n" +
                                                          "This cannot be undone!!!",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.No)
            if button_reply == QtWidgets.QMessageBox.Yes:
                channel.close_channel()

    def set_channel_policy(self):
        print('set channel policy')

    def open_block_explorer(self, linkStr):
        channel = lightning_channel.Channels.channel_index[self.channel_id][0]
        cp = lightning_channel.Channel.channel_point_str(channel.channel_point).split(':')[0]
        url = 'https://blockstream.info/tx/' + cp
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))
