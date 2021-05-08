from Animal import Animal


class Dog(Animal):
    def play(self):
        print("The dog is playing...")

    # 覆盖父类的run函数->多态
    def run(self):
        print('The dog is running!')
