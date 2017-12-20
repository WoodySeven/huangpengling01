#!/usr/bin/env python

tup1 = (1, 2, 3, 4, 5, 6, 7, 8)
#print(type(tup1))
print(max(tup1))

tup2 = ('Google', 'Runoob', 1997, 2000)
#print(type(tup2))

tup3 = "a", "b", "c", "d"
print("tup3[0:2]:",tup3[0:2])
print("tup2[0]:",tup2[0])

tup4 = tup2 + tup3
print(tup4)
del tup4


print(len(tup3))