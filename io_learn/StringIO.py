# StringIO顾名思义就是在内存中读写str。
# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

from io import StringIO

f = StringIO()
f.write("hello world!\n Hi! \n Goodbye!")

while True:
    line = f.readline()
    if line == '':
        break
    print(line)
print(f.getvalue())
