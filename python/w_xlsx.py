import os
from openpyxl import Workbook

def write_pwd_to_excel(file_path):
    # 检查文件是否存在，如果不存在则创建一个新的Excel文件
    if not os.path.exists(file_path):
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["PWD"])
    else:
        workbook = load_workbook(file_path)
        sheet = workbook.active
    
    # 执行pwd命令获取当前目录
    pwd = os.getcwd()
    
    # 将获取到的目录写入Excel文件的新一行
    sheet.append([pwd])
    
    # 保存Excel文件
    workbook.save(file_path)

# 指定Excel文件路径
file_path = "path/to/your/excel/file.xlsx"

# 调用函数将当前目录写入Excel文件
write_pwd_to_excel(file_path)