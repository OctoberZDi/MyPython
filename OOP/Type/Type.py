print(type(3.4))


class Student:
    def say(self):
        print('我要学习python！')


stu = Student()
print(type(stu))

# 使用 type() 函数创建类
Student = type("Student", (object,), dict(say=say, name="C语言中文网"))
