# 实例属性与类属性
# 类属性所有的实例对象都可以访问它 共用
# 实例属性每个实例对象有自己的一份 互不干扰

# class Pepole:
#     def __init__(self):
#         '''
#         构造方法
#         实例属性的声明
#         '''
#         self.name='小倩'
#         self.sex='女生'
#         self.age=20
#         pass
#     def eat(self):
#         '''
#         吃的行为
#         :return:
#         '''
#         print('喜欢吃榴莲')
#     pass
#
# xq=Pepole()
#--------------------添加实例属性
# xq.name='小倩'  #添加实例属性
# xq.sex='女生'   #添加实例属性
# xq.age=20    #添加实例属性
# xq.eat()
# # print(xq.name,xq.sex,xq.age)
#
# xl=Pepole()  #创建出来的
# xl.name='小倩'  #添加实例属性
# xl.sex='女生'   #添加实例属性
# xl.age=20    #添加实例属性
#
# xm=Pepole()  #在创建新对象的时候 是自动执行的
# print(xm.name) #直接输出的是默认值
# xm.name='小明'
# print(xm.name)

# 如果有n个这个对象  被实例化  那么就需要添加很多次这样的属性了 显然是比较麻烦

# init传递参数 改进
class Pepole:
    def __init__(self,name,sex,age):
        '''
        这里的参数 创建此类实例时候就得传入
        实例化pepole对象时自动执行
        实例属性的声明
        '''
        self.name=name
        self.sex=sex
        self.age=age
        pass
    def eat(self,food):
        '''
        吃的行为
        :return:
        '''
        print(self.name+'喜欢吃'+food)
    pass

#--------------在实例化时就把__init__的参数传进去
zp=Pepole('张鹏','男生',18)
print(zp.name,zp.age)
zp.eat('香蕉')
lh=Pepole('李辉','男生',28)
lh.eat('苹果')
print(lh.name,lh.age)

xh=Pepole('小花','女生',20)
xh.eat('橘子')
print(xh.name,xh.age)

# 总结 __init__
# 1. python 自带的内置函数 具有特殊的函数   使用双下划线 包起来的【魔术方法】
# 2. 是一个初始化的方法 用来定义实例属性 和初始化数据的，在创建对象的时候自动调用  不用手动去调用
# 3. 利用传参的机制可以让我们定义功能更加强大并且方便的 类
