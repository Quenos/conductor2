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

from abc import abstractmethod
from PyQt5 import QtCore, QtGui, QtWidgets
from lightning.pending_channels import PendingChannels
from lightning.lightning_channel import Channel, Channels
from utils.block_explorer import open_block_explorer
from scheduler.update_scheduler import UpdateScheduler


class PendingChannelBaseWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self._parent = parent
        self._cp = None
        self._index = 0
        self._number_pending_channels = 0
        self._pending_channels = None

        self.next_button = QtWidgets.QToolButton(self._parent)
        self.next_button.setArrowType(QtCore.Qt.RightArrow)
        self.next_button.setObjectName("toolButton")
        self.next_button.setGeometry(QtCore.QRect(750, 370, 25, 25))
        self.next_button.hide()
        self.next_button.clicked.connect(self._next_channel)

        self.prev_button = QtWidgets.QToolButton(self._parent)
        self.prev_button.setArrowType(QtCore.Qt.LeftArrow)
        self.prev_button.setObjectName("toolButton")
        self.prev_button.setGeometry(QtCore.QRect(725, 370, 25, 25))
        self.prev_button.hide()
        self.prev_button.clicked.connect(self._prev_channel)

    @abstractmethod
    def update(self, pending_channels):
        self._pending_channels = pending_channels
        if self._pending_channels is not None:
            if self._number_pending_channels != len(self._pending_channels):
                Channels.read_channels()
                UpdateScheduler.trigger('balance_info_widget')
                UpdateScheduler.trigger('channel_graph_widget')
                UpdateScheduler.trigger('channel_info_widget')

    def hide_buttons(self):
        self.prev_button.hide()
        self.next_button.hide()

    def show_buttons(self):
        self.prev_button.show()
        self.next_button.show()

    def _next_channel(self):
        if self._index < self._number_pending_channels - 1:
            self._index += 1
        self.update(self._pending_channels)

    def _prev_channel(self):
        if self._index > 0:
            self._index -= 1
        self.update(self._pending_channels)


