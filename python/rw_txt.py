1. 打开和关闭文件

# 打开文件（只读模式）
file_path = 'example.txt'
file = open(file_path, 'r')
# 读取文件内容
content = file.read()
# 关闭文件
file.close()
# 打印文件内容
print(f"文件内容: {content}")
2. 读取文本文件

# 打开文件（只读模式）
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
# 打印文件内容
print(f"文件内容: {content}")
3. 逐行读取文件

# 打开文件（只读模式）
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
# 打印每一行内容
for line in lines:
    print(f"行内容: {line.strip()}")  # strip() 去除行末的换行符
4. 写入文本文件

# 打开文件（写入模式，如果文件存在则清空内容）
file_path = 'output.txt'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("这是一个测试文件。\n")
    file.write("这是第二行内容。\n")
# 打印写入成功的信息
print("文件写入成功。")
5. 追加内容到文件

# 打开文件（追加模式）
file_path = 'output.txt'
with open(file_path, 'a', encoding='utf-8') as file:
    file.write("这是追加的内容。\n")
# 打印追加成功的信息
print("内容追加成功。")
6. 读取文件并统计行数

# 打开文件（只读模式）
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
# 统计行数
line_count = len(lines)
print(f"文件共有 {line_count} 行。")
7. 读取文件并统计字符数

# 打开文件（只读模式）
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
# 统计字符数
char_count = len(content)
print(f"文件共有 {char_count} 个字符。")
8. 读取文件并统计单词数

# 打开文件（只读模式）
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
# 分割内容为单词列表
words = content.split()
# 统计单词数
word_count = len(words)
print(f"文件共有 {word_count} 个单词。")
9. 读取文件并统计特定单词出现的次数

# 打开文件（只读模式）
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
# 要统计的单词
target_word = "测试"
# 统计单词出现的次数
word_count = content.count(target_word)
print(f"单词 '{target_word}' 出现了 {word_count} 次。")
10. 读取文件并替换特定内容

# 打开文件（只读模式）
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
# 要替换的内容
old_text = "旧内容"
new_text = "新内容"
# 替换内容
new_content = content.replace(old_text, new_text)
# 写入新的内容
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)
# 打印替换成功的信息
print(f"文件内容已替换。")
