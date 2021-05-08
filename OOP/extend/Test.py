from Cat import Cat
from Dog import Dog


def test():
    cat = Cat()
    cat.run()
    cat.eat()

    dog = Dog()
    dog.run()
    dog.play()


if __name__ == '__main__':
    test()
