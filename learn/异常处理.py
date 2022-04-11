import traceback

try:
    a = int(input('请输入'))
    print(a)

except ValueError:
    print('输入错误')
except BaseException :
    print('出错了')


