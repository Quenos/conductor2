import sys

from balance_info_widget import BalanceInfoWidget
from channel_graph_widget import ChannelGraphWidget
from channel_info_widget import ChannelInfoWidget
from channel_list_widget import ChannelListWidget
from lightning import lightning_channel
from stylesheets.dark_theme import DarkTheme

from PyQt5 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.resize(3000, 1400)
        centralwidget = QtWidgets.QWidget(self)
        centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(centralwidget)

        # Channel List needs access to the ChannelInfoWidget to display info
        # create the channel info widget to be used by the channel list
        self.channelInfoWidget = ChannelInfoWidget()

        self.dockGraphWidget = QtWidgets.QDockWidget("Lightning Channel Graph", self)
        self.dockGraphWidget.setMinimumSize(QtCore.QSize(1800, 600))
        self.dockGraphWidget.setObjectName("dockGraphWidget")
        self.dockGraphWidget.setWidget(ChannelGraphWidget(self.channelInfoWidget))
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockGraphWidget)

        self.dockListWidget = QtWidgets.QDockWidget("Lightning Channel List", self)
        self.dockListWidget.setMinimumSize(QtCore.QSize(1100, 450))
        self.dockListWidget.setObjectName("dockListWidget")
        self.dockListWidget.setWidget(ChannelListWidget(self.channelInfoWidget))
        self.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockListWidget)

        self.dockInfoWidget = QtWidgets.QDockWidget("Lightning Channel Info", self)
        self.dockInfoWidget.setMinimumSize(QtCore.QSize(1250, 600))
        self.dockInfoWidget.setObjectName("dockInfoWidget")
        self.dockInfoWidget.setWidget(self.channelInfoWidget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockInfoWidget)

        self.dockInfoWidget = QtWidgets.QDockWidget("Balance Info", self)
        self.dockInfoWidget.setMinimumSize(QtCore.QSize(1250, 200))
        self.dockInfoWidget.setObjectName("dockBalanceWidget")
        self.dockInfoWidget.setWidget(BalanceInfoWidget())
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.TopDockWidgetArea), self.dockInfoWidget)

        # because the containing view for ChannelInfoWidget did not exist on time of creation
        # of the object, the object can not show itself
        self.channelInfoWidget.show()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet(DarkTheme.get_style_sheet())
    w.show()
    sys.exit(app.exec_())
