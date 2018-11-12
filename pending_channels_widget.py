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

from PyQt5 import QtCore, QtGui, QtWidgets
from lightning.pending_channels import PendingChannels
from lightning.lightning_channel import Channel


class PendingChannelWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.pending_channels = None
        self.setObjectName("PendingChannels")

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

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(40, 80, 1500, 520))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.formLayoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(20, 20, 1641, 358))
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
        self.poc_cp_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
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

        self.tabWidget.addTab(self.tab, "")
        self._poc = 0

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 1631, 241))
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
        self.cc_cp_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
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

        self.tabWidget.addTab(self.tab_2, "")
        self._cc = 1

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.next_button = QtWidgets.QToolButton(self)
        self.next_button.setArrowType(QtCore.Qt.RightArrow)
        self.next_button.setObjectName("toolButton")
        self.next_button.setGeometry(QtCore.QRect(1465, 490, 55, 55))

        self.prev_button = QtWidgets.QToolButton(self)
        self.prev_button.setArrowType(QtCore.Qt.LeftArrow)
        self.prev_button.setObjectName("toolButton")
        self.prev_button.setGeometry(QtCore.QRect(1400, 490, 55, 55))

        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab_5)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 1621, 421))
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
        self.fcc_ctid_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
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
        self.fcc_cp_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
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

        self.tabWidget.addTab(self.tab_5, "")
        self._fcc = 2

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")

        self.formLayoutWidget_4 = QtWidgets.QWidget(self.tab_6)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 1641, 220))
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
        self.wcc_cp_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
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

        self.tabWidget.addTab(self.tab_6, "")
        self._wcc = 3

        self._next_tab_index = 4

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Pending Channels")
        self.label_17.setText("Confirmation height:")
        self.poc_ch_label.setText("TextLabel")
        self.label_18.setText("Commit fee:")
        self.poc_cf_label.setText("TextLabel")
        self.label_19.setText("Commit weight")
        self.poc_cw_label.setText("TextLabel")
        self.poc_fpkw_label.setText("TextLabel")
        self.label_201.setText("Fee per kw:")
        self.label_5.setText("Channel Point:")
        self.poc_cp_label.setText("TextLabel")
        self.label_6.setText("Capacity:")
        self.poc_cap_label.setText("TextLabel")
        self.label_8.setText("Local balance:")
        self.poc_lb_label.setText("TextLabel")
        self.label_7.setText("Remote balance:")
        self.poc_rb_label.setText("TextLabel")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Pending Open Channels")
        self.label_9.setText("Closing txid:")
        self.cc_ctid_label.setText("TextLabel")
        self.label_24.setText("Channel Point:")
        self.cc_cp_label.setText("TextLabel")
        self.label_25.setText("Capacity:")
        self.cc_cap_label.setText("TextLabel")
        self.label_26.setText("Local balance:")
        self.cc_lb_label.setText("TextLabel")
        self.label_27.setText("Remote balance:")
        self.cc_rb_label.setText("TextLabel")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Closing Channels")
        self.label_10.setText("Closing txid:")
        self.fcc_ctid_label.setText("TextLabel")
        self.label_11.setText("Limbo balance:")
        self.fcc_limbo_bal_label.setText("TextLabel")
        self.label_12.setText("Maturity height:")
        self.fcc_mh_label.setText("TextLabel")
        self.label_13.setText("Blocks till maturity:")
        self.fcc_btm_label.setText("TextLabel")
        self.label_14.setText("Recovered balance:")
        self.fcc_rb_label.setText("TextLabel")
        self.label_38.setText("Channel Point:")
        self.fcc_cp_label.setText("TextLabel")
        self.label_39.setText("Capacity:")
        self.fcc_cap_label.setText("TextLabel")
        self.label_40.setText("Local balance:")
        self.fcc_local_bal_label.setText("TextLabel")
        self.label_41.setText("Remote balance:")
        self.fcc_remote_bal_label.setText("TextLabel")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), "Forced Closing Channels")
        self.label_42.setText("Channel Point:")
        self.wcc_cp_label.setText("TextLabel")
        self.label_43.setText("Capacity:")
        self.wcc_cap_label.setText("TextLabel")
        self.label_44.setText("Local balance:")
        self.wcc_local_bal_label.setText("TextLabel")
        self.label_15.setText("Limbo balance")
        self.wcc_lb_label.setText("TextLabel")
        self.label_45.setText("Remote balance:")
        self.wcc_rb_label.setText("TextLabel")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), "Waiting Close Channels")

        self._poc_index = 0
        self._cc_index = 0
        self._fcc_index = 0
        self._wcc_index = 0
        self._tab_active = 0

        self.tabWidget.currentChanged.connect(self._tab_changed)
        self.prev_button.clicked.connect(self._prev_channel)
        self.next_button.clicked.connect(self._next_channel)

        self.update()

    def _tab_changed(self, index):
        self._tab_active = index
        self.update()
        # if self.tabWidget.

    def _next_channel(self):
        if self._poc == self._tab_active:
            if self._poc_index < len(self.pending_channels.pending_open_channels) - 1:
                self._poc_index += 1
        if self._cc == self._tab_active:
            if self._cc_index < len(self.pending_channels.pending_closing_channels) - 1:
                self._cc_index += 1
        if self._fcc == self._tab_active:
            if self._fcc_index < len(self.pending_channels.pending_force_closing_channels) - 1:
                self._fcc_index += 1
        if self._wcc == self._tab_active:
            if self._wcc_index < len(self.pending_channels.waiting_close_channels) - 1:
                self._wcc += 1
        self.update()

    def _prev_channel(self):
        if self._poc == self._tab_active:
            if self._poc_index > 0:
                self._poc_index -= 1
        if self._cc == self._tab_active:
            if self._cc_index > 0:
                self._cc_index -= 1
        if self._fcc == self._tab_active:
            if self._fcc_index > 0:
                self._fcc_index -= 1
        if self._wcc == self._tab_active:
            if self._wcc_index > 0:
                self._wcc_index -= 1
        self.update()

    def update(self):

        # self._wcc -> current tab index of waiting close channel tab
        # self._fcc -> current tab index of forced close channel tab
        # self._cc -> current tab index of pending close channel tab
        # self._poc -> current tab index of pending open channel tab
        # if any of these are -1 -> tab not shown

        # self._wcc_index -> current index of waiting close channel displayed (if tab active)
        # self._fcc_index -> current index of of forced close channel displayed (if tab active)
        # self._cc_index -> current index of pending close channel displayed (if tab active)
        # self._poc_index -> current index of of pending open channel displayed (if tab active)

        self.pending_channels = PendingChannels()
        self.pending_channels.read_pending_channels()

        ###############################################################################
        #
        # waiting close channels
        #
        ###############################################################################
        if not self.pending_channels.waiting_close_channels:
            self.tabWidget.removeTab(self._wcc)
            self._wcc = -1
            self._next_tab_index -= 1
            self.prev_button.hide()
            self.next_button.hide()
        else:
            if self._wcc == -1:  # the tab does not exist, so create it
                self.tabWidget.addTab(self.tab_6, "Waiting Close Channels")
                self._wcc = self._next_tab_index
                self._next_tab_index += 1
            self.wcc_cp_label.setText(Channel.channel_point_str(
                self.pending_channels.waiting_close_channels[self._wcc_index].channel_point))
            self.wcc_cap_label.setText(str(self.pending_channels.waiting_close_channels[self._wcc_index].capacity))
            self.wcc_local_bal_label.setText(
                str(self.pending_channels.waiting_close_channels[self._wcc_index].local_balance))
            self.wcc_rb_label.setText(str(self.pending_channels.waiting_close_channels[self._wcc_index].remote_balance))
            self.wcc_lb_label.setText(str(self.pending_channels.waiting_close_channels[self._wcc_index].limbo_balance))

            if self._tab_active == self._wcc:
                if self._wcc_index < len(self.pending_channels.waiting_close_channels) - 1 > 0:
                    self.next_button.show()
                else:
                    self.next_button.hide()

                if self._wcc_index > 0:
                    self.prev_button.show()
                else:
                    self.prev_button.hide()

        ###############################################################################
        #
        # force close channels
        #
        ###############################################################################

        if not self.pending_channels.pending_force_closing_channels:
            self.tabWidget.removeTab(self._fcc)
            self._fcc = -1
            self._next_tab_index -= 1
            self.prev_button.hide()
            self.next_button.hide()
        else:
            if self._fcc == -1:  # the tab does not exist, so create it
                self.tabWidget.addTab(self.tab_5, "Forced Closing Channels")
                self._fcc = self._next_tab_index
                self._next_tab_index += 1

            self.channel_name_label.setText(
                self.pending_channels.pending_force_closing_channels[self._fcc_index].remote_node_alias)

            self.fcc_cp_label.setText(
                Channel.channel_point_str(
                    self.pending_channels.pending_force_closing_channels[self._fcc_index].channel_point))
            self.fcc_cap_label.setText(
                str(self.pending_channels.pending_force_closing_channels[self._fcc_index].capacity))
            self.fcc_local_bal_label.setText(
                str(self.pending_channels.pending_force_closing_channels[self._fcc_index].local_balance))
            self.fcc_remote_bal_label.setText(
                str(self.pending_channels.pending_force_closing_channels[self._fcc_index].remote_balance))
            self.fcc_ctid_label.setText(
                self.pending_channels.pending_force_closing_channels[self._fcc_index].closing_txid)
            self.fcc_limbo_bal_label.setText(
                str(self.pending_channels.pending_force_closing_channels[self._fcc_index].limbo_balance))
            self.fcc_mh_label.setText(
                str(self.pending_channels.pending_force_closing_channels[self._fcc_index].maturity_height))
            self.fcc_btm_label.setText(
                str(self.pending_channels.pending_force_closing_channels[self._fcc_index].blocks_til_maturity))
            self.fcc_rb_label.setText(
                str(self.pending_channels.pending_force_closing_channels[self._fcc_index].recovered_balance))

            if self._tab_active == self._fcc:
                if self._fcc_index < len(self.pending_channels.pending_force_closing_channels) - 1 > 0:
                    self.next_button.show()
                else:
                    self.next_button.hide()

                if self._fcc_index > 0:
                    self.prev_button.show()
                else:
                    self.prev_button.hide()

        ###############################################################################
        #
        # pending close channels
        #
        ###############################################################################

        if not self.pending_channels.pending_closing_channels:
            self.tabWidget.removeTab(self._cc)
            self._cc = -1
            self._next_tab_index -= 1
            self.prev_button.hide()
            self.next_button.hide()
        else:
            if self._cc:  # the tab does not exist, so create t
                self.tabWidget.addTab(self.tab_2, "Closing Channels")
                self._cc = self._next_tab_index
                self._next_tab_index += 1
            self.cc_cp_label.setText(Channel.channel_point_str(
                self.pending_channels.pending_closing_channels[self._cc_index].channel_point))
            self.cc_cap_label.setText(str(self.pending_channels.pending_closing_channels[self._cc_index].capacity))
            self.cc_lb_label.setText(str(self.pending_channels.pending_closing_channels[self._cc_index].local_balance))
            self.cc_rb_label.setText(str(self.pending_channels.pending_closing_channels[self._cc_index].remote_balance))
            self.cc_ctid_label.setText(self.pending_channels.pending_closing_channels[self._cc_index].closing_txid)

        if self._tab_active == self._cc:
            if self._cc_index < len(self.pending_channels.pending_closing_channels) - 1 > 0:
                self.next_button.show()
            else:
                self.next_button.hide()

            if self._cc_index > 0:
                self.prev_button.show()
            else:
                self.prev_button.hide()

        ###############################################################################
        #
        # pending open channels
        #
        ###############################################################################

        if not self.pending_channels.pending_open_channels:
            self.tabWidget.removeTab(self._poc)
            self._poc = -1
            self._next_tab_index -= 1
            self.prev_button.hide()
            self.next_button.hide()
        else:
            if self._poc == -1:  # the tab does not exist, so create it
                self.tabWidget.addTab(self.tab, "Pending Open Channels")
                self._poc = self._next_tab_index
                self._next_tab_index += 1
            self.poc_cp_label.setText(
                Channel.channel_point_str(self.pending_channels.pending_open_channels[self._poc_index].channel_point))
            self.poc_cap_label.setText(str(self.pending_channels.pending_open_channels[self._poc_index].capacity))
            self.poc_lb_label.setText(str(self.pending_channels.pending_open_channels[self._poc_index].local_balance))
            self.poc_rb_label.setText(str(self.pending_channels.pending_open_channels[self._poc_index].remote_balance))
            self.poc_ch_label.setText(
                str(self.pending_channels.pending_open_channels[self._poc_index].confirmation_height))
            self.poc_cf_label.setText(str(self.pending_channels.pending_open_channels[self._poc_index].commit_fee))
            self.poc_cw_label.setText(str(self.pending_channels.pending_open_channels[self._poc_index].commit_weight))
            self.poc_fpkw_label.setText(str(self.pending_channels.pending_open_channels[self._poc_index].fee_per_kw))

            if self._tab_active == self._poc:
                if self._poc_index < len(self.pending_channels.pending_open_channels) - 1 > 0:
                    self.next_button.show()
                else:
                    self.next_button.hide()

                if self._poc_index > 0:
                    self.prev_button.show()
                else:
                    self.prev_button.hide()
