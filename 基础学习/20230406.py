import time
import chardet
import json


dic1 = {"name": "admin", "age": 18}
# 准备一个内置字典的列表
data1 = [{"name":"小米", "age": 19}, {"name":"大米", "age": 20}, {"name":"小圆", "age": 29}]

# 转换成json
json_data1 = json.dumps(data1,ensure_ascii=False)
print(data1)
print(type(dic1))

print(json_data1)
print(type(json_data1))

print("### json string to list ##")
data2 = json_data1
json_data2 = json.loads(data2)
print(data2)
print(type(data2))

print(json_data2)
print(type(json_data2))


# encodeNum = "utf-8"
# f_addr = "/Users/beibeizhang/Desktop"
# file_name = "/test001.txt"
# f = open(f_addr + file_name, 'a', encoding=encodeNum)
# f.write("n\test000002")
# f.write("!!!!")
# f.flush()
# f2 = open(f_addr+ file_name, 'r', encoding=encodeNum)
#print(f2.read())
# data = [{"name": "Amy", "age": 20}, {"name": "Bob", "age": 30}, {"name": "Sam", "age": 5}]
# print(type(data))
#
# json_data1 = json.dumps(data)
# print(type(json_data1))
#


# fileName = "/Users/beibeizhang/Desktop/test0.txt"
# encodeNum = "utf-8"
#
# f = open(fileName, 'r', encoding = encodeNum)
# 统计字数
# str0 = f.read()
# print(str0)
# print(str0.count('happy'))

# substr出现了几次
# count = 0
# for line in f:
#     line = line.strip() # 删除每行的前后空格和换行符
#     words = line.split(' ')
#     print(words)
#     for word in words:
#         if word == "happy":
#             count += 1
#     print(count)
# f.close()

#f = open('/Users/beibeizhang/Desktop/test0.txt', 'r', encoding="utf-8")
#print(f.read())
# print(f.readlines())
# lines = f.readlines()
# print(type(lines))
# print(lines)
# print('*****************')

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1, end='')
# print(line2, end='')
# print(line3, end='')

# i = 1
# for line in f:
#     print(f"第{i}行数据: {line}", end='')
#     i += 1
# # time.sleep(1000)
# f.close()

# i = 1
# with open(fileName, 'r', encoding="utf-8") as f:
#     for line in f:
#         print(f"第{i}行数据: {line}", end='')
#         i+=1
# time.sleep(1000)
#


#
#
# f = open('/Users/beibeizhang/Desktop/动物社团设计.pages', 'r', encoding="utf-16",errors="ignore")
# print(type(f))
# print(f.read())


#
# my_list1 = [1,1,1,1,4,4,4,4,6,6,6,2,3,4,5,11,22,33]
# my_set = set()
#
# for x in my_list1:
#     my_set.add(x)
#
# print(f"my_list1: {my_list1}")
# print(f"my_set: {my_set}")


# str1 = '你好吃，阿奎罗，独立卡嘛'
# print(str1)
#
# result = str1.split('，')
# set1 = {'sad', 'dsa', 'fds', 'sfdew'}
# print(set1, type(set1))
#
# set2 = set()
# print(set2, type(set2))
#
# set1.clear()
# print(set1, type(set1))
#
# print(result)
#
# set3 = {1,2,3,4,5}
# set4 = {2,3,4,5,6,7}
#
# print(set3.difference(set4))

# print(set3)
# set3.discard(3)
# print(set3)
