# 属性：类属性和实例属性
# 类属性 就是类对象所拥有的属性
class Student:
    name='李明' #-------------属于类属性  就是student类对象所拥有的
    def __init__(self,age):
        self.age=age #--------实例属性
        pass
    @staticmethod
    def aaa(x,y):
        print(x+y)
    pass

# 类对象
Student.name='李易峰' #通过类对象去修改数据 可以修改的  因为name的所拥有的权利属于类对象

lm=Student(18)
print(lm.name) #通过实例对象去访问类属性
# lm.name='刘德华'  #通过实例对象 对类属性进行修改 可以吗? 不可以的
print(lm.name)
print(lm.age)
Student.aaa(4,6)
print('---------xh的数据---------------')
xh=Student(28)
print(xh.name)
print(xh.age)
print('---------通过类对象 student 去访问name---------------')
# print(Student.name)  如 类名.属性名 形式去访问
# print(Student.age)
# 小结
#------------------- 类属性是可以 被类对象和实例对象共同访问使用的
#------------------- 实例属性只能由实例对象所访问


