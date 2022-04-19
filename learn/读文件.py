file=open('a.txt','r')
print(file.readlines())#readlines()输出为列表

#文件若是不存在将会创建文件,但模式要是写入的模式‘w’
file=open('b.txt','w')
file.write('python')
# file.readlines()

#复制文件
src_file=open('a.txt','r')
target_file=open('copy.txt','w')
target_file.write(src_file.read())#将src_file读出来的内容写入target_file，完成复制


