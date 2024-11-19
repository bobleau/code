python 数据处理专题(第 3 天：列表和字典)


目标
熟练使用列表和字典。‍

学习内容
列表的方法（append, extend, pop, remove, sort）
字典的方法（keys, values, items, get, update）‍

示例代码
1. 列表的方法
append 方法
# 创建一个空列表
fruits = []
# 使用 append 方法添加元素
fruits.append("苹果")
fruits.append("香蕉")
fruits.append("橙子")
# 打印列表
print(f"水果列表: {fruits}")
extend 方法
# 创建两个列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# 使用 extend 方法合并列表
list1.extend(list2)
# 打印合并后的列表
print(f"合并后的列表: {list1}")
pop 方法
# 创建一个列表
numbers = [1, 2, 3, 4, 5]
# 使用 pop 方法移除并返回最后一个元素
last_number = numbers.pop()
# 打印移除后的列表和被移除的元素
print(f"移除后的列表: {numbers}")
print(f"被移除的元素: {last_number}")
remove 方法
# 创建一个列表
fruits = ["苹果", "香蕉", "橙子", "香蕉"]
# 使用 remove 方法移除指定元素
fruits.remove("香蕉")
# 打印移除后的列表
print(f"移除后的列表: {fruits}")

sort 方法
# 创建一个列表
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 使用 sort 方法对列表进行排序
numbers.sort()
# 打印排序后的列表
print(f"排序后的列表: {numbers}")
2. 字典的方法
keys 方法
# 创建一个字典
person = {"姓名": "张三", "年龄": 25, "城市": "北京"}
# 使用 keys 方法获取所有键
keys = person.keys()
# 打印所有的键
print(f"字典的键: {list(keys)}")
values 方法
# 创建一个字典
person = {"姓名": "张三", "年龄": 25, "城市": "北京"}
# 使用 values 方法获取所有值
values = person.values()
# 打印所有的值
print(f"字典的值: {list(values)}")
items 方法
# 创建一个字典
person = {"姓名": "张三", "年龄": 25, "城市": "北京"}
# 使用 items 方法获取所有键值对
items = person.items()
# 打印所有的键值对
for key, value in items:
    print(f"{key}: {value}")
get 方法
# 创建一个字典
person = {"姓名": "张三", "年龄": 25, "城市": "北京"}
# 使用 get 方法获取指定键的值
name = person.get("姓名")
city = person.get("城市")
address = person.get("地址", "未知")  # 如果键不存在，返回默认值
# 打印获取的值
print(f"姓名: {name}")
print(f"城市: {city}")
print(f"地址: {address}")
update 方法
# 创建一个字典
person = {"姓名": "张三", "年龄": 25, "城市": "北京"}
# 使用 update 方法更新字典
person.update({"年龄": 26, "职业": "工程师"})
# 打印更新后的字典
print(f"更新后的字典: {person}")


实践
编写一个程序，统计文本文件中每个单词出现的次数。
# 读取文件内容
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
# 将内容分割成单词列表
words = content.split()
# 创建一个字典来存储每个单词的出现次数
word_count = {}
# 遍历单词列表，统计每个单词的出现次数
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# 打印每个单词及其出现次数
for word, count in word_count.items():
    print(f"单词 '{word}' 出现了 {count} 次。")

总结
通过今天的练习，你应该已经熟练掌握了 Python 中列表和字典的基本操作方法。接下来的几天，我们将继续深入学习更多 Python 数据处理的知识。希望你今天的学习顺利！🌟