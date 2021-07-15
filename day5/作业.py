# 写函数，接收n个数字，求这些参数数字的和
def sumFunc(*args):
    #
    '''
    处理接受的数据
    :param args: 可变长的参数 可以接受一个元组
    :return: 计算和
    '''
    result=0
    for item in args:
        result+=item
        pass
    return result
    pass
# 调用
# rs=sumFunc(1,2,3,4)
# print('rs={0}'.format(rs))  #format 格式化输出
# rs=sumFunc(4,5,6,7,8,9,10)
# print('rs1=%d'%rs)
# 写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
def process_Func(con):
    '''
    处理列表数据
    :param con: 接受的是一个列表或者元组
    :return: 新的列表对象
    '''
    listNew=[]
    index=1
    for i in con:
        if index%2==1: #判断奇数位
            listNew.append(i)
            pass
        index+=1
        pass
    return listNew
    pass


# rs3=process_Func([1,2,3,4,5,6,7])
# print(rs3)

# initData=tuple(range(10,30))
# print('init {}'.format(initData))
# rs4=process_Func(tuple(range(10,30)))
# print(rs4)

# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# PS:字典中的value只能是字符串或列表
def dictFunc(dicParms):  #**kwargs
    '''
    处理字典类型的数据
    :param dicParms: 字典
    :return:
    '''
    result={} #空字典
    for key,value in dicParms.items(): #key-value
        if len(value)>2:
            result[key]=value[:2] #像字典去添加数据
            pass
        else:
            result[key]=value
            pass
        pass
    return result
    pass

# 函数调用
dictObj={'name':'夏雨','hobby':['唱歌','跳舞','运动','编程'],'pro':'中国艺术'}
# print(dictFunc(dictObj))
