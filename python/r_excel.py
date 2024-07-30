import os
import openpyxl

path = r"/home/bob/code"
os.chdir(path)  # 修改工作路径

workbook = openpyxl.load_workbook('test.xlsx')  # 返回一个workbook数据类型的值
sheet = workbook.active  # 获取活动表
print('当前活动表是：')
print(sheet)

cell = sheet['A1:A5']  # 获取A1到A5的数据

print(cell)

# 打印A1到A5的数据
for i in cell:
    print(i.value)
