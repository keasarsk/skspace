# 取绝对值
# print(abs(-34))
# round  取近似值
# print(round(3.66,1))
# pow 求次方
# print(3**3)
# print(pow(3,3))
# max 求最大值
# print(max([23,123,4,5,2,1,786,234]))
# print(max(23,235))
# sum 使用
# print(sum(range(50),3))
# eval 执行表达式
a,b,c=1,2,3
print('动态执行的函数={}'.format(eval('a*b+c-30')))
def TestFun():
    print('我执行了吗?')
    pass
# eval('TestFun()') #可以调用函数执行
# 类型转换函数
# print(bin(10)) #转换二进制
# print(hex(23)) #十六进制
# 元组转换为列表
tup=(1,2,3,4)
# print(type(tup))
li=list(tup) #强制转换
# print(type(li))
li.append('强制转换成功')
# print(li)
tupList=tuple(li)
# print(type(tupList))

# 字典操作 dict()
# dic=dict(name='小明',age=18) #创建一个字典
# # print(type(dic))
# # # dict['name']='小明'
# # # dict['age']=18
# # print(dic)
# bytes转换
# print(bytes('我喜欢python',encoding='utf-8'))


