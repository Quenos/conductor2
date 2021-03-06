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

import sys

from balance_info_widget import BalanceInfoWidget
from channel_graph_widget import ChannelGraphWidget
from channel_info_widget import ChannelInfoWidget
from settings_widget import SettingsDialog
from pending_channel_container_widget import PendingChannelContainerWidget
from node_info_widget import NodeInfoWidget
from stylesheets.dark_theme import DarkTheme
from config.config import SystemConfiguration
from lightning import test_lnd_connection, lightning_channel
from auto_policy import AutoPolicy
from fwd_events_widget import FwdEventsWidget

from PyQt5 import QtCore, QtWidgets, QtGui

# TODO 2: Add some basic exception handling
# TODO 4: Add overview of inactive channels - toggle between node colours and green (active) red (inactive) nodes
# TODO 6: Add auto close channel after certain period of inactivity


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.system_config = SystemConfiguration()
        try:
            self.system_config.read_config()
        except FileNotFoundError:
            self.settings()

        try:
            test_lnd_connection.test_lnd_connection()
        except IOError:
            mb = QtWidgets.QMessageBox()
            mb.about(self, "Connection error", "LND not reachable. Check settings and network and try again")
            self.settings()
            exit(-1)

        self.settings_dialog = None
        self.node_info_dialog = None

        # read the channels for this node, to be used by the other widgets
        lightning_channel.Channels.read_channels()

        self.resize(50, 50)
        centralwidget = QtWidgets.QWidget(self)
        centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(centralwidget)

        exit_action = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(QtWidgets.qApp.quit)

        settings_action = QtWidgets.QAction(QtGui.QIcon('settings.png'), '&Settings', self)
        settings_action.setShortcut('Ctrl+Shift+S')
        settings_action.setStatusTip('Modify settings')
        settings_action.triggered.connect(self.settings)

        open_channel_action = QtWidgets.QAction(QtGui.QIcon('open_channel.png'), '&Open Channel', self)
        open_channel_action.setShortcut('Ctrl+Shift+O')
        open_channel_action.setStatusTip('Open channel')
        open_channel_action.triggered.connect(self.open_channel)

        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)
        file_menu.addAction(settings_action)

        action_menu = menubar.addMenu('&Action')
        action_menu.addAction(open_channel_action)

        self.dockGraphWidget = QtWidgets.QDockWidget("Lightning Channel Graph", self)
        self.dockGraphWidget.setMinimumSize(QtCore.QSize(1035, 440))
        self.dockGraphWidget.setObjectName("dockGraphWidget")
        self.dockGraphWidget.setWidget(ChannelGraphWidget())
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockGraphWidget)

        self.dockPendingChannelsWidget = QtWidgets.QDockWidget("Pending Channels", self)
        self.dockPendingChannelsWidget.setMinimumSize(QtCore.QSize(800, 400))
        self.dockPendingChannelsWidget.setObjectName("dockPendingChannelsWidget")
        self.dockPendingChannelsWidget.setWidget(PendingChannelContainerWidget())
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.RightDockWidgetArea), self.dockPendingChannelsWidget)

        self.dockInfoWidget = QtWidgets.QDockWidget("Lightning Channel Info", self)
        self.dockInfoWidget.setMinimumSize(QtCore.QSize(800, 440))
        self.dockInfoWidget.setObjectName("dockInfoWidget")
        self.dockInfoWidget.setWidget(ChannelInfoWidget())
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.LeftDockWidgetArea), self.dockInfoWidget)

        self.dockNodeInfoWidget = QtWidgets.QDockWidget("Node Info", self)
        self.dockNodeInfoWidget.setMinimumSize(QtCore.QSize(800, 400))
        self.dockNodeInfoWidget.setObjectName("dockInfoWidget")
        self.dockNodeInfoWidget.setWidget(NodeInfoWidget())
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.RightDockWidgetArea), self.dockNodeInfoWidget)

        self.dockBalanceWidget = QtWidgets.QDockWidget("Balance Info", self)
        self.dockBalanceWidget.setMinimumSize(QtCore.QSize(1600, 75))
        self.dockBalanceWidget.setObjectName("dockBalanceWidget")
        self.dockBalanceWidget.setWidget(BalanceInfoWidget())
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.TopDockWidgetArea), self.dockBalanceWidget)

        self.auto_policy = AutoPolicy()
        self.fwd_events_widget = FwdEventsWidget()

    def settings(self):
        self.settings_dialog = SettingsDialog()
        self.settings_dialog.setModal(True)
        self.settings_dialog.show()
        self.settings_dialog.exec_()
        self.system_config.admin_macaroon_directory = self.settings_dialog.admin_macaroon.text()
        self.system_config.tls_cert_directory = self.settings_dialog.tls_cert.text()
        self.system_config.lnd_rpc_address = self.settings_dialog.ip_lnd.text()
        self.system_config.lnd_rpc_port = self.settings_dialog.port_lnd.text()
        self.system_config.write_config()

    def open_channel(self):
        self.dockNodeInfoWidget.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet(DarkTheme.get_style_sheet())
    w.show()
    app.exec_()
    QtWidgets.QApplication.closeAllWindows()
    exit(0)
