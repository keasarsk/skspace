class ToolongMyException(Exception):# 传递过来一个异常
    def __init__(self,leng):
        '''
        :param len: 长度
        '''
        self.len=leng
        pass
    def __str__(self):
        return '您输入姓名数据长度是'+str(self.len)+'超过长度了..'
    pass

def name_Test():
    name=input('请输入姓名.....')
    try:
        if  len(name)>5:
            # ----------raise相当于C里的throw 抛出一个异常 此时try中剩下的语句不再执行
            raise ToolongMyException(len(name))
        else:
            print(name)
            pass
        pass
    except ToolongMyException as result:
        print(result)
        pass
    finally:
        print('执行完毕了....')

name_Test()
