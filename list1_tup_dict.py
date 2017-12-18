#!/usr/bin/env python


list1 = ["Google","IE",333,0.23,"我们"]
#
# for lists in list1:
#     print(lists)



list2 = ["Google","IE",333,0.23,"我们"]
# print(list2[0])
# print(list2[0:3])
# print(list2[:2])
# print(list2[0:3])

print(list2)
list2.insert(0,'lam')
print(list2)

print(list1)
list1.pop()
print(list1)

print(list1)
list1.pop(2)
print(list1)

##合并列表
list2 = ["Google","IE",333,0.23,"我们"]
list1 = ["apple", "orange", "pear", "banana"]

for i in list1:
    list2.append(i)
print(list2)