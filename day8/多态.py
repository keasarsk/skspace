# 案例演示
class Animal:
    '''
    父类【基类】
    '''
    def say_who(self):
        print('我是一个动物....')
        pass
    pass
class Duck(Animal):
    '''
      鸭子类 【子类】 派生类
    '''
    def say_who(self):
        '''
        在这里重写父类的方法
        :return:
        '''
        print('我是一只漂亮的鸭子')
        pass
    pass
class Dog(Animal):
    '''
     小狗类 【子类】 派生类
    '''
    def say_who(self):
        print('我是一只哈巴狗')
        pass
    pass

class Cat(Animal):
    '''
        小猫类 【子类】 派生类
    '''
    def say_who(self):
        print('我是一只小花猫 喵喵喵喵')
        pass
    pass


class Bird(Animal):
    '''
    新增鸟类 无需修改原来的代码
    '''
    def say_who(self):
        print('我是一只黄鹂鸟')
    pass

class People:
    def say_who(self):
        print('我是人类')
    pass


class student(People):
    def say_who(self):
        print('我是一年级的学习 张明')
    pass

def commonInvoke(obj):
    '''
    统一调用的方法
    :param obj: 对象的实例
    :return:
    '''
    obj.say_who()

# 多态 同一个say_who()方法 不同对象有不同的状态
# duck1=Duck()
# duck1.say_who()
# dog1=Dog()
# dog1.say_who()
# cat1=Cat()
# cat1.say_who()

listObj=[Duck(), Dog(),Cat(),Bird(),student()]#列表里面放了一堆对象
for item in listObj:
    '''
     循环去调用函数
    '''
    commonInvoke(item)# commonInvoke()是普通函数 不是类方法 不需要 对象.commonInvoke()


