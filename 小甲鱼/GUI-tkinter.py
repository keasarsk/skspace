import tkinter as tk# Tkinter 是使用 python 进行窗口视窗设计的模块。
# Tkinter模块("Tk 接口")是Python的标准Tk GUI工具包的接口

# app = tk.Tk()# 实例化TK用于容纳整个
# app.title("邵凯")# 标题栏
# # app.pack()# pack()是调节组件的
# thelable = tk.Label(app,text = "我的第二个程序窗口")# label 组件
# thelable.pack()# park（）用于自动调节组件的尺寸等
# app.mainloop()# 窗口主事件循环

class APP:
    def __init__(self,master):
        frame = tk.Frame(master)# frame 框架在复杂布局中将组件分组
        frame.pack()# pack(side = LEFT或RIGHT或BUTTOM 默认顶部)
        # pack(padx = 1,pady = 2)x轴1像素 y轴2像素

        self.hi_there = tk.Button(frame, text = '打招呼', fg = 'blue', command =self.say_hi)
        # 按钮放入框架fram中 按钮显示打招呼 按钮foreground颜色(文字的颜色)bule  bg是背景色
        # 按钮被按下时启动command命令：运行say_hi函数
        self.hi_there.pack()

        pass
    def say_hi(self):
        print('你好')

    pass

root = tk.Tk()
app = APP(root)
root.mainloop()


