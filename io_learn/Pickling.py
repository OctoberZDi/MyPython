# 序列化

import pickle

d = dict(name="张迪", age=20, score=100)

# 写入文件
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
with open("D:/cg/aaa.txt", 'wb') as f:
    pickle.dump(d, f)

print('=========')
# 读文件内容
with open("D:/cg/aaa.txt", 'rb') as f2:
    d = pickle.load(f2)
    print(d)
