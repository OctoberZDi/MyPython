class CLanguage:
    def __init__(self, name, add):
        self.__name = name
        self.__add = add

    def setName(self, name=None):
        self.__name = name
        # if len(name) < 3:
        #     raise ValueError('名称长度必须大于3！')

    def getName(self):
        return self.__name

    # 为 name 配置 setter 和 getter 方法
    name1 = property(getName, setName)

    def setAdd(self, add=None):
        self.__add = add
        # if add.startswith("https://"):
        #     self.__add = add
        # else:
        #     self.__add = "Error address"
        #     raise ValueError('地址必须以 https:// 开头')

    def getAdd(self):
        return self.__add

    # 为 add 配置 setter 和 getter 方法
    add1 = property(getAdd, setAdd)

    # 定义个私有方法
    def __display(self):
        print(self.__name, self.__add)


clang = CLanguage("C语言中文网", "https://c.biancheng.net")
print(clang.getName())
print(clang.getAdd())

clang.name1 = 'java'
print(clang.name1)
clang.add1 = 'www.baidu.com'
print(clang.add1)

# 类名.方法，需要传入对象名
print(CLanguage.getName(clang))
# clang.setName('Java官网')
# clang.setAdd('https://www.java.org')
# print(clang.getName())
# print(clang.getAdd())

# 尝试调用私有的 display() 方法
# clang.__display()
