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
from channel_list_widget import ChannelListWidget
from settings_widget import SettingsDialog
from pending_channels_widget import PendingChannelWidget
from stylesheets.dark_theme import DarkTheme
from config.config import SystemConfiguration
from lightning import test_lnd_connection

from PyQt5 import QtCore, QtWidgets, QtGui

# TODO 3: Add channel policy update window
# TODO 4: Add auto refresh every hour


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
        self.resize(3000, 1700)
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

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exit_action)
        fileMenu.addAction(settings_action)

        # Channel List and Channel Graph need access to the ChannelInfoWidget to display info
        # create the channel info widget to be used by the channel list and graph
        self.channelInfoWidget = ChannelInfoWidget()

        self.dockGraphWidget = QtWidgets.QDockWidget("Lightning Channel Graph", self)
        self.dockGraphWidget.setMinimumSize(QtCore.QSize(2075, 600))
        self.dockGraphWidget.setObjectName("dockGraphWidget")
        self.dockGraphWidget.setWidget(ChannelGraphWidget(self.channelInfoWidget))
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockGraphWidget)

        self.dockListWidget = QtWidgets.QDockWidget("Lightning Channel List", self)
        self.dockListWidget.setMinimumSize(QtCore.QSize(1100, 450))
        self.dockListWidget.setObjectName("dockListWidget")
        self.dockListWidget.setWidget(ChannelListWidget(self.channelInfoWidget))
        self.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockListWidget)
        # having the graph this list is superfluous. Hide it
        self.dockListWidget.hide()

        # instead the pending channels widget goes here
        self.dockPendingChannelsWidget = QtWidgets.QDockWidget("Pending Channels", self)
        self.dockPendingChannelsWidget.setMinimumSize(QtCore.QSize(1600, 600))
        self.dockPendingChannelsWidget.setObjectName("dockPendingChannelsWidget")
        self.dockPendingChannelsWidget.setWidget(PendingChannelWidget())
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.RightDockWidgetArea), self.dockPendingChannelsWidget)

        self.dockInfoWidget = QtWidgets.QDockWidget("Lightning Channel Info", self)
        self.dockInfoWidget.setMinimumSize(QtCore.QSize(600, 800))
        self.dockInfoWidget.setObjectName("dockInfoWidget")
        self.dockInfoWidget.setWidget(self.channelInfoWidget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.RightDockWidgetArea), self.dockInfoWidget)

        self.dockBalanceWidget = QtWidgets.QDockWidget("Balance Info", self)
        self.dockBalanceWidget.setMinimumSize(QtCore.QSize(1250, 200))
        self.dockBalanceWidget.setObjectName("dockBalanceWidget")
        self.dockBalanceWidget.setWidget(BalanceInfoWidget())
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.TopDockWidgetArea), self.dockBalanceWidget)

        # because the containing view for ChannelInfoWidget did not exist on time of creation
        # of the object, the object can not show itself
        self.channelInfoWidget.show()

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

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet(DarkTheme.get_style_sheet())
    w.showMaximized()
    sys.exit(app.exec_())
