# 定义类和对象
# 类结构  类名  属性  方法
# class 类名:
#     属性
#     方法

class Person:
    '''
    对应人的特征
    '''
    # name='小明'  #类属性
    age=20       #类属性
    '''
    对应人的行为  实例方法
    '''
    def __init__(self):
        self.name='小明'   #实例属性
        pass
    def eat(parms):
        print("大口的吃饭")
        pass
    def run(self):   #实例方法
        print('飞快的跑')
        pass
    pass
def printInfo():
    '''
    普通方法
    :return:
    '''
    pass
# 创建一个对象【类的实例化】
# 规则格式  对象名=类名()
xm=Person()
xm.eat() #调用函数
xm.run()
print("{}的年龄是：{}".format(xm.name,xm.age))

# 创建另外一个实例对象
xw=Person()
xw.eat()  #实例方法

