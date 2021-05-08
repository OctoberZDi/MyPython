class Person(object):
    # 定义一个类属性
    name = 'aa'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 定义一个类函数，第一个参数永远是实例变量self
    def printInfo(self):
        print('%s: %s' % (self.__name, self.__age))

    def getAgeEx(self):
        if self.__age <= 18:
            return '%s 了,小伙子还未成年啊！' % self.__age
        elif self.__age < 30:
            return '%s 了,年轻人，30而立了没!' % self.__age
        else:
            return '%s 了,继续努力吧！' % self.__age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if 0 <= age < 150:
            self.__age = age
        else:
            raise ValueError('bad age')

    def setName(self, name):
        self.__name = name


# 普通函数
def test2():
    print('this is test2')


if __name__ == '__main__':
    p = Person("张迪", 18)
    # name,age被定义成了__所以此处实例p无法访问
    print('姓名:' + p.getName() + '年龄：%d' % p.getAge())
    p.setName("张筱满")
    p.setAge(2)
    # 拼接字符串比较特殊
    print('姓名:' + p.getName(), '年龄：' + str(p.getAge()))
    # 打印
    p.printInfo()
    # getAge
    print(p.getAgeEx())
