# 使用json序列化

import json

# 用json把python对象编程一个json
d = dict(name="张迪1", age=20, score=100)
json1 = json.dumps(d, ensure_ascii=False)
print(json1)

# loads()把json串反序列化
jsonStr = '{"age": 20, "score": 88, "name": "Bob"}'
json2 = json.loads(jsonStr)
print(json2)

# dumps返回一个str，内容就是标准的json，类似的，dump()方法还可以直接把json写入一个file-like Object
with open("D:/cg/aaa.txt", 'w') as file:
    json.dump(json2, file)


# 类的序列化

class Student(object):
    # 类似于构造函数的感觉
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2Json(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print('====')
s = Student('zhangdi', '21', 99)
# 类的序列化方式
# 是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
# 第一种方法：任意一个对象变成一个可序列为JSON的对象方法
print(json.dumps(s, default=student2Json))
# 第二种方法：任一class的实例变为dict
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 类的反序列化
# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
s = json.loads(json_str, object_hook=dict2student)
print(s)
