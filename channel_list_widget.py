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

from lightning import lightning_channel
from channel_graph_widget import ChannelGraphWidget
from PyQt5 import QtCore, QtWidgets, QtGui


class ChannelListWidget(QtWidgets.QWidget):
    def __init__(self, channel_info_widget):
        super().__init__()

        self.channel_info_widget = channel_info_widget
        self.list_widget = QtWidgets.QListWidget(self)
        self.list_widget.setGeometry(QtCore.QRect(35, 35, 1000, 400))
        self.list_widget.setObjectName("ChannelListView")

        # add the nodes aliases to the List
        channels = ChannelGraphWidget.channels
        channels.read_channels()
        first_item = None
        for c in lightning_channel.Channels.channel_index:
            channel = lightning_channel.Channels.channel_index[c][0]
            if channel.channel_type == "open_channel":
                item = QtWidgets.QListWidgetItem()
                item.setText(channel.remote_node_alias)
                item.setData(QtCore.Qt.UserRole, channel.chan_id)
                if not first_item:
                    first_item = item
                self.list_widget.addItem(item)
        self.list_widget.setCurrentItem(first_item)
        self.channel_info_widget.update_info(self.list_widget.currentItem().data(QtCore.Qt.UserRole))
        self.show()

        # connect the click of an item
        self.list_widget.clicked.connect(self.list_click_event)

    def list_click_event(self, event):
        self.channel_info_widget.update_info(self.list_widget.currentItem().data(QtCore.Qt.UserRole))