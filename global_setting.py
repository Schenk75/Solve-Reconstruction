import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, pyqtSignal

BACKGROUND_COLOR = '#F8F8FF'  # 主界面底色
TITLE_COLOR = '#DA70D6'  # 标题栏颜色
FUNC_COLOR = '#FFF0F5'  # 功能栏颜色
LIGHT_FUNC_COLOR = '#FFF0F5'  # 到功能栏颜色的过渡色
HOVER_COLOR = '#00BFFF'  # 按钮点击时的文字颜色
GRAY_COLOR = '#EEF0F6'  # 万能的灰色

ABSOLUTE_PATH = '\\'.join(os.path.abspath(__file__).split('\\')[:-1])

def global_css():
    GLOBAL_BUTTON = """
    QPushButton{
        border:none;
        background:%s
    }
    QPushButton:hover{
        background:%s;
        border-radius:10px;
        color:%s;
    }
    #closeButton{
        background:%s;
        max-width:36px;
        max-height:36px;
        font-size:12px;
        font-family:"Webdings";
        qproperty-text:"r";
        border-radius:10px;
    }
    #closeButton:hover{
        color:white;
        border:none;
        background:red;
    }
    #minButton{
        background:%s;
        max-width:36px;
        max-height:36px;
        font-family:"Webdings";
        font-size: 12px;
        qproperty-text:"0";
        border-radius:10px;
    }
    #minButton:hover{
        color:black;
        border:none;
        background:%s;
    }
    QTableWidget{
        background:%s;
        border:none;
    }
    """ % (FUNC_COLOR, GRAY_COLOR, HOVER_COLOR, TITLE_COLOR, TITLE_COLOR, BACKGROUND_COLOR,  BACKGROUND_COLOR)
    return GLOBAL_BUTTON


class BasicWindow(QMainWindow):
    def __init__(self, parent=None):
        super(BasicWindow, self).__init__(parent)
        self.setupUi(self)
        self.m_flag = False  # 判断是否按下鼠标
        self.setFixedSize(self.width(), self.height())  # 设置窗口大小不能调整
        # self.setWindowOpacity(0.9) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 去掉窗口标题栏
        self.animation = QPropertyAnimation(self, b'windowOpacity')  # 窗口透明度动画类
        self.animation.setDuration(500)  # 持续时间0.5秒
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

    def doShow(self):
        """淡入
        """
        try:
            # 尝试先取消动画完成后关闭窗口的信号
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # 透明度范围从0逐渐增加到1
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        """淡出
        """
        self.animation.stop()
        self.animation.finished.connect(self.close)  # 动画完成则关闭窗口
        # 透明度范围从1逐渐减少到0
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def mousePressEvent(self, event):
        """鼠标左键按下变小手

        Arguments:
            event -- 事件
        """
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))

    def mouseReleaseEvent(self, event):
        """鼠标左键放开变回箭头

        Arguments:
            event -- 事件
        """
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = False
            self.setCursor(QCursor(QtCore.Qt.ArrowCursor))

    def mouseMoveEvent(self, event):
        """鼠标拖动窗口

        Arguments:
            event -- 事件
        """
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)  # 更改窗口位置
            event.accept()