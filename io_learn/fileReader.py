# 文件读写

try:
    f = open("D:/cg/aaa.txt", 'r')
    content = f.read()

    print(content)
except Exception as ex:
    print('发生异常：', ex)
finally:
    if f:
        f.close()

# 升级版本，使用with自动调用close

# 文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readline()最方便

with open("D:/cg/aaa.txt", encoding='utf-8') as file:
    for line in file:
        print(line)

# 写文件
# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，
# 空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
with open('D:/cg/aaa.txt', 'w') as file:
    file.write("hello world")
