print('Hello python')
# age = int(input('请输入年龄：'))
# 定义一个变量
age = 23
if age > 20:
    print('你真老！')
else:
    print('你真年轻！')
# 定义一个dic（词典）
names = {'tom': '汤姆', 'jerry': '杰瑞', 'zhangdi': '张迪', 'jack': '杰克'}
print(names.get('tom'))
# 重新放置一个值
names['brant'] = '布莱恩'
print(names.get('brant'))
print('如果可以不存在，则输出默认值NG！', names.get('bar', 'NG'))
# 判断一个key是否存在
# 判断一个key是否存在
print('zhangdi是否存在:', '存在' if ('zhangdi' in names) else '不存在')
# 同一个key只能存在一个值，后来存在的会被覆盖
print('names 的key=zhangdi的值是：', names['zhangdi'])
names['zhangdi'] = '张迪2'
print('names 的key=zhangdi的值是：', names['zhangdi'])


# 定义一个函数
def test(a, b):
    if a > b:
        print('第一个参数比第二个参数大！')
    else:
        print('第一个参数比第二个参数小！')


def test1():
    print("this is a method for test python...")
    print('''第一行
          ...第二行
          ...第三行''')


test1()
test(121, 1111)
