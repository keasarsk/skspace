# 文件的操作
# --------------打开文件 open('文件名称','打开模式')  打开模式见ppt
# 默认的编码是gbk 这个是中文编码，最好的习惯呢就是我们再打开一个文件的时候
# 给它指定一个编码类型

# 在给定名称的文件不存在的情况下 w 模式 是创建一个此名称的文件 ；若已存在则覆盖
# fobj=open('./Test.txt','w',encoding='utf-8')# 打开文件

# # 开始操作 读/写操作
# fobj.write('在苍茫的大海上')
# fobj.write('狂风卷积着乌云')
# fobj.write('在乌云和大海之间\r\n')
# fobj.write('海燕像黑色的闪电\r\n')

# fobj.close()# 关闭文件

# wb 以二进制的形式去写数据
# fobj=open('Test_1.txt','wb') #str-->bytes
# fobj.write('在乌云和大海之间'.encode('utf-8'))
# fobj.close()
# fobj=open('Test.txt','a') #用于追加数据
# fobj.write('在乌云和大海之间\r\n')
# fobj.write('海燕像黑色的闪电\r\n')
# fobj.close()


fobj=open('Test.txt','a') # ---------------- a  文件末追加数据
fobj.write('在苍茫的大海上')
fobj.write('狂风卷积着乌云')
fobj.write('在乌云和大海之间\n')
fobj.write('海燕像黑色的闪电\n')
fobj.write('今天我诗兴大发\n')
fobj.write('发感觉咋样呢\n')
fobj.close()

# 读数据操作
f=open('Test.txt','rb')
data=f.read() # read()默认读取所有的数据
print(data)
print(data.decode('gbk'))
# print(f.read(12))
# # print(f.read())# 两个第二个read会继续第一个read的位置继续往后读

# print(f.readline()) #读一行数据
# print(f.readlines(1))
# f.close()  #文件对象关闭掉

# with上下文管理对象
# 优点 自动释放打开关联的对象
with open('Test.txt','a') as f:
    # print(f.read())
    f.write('我觉得python非常的好学\n')


# 小结
# 文件读写的几种操作方式
# read  r r+  rb  rb+
# r r+ 只读  使用普通读取场景
# rb  rb+  适用于 文件 图片 视频 音频 这样文件读取
# write w  w+ wb+  wb a  ab
# w wb+ w+  每次都会去创建文件
# 二进制读写的时候 要注意编码问题  默认情况下 我们写入文件的编码是gbk
# a  ab a+  在原有的文件的基础之后去【文件指针的末尾】去追加，
# 并不会每次的都去创建一个新的文件

def ctime(sec):
    pass


