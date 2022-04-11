class Animal:
    def eat(self):
        print('动物吃')

class Cat(Animal):
    def eat(self):
        print('猫会吃')

class Dog(Animal):
    def eat(self):
        print('狗会吃')
    def __init__(self,name,age):
        self.name=name
        self.age=age




