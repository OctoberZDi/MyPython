name = 'Python教程'
address = 'https://c.biancheng.net/'

print(name, address)


def say():
    print('人生苦短，我要学Python！')
    return '人生呐！！'


class CLanguage:
    def __init__(self, name, address):
        self.__name = name
        self.__add = address

    def say(self):
        print(self.__name, self.__add)


if __name__ == '__main__':
    say()
    clang = CLanguage('java语言', 'https://www.java.com/')
    clang.say()
