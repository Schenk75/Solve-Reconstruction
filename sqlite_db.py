import sqlite3
import os

# 初始化数据库
def init_db(srDB):
    conn = sqlite3.connect(srDB)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE solveTable (
                        scramble text primary key,
                        time text not null,
                        date text not null,
                        inspection text not null,
                        f2l1 text not null,
                        f2l2 text not null,
                        f2l3 text not null,
                        f2l4 text not null,
                        oll text not null,
                        pll text not null,
                        auf text not null,
                        etm text,
                        tps text
                    );''')
    cursor.execute('''CREATE TABLE ollTable (
                        name text PRIMARY KEY,
                        alg text
                    );''')
    cursor.execute('''CREATE TABLE pllTable (
                        name text PRIMARY KEY,
                        alg text
                    );''')
    conn.close()


def op_init(srDB):
    conn = sqlite3.connect(srDB)
    cursor = conn.cursor()
    pll_list = [
        'Aa', 'Ab', 'E', 'F', 'Ga', 'Gb', 'Gc', 'Gd', 'H', 'Ja', 'Jb',
        'Na', 'Nb', 'Ra', 'Rb', 'T', 'Ua', 'Ub', 'V', 'Y', 'Z'
    ]

    for i in range(1, 58):
        cursor.execute(f"INSERT INTO ollTable(name) VALUES('oll{i}')")
    for pll in pll_list:
        cursor.execute(f"INSERT INTO pllTable(name) VALUES('{pll}')")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    filename = 'srDB.db'
    if not os.path.isfile(filename):  # 无文件时创建
        fd = open(filename, mode="w", encoding="utf-8")
        fd.close()
        print('File created!')
        init_db(filename)
        op_init(filename)
    else:
        print('File already exist!')
    
    