from Cat import Cat
from extend.Animal import Animal


def test():
    cat = Cat()
    cat.run()
    cat.say()
    cat.eat()
    # Python 也支持使用类名调用实例方法，但此方式需要手动给 self 参数传值。例如：
    animal = Animal()
    Animal.say(animal)
    # 对象调用类方法（×）不推荐此方法
    animal.testClassMethod()
    # 类调用类方法
    # 类方法推荐使用类名直接调用，不推荐使用对象调用
    Animal.testClassMethod()
    print("name=%s,addr=%s" % (animal.name, animal.addr), Animal.__name__)

    # 静态方法
    # 静态方法的调用：可以使用类名，也可以使用类对象
    Animal.info("张迪", "山东省济南市")
    animal.info("zhangdi", "SD JN city")


if __name__ == '__main__':
    test()
