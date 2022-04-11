#特殊方法
a=20
b=100
c=a+b
print(c)
d=a.__add__(b)#a+b的内部实现逻辑

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)


s1=Student('zhangsan')
s2=Student('lisi')
s3=s1+s2#实现了两个对象的加法，（因为在Student类中编写了__add__()的特殊方法）
print(s3)
print('-----------------------------------------------')
list=[1,2,3,4]
print(len(list))
print(list.__len__())
print(s1.__len__())#在Student类中写__len__方法
