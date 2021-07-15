# compile re模块中的编译方法 可以把一个字符串编译成字节码
# 优点: 在使用正则表达式进行 match的操作时，python会将字符串转为正则表达式对象，
# 而如果使用complie则只需要完成一次转换即可，以后再使用该模式对象的话 无需重复转换，
import re
# reobj=re.compile('\d{4}')# 把这个正则表达式用变量标记 方便以后调用变量名使用此式
# # 开始去使用模式对象reobj
# rs=reobj.match('1235678')
# print(rs.group())
#
# print(re.match('\d{4}','1235678').group())
# re.search  规则是:在全文中匹配一次，匹配到就返回
# data='我爱伟大的祖国,I love China,China is a great country'
# rs=re.search('China',data)
# print(rs)
# print(rs.group())
# print(data[19])
# print(data[20])
#re.findall() 查询字符串中某个正则表达式全部的非重复出现的情况 返回的是一个符合正则表达式的结果列表
data='华为是华人的骄傲华侨'
rs=re.findall('华.',data)
rsearch=re.search('华.',data)
# print(rsearch)
# 改造一下使用compile
# reobj=re.compile('华.') #创建一次正则对象转换
# print(reobj.search(data))
# print(reobj.findall(data))
# re.sub 实现目标的搜索和替换
# re.subn 实现目标的搜索和替换  还返回被替换的数量 以元组形式
# dataS='Python是很受欢迎的编程语言Python'
# pattern='[a-zA-Z]+'  #字符集的范围 + 号 代表 前导字符模式出现1次以上
# res=re.sub(pattern,'Java',dataS)
# resn=re.subn(pattern,'Java',dataS)
# print(res)
# print(resn)
# re.split  实现分割字符串
data='百度,腾讯,阿里,华为,360'
rs=re.split(',',data)
print(type(rs))
print(rs)

