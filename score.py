#-*- coding utf-8 -*-

score = int(input("请输入你的成绩:"))
if score < 0 or score > 100:
    print("您好，你的成绩属于无效分数")
elif score < 60:
    print("您好，你的成绩不及格")
elif score < 70:
    print("您好，你的成绩及格")
elif score < 80:
    print("您好，你的成绩良好")
else:
    print("您好，你的成绩优秀")



age = int(input("请输入你狗狗的年龄："))
print("")
if age < 0:
  print("你的狗狗年龄很小哦")
elif age > 10:
  print("你的狗狗年龄有点大了")
elif age == 2:
  human = 22 + (age - 2) * 5
  print("真可爱",human)


n = 100
sum = 0
counter = 1
while counter <= n:
  sum = sum + counter
  counter += 1
print("1 到 %d 之和为：%d "%(n,sum))



from functools import reduce
###1*100之积
def mult(begin, end):
  L = range(begin, end + 1)

  def multiFn(x, y):
    return x * y

  return reduce(multiFn, L)

print('mult = ', mult(1, 10))
