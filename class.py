#!/usr/bin/env python



class Robot(object):
    """创建一个机器人的类"""
    population = 0 #类的变量

    def __init__(self,name,age):
        """初始化数据"""
        Robot.population += 1
        self.name = name #名称实例变量
        self.age = age #年龄实例变量
        print("(我的名字是:{},{})".format(self.name,age))

    def say_hi(self):#会说话实例方法
        print("{} welcome u".format(self.name))

    def die(self):
        print("精神运气不好，我睡觉啦!".format(self.name))
        Robot.population -= 1
        if Robot.population < 0:
            print("没有机器人可以工作了，需要排队".format(self.name))
        elif Robot.population == 0:
            print("{} 最后一个机器人为你工作".format(self.name))
        else:
            print("还有{:d}个机器人在工作!".format(Robot.population))

    def walk(self):
        print("我现在在走路，稍等为你回复")


##转变为类方法，使用装饰器
    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("我们有 {:d} 个机器人.".format(cls.population))


if __name__ == "__main__":
    huangpengling = Robot("huangpengling",30)
    huangpengling.say_hi()
    huangpengling.die()
    huangpengling.die()
    r1 = Robot("a", 30)
    r2 = Robot("b", 30)
    r3 = Robot("c", 30)
    r4 = Robot("d", 30)
    r1.die()
    r2.die()
    r3.walk()

