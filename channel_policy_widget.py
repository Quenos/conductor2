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

from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from lightning.lightning_node import Node
from lightning.lightning_channel import Channels
from stylesheets.dark_theme import DarkTheme


class ChannelPolicyWidget(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.node = None
        self.setObjectName("Form")
        self.resize(1457, 700)
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 350, 1411, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pub_key_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.pub_key_label.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pub_key_label)
        self.num_chan_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.num_chan_label.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.num_chan_label)
        self.tot_capacity_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.tot_capacity_label.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tot_capacity_label)
        self.address_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.address_label.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.address_label)
        self.node_alias = QtWidgets.QLabel(self)
        self.node_alias.setGeometry(QtCore.QRect(630, 50, 400, 34))
        self.node_alias.setObjectName("node_alias")

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.last_update_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.last_update_label.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.last_update_label)

        self.open_chan_button = QtWidgets.QPushButton(self)
        self.open_chan_button.setGeometry(QtCore.QRect(610, 600, 211, 48))
        self.open_chan_button.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Node info")
        self.label.setText("Number of channels: ")
        self.label_2.setText("Total capacity:")
        self.label_3.setText("Public key:")
        self.label_4.setText("Address:")
        self.label_5.setText("Last update:")
        if self.node:
            self.pub_key_label.setText(self.node.pub_key)
            self.num_chan_label.setText(str(self.node.num_channels))
            self.tot_capacity_label.setText(str(self.node.total_capacity))
            self.address_label.setText(self.node.address)
            self.last_update_label.setText(
                datetime.utcfromtimestamp(self.node.last_update).strftime('%Y-%m-%d %H:%M:%S'))
            self.node_alias.setText(self.node.alias)
        else:
            self.pub_key_label.setText("")
            self.num_chan_label.setText("")
            self.tot_capacity_label.setText("")
            self.address_label.setText("")
            self.last_update_label.setText("")
            self.node_alias.setText("")
        self.open_chan_button.setText("Open channel")
        self.open_chan_button.clicked.connect(self.open_channel)

    def update(self):
        pass
