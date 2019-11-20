# #### !/usr/local/opt/python/bin/python3.7

# # print("Hello, World!")
# print("Hello, World!")
# # print("Hello, World!")
# # print("Hello, World!")
# # print("Hello, World!")

import time

'''
fsdfads
'''

a = 10
b = 4
a, b = b, a

# print(a)
# print(b)

tup2 = (1, 2, 3, 4, 5, 8)
# print (len(tup2))
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果：', fruits[index])

print("good bye!")


a1 = [2, 3, 4, 5]

print(a1[3])
print(fruits[0])


dict = {'a': 5, "b": 90, 'c': 'mmmmmmmm'}
print(dict['c'])


ticks = time.time()

print(ticks)


localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("本地时间为 :", localtime)

# 定义函数


def printme(str):
    "打印任何传入的字符串"
    print('say ==>', str)
    return

printme('ddddddd')

print(2, 3, 4)
