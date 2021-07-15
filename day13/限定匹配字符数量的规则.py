 # *  匹配前一个字符出现0次或者无限次，即可有可无
import re
# res=re.match('[A-Z][A-Z]*','Ay') 匹配0次
# # res=re.match('[A-Z][a-z]*','Any') 匹配了2次
# res=re.match('[A-Z][a-z]*','Anyeverydayhappyislaveer') #可以匹配无限次
# print(res.group())
# +  匹配前一个字符出现1次或者无限次，即至少有1次
# res=re.match('[a-zA-Z]+','MYNAMEisfjksg')
# 匹配符合规范【规则是：不能以数字开头，只能包含字母、数字、下划线】的python变量命名
# result=re.match('[a-zA-Z_]+[\w]*','name')
# result=re.match('[a-zA-Z_]+[\w]*','_name')
# result=re.match('[a-zA-Z_]+[\w]*','na99m_e')
# print(result.group())
# ？ 告诉引擎匹配前导字符 0 次或者一次，事实上表示前导字符是可以选择的
# result=re.match('[a-zA-Z]+[0-9]?','nameFunck99m_e')
# print(result.group())
# {min,max}  告诉引擎匹配前导字符min次到max次 ，min和max必须都是非负整数
#  {count} 精确匹配
# result=re.match('\d{4}','1234567890')
#  {min,} max被省略的话 表示max没有限制了
# result=re.match('\d{4,}','123423542355673623623473457890')
# result=re.match('\d{4,8}','1234567898888')
# if result:
#     print('匹配成功 {}'.format(result.group()))
#     pass
# 匹配邮箱demo   格式xxxxxx@163.com
# regexMail=re.match('[a-zA-Z0-9]{6,11}@163.com','wanghua123uuu@163.com')
# if regexMail:
#     print('匹配成功 {}'.format(regexMail.group()))
#     pass

# mypath = 'G:\\py资料\\1-上课资料\\4-正则表达式课件\\html'
# print(mypath) # 路劲输出异常

# print(re.match('c:\\\\a.txt','c:\\a.txt').group())
# print(re.match(r'c:\\a.txt','c:\\a.txt').group()) #在正则前面加 r  表示原生的字符串，python字符串就不转义

# ^ 匹配字符串的开头
# result=re.match('^P.*','Python is langage')
# result=re.match('^P\w{5}','Python is langage')
# if result:
#     print(result.group())
# $ 匹配邮箱的结尾
result=re.match('[\w]{5,15}@[\w]{2,5}.com$','myfunckmail@mail.comTest')
if result:
    print(result.group())
    pass

