import sys
from lightning import lightning_node, lightning_channel, channel_balance, wallet_balance
from stylesheets.dark_theme import DarkTheme

from enum import Enum
from PyQt5 import QtCore, QtGui, QtWidgets


class Location(Enum):
    BOTTOM = 0
    RIGHT = 1
    TOP = 2
    LEFT = 3


class Instruction:
    _cp_width = 0
    _cp_height = 0
    MARGIN = 20
    MIN_RECT_WIDTH = 280

    def __init__(self, pen=None):
        if pen:
            self._pen = pen
        else:
            self._pen = None

    def paint(self, widget, painter):
        if self._pen:
            painter.setPen(self._pen)


class LineInstruction(Instruction):
    def __init__(self, line, pen=None):
        super().__init__(pen)
        self._line = line

    def paint(self, widget, painter):
        super().paint(widget, painter)
        painter.drawLine(self._line)


class RectInstruction(Instruction):
    def __init__(self, rect, pen=None):
        super().__init__(pen)
        self._rect = rect

    def paint(self, widget, painter):
        super().paint(widget, painter)
        painter.drawRect(self._rect)


class NodeInstruction(Instruction):

    _offset_x = Instruction.MARGIN
    _offset_y = Instruction.MARGIN
    _location = Location.BOTTOM

    def __init__(self, node, pen=None):
        super().__init__(pen)
        self._node = node

    def paint(self, widget, painter):
        super().paint(widget, painter)

        # if the index of the node is 1 (center node == 0)
        # the offsets need to be reset so that the node is drawn at the bottom left corner of the window
        if self._node.get_node_index() == 1:
            NodeInstruction._offset_x = 10 * Instruction.MARGIN
            NodeInstruction._offset_y = Instruction.MARGIN
            NodeInstruction._location = Location.BOTTOM

        # calculate the width and height of the node rectangle based on the length and height of the node name
        font_metrics = QtGui.QFontMetrics(widget.font())
        text_width = font_metrics.width(self._node.text)
        text_height = font_metrics.height()
        rect_width = text_width + Instruction.MARGIN
        rect_height = text_height + Instruction.MARGIN / 2

        # decide whether the node can still be drawn at the current side of the window
        # if not then adjust the offsets to the next empty part of the window
        if NodeInstruction._location == Location.BOTTOM:
            if NodeInstruction._offset_x > widget.width() - rect_width - Instruction.MARGIN:
                # the node would be drawn outside the window
                NodeInstruction._location = Location.RIGHT
                NodeInstruction._offset_x = widget.width() - Instruction.MIN_RECT_WIDTH - Instruction.MARGIN
                NodeInstruction._offset_y = 2 * rect_height
        elif NodeInstruction._location == Location.RIGHT:
            if NodeInstruction._offset_y > widget.height() - 3 * rect_height:
                # the node would be drawn outside the window
                NodeInstruction._location = Location.LEFT
                NodeInstruction._offset_x = Instruction.MARGIN
                NodeInstruction._offset_y = 2 * rect_height
        elif NodeInstruction._location == Location.LEFT:
            if NodeInstruction._offset_y > widget.height() - 4 * rect_height:
                # the node would be drawn outside the window
                NodeInstruction._location = Location.TOP
                NodeInstruction._offset_x = 10 * Instruction.MARGIN
                NodeInstruction._offset_y = widget.height() - 2 * rect_height

        # set the left upper corner of the node rectangle
        rect_lu_x = NodeInstruction._offset_x
        rect_lu_y = widget.height() - NodeInstruction._offset_y - rect_height - Instruction.MARGIN

        # draw the node rectangle and write the name of the node in it
        painter.drawRect(rect_lu_x, rect_lu_y, rect_width, rect_height)
        painter.drawText(rect_lu_x + 10, rect_lu_y + text_height, self._node.text)

        # calculate the beginning and end point of the edge from the node to center node
        # this depends on the side of the window where the node is drawn
        # the bottom nodes connect from the top of the node to bottom of the center node
        # the right nodes connect from the left side of the node to the right side of the center node
        # the top nodes connect from the bottom of the node to the top of the center node
        # and the left nodes connect from the right of the node to the left of the center node
        if NodeInstruction._location == Location.BOTTOM:
            line_start_x = rect_lu_x + rect_width / 2
            line_start_y = rect_lu_y
            line_end_x = widget.width() / 2
            line_end_y = widget.height() / 2 + Instruction._cp_height / 2
        elif NodeInstruction._location == Location.RIGHT:
            line_start_x = rect_lu_x
            line_start_y = rect_lu_y + rect_height / 2
            line_end_x = widget.width() / 2 + Instruction._cp_width / 2
            line_end_y = widget.height() / 2
        elif NodeInstruction._location == Location.LEFT:
            line_start_x = rect_lu_x + rect_width
            line_start_y = rect_lu_y + rect_height / 2
            line_end_x = widget.width() / 2 - Instruction._cp_width / 2
            line_end_y = widget.height() / 2
        elif NodeInstruction._location == Location.TOP:
            line_start_x = rect_lu_x + rect_width / 2
            line_start_y = rect_lu_y + rect_height
            line_end_x = widget.width() / 2
            line_end_y = widget.height() / 2 - Instruction._cp_height / 2
        else:
            raise ValueError

        # draw the edge
        painter.drawLine(line_start_x, line_start_y, line_end_x, line_end_y)

        # calculate the starting offsets of the next node
        if NodeInstruction._location == Location.BOTTOM or NodeInstruction._location == Location.TOP:
            NodeInstruction._offset_x = rect_lu_x + rect_width + Instruction.MARGIN
        elif NodeInstruction._location == Location.RIGHT or NodeInstruction._location == Location.LEFT:
            NodeInstruction._offset_y += rect_height + Instruction.MARGIN
        else:
            raise ValueError


