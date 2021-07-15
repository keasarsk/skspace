class shenxian:
    def fly(self):
        print("神仙都会飞")
    pass
class Monkey:
    def chitao(self):
        print('猴子喜欢吃桃')
    pass

# ------------多继承
class Sunwukong(shenxian,Monkey): #既是神仙  同时也是猴子
    pass

# swk=Sunwukong()
# swk.chitao()
# swk.fly()
# 问题是  当多个父类当中存在相同方法的时候  应该去调用哪一个呢

class D(object):#----------class D继承了object 不写时默认继承
    def eat(self):
        print('D.eat')
        pass
    pass
class C(D):
    def eat(self):
        print('C.eat')
        pass
    pass
class B(D):
    pass
class A(B,C):
    pass
a=A()
a.eat()
print(A.__mro__) #--------------可以显示类的依次继承关系
#在执行eat的方法时 查找方法的顺序是----广度优先
# 首先到A里面去查找  如果A中没有 则继续的去B类中去查找 如果B中没有
# 则去C中查找 如果C类中没有 则去D类中去查找，如果还是没有找到 就会报错
# A-B-C-D  也是继承的顺序