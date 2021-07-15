# 创建字典
#dictA={"键":'值','key':'value'}
dictA={"pro":'艺术','shcool':'北京电影学院'}

# 添加字典数据
#dictA['键']=值
dictA['name']='李易峰'  #key:value
dictA['age']='30'
dictA['pos']='歌手'

# print(dictA) #输出完整的字典
#-------------键值对个数
# print(len(dictA))
# print(type(dictA))

# print(dictA['name']) #通过键获取对应的值
# dictA['name']='谢霆锋'  #修改键对应的值
dictA['shcool']='香港大学'

# ------------可以添加或者更新
# dictA.update({'height':1.80})
# print(dictA)

# ------------获取所有的键
# print(dictA.keys())
# ------------获取所有的值
# print(dictA.values())
# ------------获取所有的键和值
print(dictA.items())
for key,value in dictA.items():
    print('%s==%s'%(key,value))

# --------------------删除操作
# del dictA['name']  #--------通过指定键进行删除
# dictA.pop('age')   #--------通过指定键进行删除
#print(dictA)

# --------------按照key排序
# print(sorted(dictA.items(),key=lambda d:d[0]))
# 按照value排序
# print(sorted(dictA.items(),key=lambda d:d[1]))

# ---------------字典拷贝 字典之间不能直接赋值 dicB = dicA
# import copy
# # dictB=copy.copy(dictA) #浅拷贝
# dictC=copy.deepcopy(dictA) #深拷贝
# print(id(dictC))
# print(id(dictA))
# # dictB['name']='peter'
# dictC['name']='刘德华'
# print(dictC)
# print(dictA)

# 拷贝有三种方式：
# 直接赋值：其实就是对象的引用（别名）。
# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。在源对象上操作新对象可能会受影响。
# 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。在源对象上操作新对象不受影响

