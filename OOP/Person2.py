# 学习__slots__ 的用法，限定类实例可添加的属性
class Person2(object):
    __slots__ = ('name', 'age')

    # 重写str方法，打印实例
    def __str__(self):
        return 'name: %s, age:%s' % (self.name, self.age)


if __name__ == '__main__':
    p2 = Person2()
    p2.name = "张迪"
    p2.age = '25'
    # __slots__ 限定了当前类实例能添加的属性只有name和age,添加额外属性会报错
    print(p2)
