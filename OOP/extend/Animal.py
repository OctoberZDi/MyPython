# 基类，有一run方法

# 和类属性一样，类方法也可以进行更细致的划分，具体可以分为类方法，实例方法，静态方法

# 区分方法：
# @classmethod 类方法
# @staticmethod 静态方法
# 不用任何修改的方法为实例方法
class Animal(object):
    def __init__(self):
        # 实例的属性
        self.name = "Python"
        self.addr = "www.baidu.com"

    # 实例方法，最大的特点至少要包含一个self参数。通常由对象直接调用
    # Python 也支持使用类名调用实例方法，但此方式需要手动给 self 参数传值。例如：
    # animal = Animal();
    # Animal.run(animal);
    # 定义一个实例方法
    def run(self):
        print('Animal is running...')

    # 定义一个实例方法
    def say(self):
        print("Animal is saying!")

    # 定义一个类方法，需要使用@classmethod修饰符进行修饰
    # 类方法推荐使用类名直接调用，不推荐使用对象调用
    # cls参数固定，类似于self
    @classmethod
    def testClassMethod(cls):
        print("This is classmethod.!!!", cls, cls.__name__)

    # 静态方法
    # 静态方法没有类似于self，cls的参数，因此Python解释器不会对它包含的参数做任何类或对象的绑定。
    # 正因为如此，类的静态方法无法调用任何类的属性和方法
    @staticmethod
    def info(name, addr):
        print(name, addr)
