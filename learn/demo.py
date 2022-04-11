class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # age不希望在类的外部使用，所以加了两个__

    def show(self):
        print(self.name, self.__age)  # class内部可以调用__的属性


stu=Student('zhangsan',20)
# 在类的外部使用
print(stu.name)
# print(stu.__age) #外部直接访问是访问不了的
#但是我就是想强行访问
print(dir(stu)) #看一下变量内有什么属性，其中有'_Student__age'属性，这就是系统给改了名字的__age
print(stu._Student__age)#这样就可以访问了，所以加了__的属性，全靠程序员自觉不访问，君子协议

