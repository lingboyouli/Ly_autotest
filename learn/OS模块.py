#os模块是与操作系统相关的模块
#打开记事本
import os
# os.system('notepad.exe')
# os.system('calc.exe')
#直接调用可执行文件
# os.startfile('"C:\Program Files (x86)\Yinxiang Biji\印象笔记\Evernote.exe"')

print(os.getcwd())#当前文件所在位置
print(os.listdir('../learn'))#获取制定路径下的信息
# os.mkdir('mkdir')#创建目录
# os.makedirs('A/B/C')#创建多级目录
# os.rmdir('mkdir')#移除目录
# os.removedirs('A/B/C')#移除多级目录

import os.path

print(os.path.abspath('OS模块.py'))#获取制定文件的绝对路径
print(os.path.exists('OS模块.py'))#判断文件是否存在
print(os.path.join('D:\work\Ly_autotest','title.mp4'))#将路径和文件进行拼接（并不会有实际操作）
print(os.path.split('D:\work\Ly_autotest\\title.mp4'))#将目录和文件拆分
print(os.path.splitext('title.mp4'))#将文件名和后缀拆分
print(os.path.basename('D:\work\Ly_autotest\\title.mp4'))#从一个目录中提取文件名
print(os.path.dirname('D:\work\Ly_autotest\\title.mp4'))#从一个路径中提取文件路径，不包含文件名
print(os.path.isdir('D:\work\Ly_autotest\\title.mp4'))#判断是否为路径


#eg:列出指定目录下所有.py文件
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

#递归遍历目录下所有文件
lst=os.walk('D:\work')#输出是个元组
for dirpath,dirname,filename in lst:
    print(dirpath)
    print(dirname)
    print(filename)
    print('---------------------------------------')


