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
from stylesheets.dark_theme import DarkTheme


class FoundNodesWidget(QtWidgets.QDialog):
    def __init__(self, node_list, update):
        super().__init__()
        self.update = update
        self.setObjectName("Form")
        self.resize(520, 290)
        self.setStyleSheet(DarkTheme.get_style_sheet())
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(20, 35, 20, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.list_widget = QtWidgets.QListWidget(self.formLayoutWidget)
        self.list_widget.setObjectName("listview")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.list_widget)

        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(350, 235, 100, 30))
        self.close_button.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Select Node")
        self.label.setText("Nodes:")
        self.close_button.setText('Close')

        # self.model = QtGui.QStandardItemModel()
        for n in node_list:
            # QtGui.QListWidgetItem([n['alias'], n['pub_key']])
            item = QtWidgets.QListWidgetItem(n['alias'])
            item.setData(QtCore.Qt.UserRole, n['pub_key'])
            self.list_widget.addItem(item)
        # self.listview.setModel(self.model)
        self.list_widget.itemSelectionChanged.connect(self.item_clicked)

        self.node = None
        self.close_button.clicked.connect(self.close_dialog)

        self.show()

    def close_dialog(self, event):
        self.hide()

    def item_clicked(self):
        self.update(self.list_widget.currentItem().data(QtCore.Qt.UserRole))
