# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

import os

# 举个例子，要生成list[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 可以用list(range(1, 11))：
print(list(range(1, 20)))

# 生成[1*1,2*2,3*3....]
listX = []
for x in range(1, 10):
    listX.append(x * x)
print(listX)

# 循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
listFor = [x * x for x in range(1, 10)]
print(listFor)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，
# 就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 10) if x % 2 == 0])

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in "ABC" for n in "XYZ"])

# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir("D:/cg")])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for key, value in d.items():
    # print(key, '=', d.get(key))
    print(key, '=', value)
# 因此，列表生成式也可以使用两个变量来生成list：
print([key + '=' + value for key, value in d.items()])
print([key + '=' + value for key in d.keys() for value in d.values()])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
