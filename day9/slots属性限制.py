# 作用
# 限制要添加的实例属性
# 节约内存空间
class Student(object):
    __slots__ = ('name','age')
    def __str__(self):# 此魔术方法让print（此类的对象） 打印的不再是地址 而是其return的格式
        return '{}....{}'.format(self.name,self.age)
    pass
xw=Student()
xw.name='小王'
xw.age=20
# xw.score=96 # 没有在范围内 所以报错

# print(xw.__dict__) #所有可以用的属性都在这里存储  不足的地方就是占用的内存空间大
# 可以看到 在定义了 slots变量之后 student类的实例已经不能随意创建不在 __slots__定义的属性了
# 同时还可以看到实例当中也不在有__dict__
# print(xw)

# 在继承关系当中的使用  __slots__
# 子类未声明  __slots__时，那么是不会继承父类的__slots__，此时子类是可以随意的属性赋值的
# 子类声明 了__slots__时，子类__slots__的范围是为其自身+父类的__slots__

class subStudent(Student):
    __slots__ = ('gender','pro')
    pass
ln=subStudent()
ln.gender='男'
ln.pro='计算机信息管理'
print(ln.gender,ln.pro)



