# 为单个实例对象添加方法，不会影响该类的其它实例对象；而如果为类动态地添加方法，则所有的实例对象都可以使用。
# 学习__slots__ 的用法，限定类实例可添加的属性
class SlotTest(object):
    __slots__ = ('name', 'age')

    # 重写str方法，打印实例
    def __str__(self):
        return 'name: %s, age:%s' % (self.name, self.age)


def info(self):
    print('正在调用实例方法')


if __name__ == '__main__':
    p2 = SlotTest()
    p2.name = "张迪"
    p2.age = '25'
    # __slots__ 限定了当前类实例能添加的属性只有name和age,添加额外属性会报错
    print(p2)
    p2.say = info
    # p2.say('hello python ,hello slots!')
