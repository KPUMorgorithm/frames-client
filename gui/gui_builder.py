from PyQt5 import QtCore, QtWidgets

class GuiBuilder:
    def __init__(self):
        pass

    @staticmethod
    def makeBoxLayoutIn(parent, isVertical : bool):
        box : QtWidgets.QBoxLayout = None
        
        if isinstance(parent, QtWidgets.QLayout):
            if isVertical:
                box = QtWidgets.QVBoxLayout()
            else:
                box = QtWidgets.QHBoxLayout()

            parent.addLayout(box)

        elif isinstance(parent, QtWidgets.QWidget):
            if isVertical:
                box = QtWidgets.QVBoxLayout(parent)
            else:
                box = QtWidgets.QHBoxLayout(parent)

        if box is None:
            return 
        
        box.setSpacing(5)
        box.setContentsMargins(5,5,5,5)

        return box

    @staticmethod
    def makeLabelIn(parent : QtWidgets.QLayout , text , alignFlag : QtCore.Qt.AlignmentFlag):
        label = QtWidgets.QLabel(text)
        label.setAlignment(alignFlag)
        parent.addWidget(label)

        return label
