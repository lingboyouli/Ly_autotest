'''
语法格式：
class 子类类名（父类1，父类2...）：
    pass

python支持多继承
如果一个类没有继承任何类，默认继承object
定义子类时，必须在狗仔函数时调用父类的构造函数
'''


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no
    def info(self): #方法重写
        super().info()
        print(self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, teachyear):
        super().__init__(name, age)
        self.teachyear = teachyear
    def info(self):#方法重写
        super().info()
        print(self.teachyear)



stu=Student('zhangsan',12,1)
teacher=Teacher('lihua',30,3)

#可以调用父类的方法
stu.info()
teacher.info()