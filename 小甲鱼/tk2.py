from tkinter import  *


def callback():
    var.set("那也不行")
    pass
root = Tk()


frame1 = Frame(root)# 加了两个框架 分开窗口
frame2 = Frame(root)

var = StringVar()
var.set('您没有\n权限')

# textLabel = Label(root,text = '您没有\n权限',justify = LEFT,padx = 10)
#                 # justify 对齐
# textLabel.pack(side = LEFT)
#
# photo = PhotoImage(file='GUI.gif')# 不支持jpg png
# imgLabel = Label(root,image=photo)
# imgLabel.pack()

# 图片做背景

photo = PhotoImage(file='GUI.gif')
theLabel = Label(root,
                  # text = '您没有\n权限',
                  textvariable = var,
                 # 与上行区别在于 textvariable是个变量
                  justify = LEFT,

                  image = photo,
                  compound = CENTER,
                  font = ('宋体',20),
                  fg = 'blue')
                # compound 字体显示位置 font 字体 字号
theLabel.pack()
theButton = Button(frame2,text = '我就',command = callback)
theButton.pack()
frame1.pack(padx = 10,pady = 15)
frame2.pack(padx = 10,pady = 15)

mainloop()