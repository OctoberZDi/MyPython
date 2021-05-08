# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

def is_odd(x):
    return x % 2 == 1


r1 = filter(is_odd, [1, 2, 3, 4, 5, 6, 8])
print(list(r1))


# 删除序列中的空字符串
def not_empty(x):
    return x and x.strip()


r2 = filter(not_empty, ['', 'aa', '', 'ccc'])
print(list(r2))
