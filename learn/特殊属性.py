class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age


#特殊属性
x=C('xiaobai',3)
print(x.__dict__)  #查看实例对象的属性的字典
print(C.__dict__) #查看类对象的属性字典
print(x.__class__)#查看对象所属的类
print(C.__bases__)#查看类的父类
print(C.__base__)#查看类的基类
print(C.__mro__)#查看类的层次结构
print(A.__subclasses__())#查看类的子类列表