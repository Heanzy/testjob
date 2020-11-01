from PyQt5.QtWidgets import *
from gui.Table import Tableview

def selected_tb_text(table_view):
    try:
        indexes = table_view.selectedIndexes()  # 获取表格对象中被选中的数据索引列表
        indexes_dict = {}
        for index in indexes:  # 遍历每个单元格
            row, column = index.row(), index.column()  # 获取单元格的行号，列号
            if row in indexes_dict.keys():
                indexes_dict[row].append(column)
            else:
                indexes_dict[row] = [column]

        # 将数据表数据用制表符(\t)和换行符(\n)连接，使其可以复制到excel文件中
        text = ''
        for row, columns in indexes_dict.items():
            row_data = ''
            for column in columns:
                data = table_view.model.item(row, column).text() if table_view.model.item(row, column) else ""
                if row_data:
                    row_data = row_data + '\t' + data
                else:
                    row_data = data

            if text:
                text = text + '\n' + row_data
            else:
                text = row_data
        return text
    except BaseException as e:
        print(e)
        return ''

