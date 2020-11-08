import sys
import sqlite3
from pprint import pprint

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
from UI.Ui_input_alg import *
from alg_import import *

srDB = "./srDB.db"

class Main_window(BasicWindow, Ui_MainWindow):
    def __init__(self, user_name, parent=None):
        super(Main_window, self).__init__(parent)
        self.setupUi(self)
        self.user_name = user_name
        self.id.setText(self.user_name)
        self.pages = []
        self.tables = []
        self.left_buttons = []

        self.logo.setPixmap(QPixmap(f'{ABSOLUTE_PATH}/img/WCA.svg').scaled(self.logo.width(), self.logo.height()))  # 添加logo
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
        self.init_table()
        self.stackedWidget.setCurrentIndex(0)
        
    def init_table(self):
        """所有解法表格初始化
        """
        conn = sqlite3.connect(srDB)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM solveTable')
        raw_solves = cursor.fetchall()
        # pprint(raw_solves)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setGeometry(QRect(10, 10, 951, 631))

        if len(raw_solves):
            # 左边栏
            self.contents_table.setRowCount(len(raw_solves))
            self.contents_table.setColumnCount(1)
            self.contents_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.contents_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.contents_table.verticalHeader().setVisible(False)  #隐藏垂直头标签
            self.contents_table.horizontalHeader().setVisible(False)

            for i, raw_solve in enumerate(raw_solves):
                # stack中的具体解法
                time = raw_solve[1]
                date = raw_solve[2]
                date_list = date.split("-")
                date = date_list[0] + '-'
                if len(date_list[1]) == 1:
                    date += '0'
                date = date + date_list[1] + '-'
                if len(date_list[2]) == 1:
                    date += '0'
                date += date_list[2]
                # scramble = raw_solve[0]
                # inspection = raw_solve[3]
                # cross = raw_solve[4]
                # f2l = []
                # for j in [5, 6, 7, 8]:
                #     f2l.append(raw_solve[j])
                # oll = raw_solve[9]
                # pll = raw_solve[10]
                # auf = raw_solve[11]
                etm = raw_solve[12]
                tps = raw_solve[13]
                self.pages.append(QWidget())
                self.tables.append(QTableWidget(self.pages[i]))
                self.tables[i].setGeometry(QRect(0, 0, 951, 631))
                self.stackedWidget.addWidget(self.pages[i])
                
                self.tables[i].clear()
                self.tables[i].setColumnCount(1)
                self.tables[i].setRowCount(11)
                self.tables[i].setColumnWidth(0, 880)
                self.tables[i].horizontalHeader().setVisible(False)
                self.tables[i].setVerticalHeaderLabels(['', 'Scramble', 'Inspection', 'Cross', '1st Pair', '2nd Pair', '3rd Pair', '4th Pair', 'OLL', 'PLL', 'Auf'])
                # 设置表头字体
                self.tables[i].verticalHeader().setStyleSheet(
                    "QHeaderView::section{background-color:%s; font:10pt 'Microsoft YaHei'; color: black; border:0};" % (BACKGROUND_COLOR))
                self.tables[i].setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置为整行选中
                # self.tables[i].setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格禁止编辑
                self.tables[i].setSelectionMode(QAbstractItemView.NoSelection)
                self.tables[i].setShowGrid(False)  # 不显示网格
                for j in range(11):
                    self.tables[i].setRowHeight(j, 57)

                new = QTableWidgetItem(f"      {time}         {date}         {etm} ETM - {tps} TPS")
                new.setFont(QFont('Microsoft YaHei', 12))
                self.tables[i].setItem(0, 0, new)
                k = 1
                for j in [0]+list(range(3, 12)):
                    new = QTableWidgetItem(f"      {raw_solve[j]}")
                    new.setFont(QFont('Microsoft YaHei', 12))
                    self.tables[i].setItem(k, 0, new)
                    k += 1

                # 左边栏对应button
                btn_name = f"{time}      {date}"
                new_btn = QCommandLinkButton(btn_name)
                new_btn.setFont(QFont('Microsoft YaHei UI Light', 10))
                new_btn.setObjectName(str(i))
                new_btn.setIcon(QIcon(f"{ABSOLUTE_PATH}\\img\\course.svg"))
                new_btn.setCursor(QCursor(Qt.PointingHandCursor))
                new_btn.clicked.connect(lambda: self.btn_solve(self.sender().objectName()))
                self.left_buttons.append(new_btn)
                self.contents_table.setCellWidget(i, 0, new_btn)
        conn.close()

    def add_solve(self):
        """点击添加解法按钮事件
        """
        self.add_window = Add_window()
        self.add_window.show()
        self.add_window.signal.connect(self.add_item)

    def add_item(self, scramble):
        """添加一条解法
        """
        conn = sqlite3.connect(srDB)
        cursor = conn.cursor()

        self.contents_table.setRowCount(self.contents_table.rowCount() + 1)
        cursor.execute(f'SELECT * FROM solveTable WHERE scramble="{scramble}"')
        temp = cursor.fetchall()[0]
        # print(temp)
        time = temp[1]
        date = temp[2]
        date_list = date.split("-")
        date = date_list[0] + '-'
        if len(date_list[1]) == 1:
            date += '0'
        date = date + date_list[1] + '-'
        if len(date_list[2]) == 1:
            date += '0'
        date += date_list[2]
        etm = temp[12]
        tps = temp[13]
        i = len(self.pages)
        self.pages.append(QWidget())
        self.tables.append(QTableWidget(self.pages[i]))
        self.tables[i].setGeometry(QRect(0, 0, 951, 631))
        self.stackedWidget.addWidget(self.pages[i])
        
        self.tables[i].clear()
        self.tables[i].setColumnCount(1)
        self.tables[i].setRowCount(11)
        self.tables[i].setColumnWidth(0, 880)
        self.tables[i].horizontalHeader().setVisible(False)
        self.tables[i].setVerticalHeaderLabels(['', 'Scramble', 'Inspection', 'Cross', '1st Pair', '2nd Pair', '3rd Pair', '4th Pair', 'OLL', 'PLL', 'Auf'])
        # 设置表头字体
        self.tables[i].verticalHeader().setStyleSheet(
            "QHeaderView::section{background-color:%s; font:10pt 'Microsoft YaHei'; color: black; border:0};" % (BACKGROUND_COLOR))
        self.tables[i].setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置为整行选中
        # self.tables[i].setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格禁止编辑
        self.tables[i].setSelectionMode(QAbstractItemView.NoSelection)
        self.tables[i].setShowGrid(False)  # 不显示网格
        for j in range(11):
            self.tables[i].setRowHeight(j, 57)

        new = QTableWidgetItem(f"      {time}         {date}         {etm} ETM - {tps} TPS")
        new.setFont(QFont('Microsoft YaHei', 12))
        self.tables[i].setItem(0, 0, new)
        k = 1
        for j in [0]+list(range(3, 12)):
            new = QTableWidgetItem(f"      {temp[j]}")
            new.setFont(QFont('Microsoft YaHei', 12))
            self.tables[i].setItem(k, 0, new)
            k += 1

        # 左边栏对应button
        btn_name = f"{time}      {date}"
        new_btn = QCommandLinkButton(btn_name)
        new_btn.setFont(QFont('Microsoft YaHei UI Light', 10))
        new_btn.setObjectName(str(i))
        new_btn.setIcon(QIcon(f"{ABSOLUTE_PATH}\\img\\course.svg"))
        new_btn.setCursor(QCursor(Qt.PointingHandCursor))
        new_btn.clicked.connect(lambda: self.btn_solve(self.sender().objectName()))
        self.left_buttons.append(new_btn)
        self.contents_table.setCellWidget(i, 0, new_btn)
        conn.close()

    def show_alg(self):
        """打开公式编辑界面
        """
        self.alg_window = Alg_window(self.user_name)
        self.alg_window.show()

    def btn_solve(self, solve_id):
        """切换解法
        """
        self.stackedWidget.setCurrentIndex(int(solve_id))


