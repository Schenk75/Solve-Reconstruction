import sys
import sqlite3
import qtawesome

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from global_setting import *
from utils.FramelessDialog import *
from utils.Notification import *
from UI.Ui_alg_import import *

srDB = "./srDB.db"

class Alg_window(BasicWindow, Ui_AlgWindow):
    def __init__(self, user_name, parent=None):
        super(Alg_window, self).__init__(parent)
        self.setupUi(self)
        self.id.setText(user_name)

        self.left_column = {'oll_btn': 0, 'pll_btn': 1}  # 左边栏

        self.logo.setPixmap(QPixmap(
            f'{ABSOLUTE_PATH}/img/WCA.svg').scaled(self.logo.width(), self.logo.height()))  # 添加logo
        self.doShow()   # 淡入
        self.init_ui()  # 初始化界面
        # index(self.username)
        # widget美化
        Qss = 'QWidget#widget{background-color:%s;}' % TITLE_COLOR
        Qss += 'QWidget#widget_2{background-color:%s;}' % GRAY_COLOR
        Qss += 'QWidget#widget_3{background-color:%s;}' % BACKGROUND_COLOR
        Qss += '#save_btn{background-color:%s; border-radius:10px;}' % (TITLE_COLOR)
        Qss += '#save_btn:hover{background-color:%s; border-radius:10px;}' % (FUNC_COLOR)
        
        for btn in self.left_column:
            Qss += '#%s{background-color:%s; border-radius:0;}' % (
                btn, GRAY_COLOR)
            Qss += '#%s:hover{background-color:%s; border-radius:0;}' % (
                btn, LIGHT_FUNC_COLOR)
            eval(f'self.{btn}').setCursor(QCursor(Qt.PointingHandCursor))  # 鼠标悬停按钮上时变小手
        Qss += global_css()
        self.setStyleSheet(Qss)  # 边框部分qss重载

        # 所有按钮的初始化
        self.minButton.clicked.connect(self.showMinimized)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.clicked.connect(self.doClose)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.oll_btn.clicked.connect(lambda: self.btn_left('oll_btn'))
        self.pll_btn.clicked.connect(lambda: self.btn_left('pll_btn'))
        self.save_btn.clicked.connect(self.save_db)
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))

    def init_ui(self):
        """初始化界面
        """
        self.oll_btn.setStyleSheet('#oll_btn{background-color:%s; color:%s; border-left:6px solid %s}' 
                                    % (FUNC_COLOR, HOVER_COLOR, HOVER_COLOR))
        for btn in self.left_column:  # 其他按钮全部恢复
            if btn != 'oll_btn':
                eval(f'self.{btn}').setStyleSheet(
                    '#%s{background-color:%s; border-radius:0;}' % (btn, GRAY_COLOR))
        self.stackedWidget.setCurrentIndex(0)
        self.init_table("oll")
        self.init_table("pll")

    def save_db(self):
        """将表格内容保存到数据库
        """
        conn = sqlite3.connect(srDB)
        cursor = conn.cursor()

        # 保存oll-alg
        for i in range(57):
            name = f"oll{i+1}"
            cursor.execute(f'UPDATE ollTable SET alg="{self.oll_table.item(i, 1).text()}" WHERE name="{name}"')
            conn.commit()
        # 保存pll-alg
        for i in range(21):
            name = self.pll_table.item(i, 0).text()
            cursor.execute(f'UPDATE pllTable SET alg="{self.pll_table.item(i, 2).text()}" WHERE name="{name}"')
            conn.commit()
            i += 1
        
        self.info = Info_Dialog()
        self.info.label.setText("Save Successfully")
        self.info.show()

        conn.close()
        self.doClose()


    def init_table(self, table_name):
        """表格初始化

        Args:
            table_name (str): 表名，oll或pll
        """
        if table_name == 'oll':
            row_count = 57
            self.oll_table.clear()  # 表格先清空
            self.oll_table.setRowCount(row_count)
            # 设置表格每项大小
            self.oll_table.setColumnWidth(0, 110)
            self.oll_table.setColumnWidth(1, 800)
            for i in range(row_count):
                self.oll_table.setRowHeight(i, 100)
            self.oll_table.setHorizontalHeaderLabels(['OLL', 'Algorithm'])
            self.oll_table.verticalHeader().setVisible(False)  # 隐藏水平头标签
            self.oll_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置为整行选中
            self.oll_table.setSelectionMode(QAbstractItemView.NoSelection)
            self.oll_table.setShowGrid(False)  # 不显示网格
            self.oll_table.setIconSize(QSize(100, 100))
            # 设置oll图标
            for i in range(1, 58):
                item = QTableWidgetItem()
                icon = QIcon(f"{ABSOLUTE_PATH}\\img\\oll\\oll{i}.svg")
                item.setIcon(QIcon(icon))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # 设置不可编辑
                self.oll_table.setItem(i-1, 0, item)
        else:
            row_count = 21
            self.pll_table.clear()  # 表格先清空
            self.pll_table.setRowCount(row_count)
            # 设置表格每项大小
            self.pll_table.setColumnWidth(0, 60)
            self.pll_table.setColumnWidth(1, 110)
            self.pll_table.setColumnWidth(2, 740)
            for i in range(row_count):
                self.pll_table.setRowHeight(i, 100)
            self.pll_table.setHorizontalHeaderLabels(['Name', "PLL", 'Algorithm'])
            self.pll_table.verticalHeader().setVisible(False)  # 隐藏水平头标签
            self.pll_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置为整行选中
            self.pll_table.setSelectionMode(QAbstractItemView.NoSelection)
            self.pll_table.setShowGrid(False)  # 不显示网格
            self.pll_table.setIconSize(QSize(100, 100))
            # 设置pll图标
            for _, _, files in os.walk(f"{ABSOLUTE_PATH}\\img\\pll"):
                i = 0
                for f in files:
                    item1 = QTableWidgetItem()
                    item1.setFont(QFont('Microsoft YaHei', 12, QFont.Black))
                    item1.setText(f.split(".")[0])
                    item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # 设置不可编辑
                    self.pll_table.setItem(i, 0, item1)

                    item2 = QTableWidgetItem()
                    icon = QIcon(f"{ABSOLUTE_PATH}\\img\\pll\\{f}")
                    item2.setIcon(QIcon(icon))
                    item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # 设置不可编辑
                    self.pll_table.setItem(i, 1, item2)
                    i += 1
        self.alg_show(table_name)


    def alg_show(self, table_name):
        """从数据库读取公式并显示在表格上

        Args:
            table_name (str): 表名，oll或pll
        """
        conn = sqlite3.connect(srDB)
        cursor = conn.cursor()

        if table_name == 'oll':
            for i in range(1, 58):
                item = QTableWidgetItem()
                cursor.execute(f"SELECT alg FROM ollTable WHERE name='oll{i}'")
                temp = cursor.fetchall()[0][0]
                item.setFont(QFont('Microsoft YaHei', 12, QFont.Black))
                item.setText(temp)
                self.oll_table.setItem(i-1, 1, item)
            
        else:
            for _, _, files in os.walk(f"{ABSOLUTE_PATH}\\img\\pll"):
                i = 0
                for f in files:
                    item = QTableWidgetItem()
                    item.setFont(QFont('Microsoft YaHei', 12, QFont.Black))
                    pll = f.split(".")[0]
                    cursor.execute(f"SELECT alg FROM pllTable WHERE name='{pll}'")
                    temp = cursor.fetchall()[0][0]
                    item.setText(temp)
                    self.pll_table.setItem(i, 2, item)
                    i += 1

        conn.close()


    def btn_left(self, left_btn):
        """左边栏按钮对应事件
        """
        # index(self.username)
        eval(f'self.{left_btn}').setStyleSheet('#%s{background-color:%s; color:%s; border-left:6px solid %s}' %
                                            (left_btn, FUNC_COLOR, HOVER_COLOR, HOVER_COLOR))  # 当前点击按钮高亮
        for btn in self.left_column:  # 其他按钮全部恢复
            if btn != left_btn:
                eval(f'self.{btn}').setStyleSheet(
                    '#%s{background-color:%s; border-radius:0;}' % (btn, GRAY_COLOR))
        self.stackedWidget.setCurrentIndex(self.left_column[left_btn])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    alg_window = Alg_window('2018SHEN04')
    alg_window.show()

    sys.exit(app.exec_())