import sys# 该模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数
import psutil# 获取系统信息的第三方模块
import os
import gc# 垃圾回收机制模块

print(gc.get_threshold())# 返回当前集合阈值。
def showMemSize(tag):
    pid=os.getpid()# 返回当前进程id
    p=psutil.Process(pid)# 返回进程pid的基本信息
    info=p.memory_full_info()# ？？？？？？
    memory=info.uss/1024/1024# ？？？？？？
    print('{} memory used:{} MB'.format(tag,memory))
    pass

# 验证循环引用的情况
def func():
    showMemSize('初始化')
    a=[i for i in range(10000000)]
    b=[i for i in range(10000000)]
    a.append(b)
    b.append(a)
    showMemSize('创建列表对象 a b 之后')
    # print(sys.getrefcount(a))
    # print(sys.getrefcount(b))
    # del a
    # del b
    pass

func()
gc.collect() #手动释放
# showMemSize('完成时候的')
# sys.getrefcount(变量名)# 获取变量引用次数
# a=[]
# print(sys.getrefcount(a)) #两次
# b=a
# print(sys.getrefcount(a)) #三次
# c=b
# d=b
# e=c
# f=e
# g=d
# print(sys.getrefcount(a)) #八次