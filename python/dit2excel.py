import openpyxl

data = [
    {'name': 'Alice', 'age': 25, 'gender': 'Female'},
    {'name': 'Bob', 'age': 30, 'gender': 'Male'},
    {'name': 'Catherine', 'age': 28, 'gender': 'Female'}
]

workbook = openpyxl.Workbook()
worksheet = workbook.active

header = list(data[0].keys())
worksheet.append(header)

for d in data:
    row = list(d.values())
    worksheet.append(row)

workbook.save('data.xlsx')


准备工作

在开始编写代码之前，我们需要先安装openpyxl库，这是一个用于读写Excel文件的第三方库。你可以在终端中运行以下命令来安装它：

pip install openpyxl
Bash
安装完成后，我们就可以开始编写代码了。

4. 代码实现

首先，我们需要导入需要的库：

import openpyxl
Python
然后，假设我们有一个包含多个字典的列表，每个字典代表一个人的信息。每个字典有相同的键，如'name'、'age'、'gender'等：

data = [
    {'name': 'Alice', 'age': 25, 'gender': 'Female'},
    {'name': 'Bob', 'age': 30, 'gender': 'Male'},
    {'name': 'Catherine', 'age': 28, 'gender': 'Female'}
]
Python
接下来，我们创建一个新的Excel文件，并选择其中的一个工作表：

workbook = openpyxl.Workbook()
worksheet = workbook.active
Python
然后，我们将列表中的第一个字典的键作为Excel表格的表头，并将其写入到工作表的第一行：

header = list(data[0].keys())
worksheet.append(header)
Python
接下来，我们需要逐行写入字典中的值。我们可以使用一个循环来遍历列表，并使用worksheet.append()方法将每个字典的值写入一个新的行：

for d in data:
    row = list(d.values())
    worksheet.append(row)
Python
最后，我们将数据保存到Excel文件中：

workbook.save('data.xlsx')
Python
