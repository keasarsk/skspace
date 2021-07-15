#----------------- 求三组连续自然数的和 ：1-10、20-30、35-45的和-----------
# def numberSum(start,end):
#     result=start
#     index=start
#     while index<end:
#         index += 1
#         result+=index
#         pass
#     return result
#     pass
#
# print(numberSum(1,10)+numberSum(20,30)+numberSum(35,45))
#----------------- 100个和尚吃100个馒头，大和尚一人吃3个馒头
# 小和尚三人吃1个馒头。请问大小和尚各多少人？
# big=range(33)
# small=range(300)
# for i in big:
#     if ((100-i)/3)%1==0 and i*3+(100-i)/3==100:
#         print('大和尚%d个，小和尚%d个'%(i,100-i))
#         pass
#     else:continue
#     pass

#----------------- 指定一个列表，列表里含有唯一一个只出现过一次的数字。
# 写程序找出这个“独一无二”的数字
listA=[1,1,2,3,4,5,6,7,8,9,0,1,3,4,5,6,7,8,2,0]
# setA={listA[0]}
# listB 隔一个存一下 间隔处存放上位置元素出现次数
# listB 依次存listA 存时对比是否已在listB存在 若存在就将listA所有该元素删除
# 直至listA遍历结束 剩的那个就是
# list的count()函数 统计某元素出现次数
for items in listA:
    if listA.count(items)==1:
        print(items)
        break
        pass
    else:continue


