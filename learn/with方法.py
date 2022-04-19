class MyContentMgr:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用了')
    def show(self):
        print('show方法被调用了')

with MyContentMgr() as file:#相当于file=MyContentMgr()
    file .show()
#无论是不是正常运行，都会执行exit方法

#复制图片
with open('a.txt','r') as src_file:
    with open('copy.txt','w') as target_file:
        target_file.write(src_file.read())