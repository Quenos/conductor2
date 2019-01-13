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
from stylesheets.dark_theme import DarkTheme
from lightning.fwding_event import FwdingEvents
from lightning.lightning_channel import Channels
from scheduler.update_scheduler import UpdateScheduler


class FwdEventsWidget(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.forwarding_events = FwdingEvents()

        self.setObjectName("Form")
        self.resize(800, 340)
        self.setStyleSheet(DarkTheme.get_style_sheet())

        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 35, 800, 470))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(20, 0, 20, 0)
        self.formLayout.setObjectName("formLayout")

        self.table_widget = QtWidgets.QTableWidget(self.formLayoutWidget)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setColumnCount(5)
        self.table_widget.setColumnWidth(0, 150)
        self.table_widget.setColumnWidth(2, 20)
        self.table_widget.setColumnWidth(3, 210)
        self.table_widget.setColumnWidth(4, 210)

        self.table_widget.setGeometry(QtCore.QRect(0, 0, 500, 420))
        self.table_widget.setObjectName("table view")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.table_widget)

        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(350, 275, 100, 30))
        self.close_button.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Forwarding Events")
        self.close_button.setText('Close')

        self.close_button.clicked.connect(self.close_dialog)

        # register the fwd events widget update function, and start an automatic update every 90s
        UpdateScheduler.register('fwd_events_widget', self.update, interval=900000, start=True, immediate=True)

        self.show()

    def update(self):
        self.table_widget.clear()
        self.table_widget.setHorizontalHeaderLabels(('Timestamp (UTC)', 'Amount', 'Fee', 'In', 'Out'))
        self.table_widget.setRowCount(len(self.forwarding_events.forwarding_events))
        self.forwarding_events.update_forwarding_events()
        reverse_events = self.forwarding_events.reverse_fwd_events()
        row = 0
        for fe in reverse_events:
            try:
                in_alias = Channels.channel_index[fe.chan_id_in][0].remote_node_alias
            except IndexError:
                in_alias = 'Unknown'
            try:
                out_alias = Channels.channel_index[fe.chan_id_out][0].remote_node_alias
            except IndexError:
                out_alias = 'Unknown'
            self.table_widget.setItem(row,
                                      0,
                                      QtWidgets.QTableWidgetItem(
                                          datetime.utcfromtimestamp(fe.timestamp).strftime('%Y-%m-%d %H:%M:%S')))
            self.table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(fe.amt_in)))
            self.table_widget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(fe.fee)))
            self.table_widget.setItem(row, 3, QtWidgets.QTableWidgetItem(in_alias))
            self.table_widget.setItem(row, 4, QtWidgets.QTableWidgetItem(out_alias))
            row += 1

    def close_dialog(self, event):
        self.hide()
