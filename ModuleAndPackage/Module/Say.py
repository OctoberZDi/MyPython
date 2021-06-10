import os
import sys

from Module import ByeBye, Hello

# from sys import argv

print('=====')
print('sys模块下的argv变量用于获取运行Python程序的命令行参数，其中argv[0]用于获取当前Python程序的存储路径 \n', sys.argv[0])
print(os.name, os.path)
Hello.say()
ByeBye.bye()
