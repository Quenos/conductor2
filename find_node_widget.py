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
from lightning.lightning_node import Node


class FindNodeWidget(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(1040, 400)
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 130, 960, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.node_alias_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.node_alias_edit.setObjectName("node_alias_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.node_alias_edit)
        self.public_key_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.public_key_edit.setObjectName("public_key_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.public_key_edit)
        self.instruction_label = QtWidgets.QLabel(self)
        self.instruction_label.setGeometry(QtCore.QRect(100, 50, 1000, 34))
        self.instruction_label.setObjectName("instruction_label")
        self.find_button = QtWidgets.QPushButton(self)
        self.find_button.setGeometry(QtCore.QRect(450, 300, 211, 48))
        self.find_button.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Find Node")
        self.label_3.setText("Node Alias:")
        self.label.setText("Public key:")
        self.instruction_label.setText("Enter the node's alias or public key")
        self.find_button.setIcon(QtGui.QIcon('./resources/icons/mag-glass.png'))

        self.node = None
        self.find_button.clicked.connect(self.find_node)

    def find_node(self, event):
        if self.public_key_edit.text():
            self.node = Node.find_node(self.public_key_edit.text())
        elif self.node_alias_edit.text():
            self.node = Node.find_node(alias=self.node_alias_edit.text())
        if self.node:
            self.hide()