class PendingOpenChannelWidget(PendingChannelBaseWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.formLayoutWidget_7 = QtWidgets.QWidget(self)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(20, 20, 800, 175))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")

        self.formLayout_11 = QtWidgets.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_11.setContentsMargins(0, 0, 0, 0)
        self.formLayout_11.setObjectName("formLayout_11")

        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.formLayout_11.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_17)

        self.poc_ch_label = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poc_ch_label.setFont(font)
        self.poc_ch_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.poc_ch_label.setObjectName("poc_ch_label")

        self.formLayout_11.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.poc_ch_label)

        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")

        self.formLayout_11.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_18)

        self.poc_cf_label = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poc_cf_label.setFont(font)
        self.poc_cf_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.poc_cf_label.setObjectName("poc_cf_label")

        self.formLayout_11.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.poc_cf_label)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")

        self.formLayout_11.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_19)

        self.poc_cw_label = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poc_cw_label.setFont(font)
        self.poc_cw_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.poc_cw_label.setObjectName("poc_cw_label")

        self.formLayout_11.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.poc_cw_label)

        self.poc_fpkw_label = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poc_fpkw_label.setFont(font)
        self.poc_fpkw_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.poc_fpkw_label.setObjectName("poc_btm_label")

        self.formLayout_11.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.poc_fpkw_label)

        self.label_201 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_201.setFont(font)
        self.label_201.setObjectName("label_201")

        self.formLayout_11.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_201)

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.poc_cp_label = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poc_cp_label.setFont(font)
        # self.poc_cp_label.setTextInteractionFlags(
        #    QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.poc_cp_label.linkActivated.connect(open_block_explorer)
        self.poc_cp_label.setObjectName("poc_cp_label")

        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.poc_cp_label)

        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.poc_cap_label = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poc_cap_label.setFont(font)
        self.poc_cap_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.poc_cap_label.setObjectName("poc_cap_label")

        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.poc_cap_label)

        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.formLayout_11.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)

        self.poc_lb_label = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poc_lb_label.setFont(font)
        self.poc_lb_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.poc_lb_label.setObjectName("poc_lb_label")

        self.formLayout_11.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.poc_lb_label)

        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.formLayout_11.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.poc_rb_label = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poc_rb_label.setFont(font)
        self.poc_rb_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.poc_rb_label.setObjectName("poc_rb_label9")

        self.formLayout_11.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.poc_rb_label)
        self.label_17.setText("Confirmation height:")
        self.label_18.setText("Commit fee:")
        self.label_19.setText("Commit weight")
        self.label_201.setText("Fee per kw:")
        self.label_5.setText("Channel Point:")
        self.label_6.setText("Capacity:")
        self.label_8.setText("Local balance:")
        self.label_7.setText("Remote balance:")

    def update(self, pending_open_channels=None):
        if pending_open_channels is None:
            pending_open_channels = self._pending_channels
        super().update(pending_open_channels)
        self._number_pending_channels = len(pending_open_channels)
        if self._number_pending_channels > self._index:
            self._parent.channel_name_label.setText('')  # we don't know the name of the remote node

            self._cp = Channel.channel_point_str(pending_open_channels[self._index].channel_point)
            link = '<style> a {color:#3daee9;}</style><a href="https://blockstream.info/tx/' + self._cp.split(':')[0] \
                   + '">' \
                   + self._cp + '</a>'
            self.poc_cp_label.setText(link)

            self.poc_cap_label.setText(str(pending_open_channels[self._index].capacity))
            self.poc_lb_label.setText(str(pending_open_channels[self._index].local_balance))
            self.poc_rb_label.setText(str(pending_open_channels[self._index].remote_balance))
            self.poc_ch_label.setText(str(pending_open_channels[self._index].confirmation_height))
            self.poc_cf_label.setText(str(pending_open_channels[self._index].commit_fee))
            self.poc_cw_label.setText(str(pending_open_channels[self._index].commit_weight))
            self.poc_fpkw_label.setText(str(pending_open_channels[self._index].fee_per_kw))

            if len(pending_open_channels) > 1 and self._index < len(pending_open_channels) - 1:
                self.next_button.show()
            else:
                self.next_button.hide()

            if self._index > 0:
                self.prev_button.show()
            else:
                self.prev_button.hide()
        else:
            self.poc_cp_label.setText("")
            self.poc_cap_label.setText("")
            self.poc_lb_label.setText("")
            self.poc_rb_label.setText("")
            self.poc_ch_label.setText("")
            self.poc_cf_label.setText("")
            self.poc_cw_label.setText("")
            self.poc_fpkw_label.setText("")


class PendingCloseChannelWidget(PendingChannelBaseWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.formLayoutWidget_2 = QtWidgets.QWidget(self)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 800, 175))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")

        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")

        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.cc_ctid_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cc_ctid_label.setFont(font)
        self.cc_ctid_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.cc_ctid_label.setObjectName("cc_ctid_label")

        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cc_ctid_label)

        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")

        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)

        self.cc_cp_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cc_cp_label.setFont(font)
        # self.cc_cp_label.setTextInteractionFlags(
        #    QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.cc_cp_label.linkActivated.connect(open_block_explorer)
        self.cc_cp_label.setObjectName("cc_cp_label")

        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cc_cp_label)

        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")

        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_25)

        self.cc_cap_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cc_cap_label.setFont(font)
        self.cc_cap_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.cc_cap_label.setObjectName("cc_cap_label")

        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cc_cap_label)

        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")

        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_26)

        self.cc_lb_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cc_lb_label.setFont(font)
        self.cc_lb_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.cc_lb_label.setObjectName("cc_lb_label")

        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cc_lb_label)

        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")

        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_27)

        self.cc_rb_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cc_rb_label.setFont(font)
        self.cc_rb_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.cc_rb_label.setObjectName("cc_rb_label")

        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cc_rb_label)
        self.label_9.setText("Closing txid:")
        self.label_24.setText("Channel Point:")
        self.label_25.setText("Capacity:")
        self.label_26.setText("Local balance:")
        self.label_27.setText("Remote balance:")

    def update(self, pending_closing_channels=None):
        if pending_closing_channels is None:
            pending_closing_channels = self._pending_channels
        super().update(pending_closing_channels)
        self._number_pending_channels = len(pending_closing_channels)
        if self._number_pending_channels > self._index:
            self._parent.channel_name_label.setText(pending_closing_channels[self._index].remote_node_alias)

            self._cp = Channel.channel_point_str(pending_closing_channels[self._index].channel_point)
            link = '<style> a {color:#3daee9;}</style><a href="https://blockstream.info/tx/' + self._cp.split(':')[0] \
                   + '">' + self._cp + '</a>'
            self.cc_cp_label.setText(link)

            self.cc_cap_label.setText(str(pending_closing_channels[self._index].capacity))
            self.cc_lb_label.setText(str(pending_closing_channels[self._index].local_balance))
            self.cc_rb_label.setText(str(pending_closing_channels[self._index].remote_balance))
            self.cc_ctid_label.setText(pending_closing_channels[self._index].closing_txid)

            if len(pending_closing_channels) > 1 and self._index < len(pending_closing_channels) - 1:
                self.next_button.show()
            else:
                self.next_button.hide()

            if self._index > 0:
                self.prev_button.show()
            else:
                self.prev_button.hide()
        else:
            self._parent.channel_name_label.setText("")
            self.cc_cp_label.setText("")
            self.cc_cap_label.setText("")
            self.cc_lb_label.setText("")
            self.cc_rb_label.setText("")
            self.cc_ctid_label.setText("")