class CenterNodeInstruction(Instruction):

    def __init__(self, center_node, pen=None):
        super().__init__(pen)
        self._center_node = center_node

    def paint(self, widget, painter):
        super().paint(widget, painter)
        font_metrics = QtGui.QFontMetrics(widget.font())
        text_width = font_metrics.width(self._center_node.text)
        text_height = font_metrics.height()
        rect_width = text_width + Instruction.MARGIN
        rect_height = text_height + Instruction.MARGIN
        Instruction._cp_width = rect_width
        Instruction._cp_height = rect_height
        rect_lu_x = widget.width() / 2 - rect_width / 2
        rect_lu_y = widget.height() / 2 - rect_height / 2
        painter.drawRect(rect_lu_x, rect_lu_y, rect_width, rect_height)
        painter.drawText(rect_lu_x + 10, rect_lu_y + text_height, self._center_node.text)


class TextInstruction(Instruction):
    def __init__(self, text, pen=None):
        super().__init__(pen)
        self._text = text

    def paint(self, widget, painter):
        super().paint(widget, painter)
        painter.drawText(self._text)


class ChannelGraphPicture:
    instructions = []


class Node(object):
    _index = 0

    def __init__(self, text):
        self.text = text
        self._index = Node._index
        Node._index += 1

    def get_node_index(self):
        return self._index


class CenterNode(Node):
    def __init__(self, text):
        super().__init__(text)


class BalanceInfoWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 0, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("channel_name_label")
        self.label.setText("Wallet balance:")

        wb = wallet_balance.WalletBalance()
        self.wallet_balance_label = QtWidgets.QLabel(self)
        self.wallet_balance_label.setGeometry(QtCore.QRect(350, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wallet_balance_label.setFont(font)
        self.wallet_balance_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wallet_balance_label.setObjectName("wallet_balance_label")
        self.wallet_balance_label.setText(str(wb.total_balance) + " sat")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("wallet_balance_unconf_label")
        self.label_2.setText("Unconf:")

        self.unconf_wallet_balance_label = QtWidgets.QLabel(self)
        self.unconf_wallet_balance_label.setGeometry(QtCore.QRect(130, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.unconf_wallet_balance_label.setFont(font)
        self.unconf_wallet_balance_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.unconf_wallet_balance_label.setObjectName("channel_name_label")
        self.unconf_wallet_balance_label.setText(str(wb.unconfirmed_balance) + " sat")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(350, 70, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("wallet_balance_conf_label")
        self.label_3.setText("Conf:")

        self.conf_wallet_balance_label = QtWidgets.QLabel(self)
        self.conf_wallet_balance_label.setGeometry(QtCore.QRect(415, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.conf_wallet_balance_label.setFont(font)
        self.conf_wallet_balance_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conf_wallet_balance_label.setObjectName("wallet_balance_conf_label")
        self.conf_wallet_balance_label.setText(str(wb.confirmed_balance) + " sat")

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(600, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("channel_name_label")
        self.label_1.setText("Channel balance:")

        cb = channel_balance.ChannelBalance()
        self.channel_balance_label = QtWidgets.QLabel(self)
        self.channel_balance_label.setGeometry(QtCore.QRect(900, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.channel_balance_label.setFont(font)
        self.channel_balance_label.setObjectName("channel_name_label")
        self.channel_balance_label.setText(str(cb.balance) + " sat")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(600, 70, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("pending_open_balance_label")
        self.label_4.setText("Pending:")

        self.pending_open_balance_label = QtWidgets.QLabel(self)
        self.pending_open_balance_label.setGeometry(QtCore.QRect(700, 70, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.pending_open_balance_label.setFont(font)
        self.pending_open_balance_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pending_open_balance_label.setObjectName("wallet_balance_conf_label")
        self.pending_open_balance_label.setText(str(cb.pending_open_balance) + " sat")

        self.show()


class ChannelListWidget(QtWidgets.QWidget):
    def __init__(self, channel_info_widget):
        super().__init__()

        self.channel_info_widget = channel_info_widget
        self.list_widget = QtWidgets.QListWidget(self)
        self.list_widget.setGeometry(QtCore.QRect(35, 35, 1000, 400))
        self.list_widget.setObjectName("ChannelListView")

        # add the nodes aliases to the List
        channels = MainWindow.channels
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


class ChannelInfoWidget(QtWidgets.QWidget):
    def __init__(self, channel_id=0):
        super().__init__()

        self.channel_name_label = QtWidgets.QLabel(self)
        self.channel_name_label.setGeometry(QtCore.QRect(200, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.channel_name_label.setFont(font)
        self.channel_name_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.channel_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.channel_name_label.setObjectName("channel_name_label")

        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 80, 610, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(50, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.active_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.active_label.setObjectName("active_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.active_label)

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.channel_id_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.channel_id_label.setObjectName("channel_id_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel_id_label)

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.capacity_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.capacity_label.setObjectName("capacity_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.capacity_label)

        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.local_balance_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.local_balance_label.setObjectName("local_balance_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.local_balance_label)

        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.remote_balance_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.remote_balance_label.setObjectName("remote_balance_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.remote_balance_label)

        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)

        self.commit_fee_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.commit_fee_label.setObjectName("commit_fee_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.commit_fee_label)

        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)

        self.commit_weight_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.commit_weight_label.setObjectName("commit_weight_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.commit_weight_label)

        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_17)

        self.fee_per_kw_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.fee_per_kw_label.setObjectName("fee_per_kw_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.fee_per_kw_label)

        self.formLayoutWidget_2 = QtWidgets.QWidget(self)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(610, 80, 621, 431))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(50, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)

        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)

        self.unsettled_balance_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.unsettled_balance_label.setObjectName("unsettled_balance_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.unsettled_balance_label)

        self.tot_sat_sent_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.tot_sat_sent_label.setObjectName("tot_sat_sent_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tot_sat_sent_label)

        self.tot_sat_received_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.tot_sat_received_label.setObjectName("tot_sat_received_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tot_sat_received_label)

        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_20)

        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_21)

        self.num_updates_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.num_updates_label.setObjectName("num_updates_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.num_updates_label)

        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_29.setObjectName("label_29")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_29)

        self.pending_htlcs_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.pending_htlcs_label.setObjectName("pending_htlcs_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pending_htlcs_label)

        self.label_31 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_31)

        self.csv_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.csv_label.setObjectName("csv_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.csv_label)

        self.label_33 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_33.setObjectName("label_33")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_33)

        self.private_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.private_label.setObjectName("private_label")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.private_label)

        self.formLayoutWidget_3 = QtWidgets.QWidget(self)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 471, 1251, 150))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(50, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.label_42 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_42.setObjectName("label_4")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_42)

        self.channel_point_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9.5)
        self.channel_point_label.setFont(font)
        self.channel_point_label.setObjectName("channel_point_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel_point_label)

        self.remote_pubkey_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9.5)
        self.remote_pubkey_label.setFont(font)
        self.remote_pubkey_label.setObjectName("remote_pubkey_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.remote_pubkey_label)

        self.uri_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9.5)
        self.uri_label.setFont(font)
        self.uri_label.setObjectName("remote_pubkey_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uri_label)

        self.channel_name_label.setText("TextLabel")
        self.label.setText("Active:")
        self.active_label.setText("TextLabel")
        self.label_2.setText("Remote pubkey:")
        self.remote_pubkey_label.setText("TextLabel")
        self.label_3.setText("Channel point:")
        self.channel_point_label.setText("TextLabel")
        self.label_4.setText("Channel id:")
        self.channel_id_label.setText("TextLabel")
        self.label_5.setText("Capacity:")
        self.capacity_label.setText("TextLabel")
        self.label_6.setText("Local balance:")
        self.local_balance_label.setText("TextLabel")
        self.label_7.setText("Remote balance:")
        self.remote_balance_label.setText("TextLabel")
        self.label_15.setText("Commit fee:")
        self.commit_fee_label.setText("TextLabel")
        self.label_16.setText("Commit weight:")
        self.commit_weight_label.setText("TextLabel")
        self.label_17.setText("Fee per kw:")
        self.fee_per_kw_label.setText("TextLabel")
        self.label_18.setText("Unsettled balance:")
        self.label_19.setText("Total satoshis sent:")
        self.unsettled_balance_label.setText("TextLabel")
        self.tot_sat_sent_label.setText("TextLabel")
        self.tot_sat_received_label.setText("TextLabel")
        self.label_20.setText("Total satoshis received:")
        self.label_21.setText("Number of updates:")
        self.num_updates_label.setText("TextLabel")
        self.label_29.setText("Pending htlcs")
        self.pending_htlcs_label.setText("TextLabel")
        self.label_31.setText("CSV delay")
        self.csv_label.setText("TextLabel")
        self.label_33.setText("Private")
        self.private_label.setText("TextLabel")
        self.label_42.setText("Uri:")
        self.uri_label.setText("TextLabel")

        if channel_id != 0:
            self.update_info(channel_id)
        # don't show the object yet, because it is forward created
        # in order for the channel list to access this object
        # to update info

    def update_info(self, channel_id):
        channel = lightning_channel.Channels.channel_index[channel_id][0]
        self.channel_name_label.setText(channel.remote_node_alias)
        self.active_label.setText(str(channel.channel_state))
        self.remote_pubkey_label.setText(channel.remote_pubkey)
        self.channel_point_label.setText(channel.channel_point.get("funding_txid_str")+':'+str(channel.channel_point.get("output_index")))
        self.channel_id_label.setText(str(channel.chan_id))
        self.capacity_label.setText(str(channel.capacity))
        self.local_balance_label.setText(str(channel.local_balance))
        self.remote_balance_label.setText(str(channel.remote_balance))
        self.commit_fee_label.setText(str(channel.commit_fee))
        self.commit_weight_label.setText(str(channel.commit_weight))
        self.fee_per_kw_label.setText(str(channel.fee_per_kw))
        self.unsettled_balance_label.setText(str(channel.unsettled_balance))
        self.tot_sat_sent_label.setText(str(channel.total_satoshis_sent))
        self.tot_sat_received_label.setText(str(channel.total_satoshis_received))
        self.num_updates_label.setText(str(channel.num_updates))
        # TODO: add pending htlcs link
        if not channel.pending_htlcs:
            self.pending_htlcs_label.setText("No pending HTLC")
        self.csv_label.setText(str(channel.csv_delay))
        self.private_label.setText(str(channel.private))
        self.uri_label.setText(channel.remote_uri)


class ChannelGraphWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self.resize(1752, 916)

        # draw center node (HomeNode - your node)
        home_node = lightning_node.HomeNode()
        center_node = CenterNode(home_node.name)
        colour = QtGui.QColor(QtCore.Qt.darkGreen)
        pen = QtGui.QPen(colour, 4)

        instruction = CenterNodeInstruction(center_node, pen)
        ChannelGraphPicture.instructions.append(instruction)

        # draw the nodes and channels connect to the center node
        channels = MainWindow.channels
        channels.read_channels()
        for c in lightning_channel.Channels.channel_index:
            channel = lightning_channel.Channels.channel_index[c][0]
            if channel.channel_type == "open_channel":
                # TODO: make node colour configurable
                colour = QtGui.QColor(int(channel.remote_node_colour[1:], 16))
                pen = QtGui.QPen(colour, 4)
                node = Node(channel.remote_node_alias)
                instruction = NodeInstruction(node, pen)
                ChannelGraphPicture.instructions.append(instruction)
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        for instruction in ChannelGraphPicture.instructions:
            instruction.paint(self, qp)


class MainWindow(QtWidgets.QMainWindow):
    channels = lightning_channel.Channels()

    def __init__(self):
        super().__init__()

        self.resize(3000, 1400)
        centralwidget = QtWidgets.QWidget(self)
        centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(centralwidget)

        self.dockGraphWidget = QtWidgets.QDockWidget("Lightning Channel Graph", self)
        self.dockGraphWidget.setMinimumSize(QtCore.QSize(1800, 600))
        self.dockGraphWidget.setObjectName("dockGraphWidget")
        self.dockGraphWidget.setWidget(ChannelGraphWidget())
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockGraphWidget)

        # Channel List needs access to the ChannelInfoWidget to display info
        # create the channel info widget to be used by the channel list
        self.channelInfoWidget = ChannelInfoWidget()

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
