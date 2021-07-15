# -------------------- 基本数据类型
# 变量
# a='' 字符串
# a=[] 列表类型
# a=() 元组类型     元组中各个类型元素都可以
# a={} 字典类型

# ----------------------------元组 创建后不能进行修改
tupleA=() #空元组
# print(id(tupleA))
tupleA=('abcd',89,9.12,'peter',[11,22,33])
# print(id(tupleA))
# print(type(tupleA))
# print(tupleA)
# ----------------------------元组的查询
# for item in tupleA:
# #     print(item,end=' ')
# ----------------------------print(tupleA[2:4])
# print(tupleA[::-1])

# print(tupleA[::-2]) #表示倒叙输出 每隔两个取一次
# # print(tupleA[::-3]) #每隔三个取一次
# # print(tupleA[-2:-1:]) #倒着取下标 为-2 到 -1 区间的
# # print(tupleA[-4:-2:]) #倒着取下标 为-2 到 -1 区间的

# tupleA[0]='PythonHello'  #错误的
# tupleA[4][0]=285202  #----------可以对元组中的列表类型的数据进行修改
# print(tupleA)
# print(type(tupleA[4]))

tupleB=('1',) # -------------------当元组中只有一个数据项的时候，
# 必须要在第一个数据项后面加上 逗号
# print(type(tupleB))
# --------------对range（）强制转换成tuple tuple(range(10))
tupleC=(1,2,3,4,3,4,4,1)

print(tupleC.count(4)) #-----------可以统计元素出现的次数