class PendingForcedCloseChannelWidget(PendingChannelBaseWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.formLayoutWidget_3 = QtWidgets.QWidget(self)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 800, 175))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")

        self.formLayout_7 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")

        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)

        self.fcc_ctid_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fcc_ctid_label.setFont(font)
        # self.fcc_ctid_label.setTextInteractionFlags(
        #    QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.fcc_ctid_label.linkActivated.connect(open_block_explorer)
        self.fcc_ctid_label.setObjectName("fcc_ctid_label")

        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fcc_ctid_label)

        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)

        self.fcc_limbo_bal_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fcc_limbo_bal_label.setFont(font)
        self.fcc_limbo_bal_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.fcc_limbo_bal_label.setObjectName("fcc_lb_label")

        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.fcc_limbo_bal_label)

        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.formLayout_7.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)

        self.fcc_mh_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fcc_mh_label.setFont(font)
        self.fcc_mh_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.fcc_mh_label.setObjectName("fcc_mh_label")

        self.formLayout_7.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.fcc_mh_label)

        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.formLayout_7.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_13)

        self.fcc_btm_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fcc_btm_label.setFont(font)
        self.fcc_btm_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.fcc_btm_label.setObjectName("fcc_btm_label")

        self.formLayout_7.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.fcc_btm_label)

        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.formLayout_7.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_14)

        self.fcc_rb_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fcc_rb_label.setFont(font)
        self.fcc_rb_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.fcc_rb_label.setObjectName("fcc_rb_label")

        self.formLayout_7.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.fcc_rb_label)

        self.label_38 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")

        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_38)

        self.fcc_cp_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fcc_cp_label.setFont(font)
        # self.fcc_cp_label.setTextInteractionFlags(
        #    QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.fcc_cp_label.linkActivated.connect(open_block_explorer)
        self.fcc_cp_label.setObjectName("fcc_cp_label")

        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fcc_cp_label)

        self.label_39 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")

        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_39)

        self.fcc_cap_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fcc_cap_label.setFont(font)
        self.fcc_cap_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.fcc_cap_label.setObjectName("fcc_cap_label")

        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fcc_cap_label)

        self.label_40 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")

        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_40)

        self.fcc_local_bal_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fcc_local_bal_label.setFont(font)
        self.fcc_local_bal_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.fcc_local_bal_label.setObjectName("fcc_lb_label_2")

        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fcc_local_bal_label)

        self.label_41 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")

        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_41)

        self.fcc_remote_bal_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fcc_remote_bal_label.setFont(font)
        self.fcc_remote_bal_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.fcc_remote_bal_label.setObjectName("fcc_rb_label_2")

        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fcc_remote_bal_label)

        self.label_10.setText("Closing txid:")
        self.label_11.setText("Limbo balance:")
        self.label_12.setText("Maturity height:")
        self.label_13.setText("Blocks till maturity:")
        self.label_14.setText("Recovered balance:")
        self.label_38.setText("Channel Point:")
        self.label_39.setText("Capacity:")
        self.label_40.setText("Local balance:")
        self.label_41.setText("Remote balance:")

    def update(self, pending_force_closing_channels=None):
        if pending_force_closing_channels is None:
            pending_force_closing_channels = self._pending_channels
        super().update(pending_force_closing_channels)
        self._number_pending_channels = len(pending_force_closing_channels)
        if self._number_pending_channels > self._index:

            self._parent.channel_name_label.setText(pending_force_closing_channels[self._index].remote_node_alias)

            self._cp = Channel.channel_point_str(pending_force_closing_channels[self._index].channel_point)
            link = '<style> a {color:#3daee9;}</style><a href="https://blockstream.info/tx/' + self._cp.split(':')[0] \
                   + '">' \
                   + self._cp + '</a>'
            self.fcc_cp_label.setText(link)

            self.fcc_cap_label.setText(str(pending_force_closing_channels[self._index].capacity))
            self.fcc_local_bal_label.setText(str(pending_force_closing_channels[self._index].local_balance))
            self.fcc_remote_bal_label.setText(str(pending_force_closing_channels[self._index].remote_balance))
            txid = pending_force_closing_channels[self._index].closing_txid
            link = '<style> a {color:#3daee9;}</style><a href="https://blockstream.info/tx/' + txid + '">' \
                   + txid + '</a>'
            self.fcc_ctid_label.setText(link)
            self.fcc_limbo_bal_label.setText(str(pending_force_closing_channels[self._index].limbo_balance))
            self.fcc_mh_label.setText(str(pending_force_closing_channels[self._index].maturity_height))
            self.fcc_btm_label.setText(str(pending_force_closing_channels[self._index].blocks_til_maturity))
            self.fcc_rb_label.setText(str(pending_force_closing_channels[self._index].recovered_balance))

            if len(pending_force_closing_channels) > 1 and self._index < len(pending_force_closing_channels) - 1:
                self.next_button.show()
            else:
                self.next_button.hide()

            if self._index > 0:
                self.prev_button.show()
            else:
                self.prev_button.hide()
        else:
            self._parent.channel_name_label.setText("")
            self.fcc_cp_label.setText("")
            self.fcc_cap_label.setText("")
            self.fcc_local_bal_label.setText("")
            self.fcc_remote_bal_label.setText("")
            self.fcc_ctid_label.setText("")
            self.fcc_limbo_bal_label.setText("")
            self.fcc_mh_label.setText("")
            self.fcc_btm_label.setText("")
            self.fcc_rb_label.setText("")


