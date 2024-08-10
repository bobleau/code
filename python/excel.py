# python按行append写入内容到file文件中
import openpyxl
openpyxl.load_workbook(file).active.append(row).save(file)