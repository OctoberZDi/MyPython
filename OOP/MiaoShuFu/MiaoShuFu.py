# 描述符类

class RevealAccess(object):
    def __init__(self, initValue=None, name="var"):
        self.value = initValue
        self.name = name

    def __get__(self, instance, owner):
        print("__get__", self.name)
        return self.value

    def __set__(self, instance, value):
        print("__set__", self.name)
        self.value = value


class MyClass:
    x = RevealAccess(10, 'x')
    y = 5


# 如果一个类的某个属性有数据描述符，那么每次查抄这个属性时，都会调用描述符的__get__()方法，并返回它得值。
# 同样，每次在对该属性复制时，也会调用__set__()方法。
myClass = MyClass()
print(myClass.x)
myClass.x = 20
print(myClass.x)
print(myClass.y)