class WaitingCloseChannelWidget(PendingChannelBaseWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.formLayoutWidget_4 = QtWidgets.QWidget(self)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 800, 175))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")

        self.formLayout_8 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_8.setObjectName("formLayout_8")

        self.label_42 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")

        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_42)

        self.wcc_cp_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wcc_cp_label.setFont(font)
        # self.wcc_cp_label.setTextInteractionFlags(
        #    QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.wcc_cp_label.linkActivated.connect(open_block_explorer)
        self.wcc_cp_label.setObjectName("wcc_cp_label")

        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.wcc_cp_label)

        self.label_43 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")

        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_43)

        self.wcc_cap_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wcc_cap_label.setFont(font)
        self.wcc_cap_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.wcc_cap_label.setObjectName("wcc_cap_label_2")

        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.wcc_cap_label)

        self.label_44 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")

        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_44)

        self.wcc_local_bal_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wcc_local_bal_label.setFont(font)
        self.wcc_local_bal_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.wcc_local_bal_label.setObjectName("wcc_lb_label_2")

        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.wcc_local_bal_label)

        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)

        self.wcc_lb_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wcc_lb_label.setFont(font)
        self.wcc_lb_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.wcc_lb_label.setObjectName("wcc_lb_label")

        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.wcc_lb_label)

        self.label_45 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")

        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_45)

        self.wcc_rb_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wcc_rb_label.setFont(font)
        self.wcc_rb_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.wcc_rb_label.setObjectName("wcc_rb_label")

        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wcc_rb_label)

        self.label_42.setText("Channel Point:")
        self.label_43.setText("Capacity:")
        self.label_44.setText("Local balance:")
        self.label_15.setText("Limbo balance")
        self.label_45.setText("Remote balance:")

    def update(self, waiting_close_channels=None):
        if waiting_close_channels is None:
            waiting_close_channels = self._pending_channels
        super().update(waiting_close_channels)
        self._number_pending_channels = len(waiting_close_channels)
        if self._number_pending_channels > self._index:
            self._parent.channel_name_label.setText(waiting_close_channels[self._index].remote_node_alias)

            self._cp = Channel.channel_point_str(waiting_close_channels[self._index].channel_point)
            link = '<style> a {color:#3daee9;}</style><a href="https://blockstream.info/tx/' \
                   + self._cp.split(':')[0] + '">' \
                   + self._cp + '</a>'
            self.wcc_cp_label.setText(link)

            self.wcc_cap_label.setText(str(waiting_close_channels[self._index].capacity))
            self.wcc_local_bal_label.setText(str(waiting_close_channels[self._index].local_balance))
            self.wcc_rb_label.setText(str(waiting_close_channels[self._index].remote_balance))
            self.wcc_lb_label.setText(str(waiting_close_channels[self._index].limbo_balance))

            if len(waiting_close_channels) > 1 and self._index < len(waiting_close_channels) - 1:
                self.next_button.show()
            else:
                self.next_button.hide()

            if self._index > 0:
                self.prev_button.show()
            else:
                self.prev_button.hide()
        else:
            self._parent.channel_name_label.setText("")
            self.wcc_cp_label.setText("")
            self.wcc_cap_label.setText("")
            self.wcc_local_bal_label.setText("")
            self.wcc_rb_label.setText("")
            self.wcc_lb_label.setText("")


class PendingChannelContainerWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.pending_channels = None
        self.txid = None
        self.setObjectName("PendingChannels")

        self.channel_name_label = QtWidgets.QLabel(self)
        self.channel_name_label.setGeometry(QtCore.QRect(150, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.channel_name_label.setFont(font)
        self.channel_name_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.channel_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.channel_name_label.setObjectName("channel_name_label")
        self.channel_name_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(50, 60, 725, 300))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")

        self.poc_tab = PendingOpenChannelWidget(self)
        self.poc_tab.setObjectName("poc_tab")
        self.tabWidget.addTab(self.poc_tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.poc_tab), "Pending Open Channels")

        self.cc_tab = PendingCloseChannelWidget(self)
        self.cc_tab.setObjectName("cc_tab")
        self.tabWidget.addTab(self.cc_tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cc_tab), "Pending Close Channels")

        self.fcc_tab = PendingForcedCloseChannelWidget(self)
        self.fcc_tab.setObjectName("fcc_tab")
        self.tabWidget.addTab(self.fcc_tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fcc_tab), "Forced Close Channels")

        self.wcc_tab = WaitingCloseChannelWidget(self)
        self.wcc_tab.setObjectName("wcc_tab")
        self.tabWidget.addTab(self.wcc_tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wcc_tab), "Waiting Close Channels")

        self.tabWidget.setCurrentIndex(0)
        self._active_tab_widget = self.tabWidget.currentWidget()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Pending Channels")

        self.tabWidget.currentChanged.connect(self._tab_changed)

        # start a periodic update of the pending channel container widget every 30 seconds
        # and run it once from the start
        UpdateScheduler.register('pending_channel_container_widget', self.update, interval=30 * 1000, immediate=True)

    def _tab_changed(self, index):
        # hide the buttons of the previous active tab, so that these buttons do not interfere with the buttons of
        # the new tab
        self._active_tab_widget.hide_buttons()
        self.channel_name_label.setText('')
        self._active_tab_widget = self.tabWidget.currentWidget()
        self._active_tab_widget.update()

    def update(self):
        self.pending_channels = PendingChannels()
        self.pending_channels.read_pending_channels()

        self.poc_tab.update(self.pending_channels.pending_open_channels)
        self.cc_tab.update(self.pending_channels.pending_closing_channels)
        self.fcc_tab.update(self.pending_channels.pending_force_closing_channels)
        self.wcc_tab.update(self.pending_channels.waiting_close_channels)
