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


class FwdEventsWidget(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.setObjectName("Form")
        self.resize(1457, 700)
        self.setStyleSheet(DarkTheme.get_style_sheet())

        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 350, 1411, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.time_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.time_label.setObjectName("time_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.time_label)

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.tot_amt_in_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.tot_amt_in_label.setObjectName("amt_in_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tot_amt_in_label)

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.tot_amt_out_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.tot_amt_out_label.setObjectName("amt_out_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tot_amt_out_label)

        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.fee_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.fee_label.setObjectName("fee_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.fee_label)

        self.label.setText('Date:')
        self.time_label.setText('xxx')
        self.label_2.setText('Input Channel:')
        self.chan_in_label.setText('xxx')
        self.label_3.setText('Output Channel')
        self.chan_out_label.setText('xxx')
        self.label_4.setText('Input Amount:')
        self.tot_amt_in_label.setText('xxx')
        self.label_5.setText('Output Amount:')
        self.tot_amt_out_label.setText('xxx')
        self.label_6.setText('Fee:')
        self.fee_label.setText('xxx')

        self.show()
