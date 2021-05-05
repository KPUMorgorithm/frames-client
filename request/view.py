from client.src.gui.gui_builder import GuiBuilder
from PyQt5 import QtCore, QtWidgets


class RequestLayout(QtWidgets.QVBoxLayout):

    LB_title : QtWidgets.QLabel
    LB_subtitle : QtWidgets.QLabel

    def __init__(self, parent : QtWidgets.QBoxLayout, stretch , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._initLayout()
        parent.addLayout(self, stretch)

    
    def _initLayout(self):

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

        self.LB_title = GuiBuilder.makeLabelIn(self, "test", 
                            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

        self.LB_subtitle = GuiBuilder.makeLabelIn(self, "test",
                            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        self.LB_title.setStyleSheet(
            "width: 100%;"
            "color: #FFFFFF;"
            "background-color: #333333;"
            "font-weight: bold;"
            "font-size: 32px;"
            "margin: 0;"
        )
        self.LB_subtitle.setStyleSheet(
            "width: 100%;"
            "color: #FFFFFF;"
            "background-color: #333333;"
            "font-weight: bold;"
            "font-size: 28px;"
            "margin: 0;"
        )

    def getLB_title(self):
        return self.LB_title
    
    def getLB_subtitle(self):
        return self.LB_subtitle