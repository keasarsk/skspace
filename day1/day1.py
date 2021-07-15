# print('hello python')
# print('人生苦短、我用python')
# print('欢迎同学们来到求知讲堂学习python')
# print('一起加油吧')

# 变量
# 定义规则： 变量名=数据
# 赋值时候不需要指定数据类型（与c java不同）

# a就是变量的名字 对应一个盒子 里面装的数据就是10
a=10#解释器为a和10分别开辟了一个空间 然后在a的物理地址中放入10的物理地址即完成了=
print(type(a))
# 变量是可以多次赋值的【在程序执行的过程中 值可以改变的量】
a=20
a=100
# 变量就是用来存储数据的
a='吴老师外文'

# ------------------查看变量是什么类型
print(type(a))
a=12.67
print(type(a))
a=True
print(type(a))
#print(a) #使用变量  先定义变量 然后才能使用
# 高级类型
b=()  #元组类型
print(type(b))
c=[]  #列表类型
print(type(c))
#
d={}  #字典类型
print(type(d))
# 变量的命名规则
# 变量必须以字母（a - z，A - Z）或下划线（_）开头
# 其他字符可以是字母，数字或 _
# 变量区分大小写
# Python关键字不能用作变量名。
# 变量的命名不能以数字来开头
Name='刘德华'
name='吴老师那你'
_age=50
# True=12.3 #不能这样定义  因为True是关键字
print(name,Name)
print(Name,_age)
userName='李明'
userAge=30
user_name='李明'
user_age=30

# + - * / % **（幂） //（除，只保留整）  算符运算符
# += -= *= %= **=   赋值运算符
# 定义如下两个变量
a=7
b=3
c=10
print(a+b*c)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)


# == !=  > <  >=  <= 比较运算符 结果是bool【True/False】
a,b=10,5
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

#-------------------- 逻辑运算符  and or not
# and 规则 x and y , x 和y 同为真【True】 结果才为真，否则结果就为假
# 定义四个变量
a,b,c,d=20,13,2,14
# 操作是bool类型的表达式
# print(a+b>c*d and c+d<a) #True
# print(a+b>c*d and c+d>a) #False

# ------------------- 操作数字和其他类型表达式
# x and y：如果x非零或者True, 运算的结果是y ; 如果x为零，则结果为0
# print(a and b)
# print(1 and 20)
# print(12 and 23)
# print(0 and 34)
# print(0 and 12)

# or 逻辑或  x or y ,x 或者y 只要有其中一个条件为真,结果就为True
print('or')
# print(a-b>d or c>a) #全部为False  结果是false
# print(a-b<d or c>a)
# or 操作数字和其他类型表达式
# 如果x非零或者True 则结果为x，如果x为零 则结果为y
# print(a or b) #b
# print(1 or 3) #3
# print(3 or 12) #12
# print(0 or 6) #6

#-------------------- not 取反 真假切换
# print(not 2>3)
# print(not True)

#-------------------- 优先级
# ()->not-->and-->or
# 例子
print(2>1 and 1<4 or 2<3 and 9>6 or 2<4 and not 3<2)

#-------------------- 输出 %占位符
# me='我的'
# # # classPro='清华附中一年3班'
# # # age=7
# # # print('%s名字是小明: 来自【%s】 今年%d岁了'%(me,classPro,age))
# # # print('%s名字是胖虎: 来自【%s】 今年%d岁了'%(me,classPro,age))
# # # print('%s名字是小叮当: 来自【%s】 今年%d岁了'%(me,classPro,age))

#--------------------\n换行效果 print('我可以\n换行吗')

#-------------------- 练习输出
# 姓名: 老夫子
# QQ:66666666
# 手机号:5024193635
# 公司地址:广州市白云区1
# name='老夫子'
# QQ='66666666'
# phone='5024193635'
# addr='广州市白云区1'

#-------------------- 格式化输出 字符串理用{} 外边.format
# print('姓名:{} 年龄是:{} 岁'.format(name,23))
# print('QQ:{}'.format(QQ))
# print('手机号:{}'.format(phone))
# print('地址:{}'.format(addr))
# print('------------以上是format形式的-------------------')
# print("姓名:%s"%name)
# print("QQ:%s"%QQ)
# print("手机号:%s"%phone)
# print("地址:%s"%addr)
#格式输出的其他方式 .format()

#-------------------- input("提示语")   获取键盘输入的内容 单引号也可
name=input("请输入您的姓名:")
age=int(input("请输入您的年龄:"))#接受时转换成想要的类型
print(type(name))
QQ=input('请输入您的qq')
phone=input("请输入您的电话:")
addr=input("请输入您的地址:")
print('姓名:%s 年龄是:%d 岁'%(name,age))
# print('姓名:{} 年龄是:{} 岁'.format(name,age))
print('QQ:{}'.format(QQ))
print('手机号:{}'.format(phone))
print('地址:{}'.format(addr))

# -------------------- 注释
# 单行注释#
# 多行注释''' 注释'''或者"""注释 """
# ctrl +/ 注释全部选中内容
# 特别注释 指定python解析器的路径 ，在py文件首行 #!/usr/bin/python3








