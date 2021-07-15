# 循环的分类
# while 语法结构
# while 条件表达式:
#     代码指令
# 语法特点
# 1.有初始值
# 2.条件表达式
# 3.变量【循环体内计数变量】的自增自减, 否则会造成死循环
# 使用条件：循环的次数不确定，是依靠循环条件来 结束
# 目的: 为了将相似或者相同的代码操作变得更加简洁，使得代码可以重复利用

# while的使用
# print(1)
# print(2)
# print(3)
# ......
# 案例  输出1-100之间的数据
# index=1 #定义一个变量
# while index<=100:
#     print(index)
#     index+=1
#     pass
# 打印九九乘法表  循环的嵌套
# row=9
# while row>=1:
#     col=1
#     while col<=row:
#         print("%d*%d=%d"%(row,col,row*col),end=" ")
#         col+=1
#         pass
#     print()
#     # row+=1
#     row -= 1
#     pass
# while False:
#     if 3==3:
#         print('树池福克斯劳动法开始了')
#         continue
#     pass
# else:
#     print('可以执行吗')

# -------------------------------------for 循环
# 语法特点:遍历操作，依次的取集合容器中的每个值
# for 临时变量 in 容器:
#     执行代码块
tags='我是一个中国人' #字符串类型本身就是一个字符类型的集合
# for item in tags:
#     print(item)
#     pass
# range 此函数可以生成一个数据集合列表
# range(起始:结束:步长)  步长不能为0
# sum=0
# for data in range(1,101): #左边包含右边不包含
#     sum+=data #求累加和
#     # print(data,end=' ')
#     pass
#
# print("sum=%d"%sum)
# print('---for的使用---')
# for data in range(50,201):
#     if data%2==0:
#         print("%d是偶数" %data)
#         pass
#     else:
#         print("%d是奇数"%data)
# pass

# -------------------------------------------break和continue
# break 代表中断结束   满足条件直接的结束本层循环
# continue:结束本次循环，继续的进行下次循环（当continue的条件满足的时候，本次循环剩下的语句将不在执行
# 后面的循环继续）
# 这两个关键字只能用在循环中
sum=0
for item in range(1,51):
    if sum>100:
        print('循环执行到%d就退出来了'%item)
        break #退出循环体
        pass
    sum+=item
    pass

# print("sum=%d"%sum)
# print('continue的使用')
# for item in range(1,100): #求出来奇数
#     if item%2==0:
#         continue
#         print('在continue的额后面会不会执行呢')
#         pass
#     print(item)
#     pass

# for item in 'l love python':
#     # if item=='e':
#     #     break #彻底中断循环
#     if item=='o':
#         continue
#     print(item,end=' ')

# index=1
# while index<=100:
#     if index>20:
#         break
#         pass
#     print(index)
#     index+=1

# 99乘法表用for来实现
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end=' ')
#         pass
#     print() #控制换行
#     pass
# for----else
# for item in range(1,11):
#     print(item,end=' ')
#     if item>=5:
#         break
#     pass
# else:
#     print('就是在上面循环当中 只要是出现了break 那么else的代码将不在执行')

# account='wyw'
# pwd='123'
# for i in range(3):
#     zh=input('请输入账号:')
#     pd=input('请输入密码:')
#     if account==zh and pwd==pd:
#         print('恭喜您登录成功...')
#         break #退出本层循环了
#         pass
#
#     pass
# else:
#     print('您的账号已经被系统锁定...')


# while----else

index=1
while index<=10:
    print(index)
    if index==6:
        break
    index+=1
    pass
else:
    print('else执行了吗.....')










