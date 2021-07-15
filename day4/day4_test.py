#------------------------函数---求接收多个参数和------------------
# def arguements_sum(*args):
#     sum=0
#     for i in args:
#         sum+=i
#         pass
#     return sum
#     pass
# print(arguements_sum(1,3,5,9))

#------------------------函数---列表形式返回参数（列表或元组）序列的奇数位元素------------------
# def jishu(ls):
#     j=1
#     listss=[]
#     for i in ls:
#         if j % 2 == 1:  # 判断奇数位
#             listss.append(i)
#             pass
#         j+=1
#         pass
#     return listss
# ls=[1,2,3,4,5,6,7]
# lists=jishu(ls)
# print(lists)

#----------------------------------函数---检查输入字典的value 长度------------------------------
def addToDic(**kwargs):
    new_kwargs= {}
    for key,value in kwargs.items():
        if len(value)>=2:
            new_kwargs[key]=value[:2]
        else:
            new_kwargs[key]=value
        pass
    return new_kwargs
    pass
dicA={'s':'sss','sk':'sksk'}
print(dicA)
print(addToDic(**dicA))
