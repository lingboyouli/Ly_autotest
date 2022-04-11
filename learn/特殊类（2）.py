class Person:
    def __init__(self,name,age):#初始化对象
        print('__init__被调用了，self的id为{0}'.format(id(self)))
        self.name=name
        self.age=age
    def __new__(cls, *args, **kwargs):#创建对象（先执行）
        print('__new__被调用了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建对象的id为{0}'.format(id(obj)))
        return obj #return返回给了self

print('object这个类的对象id为{0}'.format(id(object)))
print('Person这个类的对象id为{0}'.format(id(Person)))

#创建实例对象
p1=Person('zhangsan',20)
print('p1这个实例对象的id为{0}'.format(id(p1)))

'''
参数传递：
1、创建Person对象，调用__new__把值给了cls
2、cls的值付给了obj
3、return obj，将obj的id传给了self
4、self的id传给了p1
'''