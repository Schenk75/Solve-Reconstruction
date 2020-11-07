import sys
import sqlite3
import qtawesome

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from global_setting import *
from utils.FramelessDialog import *
from utils.Notification import *
from UI.Ui_main_window import *
from UI.Ui_add_solve import *
from UI.Ui_oll_choose import *
from UI.Ui_pll_choose import *
from alg_import import *

srDB = "./srDB.db"

class Main_window(BasicWindow, Ui_MainWindow):
    def __init__(self, user_name, parent=None):
        super(Main_window, self).__init__(parent)
        self.setupUi(self)
        self.user_name = user_name
        self.id.setText(self.user_name)

        self.logo.setPixmap(QPixmap(
            f'{ABSOLUTE_PATH}/img/WCA.svg').scaled(self.logo.width(), self.logo.height()))  # 添加logo
        self.doShow()   # 淡入
        self.init_ui()  # 初始化界面
        # index(self.username)
        # widget美化
        Qss = 'QWidget#widget{background-color:%s;}' % TITLE_COLOR
        Qss += 'QWidget#widget_2{background-color:%s;}' % GRAY_COLOR
        Qss += 'QWidget#widget_3{background-color:%s;}' % BACKGROUND_COLOR
        Qss += '#add_btn{background-color:%s; border-radius:10px;}' % (TITLE_COLOR)
        Qss += '#add_btn:hover{background-color:%s; border-radius:10px;}' % (FUNC_COLOR)
        Qss += '#edit_btn{background-color:%s; border-radius:10px;}' % (TITLE_COLOR)
        Qss += '#edit_btn:hover{background-color:%s; border-radius:10px;}' % (FUNC_COLOR)
        
        Qss += global_css()
        self.setStyleSheet(Qss)  # 边框部分qss重载

        # 所有按钮的初始化
        self.minButton.clicked.connect(self.showMinimized)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.clicked.connect(self.doClose)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.add_btn.clicked.connect(self.add_solve)
        self.add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_btn.clicked.connect(self.show_alg)
        self.edit_btn.setCursor(QCursor(Qt.PointingHandCursor))

    def init_ui(self):
        """初始化界面
        """
        self.stackedWidget.setCurrentIndex(0)
        self.init_table()

    def add_solve(self):
        self.add_window = Add_window()
        self.add_window.show()

    def show_alg(self):
        """打开公式编辑界面
        """
        self.alg_window = Alg_window(self.user_name)
        self.alg_window.show()

    def init_table(self):
        """所有解法表格初始化
        """
        print('Init Tables')


