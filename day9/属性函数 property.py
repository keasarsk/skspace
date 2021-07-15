class Person(object):
    def __init__(self):
        self.__age = 18 # 定义一个私有化属性，属性名字前加连个 __ 下滑线

    # def get_age(self): # ----------------访问私有实例属性
    #     return self.__age
    # def set_age(self,age): # -----------------修改私有实例属性
    #     if age < 0:
    #         print('年龄不能小于0')
    #     else:
    #         self.__age=age
    #         pass
    #     pass
    # 定义一个类属性  实现通过直接访问属性的形式去访问私有的属性
    # age=property(get_age,set_age)
    # 此时通过实例对象.age就可以修改age的值了

    # 实现方式2  通过装饰器的方式去声明  ？？？？？？？？？
    @property  #用装饰器修饰 添加属性标志  提供一个getter方法
    def age(self):
        return self.__age
    @age.setter   #提供一个setter方法
    def age(self,parms):
        if parms < 0:
            print('年龄不能小于0')
        else:
            self.__age=parms
            pass
        pass
    pass

p1=Person()
print(p1.age)
p1.age=30
print(p1.age)
# p1.get_age()
# p1.set_age()
# 装饰器 写法如上固定 作用让私有属性可以在外部对象使用起来和普通属性没区别
# 对象.属性 -----调用  对象.属性=值 -----赋值

