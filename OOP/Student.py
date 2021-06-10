class Student(object):
    # 类变量：定义在各个类方法之外，包含在类中的变量为类变量或类属性。
    type = "Python"
    content = "I am learning python"

    # 设置默认值 name= , score=
    def __init__(self, name="undefined", score=100):
        print("调用构造方法")
        # 定义在类方法中的变量为实例变量或者实例属性
        self.__name = name
        self.__score = score
        # 类体中，所有函数之外：以此范围定义的变量，成为类属性或类变量。
        # 类体中，所有函数内部：以self.变量名的方式定义的变量，成为实例属性或实例变量。
        # 类中中，所有函数内部，以变量名= 变量值得方式定义的变量，成为局部变量。

    def printScore(self):
        print("%s:%s" % (self.__name, self.__score))


if __name__ == '__main__':
    student = Student("张迪", 200)
    # 打印
    student.printScore()

    stu1 = Student()
    stu1.printScore()
