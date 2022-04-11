if __name__ == '__main__':
    str = "hi, kkworld"
    print(type(str))
    print(str)
    print(str[6])
    print("-------------------------")
    list1 = [1, True, 2.4, 'hahaha']
    print(type(list1))
    print(list1)
    print(list1[3])
    print("-------------------------")

    # Tuple（元组）
    tuple1 = (22, "kekeke", True, 4.5)
    print(type(tuple1))
    print(tuple1)
    print(tuple1[3])
    print("-------------------------")

    # Set（集合）
    set1 = {'haha', 23}
    print(type(set1))
    print(set1)
    # print(set1[1])
    print("-------------------------")

    # Dictionary（字典）
    dict = {'name': 'kkworld', 'phone': 123456, 'address': 'beijing'}
    print(type(dict))
    print(dict['phone'])
    print(dict.get('address'))
    print("-------------------------")


class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #age不希望在类的外部使用，所以加了两个__
    def show(self):
        print(self.name,self.__age)#class内部可以调用__的属性

#在类的外部使用
print(Student.name)
print(Student.__age)






















