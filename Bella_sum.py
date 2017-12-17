#!/usr/bin/env python



def sum():
    """定义一个函数"""
    sum = 0
    for n in range(1,101):
        sum = sum + n
    return sum


def sumstartTOEnd(start,end):
    sum = 0
    for n in range(start,end+1,1):
        sum = sum + n
    return  sum




if __name__ == "__main__":
    print(sum())
    print(sumstartTOEnd(1,1000))





