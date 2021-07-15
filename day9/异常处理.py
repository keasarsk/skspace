# import Exception
# except 在捕获错误异常的时候  只要根据具体的错误类型来捕获的
# 用一个块 可以捕获多个不同类型的异常
# Exception 可以捕获所有的异常  当对出现的问题或者错误不确定的情况下  可以使用Exception
# print(dir(Exception))
try:
    # print(b) #捕获逻辑的代码
    li=[1,2,34]
    print(li[10])  #通过下标去访问列表
    # a=10/0
    pass
# except  NameError as msg:
#     # 捕获到的错误 才会在这里执行
#     print(msg)
#     pass
# except IndexError as msg:
#     print(msg)
#     pass
# except ZeroDivisionError as msg:
#     print(msg)
#     pass
except Exception as result:
    # print(result)
    # 在此尽量的去处理捕获到的错误
    pass
# print('初次接触异常处理')
# print('HAHAHAHHAHA')

def A(s):
    return 10/int(s)
    pass
def B(s):
    return A(s)*2
def main():
    # B(0)
    try:
        B('0')
        pass
    except Exception as msg:
        print(msg)
        pass
    pass

main()
# 不需要在每个可能出错的地方去捕获，只要在合适的层次去捕获错误就可以了 这样的话 就大大减少我们写try---except的麻烦
# 异常的抛出机制
#如果在运行时发生异常  解释器会查找相应的异常捕获类型
#如果在当前函数里面没有找到的话  它会将异常传递给上层的调用函数，看能否处理
# 如果在最外层 没有找到的话，解释器就会退出 程序down哦

# try-except-else

# try:
#     print('我是没有错误产生的')
#     pass
# except SyntaxError as msg:
#     print(msg)
# except Exception as msg:
#     print('error',msg)
# else:
#     print('当Try里面的代码 没有出现异常的情况下 我才会执行')
#     pass

# try-except-finally
# try:
#     int('34')
#     open('aaaa.txt')
# except Exception as msg:
#     print(msg)
#     pass
# finally:
#     print('释放文件的资源、数据库连接是资源等等')
#     print('不管有没有出错都执行的代码块')



