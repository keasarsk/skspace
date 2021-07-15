from tkinter import *


root = Tk()# 一个窗口
root.title('翻牌子')

# girls = ['刘亦菲','刘诗诗','桂纶镁','佟丽娅','王冰冰',]
# v = IntVar()# tkinter的IntVar类型 二进制整数 0或1
# print(type(v))
## -----------------checkbutton 带确认的选项按钮
# for i in girls:
#
#     v.append(IntVar())
#     b = Checkbutton(root,text = i)#,variable = v[-1])???????
#     b.pack(anchor=NW)# anchor指定显示位置N W S E NW NE SW SE,与side不同 ？？？？？？
#     #b.pack(side = LEFT)
#     pass

# -----------------Radiobutton 单选的待确认的选项按钮
# Radiobutton(root,text = girls[0],variable = v,value = 1).pack(anchor = W)
# # 这些Radiobutton都使用variable（变量） v ，value是当点击此按钮后赋予v的值，
# # 用来互斥其他的选项（因为v已有值，且值不同于其他选项，故不能再选其他的选项）
# # 若多个选项同value 则点击其中任一选项 其他同value选项也会选上
# Radiobutton(root,text = girls[1],variable = v,value = 2).pack(anchor = W)
# Radiobutton(root,text = girls[2],variable = v,value = 3).pack(anchor = W)
# Radiobutton(root,text = girls[3],variable = v,value = 4).pack(anchor = W)
# # indicatoron = False # 复选框形式不以选项点 而以选项框形式
# Radiobutton(root,text = girls[4],variable = v,value = 5,indicatoron = False).pack(anchor = W)

# ---------------循环使用Radiobutton
# ---------------添加frame标题
frame = LabelFrame(root, text ="一些脚本语言", padx = 1, pady = 1)
frame.pack(padx = 10, pady = 10)
langs = [
    ("python",1),
    ("perl",2),
    ("ruby",3),
    ("lua",4),]

v = IntVar()

for lang,num in langs:
    b = Radiobutton(frame, text = lang, variable = v, value = num)
    b.pack(anchor = W)

mainloop()