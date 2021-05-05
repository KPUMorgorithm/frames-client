from client.src.gui.gui_builder import GuiBuilder
from PyQt5 import QtCore, QtWidgets


class RequestLayout(QtWidgets.QVBoxLayout):

    GB_labelBox : QtWidgets.QGroupBox
    LB_title : QtWidgets.QLabel
    LB_subtitle : QtWidgets.QLabel

    def __init__(self, parent : QtWidgets.QBoxLayout, stretch , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._initLayout()
        parent.addLayout(self, stretch)

    
    def _initLayout(self):

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.GB_labelBox = GuiBuilder.makeGroupBoxIn(self)
        Vbox = GuiBuilder.makeBoxLayoutIn(self.GB_labelBox, True)
        self.LB_title = GuiBuilder.makeLabelIn(Vbox, "test", 
                            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

        self.LB_subtitle = GuiBuilder.makeLabelIn(Vbox, "test",
                            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        self.GB_labelBox.setStyleSheet(
            "width: 100%;"
            "color: #FFFFFF;"
            "background-color: #333333;"
            "font-weight: bold;"
            "font-size: 32px;"
            "margin: 0;"
        )

    def getLB_title(self):
        return self.LB_title
    
    def getLB_subtitle(self):
        return self.LB_subtitle
    
    def getGB_labelBox(self):
        return self.GB_labelBox