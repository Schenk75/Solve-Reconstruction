import sys
import os
root_path = os.getcwd()
sys.path.append(root_path)
sys.path.append(f'{root_path}\\qt')
sys.path.append('..')
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI.Ui_warn_dialog import Ui_Warn_Dialog
from UI.Ui_info_dialog import Ui_Info_Dialog


Stylesheet = """
#Custom_Widget {
    background: white;
}
#Warn_Widget{
    background: red;
}
#Info_Widget{
    background: #4DBCFF;
}
QPushButton{
    border-radius: 10px;
}
QPushButton:hover{
    background:#EEF0F6;
}
QPushButton:pressed{
    background:#D3D3D3;
}
"""


class Warn_Dialog(QDialog, Ui_Warn_Dialog):
    def __init__(self, *args, **kwargs):
        super(Warn_Dialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.widget.setObjectName('Custom_Widget')
        self.widget_2.setObjectName('Warn_Widget')
        self.setStyleSheet(Stylesheet)
        self.label_2.setStyleSheet('color:white')
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.close)

    def sizeHint(self):
        return QSize(400, 200)


class Info_Dialog(QDialog, Ui_Info_Dialog):
    def __init__(self, *args, **kwargs):
        super(Info_Dialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.widget.setObjectName('Custom_Widget')
        self.widget_2.setObjectName('Info_Widget')
        self.setStyleSheet(Stylesheet)
        self.label_2.setStyleSheet('color:white')
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.close)

    def sizeHint(self):
        return QSize(400, 200)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    # w = Warn_Dialog()
    w = Info_Dialog()
    w.exec_()
    QTimer.singleShot(200, app.quit)
    sys.exit(app.exec_())