class Add_window(BasicWindow, Ui_AddSolveWindow):
    signal = QtCore.pyqtSignal(str)     # 告知主页面解法已经存入数据库，使得主页面进行刷新
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
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnWidth(0, 400)
        self.tableWidget.setColumnWidth(1, 95)
        self.tableWidget.setHorizontalHeaderLabels(['Moves', 'Preparation'])
        self.tableWidget.setVerticalHeaderLabels(['Time', 'Date', 'Scramble', 'Inspection', 'Cross', '1st Pair', '2nd Pair', '3rd Pair', '4th Pair', 'OLL', 'PLL', 'Auf'])
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置为整行选中
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(False)  # 不显示网格
        for i in range(12):
            self.tableWidget.setRowHeight(i, 40)

        # 设置某些单元格不可编辑
        rows = list(range(9)) + [11]
        for i in rows:
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 1, item)
        
        # 日期选择
        self.date_edit = QDateTimeEdit(QDate.currentDate(), self.tableWidget)
        self.date_edit.setDisplayFormat("yyyy-MM-dd")
        self.date_edit.setCalendarPopup(True)
        self.tableWidget.setCellWidget(1, 0, self.date_edit)
        
        # oll和pll按钮
        self.oll_btn = QPushButton(self.tableWidget)
        self.oll_btn.setText("Choose OLL")
        self.oll_btn.setFont(QFont('Microsoft YaHei', 10))
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
        self.tableWidget.setCellWidget(9, 0, self.oll_btn)

        self.pll_btn = QPushButton(self.tableWidget)
        self.pll_btn.setText("Choose PLL")
        self.pll_btn.setFont(QFont('Microsoft YaHei', 10))
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
        self.tableWidget.setCellWidget(10, 0, self.pll_btn)

    def add_solve(self):
        """将解法导入数据库
        """
        conn = sqlite3.connect(srDB)
        cursor = conn.cursor()
        try:
            scramble = self.tableWidget.item(2, 0).text().strip()
        except:
            self.warn_window = Warn_Dialog()
            self.warn_window.label.setText('Please input a scamble!')
            self.warn_window.show()
            return
        
        if self.tableWidget.item(0, 0) != None:
            solve_time = self.tableWidget.item(0, 0).text().strip()
        else:
            solve_time = '9999'

        _date = self.date_edit.date()
        date_time = f"{_date.year()}-{_date.month()}-{_date.day()}"
        # print(date_time)

        if self.tableWidget.item(3, 0) != None:
            inspection = self.tableWidget.item(3, 0).text().strip()
        else:
            inspection = '/'

        if self.tableWidget.item(4, 0) != None:
            cross = self.tableWidget.item(4, 0).text().strip()
        else:
            cross = '/'

        f2l = []
        for i in [5, 6, 7, 8]:
            if self.tableWidget.item(i, 0) != None:
                f2l.append(self.tableWidget.item(i, 0).text().strip())
            else:
                f2l.append('/')
        
        # 检查有没有选择OLL
        if self.oll_btn.text() == 'Choose OLL':
            self.warn_window = Warn_Dialog()
            self.warn_window.label.setText('ILLEGAL OLL!')
            self.warn_window.show()
            return
        if self.tableWidget.item(9, 1) != None:
            oll = f"{self.tableWidget.item(9, 1).text().strip()} {self.oll_btn.text().strip()}"
        else:
            oll = self.oll_btn.text().strip()

        # 检查有没有选择PLL
        if self.pll_btn.text() == 'Choose PLL':
            self.warn_window = Warn_Dialog()
            self.warn_window.label.setText('ILLEGAL PLL!')
            self.warn_window.show()
            return
        if self.tableWidget.item(10, 1) != None:
            pll = f"{self.tableWidget.item(10, 1).text().strip()} {self.pll_btn.text().strip()}"
        else:
            pll = self.pll_btn.text().strip()
        # print(oll, '\n', pll)

        if self.tableWidget.item(11, 0) != None:
            auf = self.tableWidget.item(11, 0).text().strip()
        else:
            auf = '/'

        etm = 0
        if cross != '\\' and cross != '/':
            etm += len(cross.split(' '))
        for i in range(4):
            if f2l[i] != '\\' and f2l[i] != '/':
                etm += len(f2l[i].split(' '))    
        if not 'Skip' in oll:
            etm += len(oll.split(' '))
        if not 'Skip' in pll:
            etm += len(pll.split(' '))
        if auf != '\\' and auf != '/':
            etm += len(auf.split(' '))

        # if cross != '\\' and cross != '/':
        #     print(f"{cross}: {len(cross.split(' '))}")
        # for i in range(4):
        #     if f2l[i] != '\\' and f2l[i] != '/':
        #         print(f"{f2l[i]}: {len(f2l[i].split(' '))}")
        # if not 'Skip' in oll:
        #     print(f"{oll}: {len(oll.split(' '))}")
        # if not 'Skip' in pll:
        #     print(f"{pll}: {len(pll.split(' '))}")
        # if auf != '\\' and auf != '/':
        #     print(f"{auf}: {len(auf.split(' '))}")

        tps = round(etm / float(solve_time), 2)

        # print(
        #     f"""
        #     scramble={scramble}\n
        #     time={solve_time}\n 
        #     date={date_time}\n
        #     inspection={inspection}\n
        #     cross="{cross}"\n
        #     f2l1="{f2l[0]}"\n
        #     f2l2="{f2l[1]}"\n
        #     f2l3="{f2l[2]}"\n
        #     f2l4="{f2l[3]}"\n
        #     oll="{oll}"\n
        #     pll="{pll}"\n
        #     auf="{auf}"\n
        #     etm="{etm}"\n
        #     tps="{tps}" 
        # """)

        try:
            cursor.execute(f'INSERT INTO solveTable(scramble) VALUES("{scramble}")')
            conn.commit()
        except:
            self.warn_window = Warn_Dialog()
            self.warn_window.label.setText('Do not import SAME scramble!')
            self.warn_window.show()
            return
        
        cursor.execute(
            f'''UPDATE solveTable SET 
            time="{solve_time}", 
            date="{date_time}",
            inspection="{inspection}",
            cross="{cross}",
            f2l1="{f2l[0]}",
            f2l2="{f2l[1]}",
            f2l3="{f2l[2]}",
            f2l4="{f2l[3]}",
            oll="{oll}",
            pll="{pll}",
            auf="{auf}",
            etm="{etm}",
            tps="{tps}" 
            WHERE scramble="{scramble}"''')
        conn.commit()
        conn.close()

        self.signal.emit(scramble)

        self.success_info = Info_Dialog()
        self.success_info.label.setText("Add Solve Successfully")
        self.success_info.show()

        self.doClose()

    def choose_oll(self):
        """OLL选择界面
        """
        self.oll_window = OLL_window()
        self.oll_window.show()
        self.oll_window.signal.connect(self.get_oll)

    def get_oll(self, name):
        if name == 'skip':
            self.oll_btn.setText('OLL Skip')
        elif name == 'input':
            self.input_window = Input_window()
            self.input_window.show()
            self.input_window.signal.connect(self.get_input_oll)
        else:
            conn = sqlite3.connect(srDB)
            cursor = conn.cursor()
            cursor.execute(f"SELECT alg FROM ollTable WHERE name='{name}'")
            alg = cursor.fetchall()[0][0]
            self.oll_btn.setText(alg)
            conn.close()

    def get_input_oll(self, alg):
        self.oll_btn.setText(alg)

    def choose_pll(self):
        """PLL选择界面
        """
        self.pll_window = PLL_window()
        self.pll_window.show()
        self.pll_window.signal.connect(self.get_pll)

    def get_pll(self, name):
        if name == 'skip':
            self.pll_btn.setText('PLL Skip')
        elif name == 'input':
            self.input_window = Input_window()
            self.input_window.show()
            self.input_window.signal.connect(self.get_input_pll)
        else:
            conn = sqlite3.connect(srDB)
            cursor = conn.cursor()
            cursor.execute(f"SELECT alg FROM pllTable WHERE name='{name}'")
            alg = cursor.fetchall()[0][0]
            self.pll_btn.setText(alg)
            conn.close()

    def get_input_pll(self, alg):
        self.pll_btn.setText(alg)


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
        # 跳O
        new = new = QPushButton(self.tableWidget)
        new.setObjectName("skip")
        new.setText("Skip")
        new.setFont(QFont('Microsoft YaHei', 12))
        new.setCursor(QCursor(Qt.PointingHandCursor))
        new.clicked.connect(lambda: self.select_oll(self.sender()))
        self.tableWidget.setCellWidget(j, k, new)
        temp = k
        k = k + 1 if k < 5 else 0
        j = j + 1 if k - temp != 1 else j

        # 自行输入公式
        new = new = QPushButton(self.tableWidget)
        new.setObjectName("input")
        new.setText("Input")
        new.setFont(QFont('Microsoft YaHei', 12))
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
        # 跳P
        new = new = QPushButton(self.tableWidget)
        new.setObjectName("skip")
        new.setText("Skip")
        new.setFont(QFont('Microsoft YaHei', 12))
        new.setCursor(QCursor(Qt.PointingHandCursor))
        new.clicked.connect(lambda: self.select_pll(self.sender()))
        self.tableWidget.setCellWidget(j, k, new)
        temp = k
        k = k + 1 if k < 5 else 0
        j = j + 1 if k - temp != 1 else j

        # 自行输入公式
        new = new = QPushButton(self.tableWidget)
        new.setObjectName("input")
        new.setText("Input")
        new.setFont(QFont('Microsoft YaHei', 12))
        new.setCursor(QCursor(Qt.PointingHandCursor))
        new.clicked.connect(lambda: self.select_pll(self.sender()))
        self.tableWidget.setCellWidget(j, k, new)

    def select_pll(self, btn):
        pll_name = btn.objectName()
        self.signal.emit(pll_name)
        self.doClose()


class Input_window(BasicWindow, Ui_InputWindow):
    signal = QtCore.pyqtSignal(str)     # 向父窗口传值
    def __init__(self, parent=None):
        super(Input_window, self).__init__(parent)
        self.setupUi(self)
        self.doShow()
        Qss = global_css()
        Qss += 'QWidget#widget_3{background-color:%s;}' % TITLE_COLOR
        Qss += 'QWidget#widget{background-color:%s;}' % BACKGROUND_COLOR
        self.setStyleSheet(Qss)  # 边框部分qss重载

        # 所有按钮的初始化
        self.minButton.clicked.connect(self.showMinimized)
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.clicked.connect(self.doClose)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ok_btn.clicked.connect(self.input_alg)
        self.ok_btn.setCursor(QCursor(Qt.PointingHandCursor))

    def input_alg(self):
        if self.lineEdit != None:
            self.signal.emit(self.lineEdit.text())
            self.doClose()
        else:
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Main_window('2018SHEN04')
    main_window.show()

    # main_window = Add_window()
    # main_window.show()

    sys.exit(app.exec_())