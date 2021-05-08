# 学习@Property
class Person3(object):
    @property
    def name(self):
        return self.nameP

    @name.setter
    def name(self, value):
        self.nameP = value

    @property
    def age(self):
        return self.ageP

    @age.setter
    def age(self, value):
        self.ageP = value

    # 打印对象示例显示的内容，类似于java的toString
    def __str__(self):
        return 'name: %s;age: %d' % (self.nameP, self.ageP)

    # 实例显示内容
    __repr__ = __str__


if __name__ == '__main__':
    p3 = Person3()
    p3.name = "张迪"
    p3.age = 25

    print(p3)
