# 鸵鸟类，子类
# python支持多重继承
# 如果子类继承的多个父类中包含同名的类实例方法，则子类对象在调用该方法时，会优先选择排在最前面的父类中的实例
from ChongXie.Bird import Bird


# 继承自Bird
class Ostrich(Bird):
    def fly(self):
        super(Ostrich, self).fly()
        print("Ostriches can fly! 重写fly")


if __name__ == '__main__':
    ostrich = Ostrich()
    # 调用子类本身的fly
    ostrich.fly()
    ostrich.hasWing()
    # 多重继承的时候，子类调用父类的同名方法的时候，优先选择前面的父类中的实例方法。
    ostrich.eat()

    # 调用Bird父类的方法
    # 使用类名调用类方法，Python不会为该方法第一个self参数自动绑定值，需要手动为self参数赋值
    Bird.fly(ostrich)
