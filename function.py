#!/usr/bin/env python


# 代码作用域
c = 1  # 全局变量

##定义一个函数
def say_hi():
    """表明函数的功能和目的"""
    print("hello world ")
    print("my name is hangpengling")
    print("buy buy world")

# 强制规则：如果参数有默认值，必须在没有默认值后面
def say_hello(name , age=30):
    print("hello {} ！,age is a {}".format(name, age))
    return True  ##返回True

def get_sum(x, y):
    """c 是一个局部变量"""
    global c
    c = x + y
    return c

##修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    c = 10
    def inner():
        nonlocal c   # nonlocal关键字声明
        c = 100
        print(c)
    inner()
    print(c)
outer()


def print_var_params(var1, *var_args, **kw_args):
    """接受可变参数"""
    print(var1)
    for i in var_args:
        print(i)

    for i in kw_args.keys():
        print("{}'s value is {}".format(i, kw_args[i]))


if __name__ == '__main__':
    """入口函数，执行py文件的时候，python解释器会自动去寻找有没有main函数"""
    say_hi()
    print(say_hello("Bella" ))
    #print("函数内是局部变量：",get_sum(6, 5))
    #print("函数内是外部变量：",c)
    outer()
    print_var_params(10)
    print_var_params(10, 50, 60, 70, name="sam", age=16)