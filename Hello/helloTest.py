# name = input("please input your name...")
import math

name = '张迪'
print("hello", name)

print("1024 *  1024 = ", 1024 * 1024)
a = 100
if a >= 200:
    print(a)
else:
    print(-a)

print('你好', '2021', '你好', '张迪')

# list 和 tuple
print('=============测试list=============')
classmates = ['张迪', '朱玉', '张筱满']

print('长度：', len(classmates), '所有元素：', classmates, '第一个元素：', classmates[0])
print('获取最后一个元素，使用-1做索引===>', '最后一个元素：', classmates[-1])
classmates.append('你好')
print('append 添加元素到末尾：', classmates)
classmates.pop()
print('pop 删除最后一个元素：', classmates)
print('=============测试tuple=============')
t = (1, 2, 3, 4, 5)
print('长度：', len(t))

print('=============测试 循环=============')
for x in classmates:
    print('***' + x)

# range 随机生成整数序列
sumAll = 0
for x in range(101):
    sumAll = sumAll + x
print(sumAll)

print(abs(-111))


# 自定义函数，求绝对值
def my_abs(param):
    # 抛出一个错误TypeError
    if not isinstance(param, (int, float)):
        raise TypeError('bad params given!!!')
    if 0 < param <= 10:
        return param
    elif param > 10:
        return param - 10
    else:
        return -param


# 测试函数返回多个值
print('=============测试函数返回多个值=============')


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

returnVal = move(100, 100, 60, math.pi / 6)
print(returnVal)


# 请定义一个函数接收3个参数，返回一元二次方程 两个解
def quadratic(a, b, c):
    x = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    y = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x, y


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

# 位置参数
# 默认参数，n=2代表，如果不传第二个参数。默认为2
print('位置参数')


def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1

    return s


print(power(5))
print(power(2, 2))
print(power(2, 3))

# 可变参数
print('可变参数')


def calc(*numbers):
    s = 0
    for num in numbers:
        s = s + num

    return s


print(calc(1, 2, 3, 4, 5))
print(calc())
print(calc(3, 445, 6))

# 构造列表
L = []
n = 1
while n < 100:
    L.append(n)
    n = n + 2
print(L)
