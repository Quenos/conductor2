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
from lightning.fwding_event import FwdingEvents
from stylesheets.dark_theme import DarkTheme
from config.config import SystemConfiguration


class NodeInfoWidget(QtWidgets.QDialog):
    class Amount(QtWidgets.QDialog):
        def __init__(self, parent):
            super().__init__()

            self.parent = parent
            self.setObjectName("Amount dialog")
            self.setWindowTitle("Input amount")
            self.resize(650, 250)
            self.formLayoutWidget = QtWidgets.QWidget(self)
            self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 590, 170))
            self.formLayoutWidget.setObjectName("formLayoutWidget")
            self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
            self.formLayout.setContentsMargins(0, 0, 0, 0)
            self.formLayout.setObjectName("formLayout")
            self.label = QtWidgets.QLabel(self.formLayoutWidget)
            self.label.setObjectName("label")
            self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
            self.amount_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
            self.amount_edit.setObjectName("amount_edit")
            self.amount_edit.setInputMask('00000000')
            self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.amount_edit)

            self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
            self.label_2.setObjectName('sat_per_byte_label')
            self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)

            self.sat_per_byte_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
            self.sat_per_byte_edit.setObjectName('sat_per_byte_edit')
            self.sat_per_byte_edit.setInputMask('0000')
            self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sat_per_byte_edit)

            self.buttonBox = QtWidgets.QDialogButtonBox(self)
            self.buttonBox.setGeometry(QtCore.QRect(280, 175, 341, 50))
            self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
            self.buttonBox.setObjectName("buttonBox")

            self.setModal(True)
            self.setStyleSheet(DarkTheme.get_style_sheet())
            self.label.setText('Amount to allocate to channel:')
            self.label_2.setText('Commit fee in sat/byte:')
            sc = SystemConfiguration()
            self.sat_per_byte_edit.setText(sc.default_sat_per_byte)

            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)

        def accept(self):
            self.parent.amount_allocate = int(self.amount_edit.text())
            self.parent.sat_per_byte = int(self.sat_per_byte_edit.text())
            if self.parent.sat_per_byte > 20:
                mb_reply = QtWidgets.QMessageBox.question(self,
                                                          'Are you sure?', "Do you really want to pay "
                                                          + str(self.parent.sat_per_byte) + " sat/byte commit fee",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.No)
                if mb_reply == QtWidgets.QMessageBox.No:
                    # Setting the amount to 0 will effectively cancel the open channel command
                    self.parent.amount_allocate = 0
            self.hide()

        def reject(self):
            self.parent.amount_allocate = 0
            self.hide()

    def __init__(self):
        super().__init__()

        self.node = None
        self.setObjectName("Form")
        # self.resize(1457, 700)
        self.formLayoutWidget_2 = None
        self.formLayout_2 = None
        self.label_13 = None
        self.label_10 = None
        self.node_alias_edit = None
        self.public_key_edit = None
        self.find_button = None
        self.amount_form = None
        self.amount_allocate = 0
        self.sat_per_byte = 1
        self.add_search_widget()
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 200, 800, 500))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(50, 0, 0, 0)
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
        self.node_alias.setGeometry(QtCore.QRect(300, 150, 200, 34))
        self.node_alias.setObjectName("node_alias")

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.last_update_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.last_update_label.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.last_update_label)

        self.open_chan_button = QtWidgets.QPushButton(self)
        self.open_chan_button.setGeometry(QtCore.QRect(300, 350, 120, 25))
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

    def open_channel(self, event):
        self.amount_form = NodeInfoWidget.Amount(self)
        self.amount_form.show()
        self.amount_form.exec_()
        if self.amount_allocate > 0:
            Channels.open_channel(self.pub_key_label.text(),
                                  self.amount_allocate,
                                  self.sat_per_byte,
                                  self.address_label.text())
        self.amount_form.hide()

    def update(self):
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

    def find_node(self, event):
        if self.public_key_edit.text():
            self.node = Node.find_node(self.public_key_edit.text())
        elif self.node_alias_edit.text():
            self.node = Node.find_node(alias=self.node_alias_edit.text())
        self.update()
        if not self.node:
            self.node_alias.setText('Node not found')

    def add_search_widget(self):
        self.formLayoutWidget_2 = QtWidgets.QWidget(self)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 700, 200))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(50, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout")
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.node_alias_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.node_alias_edit.setObjectName("node_alias_edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.node_alias_edit)
        self.public_key_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.public_key_edit.setObjectName("public_key_edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.public_key_edit)
        self.find_button = QtWidgets.QPushButton(self)
        self.find_button.setGeometry(QtCore.QRect(720, 75, 50, 30))
        self.find_button.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        self.label_13.setText("Node Alias:")
        self.label_10.setText("Public key:")
        self.find_button.setIcon(QtGui.QIcon('./resources/icons/mag-glass.png'))
        self.find_button.clicked.connect(self.find_node)
