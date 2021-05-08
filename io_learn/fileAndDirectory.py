# 操作文件和目录

import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)
# 详细信息 os.uname()在windows不提供
# print(os.uname())
# 打印环境变量
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print("获取某个环境变量的值：", os.environ.get("SYSTEMROOT"))

# 操作文件和目录
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
os.path.join('D:/cg/', 'cgForPython')
# 然后创建一个目录:
# os.mkdir("D:/cg/cgForPython")
# 删掉一个目录:
# os.rmdir('/Users/michael/testdir')

# 拆分路径
os.path.split("D:/cg/temp/projectZIp")
# 拆分路径带着扩展名
os.path.splitext("D:/cg/aaa.txt")
# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')

# 列出当前目录下的所有文件
[x for x in os.listdir("D:/cg") if os.path.isdir(x)]

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
