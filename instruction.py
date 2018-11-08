from enum import Enum
from PyQt5 import QtCore, QtWidgets, QtGui


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

    def __init__(self, node, pen=None, chan_id=0):
        super().__init__(pen)
        self._window_position = None
        self.chan_id = chan_id
        self._node = node

    def _set_window_position(self, pos_x, pos_y, width, height):
        self._window_position = QtCore.QRect(pos_x, pos_y, width, height)

    def get_window_position(self):
        return self._window_position

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

        # Safe and draw the node rectangle and write the name of the node in it
        self._set_window_position(rect_lu_x, rect_lu_y, rect_width, rect_height)
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
