# class 关键字；Person类名，一般大写；(object）表示该类从哪个类集成袭来。
class Person(object):
    # 定义一个类属性
    __name1 = 'aa'

    # 特殊方法“__init__”前后分别有两个下划线！！
    # 创建实例的时候，绑定一些属性
    # 第一个参数永远是self，表示创建的实例本身，在__init__内部可以把各种属性绑定到self
    # 因为self就指向创建的实例本身

    # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
    # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
    # 只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 定义一个类函数，第一个参数永远是实例变量self
    def printInfo(self):
        print('%s: %s' % (self.__name, self.__age))

    def getNameLength(self):
        return "名称长度：%d" % len(self.__name)

    def getNameEx(self):
        if len(self.__name) > 5:
            return "%s is to lang...please change it" % self.__name
        elif len(self.__name) > 1:
            return "%s is to short...very good!" % self.__name
        else:
            raise ValueError("bad value")

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
# 和普通的函数相比，
# 在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
# 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，
# 所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
def test2():
    print('this is test2')


if __name__ == '__main__':
    p = Person("张迪", 18)
    # name,age被定义成了__所以此处实例p无法访问
    print('姓名:' + p.getNameEx() + ' 年龄：%d' % p.getAge())
    p.setName("张筱满")
    p.setAge(2)
    # 拼接字符串比较特殊
    print('姓名:' + p.getName(), ' 年龄：' + str(p.getAge()))
    # 打印
    p.printInfo()
    # getAge
    print(p.getAgeEx())

    print(p.getNameEx())

    print(p.getNameLength())

    p.setName("ambulance 张迪")
    print(p.getNameLength())
