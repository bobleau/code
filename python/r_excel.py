import os
import openpyxl

path = r"/home/bob/code/python"
os.chdir(path)  # 修改工作路径

workbook = openpyxl.load_workbook('test.xlsx')  # 返回一个workbook数据类型的值
sheet = workbook.active  # 获取活动表
print('当前活动表是：')
print(sheet)

table = sheet['A1:A5']  # 获取A1到A5的数据，返回工作表的二维数组

print(table)

# 打印A1到A5的数据
for row in table: # 从表中逐行遍历
    for cell in row: # 从每行中逐个遍历
        print(cell.value)
