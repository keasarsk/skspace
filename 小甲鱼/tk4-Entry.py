from tkinter import *

root = Tk()

# # ----------------------简单的文本框方法实验
# e = Entry(root)# Entry() 简单的文本框
# e.pack(padx = 10,pady = 10)
# e.delete(0,END)# 删除index 从0 到END（或者-1）的内容
# e.insert(0,"默认文本")# 在index = 0 处插入“默认文本”


# # grid（row = 行数值，Column = 列数值）# 以表格形式管理组件
# Label(root,text = "作品：").grid(row = 0,column = 0)
# Label(root,text = "作者：").grid(row = 1,column = 0)
# e1 = Entry(root)
# e2 = Entry(root)
# e1.grid(row = 0,column = 1)
# e2.grid(row = 1,column = 1)
# def show():
#     print("作品：《{}》".format(e1.get()))
#     print("作者：{}".format(e2.get()))
#     pass
#
# Radiobutton(root,text = "获取信息",width = 10,indicatoron = False,command = show)\
#     .grid(row = 2,column = 0,sticky = W,padx = 10,pady = 5)# sticky作用和pack()方法里的anchor一样 用法也一样
# # root.qiut()根窗口退出方法
# Radiobutton(root,text = "退出",width = 10,indicatoron = False,command = root.quit)\
#     .grid(row = 2,column = 1,sticky = E,padx = 5,pady = 10)

# # -----------------隐藏输入时内容 基本代码与上文同
# Label(root,text = "账号：").grid(row = 0,column = 0)
# Label(root,text = "密码：").grid(row = 1,column = 0)
# # 需要两个变量存放账号和密码
# v1 = StringVar()
# v2 = StringVar()
#
# e1 = Entry(root,textvariable = v1)
# e2 = Entry(root,textvariable = v2,show = "*")# 在Entry输入框显示的就是 *
#
# e1.grid(row = 0,column = 1)
# e2.grid(row = 1,column = 1)
# def show():
#     print("账号：{}".format(e1.get()))
#     print("密码：{}".format(e2.get()))
#     pass
#
# Radiobutton(root,text = "确认",width = 10,indicatoron = False,command = show)\
#     .grid(row = 2,column = 0,sticky = W,padx = 10,pady = 5)# sticky作用和pack()方法里的anchor一样 用法也一样
# # root.qiut()根窗口退出方法
# Radiobutton(root,text = "退出",width = 10,indicatoron = False,command = root.quit)\
#     .grid(row = 2,column = 1,sticky = E,padx = 5,pady = 10)

# ----------------------------Entry验证功能 简单的计算器例子
'''
开启Entry对输入文本验证功能。
1、实现该功能，需要通过设置validate、validatecommand和invalidcommand三个选项。 
2、启用验证的开关是validate选项，该选项可以设置以下的值：
    focus：当entry组件获得或者失去焦点的时候验证 
    focusin：当entry组件获得焦点的时候验证 
    focusout:当entry组件失去焦点的时候验证 
    key:当输入框被编辑的时候验证 
    all:当出现上面任何一种情况时候验证 
    none:关闭验证功能。默认设置为该选项
3、validatecommand选项指定一个验证函数，该函数只能返回True或者False表示验证结果，一般情况下验证函数只需要知道输入框中的内容即可，
可以通过Entry组件的get()方法来获得该字符串。
4、invalidcommand选项指定的函数只有在validatecommand的返回值为False的时候才被调用。
'''
'''
validatecommand选项指定一个验证函数，该函数只能返回True或者False表示验证结果
invalidcommand选项指定的函数只有在validatecommand的返回值为False的时候才被调用。
'''
root.title("简单的计算器")
frame = LabelFrame(root)
frame.pack(padx =10,pady = 10)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
    return content.isdigit()

'''
Tkinter 为验证函数提供了一些隐藏的功能选项。
%d:操作代码-0表示删除操作，1表示插入操作，2表示获得、失去焦点或textvariable变量值被修改
%i:1、当用户尝试插入或删除操作时候，该选项表示插入或删除的位置（索引号）
    2、如果是获得、失去焦点或textvariable变量值被修改该而地啊哟用验证函数，那么该值是-1
%P: 1、当输入框的值允许改变的时候，该值有效
    2、该值为输入框的最新文本内容    
%s: 1、该值为调用验证函数前输入框的文本内容
%S：1、当插入或删除操作出发验证函数的时候，该值有效
    2、该选项表示文本被插入和删除的内容
%v: 1、该组件的validate选项的值
%V: 1、调用验证函数的原因
    2、该值是focusin，focusout，ke，或forced（textvariable选项指定的变量值被修改）中的一个
%W: 该组件的名称   
'''
'''
为了使用这些选项，我们可以这样修改我们的validatecommand选项：
validatecommand=(f,s1,s2,……)
其中，f是验证函数名，s1,s2等是额外的选项，这些选项会作为参数依次传给f函数，
我们在使用隐藏的功能选项前需要冷却，这就是register()方法将验证函数包装起来。
'''

'''
注意在这里我们不能使用entry控件的get()方法来获取输入的内容
因为当validate选项指定为key的时候，有任何的输入操作都会被拦截
到这个函数当中，也就是说先拦截，只有这个函数返回True，那么输入的内容
才会到变量里面去，也就是说我们使用get函数并无法get到数据，get函数在这个
函数之后才会有效，get函数得到的是变量的值。
所以只有使用%P来获得最新的输入框的内容
'''

def test(content):
    if content.isdigit():
        return True
    else:
        return False

# 使用了特殊技能的函数需要使用register将其封装起来才可以
testCMD = root.register(test)

e1 = Entry(frame, width=10, textvariable=v1, validate='key', \
           validatecommand=(testCMD, '%P')).grid(row=0, column=0)
Label(frame, text='+').grid(row=0, column=1)

e2 = Entry(frame, width=10, textvariable=v2, validate='key', \
           validatecommand=(testCMD, '%P')).grid(row=0, column=2)
Label(frame, text='=').grid(row=0, column=3)
# e3输入框是显示结果文本框，所以不允许修改里面的值。将state属性设置为state='readonly'只读
e3 = Entry(frame, width=10, textvariable=v3, state='readonly').grid(row=0, column=4)

def calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(str(result))

Button(frame, text='计算结果', command=calc).grid(row=1, column=2, padx=5)


mainloop()