class Add_window(BasicWindow, Ui_AddSolveWindow):
    def __init__(self, parent=None):
        super(Add_window, self).__init__(parent)
        self.setupUi(self)
        self.doShow()
        Qss = global_css()
        Qss += 'QWidget#widget{background-color:%s;}' % TITLE_COLOR
        Qss += '#add_btn{background-color:%s; border-radius:10px;}' % (TITLE_COLOR)
        Qss += '#add_btn:hover{background-color:%s; border-radius:10px;}' % (FUNC_COLOR)
        self.setStyleSheet(Qss)  # 边框部分qss重载

        # 所有按钮的初始化
        self.minButton.clicked.connect(self.showMinimized)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.clicked.connect(self.doClose)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_btn.clicked.connect(self.add_solve)
        self.add_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.init_table()

    def init_table(self):
        """将表格初始化
        """
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnWidth(0, 400)
        self.tableWidget.setColumnWidth(1, 95)
        self.tableWidget.setHorizontalHeaderLabels(['Moves', 'Preparation'])
        self.tableWidget.setVerticalHeaderLabels(['Time', 'Date', 'Scramble', 'Inspection', '1st Pair', '2nd Pair', '3rd Pair', '4th Pair', 'OLL', 'PLL', 'Auf'])
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置为整行选中
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(False)  # 不显示网格
        for i in range(11):
            self.tableWidget.setRowHeight(i, 44)
        
        # oll和pll按钮
        self.oll_btn = QPushButton(self.tableWidget)
        self.oll_btn.setText("Choose OLL")
        self.oll_btn.setFont(QFont('Microsoft YaHei', 10, QFont.Black))
        self.oll_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.oll_btn.setStyleSheet("""
                QPushButton{
                    background-color:%s;
                    text-align:center
                }
                QPushButton:hover{
                    color:%s;
                }
                """ % (BACKGROUND_COLOR, HOVER_COLOR))
        self.oll_btn.clicked.connect(self.choose_oll)
        self.tableWidget.setCellWidget(8, 0, self.oll_btn)

        self.pll_btn = QPushButton(self.tableWidget)
        self.pll_btn.setText("Choose PLL")
        self.pll_btn.setFont(QFont('Microsoft YaHei', 10, QFont.Black))
        self.pll_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pll_btn.setStyleSheet("""
                QPushButton{
                    background-color:%s;
                    text-align:center
                }
                QPushButton:hover{
                    color:%s;
                }
                """ % (BACKGROUND_COLOR, HOVER_COLOR))
        self.pll_btn.clicked.connect(self.choose_pll)
        self.tableWidget.setCellWidget(9, 0, self.pll_btn)

    def add_solve(self):
        """将解法导入数据库
        """
        conn = sqlite3.connect(srDB)
        cursor = conn.cursor()

        print('Add')

        conn.close()

    def choose_oll(self):
        """OLL选择界面
        """
        self.oll_window = OLL_window()
        self.oll_window.show()
        self.oll_window.signal.connect(self.get_oll)

    def get_oll(self, name):
        if name != 'skip':
            conn = sqlite3.connect(srDB)
            cursor = conn.cursor()
            cursor.execute(f"SELECT alg FROM ollTable WHERE name='{name}'")
            alg = cursor.fetchall()[0][0]
            self.oll_btn.setText(alg)
            conn.close()
        else:
            self.oll_btn.setText('OLL Skip')

    def choose_pll(self):
        """PLL选择界面
        """
        self.pll_window = PLL_window()
        self.pll_window.show()
        self.pll_window.signal.connect(self.get_pll)

    def get_pll(self, name):
        if name != 'skip':
            conn = sqlite3.connect(srDB)
            cursor = conn.cursor()
            cursor.execute(f"SELECT alg FROM pllTable WHERE name='{name}'")
            alg = cursor.fetchall()[0][0]
            self.pll_btn.setText(alg)
            conn.close()
        else:
            self.pll_btn.setText('PLL Skip')


