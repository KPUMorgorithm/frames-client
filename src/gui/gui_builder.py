from PyQt5 import QtCore, QtWidgets, QtGui

class GuiBuilder:
    def __init__(self):
        pass
    
    @staticmethod
    def __isWidget(parent) -> bool:
        if isinstance(parent, QtWidgets.QWidget):
            return True
        else:
            return False


    @classmethod
    def makeBoxLayoutIn(cls, parent, isVertical : bool):
        box : QtWidgets.QBoxLayout = None
        
        if cls.__isWidget(parent):
            if isVertical:
                box = QtWidgets.QVBoxLayout(parent)
            else:
                box = QtWidgets.QHBoxLayout(parent)
        else:
            if isVertical:
                box = QtWidgets.QVBoxLayout()
            else:
                box = QtWidgets.QHBoxLayout()

            parent.addLayout(box)
        
        box.setSpacing(5)
        box.setContentsMargins(5,5,5,5)
        return box

    @classmethod
    def makeLabelIn(cls, parent , text , alignFlag : QtCore.Qt.AlignmentFlag):
        
        if cls.__isWidget(parent):
            label = QtWidgets.QLabel(text,parent)
        else: 
            label = QtWidgets.QLabel(text)
            parent.addWidget(label)

        label.setAlignment(alignFlag)
        return label

    @staticmethod
    def makePushButtonIn(parent, stretch, imagePath, text):
        btn = QtWidgets.QPushButton(QtGui.QIcon(imagePath), text)
        btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        parent.addWidget(btn, stretch = stretch)

        return btn

    @staticmethod
    def makeLineEditIn(parent, stretch, text):
        lineEdit = QtWidgets.QLineEdit(text)
        parent.addWidget(lineEdit, stretch = stretch)
        return lineEdit

    @staticmethod
    def makeRadioButton(parent, text):
        btn = QtWidgets.QRadioButton(f"{text} ")
        btn.setStyleSheet('''
        QRadioButton { font: 15pt;} 
        QRadioButton::indicator { width: 0px; height: 0px; }
        QRadioButton::checked{
            background-color: gray; 
            border : 2px solid black; 
        }
        QRadioButton::unchecked{ 
            background-color: light gray; 
            border : 2px solid black; }
        ''')

        parent.addWidget(btn)
        return btn

    @staticmethod
    def makeGroupBoxIn(parent):
        gb = QtWidgets.QGroupBox()
        parent.addWidget(gb)

        return gb