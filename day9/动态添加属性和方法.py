import types  #添加方法的库

def dymicMethod(self):
    print('{}的体重是:{}kg 在 {} 读大学'.format(self.name,self.weight,Student.shcool))
    pass
@classmethod
def classTest(cls):
    print('这是一个类方法')
    pass

@staticmethod
def staticMethodTest():
    print('这是一个静态方法')
    pass

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    pass
    def __str__(self):
        return '{}今天{}岁了'.format(self.name,self.age)
    pass

print('绑定类方法')
Student.TestMethod=classTest # 把写在类外部的classTest方法添加到类 命名为TestMethod
# Student.TestMethod()

Student.staticMethodTest=staticMethodTest
Student.staticMethodTest()
print('---------------绑定类方法执行结束----------------------')

zyh=Student('张艳华',20)
zyh.weight=50 #动态添加
zyh.printInfo=types.MethodType(dymicMethod,zyh)
# ----------动态的绑定方法 把写在外部的dymicMethod方法动态的添加给对象zyh 并命名为printInfo

zyh.TestMethod()
print('-------------实例对象调用 动态绑定类方法-----------------------')
# print(zyh)
# print(zyh.weight)
print('-------------另外一个实例对象  张明--------------------------')
zm=Student('张名',20)
zm.weight=80 #动态添加
print(zm)

zm.printInfo=types.MethodType(dymicMethod,zm) #动态的绑定方法
# print(zm.weight)
print('-------------给类对象添加属性--------------------------')
Student.shcool='北京邮电大学' #动态添加类属性
print(zm.shcool)
print('-------------执行动态调用实例方法--------------------------')
zyh.printInfo() #调用动态绑定的方法
zm.printInfo()