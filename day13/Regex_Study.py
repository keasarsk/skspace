# 通过python中的re模块的使用最终掌握正则表达式的常用匹配规则
# 匹配的整个表达式的字符串，group() 可以一次输入多个组号，
#   在这种情况下它将返回一个包含那些组所对应值的元组
import re
strData = 'Python is the best language in the world'

# match 只能匹配以xxx开头的子符串，第一个参数是正则，第二个参数是需要匹配的字符串
# res = re.match('python',strData,re.I|re.M) #第三个参数 I 表示忽略大小写
res = re.match('(.*) is (.*?) .*',strData,re.I|re.M)
if res:
    print('匹配成功...')
    # print(res)
    print(res.groups())
    print(res.group(1))
    print(res.group(2))
    # print(res.group(3))# 出错 因为正则表达式中没有第三组了
else:
    print(res.group()) #如果匹配失败 是没有group函数的 因为是一个空对象None
    print(res)
    print('匹配失败...')

