import MyAbs

print(MyAbs.my_abs(-3999))
print(MyAbs.sayHello('tom'))


def power(x, n=3):
    s = 1 
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(2, 2))
print(power(2, 3))
print(power(2, 4))
print(power(2, 5))
