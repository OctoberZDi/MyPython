# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
#
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

L1 = [1, 2, 3, 4, 5, ]
print(L1)
L2 = iter(L1)
print(next(L2))
print(next(L2))
print(next(L2))
print(next(L2))
print(next(L2))
print(L2)