class OLL_window(BasicWindow, Ui_OLLWindow):
    signal = QtCore.pyqtSignal(str)     # 向父窗口传值
    def __init__(self, parent=None):
        super(OLL_window, self).__init__(parent)
        self.setupUi(self)
        self.doShow()
        Qss = global_css()
        Qss += 'QWidget#widget{background-color:%s;}' % TITLE_COLOR
        self.setStyleSheet(Qss)  # 边框部分qss重载

        # 所有按钮的初始化
        self.minButton.clicked.connect(self.showMinimized)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.clicked.connect(self.doClose)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.init_table()

    def init_table(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(10)
        for i in range(6):
            self.tableWidget.setColumnWidth(i, 100)
        for i in range(10):
            self.tableWidget.setRowHeight(i, 100)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置为整行选中
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(False)  # 不显示网格

        j, k = 0, 0
        # oll按形状重新排序，便于寻找
        range_oll = [
            1, 2, 3, 4, 17, 18, 19, 20,            # 点O
            5, 6, 7, 8, 9, 10, 11, 12, 28, 29, 30, 31, 32, 35, 37, 36, 38, 41, 42, 43, 44, 47, 48, 49, 50, 53, 54,       # 拐弯O
            13, 14, 15, 16, 33, 34, 39, 40, 45, 46, 51, 52, 55, 56, 57,       # 一字O
            21, 22, 23, 24, 25, 26, 27                        # 十字O
            ]
        for i in range_oll:
            name = f"oll{i}"
            new = QPushButton(self.tableWidget)
            new.setObjectName(name)
            icon = QIcon(f"{ABSOLUTE_PATH}\\img\\oll\\{name}.svg")
            new.setIcon(QIcon(icon))
            new.setIconSize(QSize(100, 100))
            new.setCursor(QCursor(Qt.PointingHandCursor))
            new.clicked.connect(lambda: self.select_oll(self.sender()))
            # print(j, k)
            self.tableWidget.setCellWidget(j, k, new)
            temp = k
            k = k + 1 if k < 5 else 0
            j = j + 1 if k - temp != 1 else j
        new = new = QPushButton(self.tableWidget)
        new.setObjectName("skip")
        new.setText("Skip")
        new.setFont(QFont('Microsoft YaHei', 12, QFont.Black))
        new.setCursor(QCursor(Qt.PointingHandCursor))
        new.clicked.connect(lambda: self.select_oll(self.sender()))
        self.tableWidget.setCellWidget(j, k, new)

    def select_oll(self, btn):
        oll_name = btn.objectName()
        self.signal.emit(oll_name)
        self.doClose()


class PLL_window(BasicWindow, Ui_PLLWindow):
    signal = QtCore.pyqtSignal(str)     # 向父窗口传值
    def __init__(self, parent=None):
        super(PLL_window, self).__init__(parent)
        self.setupUi(self)
        self.doShow()
        Qss = global_css()
        Qss += 'QWidget#widget{background-color:%s;}' % TITLE_COLOR
        self.setStyleSheet(Qss)  # 边框部分qss重载

        # 所有按钮的初始化
        self.minButton.clicked.connect(self.showMinimized)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.clicked.connect(self.doClose)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.init_table()

    def init_table(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(4)
        for i in range(6):
            self.tableWidget.setColumnWidth(i, 100)
        for i in range(4):
            self.tableWidget.setRowHeight(i, 100)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置为整行选中
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(False)  # 不显示网格

        j, k = 0, 0
        # oll按形状重新排序，便于寻找
        range_pll = [
            'Aa', 'Ab', 'E', 'F', 'Ga', 'Gb', 'Gc', 'Gd', 'H', 'Ja', 'Jb',
            'Na', 'Nb', 'Ra', 'Rb', 'T', 'Ua', 'Ub', 'V', 'Y', 'Z'
        ]
        for name in range_pll:
            new = QPushButton(self.tableWidget)
            new.setObjectName(name)
            icon = QIcon(f"{ABSOLUTE_PATH}\\img\\pll\\{name}.svg")
            new.setIcon(QIcon(icon))
            new.setIconSize(QSize(100, 100))
            new.setCursor(QCursor(Qt.PointingHandCursor))
            new.clicked.connect(lambda: self.select_pll(self.sender()))
            # print(j, k)
            self.tableWidget.setCellWidget(j, k, new)
            temp = k
            k = k + 1 if k < 5 else 0
            j = j + 1 if k - temp != 1 else j
        new = new = QPushButton(self.tableWidget)
        new.setObjectName("skip")
        new.setText("Skip")
        new.setFont(QFont('Microsoft YaHei', 12, QFont.Black))
        new.setCursor(QCursor(Qt.PointingHandCursor))
        new.clicked.connect(lambda: self.select_pll(self.sender()))
        self.tableWidget.setCellWidget(j, k, new)

    def select_pll(self, btn):
        pll_name = btn.objectName()
        self.signal.emit(pll_name)
        self.doClose()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Main_window('2018SHEN04')
    main_window.show()

    # main_window = Add_window()
    # main_window.show()

    sys.exit(app.exec_())