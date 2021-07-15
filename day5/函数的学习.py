# print('小张的身高是%f'%1.73)
# print('小张的体重是%f'%160)
# print('小张的爱好是%s'%'唱歌')
# print('小张的身高是%s'%'计算机信息管理')
#处理其他的逻辑信息
# 多次去打印出小张的信息
print('---------------多次输出相同的信息---------------------')
# print('小张的身高是%f'%1.73)
# print('小张的体重是%f'%160)
# print('小张的爱好是%s'%'唱歌')
# print('小张的专业是%s'%'计算机信息管理')
# 针对上面的场景 就需要进一步的去优化代码【方案：封装函数】
# 函数的定义
# def 函数名(参数列表):0-n 个
#     代码块

def printInfo():
    '''
    这个函数是用来打印个人信息的 是对小张信息显示的组合
    :return:
    '''
    # 函数代码块
    print('小张的身高是%f' % 1.73)
    print('小张的体重是%f' % 160)
    print('小张的爱好是%s' % '唱歌')
    print('小张的专业是%s' % '计算机信息管理')
    pass
#函数的调用
# printInfo() #函数的调用
# printInfo() #多次调用
# printInfo()
# printInfo()
# printInfo()
# print('我是其他的代码块...')
# 进一步的去完善这样的需求【输出不同人的信息】 方案：通过传入参数来解决
def printInfo(name,height,weight,hobby,pro): #形式参数
    # 函数代码块
    print('%s的身高是%f' %(name,height))
    print('%s的体重是%f' %(name,weight))
    print('%s的爱好是%s' %(name,hobby))
    print('%s的专业是%s' %(name,pro))
    pass

# 调用带参数的信息
printInfo('小李',189,200,'打游戏','咨询师') #实参
print('------------------带参数的调用---------------------------')
printInfo('peter',175,160,'码代码','计算机应用')
