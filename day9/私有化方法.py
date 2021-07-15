class Animal:
    def __eat(self):#私有化方法  __方法名
        print('吃东西')
        pass
    def run(self):
        self.__eat() # 本类内部可以调用本类私有化方法
        print('飞快的跑')
    pass

class Bird(Animal):
    pass

b1=Bird()
# print(b1.eat()) # 子类Brid没有继承方法__eat()
b1.run()


