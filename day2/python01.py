# --------------------------------单分支
# if  条件表达式: 比较运算符 逻辑运算符 /复合的条件表达式
#     代码指令
#     .......

# if score<=60: #满足条件就会输出打印的提示
#     print("成绩不是太理想,要继续加油哦")
#     pass #空语句
# print("语句运行结束")
# 双分支
# if  条件表达式: 比较运算符 逻辑运算符 /复合的条件表达式
#     代码指令
# else:
#     代码指令
# 必定会执行其中一个分支

# if score>60: #True
#     print("你的成绩及格了...")
#     pass
# else: #false时候才会执行
#     print('成绩不合格，请继续努力')
#     pass

# --------------------------------多分支的选择【多个条件】
#  if  条件表达式: 比较运算符 逻辑运算符 /复合的条件表达式
#     代码指令
#  elif 条件表达式:
#     代码指令
#  ......
#     else:
# 特征:
# 1.只要满足其中一个分支，就会退出本层if语句结构【必定会执行其中一个分支】
# 2.至少有2中情况可以选择
# elif 后面必须的写上条件和语句
# ----------------else 是选配，根据实际的情况来填写

# score=int(input('请输入你的成绩...'))
# print(type(score))
# if score>90:
#     print('您的成绩是A等级')
#     pass
# elif score>=80:
#     print('您的成绩是B等级')
#     pass
# elif score>=70:
#     print('您的成绩是C等级')
#     pass
# elif score>=60:
#     print('您的成绩是D等级')
#     pass
# else:#选配
#     print('可以回家修理地球了....')

# print('程序运行结束了.....')

# 多分支 多条件的演练
# 猜拳击的小游戏
# 0:石头 1:剪刀 2:布
import random #直接导入产生随机数的模块
# 计算机  人
count=1
while count<=10:
    person=int(input('请出拳:[0:石头 1:剪刀 2:布]'))
    computer=random.randint(0,2)
    if person==0 and computer==1: #多条件
        print("厉害了..你赢了")
        pass
    elif person==1 and computer==2:
        print("厉害了..你赢了")
    elif person==2 and computer==0:
        print("厉害了..你赢了")
        pass
    elif person==computer:
        print('不错 居然是平手')
        pass
    else:
        print('哈哈...你输了吧')
        pass
    count+=1



