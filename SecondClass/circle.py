'''
作业计算圆的周长和面积，要求从终端输入圆的半径r，输出格式： 圆的周长为: 5，圆的面积为: 10
'''
# try:
#     r=int(input('请输入半径'))
# except Exception:
#     print('输入有误')
# c =3.14*2*r
# s =3.14*r*r
# print('周长是：%2f,面积是：%2f'%(c,s))



def circle(r):
    return '周长是：%2f,面积是：%2f'%(3.14*2*r,3.14*r*r)


if __name__ == '__main__':
    try:
        r = float(input('请输入半径'))
    except Exception:
        print('输入有误')
    print(circle(2))


