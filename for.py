#!/usr/bin/env python


import random

##input 输入
user_name = input("请输入你的名字:")
print(user_name)
print(type(user_name))

user_age = input("请输入你的年龄:")
print("你的年龄是:%s"%(user_age))
print(type(user_age))

str = "huangpengling"
print(str[0:4])
print(str[::-1])

##写一个程序，猜数字，能够接受用户的输入，并且有一些判断，输出结果
magic_num = random.randint(1,20)

while True:
    user_num = int(input("请你输入1-20的数字："))
    if user_num == magic_num:
        print("恭喜你猜对了！")
        break
    elif user_num < magic_num:
        print("你输入的数字太小了")
    else:
        print("你输入的数字太大了")

a,b = 10,20
print("%s + %s = %s" %(a, b, a+b))
print("{} + {} = {}".format(a, b, a+b))
print("{0} + {1} = {2}".format(a, b, a+b))

##for循环
list1 = ["apple", "orange", "pear", "banana"]
for i in list1:
    print("我不喜欢吃：",i)


##range()函数
range(9)
print(list(range(9)))
for c in range(9):
    print(c)