# python 高级特性之切片
list = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('所有元素')
print(list)
print('使用切片 取前三个元素')
print(list[0:3])

print('ABCDEFGHIJKLMN'[1:7])
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']


# 切片+迭代函数
def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])


# 测试:
if trim('hello     ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

