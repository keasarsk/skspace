# 使用私有属性的场景
# __变量名
# 1.把特定的一个属性隐藏起来  不想让类的外部进行直接调用
# 2.我想保护这个属性 不想让属性的值随意的改变
# 3.保护这个属性   不想让派生类【子类】去继承

class Person:
    __hobby='跳舞'  #私有的类属性
    def __init__(self):
        self.__name='李四' #加两个下划线 将此属性私有化之后  就不能再外部直接访问了,当然在类的内部可以
        self.age=30
        pass
    def __str__(self):
        '''
        私有化的属性在内部可以使用 self.__name
        :return:
        '''
        return '{}的年龄是{} 爱好是{}'.format(self.__name,self.age,Person.__hobby)
    def  changeValue(self):
        Person.__hobby='唱歌'

class Student(Person):
    def printInfo(self):
        # print(self.__name)  #在此访问父类中的私有属性 可以吗?   不可以
        print(self.age)
    pass


stu=Student()
stu.printInfo()
stu.changeValue() #修改私有属性的值
print(stu)
print(1)
# print(stu.__hobby) #实例对象访问类属性 不可以 因为没继承
print(2)
# print(Person.__hobby) #类对象访问类属性 不可以 因为私有属性只能类内部自己使用
print(3)

# xl=Person()
# # print(xl.__name) #不能访问实例私有属性__name
# print(xl)

# 小结：
# 1 私有化的属性 不能再外部直接的访问  可以在类的内部随意的使用
# 2.子类不能继承父类的私有化属性【只能继承父类公共的属性和行为】
# 3.在属性名的前面直接加 __  就可以变为私有化了
# 4.若想在类外部（类对象、实例对象）改变私有属性的值 需要在类本身定义时添加一个方法，然后对象调用该方法