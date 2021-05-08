from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7])
print(list(r))

# 用map把所有的数字转化为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6])))


# reduce
# 说对一个序列求和，就可以用reduce实现：

def add(x, y):
    return x + y


r2 = reduce(add, [1, 3, 5, 7, 9])
print(r2)


def prod(list1):
    def m(x, y):
        return x * y

    return reduce(m, list1)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
