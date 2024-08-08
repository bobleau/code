import os
from openpyxl import load_workbook

path = r"/home/bob/code/python"
os.chdir(path)  # 修改工作路径
file = 'test.xlsx'

workbook = load_workbook(file)  # 返回一个workbook数据类型的值
sheet = workbook.active  # 获取活动表
print('当前活动表是：' + str(sheet))

data = [
    ['素子',23],
    ['巴特',24],
    ['塔奇克马',2]
]
for row in data:
    sheet.append(row)   # 使用append插入数据
workbook.save(file)
