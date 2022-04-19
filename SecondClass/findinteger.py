'''
出现最多次的整数，输入多个逗号分隔的整数，输出出现最多次的整数的值以及对应的出现次数 1,1,3,4,5,7,11,3,3,3,4,6,8,9,2
'''
#输入
try:
    a=input('请输入整数，用“,”分割')#用中文，怎么办
    intlist=[]
    if ',' not in a:
        print(f'出现最多的数字是{int(a)}，出现次数为1次')
        exit()
    else:
        list = a.split(',')
        intlist = [int(i) for i in list]
except ValueError:
    print('请输入整数，多个整数请用,分割')
    exit()
except Exception:
    print('输入有误')
    exit()

#方法1
dict= {}
num=[]
temp=1
for i in intlist:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i]=dict[i]+1
        #判断出现最多的次数temp
        if dict[i] > temp:
            temp=dict[i]
#循环遍历找到最多次数对应的key
for key,value in dict.items():
    if value == temp:
        num.append(key)
print(f'出现最多的数字是{num}，出现次数为{temp}次')



#方法2
dict= {}
num=[]
temp=1
for i in intlist:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i]=dict[i]+1
    #判断出现最多的次数temp
    if dict[i] > temp:
        temp=dict[i]
        num.clear()
        num.append(i)
    elif dict[i] == temp:
        num.append(i)
print(f'出现最多的数字是{num}，出现次数为{temp}次')