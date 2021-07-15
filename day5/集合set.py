# set 不支持索引和切片，是一个无序的且不重复的容器
# 类似于字典 但是只有key  没有value
#------------- 创建集合
dic1={1:3}
set1={1,2,3}
set2={2,3,4}
# print(type(set1))
# print(type(dic1))
#------------- 添加操作
# set1.add('python')
# print(set1)
#------------- 清空操作
# set1.clear()
# print(set1)
#------------- 差集操作
# rs=set1.difference(set2)
# print(rs)
# print(set1-set2)
# print(set1)
#------------- 交集操作
# print(set1.intersection(set2))
# print(set2&set1)
#------------- 并集操作
# print(set1.union(set2))
# print(set1 | set2)
#------------- pop 就是从集合中拿数据并且同时删除
# print(set1)
# quData=set1.pop()#随机拿 因为set没索引
# print(quData)
# print(set1)
#------------- 指定移除的元素
# print(set1.discard(3))
# print(set1)
#------------- update 两个集合
set1.update(set2)
print(set1)