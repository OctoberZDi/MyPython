from Animal import Animal


class Cat(Animal):

    def eat(self):
        print("The cat is eating!")

    # 覆盖父类的run函数
    def run(self):
        print('The cat is running!')

    def say(self):
        print("The cat is saying!")
