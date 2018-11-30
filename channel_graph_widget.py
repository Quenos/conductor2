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

from PyQt5 import QtCore, QtWidgets, QtGui
from instruction import CenterNode, CenterNodeInstruction, ChannelGraphPicture, Node, NodeInstruction
from lightning import lightning_node, lightning_channel


class ChannelGraphWidget(QtWidgets.QWidget):
    channels = lightning_channel.Channels()

    def __init__(self, channel_info_widget):
        super().__init__()
        self._stop_repaint = False
        self.channel_info_widget = channel_info_widget
        self.update()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 * 60 * 60)  # update once every hour

        self.show()

    def update(self):
        ChannelGraphPicture.reset()
        self._stop_repaint = True
        # draw center node (HomeNode - your node)
        home_node = None
        try:
            home_node = lightning_node.HomeNode()
        except IOError:
            mb = QtWidgets.QMessageBox()
            mb.about(self, "Lightning network error", "Check the network settings and connection")
            exit(-1)
        center_node = CenterNode(home_node.name)
        colour = QtGui.QColor(QtCore.Qt.darkGreen)
        pen = QtGui.QPen(colour, 4)

        instruction = CenterNodeInstruction(center_node, pen)
        ChannelGraphPicture._instructions.append(instruction)

        # draw the nodes and channels connect to the center node
        for c in lightning_channel.Channels.channel_index:
            channel = lightning_channel.Channels.channel_index[c][0]
            if channel.channel_type == "open_channel":
                # TODO: make node colour configurable
                colour = QtGui.QColor(int(channel.remote_node_colour[1:], 16))
                pen = QtGui.QPen(colour, 4)
                node = Node(channel.remote_node_alias)
                instruction = NodeInstruction(node, pen, channel.chan_id)
                ChannelGraphPicture._instructions.append(instruction)
        if ChannelGraphPicture._instructions[1]:
            self.channel_info_widget.update(ChannelGraphPicture._instructions[1].chan_id)
        self._stop_repaint = False

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        for instruction in ChannelGraphPicture._instructions:
            instruction.paint(self, qp)

    def mousePressEvent(self, event):
        for i in ChannelGraphPicture._instructions:
            if isinstance(i, NodeInstruction):
                try:
                    if i.get_window_position().contains(event.pos()):
                        self.channel_info_widget.update(i.chan_id)
                        break
                except AttributeError:
                    pass
