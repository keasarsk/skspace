# 局部变量 就是在函数内部定义的变量【作用域仅仅局限在函数的内部】
# 不同的函数 可以定义相同的局部变量，但是各自用各自的 不会产生影响
# 局部变量的作用：为了临时的保存数据 需要在函数中定义来进行存储
# ------------全局变量----------------
# pro的定义就是一个全局变量【作用域的范围不同】
# 当全局变量和局部变量出现重复定义的时候，程序会优先执行使用函数内部定义的变量【地头蛇】
#如果在函数的内部要想对全局变量进行修改的话 必须使用global 关键字进行声明
# 对于可变类型【dict、list】来讲，全局变量要想在函数中修改的话，我们不需要用global关键字去声明的
# 【因为对象的内存地址不会改变】
def Test():
    global A #局部变量提升为全部变量
    A=200
    pass
Test()
def TTT():
    print('函数调用',A)
print(A)#在外部访问A
TTT()
# 针对数据类型来讲 可变类型和不可变类型
# 可变类型 dict list
# li=[1,2]
# print(id(li))
# li.append('我是认真的')
# print(li)
# print(id(li))
# 不可变类型  str tuple number【int、float、complex】
# age=20
# print(id(age))
# age=30
# print(id(age))
# age1=age
# age1=100
# print(id(age1))
# name='peter'
# print(id(name))
# name='刘德华'
# print(id(name))
listObj=[] #全局变量
def demoList():
    listObj.append('你好')
    pass
demoList()
print(listObj)


