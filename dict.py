#!/usr/bin/env python

dict1 = {"Alice":"1993",'Beth': '9102', 'Cecil': '3258'}
print(dict1['Alice'])
#print(dict1['huang'])
##更新Beth的值
dict1['Beth'] = 32;
##新增信息
dict1['school'] = '菜鸟教程'
print(dict1['Beth'])
print(dict1['school'])
print(dict1)

for i in dict1:
    print("key: %s, value: %s"%(i,dict1[i]))