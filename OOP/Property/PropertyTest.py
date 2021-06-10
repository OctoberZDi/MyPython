class CLanguage:
    # 构造函数
    def __init__(self, n, age):
        self.__name = n
        self.__age = age

    # 设置 name 属性值的函数
    def setName(self, n):
        print("setName")
        self.__name = n

    # 设置age属性值得函数
    def setAge(self, age):
        print("setAge")
        self.__age = age

    # 访问name属性值的函数
    def getName(self):
        print("getName")
        # 由于getName方法中需要返回name属性，如果使用self.name的话，本身又被调用getName，就会进入无限死循环
        # 为了避免这种情况出现，程序中的name属性必须设置为私有属性，使用__name
        # RecursionError: maximum recursion depth exceeded while calling a Python object
        return self.__name

    # 访问age属性值得函数
    def getAge(self):
        print("getAge")
        return self.__age

    # 删除name属性值的函数
    def delName(self):
        print("delName")
        self.__name = "xxx"

    # 删除age属性值得函数
    def delAge(self):
        print("delAge")
        self.__age = 0

    # 为name 属性配置 property() 函数
    # 属性名=property(fget=None, fset=None, fdel=None, doc=None)
    # fget:指定获取该属性值得方法
    # fset:指定设置该属性值得方法
    # fdel:指定删除该属性值得方法
    # doc:文档字符串，用于说明次函数的作用
    name = property(getName, setName, delName, 'name属性的使用说明')

    # 为age 属性配置property() 函数
    age = property(getAge, setAge, delAge, "age属性的使用说明")

    # name只有get，set参数，意味着name属性时一个读写的属性，但不能删除
    # name = property(getName, setName)

    # name 属性可读，不可写，也不能删除
    # name = property(getName)


# 调取说明文档的 2 种方式
# print(CLanguage.name.__doc__)
help(CLanguage.name)
clang = CLanguage("C语言中文网", 33)
# 调用 getName() 方法
print("测试name属性")
print(clang.name)
# 调用 setName() 方法
clang.name = "Python教程"
print(clang.name)
# 调用 delName() 方法
del clang.name
print(clang.name)

print("测试age属性")
# 调用getAge
print(clang.age)
# 调用setAge
clang.age = 20
print(clang.age)
del clang.age
print(clang.age)
