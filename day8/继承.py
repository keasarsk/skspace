class Animal:
    def  eat(self):
        '''
        吃
        :return:
        '''
        print('吃饭了')
        pass
    def drink(self):
        '''
        喝
        :return:
        '''
        pass

class Dog(Animal): #-----------继承了Animal 父类 此时dog就是子类
    def wwj(self):
        '''
        子类独有的实现
        :return:
        '''
        print('小狗汪汪叫')
    pass
class Cat(Animal):
    def mmj(self):
        '''
         子类独有的实现
        :return:
        '''
        print('小猫喵喵叫')
    pass

d1=Dog()
d1.eat() # 继承了父类吃的行为
d1.wwj() # 自己的行为
print('**************cat 的行为**********************')
c1=Cat()
c1.eat()
c1.mmj()