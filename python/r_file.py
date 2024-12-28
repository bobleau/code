
### 逐行读取文件

# 打开文件（只读模式）
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
# 打印每一行内容
for line in lines:
    print(f"行内容: {line.strip()}")  # strip() 去除行末的换行符



### 读取文本文件

# 打开文件（只读模式）
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
# 打印文件内容
print(f"文件内容: {content}")
