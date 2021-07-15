class  People:
    country='china'
    #------------------------类方法 用 classmethod 来进行修饰
    @classmethod
    def get_country(cls):
        return cls.country #访问类属性
        pass
    @classmethod
    def change_country(cls,data):
        cls.country=data #修改类属性的值  在类方法中
        pass
    @staticmethod
    def getData():#不需要传参数 也可以传
        return People.country  #通过类对象去引用
        pass
    @staticmethod
    def add(x,y):
        return x+y
        pass

print(People.add(10,56)) #带有参数的静态方法
# print(People.getData())
# print(People.get_country()) #通过类对象去引用

p=People()
print(p.getData()) #注意 一般情况下 我们不会通过实例对象去访问静态方法
# print('实例对象访问 %s'%p.get_country())
# print('-----------------修改之后---------------------------')
# People.change_country('英国')
# print(People.get_country()) #通过类对象去引用

#-------------- 为什么要使用静态方法呢
# 由于静态方法主要来存放逻辑性的代码，本身和类以及实例对象没有交互，
# 也就是说，在静态方法中，不会涉及到类中方法和属性的操作
# 数据资源能够得到有效的充分利用
# 在一个类中 某个方法不会牵扯类的属性或其他方法 是独立的 此时可以定义成静态方法
# 静态方法使用方式和类方法一样 不用创建实例对象后用

# demo  返回当前的系统时间
import  time # 引入第三方的时间模块
class TimeTest:
    def __init__(self,hour,min,second):
        self.hour=hour
        self.min = min
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S",time.localtime())
        pass
    pass

print(TimeTest.showTime())# 用类对象调用静态方法
t=TimeTest(2,10,15)
print(t.showTime()) #没有必要通过这种方式去访问 静态方法
