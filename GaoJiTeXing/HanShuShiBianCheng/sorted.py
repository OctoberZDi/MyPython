# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。


from operator import itemgetter

r1 = sorted([36, 5, -12, 9, -21])
print(r1)

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
r2 = sorted([36, 5, -12, 9, -21], key=abs)
print(r2)

# 字符串排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
r3 = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(r3)

# 忽略大小写的排序
r4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(r4)

# 忽略大小写的排序,反向排序
r5 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(r5)


def by_name(x):
    return x[0]


def by_score(x):
    return x[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score, reverse=True)
print(L3)
L4 = sorted(L, key=by_score)
print(L4)

print('====================')
L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
print(by_name.__name__)
