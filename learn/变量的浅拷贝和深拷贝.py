class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk


#变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)#cpu1和cpu2的内存地址相同
print('----------------------------------------')

disk=Disk()
com=Computer(cpu1,disk)

#类的浅拷贝（只拷贝源对象，子对象不拷贝）
import copy
com2=copy.copy(com)
print(com,com.cpu,com.disk)
print(com2,com2.cpu,com2.disk)#com和com2内存地址不同，cpu和disk内存地址相同
print('----------------------------------------')

#深拷贝（源对象和子对象都拷贝）
com3=copy.deepcopy(com)
print(com,com.cpu,com.disk)
print(com3,com3.cpu,com3.disk)#com、cpu、disk的内存地址均不相同




