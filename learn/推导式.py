if __name__ == '__main__':
    list =[]
    names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
    new_names = [name.title() for name in names if len(name) > 3]
    # print(new_names)




    def fun(a,b,c):
        print(a,b,c)


    fun(10,"10",10)

    list=[1,2,3]
    fun(*list)

    dic={"1":100,'2':200,'3':300}
    fun(**dic)


    def fun1(a,b=10):#b为默认值形参
        print(a,b)

    def fun2(*args):#个数可变的位置形参
        print(args)

    def fun3(**args):#个数可变的关键字形参
        print(args)

    def fun4(a,b,*,c,d):# *号后面的参数只能是关键字参数
        print(a,b,c,d)

    def fun5(a,b,*,c,d,**args):
        pass

    def fun6(*args,**args1):
        pass




    def fun():
        global name#global将变量声明为全局变量
        

