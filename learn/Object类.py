class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0}，我的年龄是{1}'.format(self.name,self.age)

stu=Student('liuyan',25)
print(stu)