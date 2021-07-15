# 序列操作 str 元组、 list

# all()  result:bool 对象中的元素除了是 0、NULL、FALSE 外都算 TRUE, 所有的元素都为True时结果就为True
# print(all([])) #True
# print(all(())) #True
# print(all([1,2,4,False]))
# print(all([1,2,4]))
# print(all((3,4,0)))

# any  result:bool 类似于逻辑运算符 or的判断，只要有一个元素为True 结果就为True
# print('--------any-------------')
# print(any(('',False,0)))
# print(any((1,2,3)))

# # sort 和sorted
# li=[2,45,1,67,23,10] #原始对象
# # li.sort() #list的排序方法 直接修改的原始对象
# tupArray=(2,45,1,67,23,10)

# # varList=sorted(li) #升序排列
# # varList=sorted(li,reverse=True) #降序排序
# # print('--------排序之后---------{}'.format(varList))

# # zip() :就是用来打包的，会把序列中对应的索引位置的元素存储为一个元组
# s1=['a','b','c']
# s2=['你','我','c他','peter']
# s3=['你','我','c他','哈哈','呵呵']
# print(list(zip(s1))) # 压缩一个数据 结果 [('a',), ('b',), ('c',)]
# zipList=zip(s2,s3) #两个参数
# print(list(zipList))
def printBookInfo():
    '''
    zip 函数的使用
    :return:
    '''
    books=[] #存储所有的图书信息
    id=input('请输入编号: 每个项以空格分隔')  #str
    bookName = input('请输入书名: 每个项以空格分隔') #str
    bookPos = input('请输入位置: 每个项以空格分隔')
    idList=id.split(' ')
    nameList = id.split(' ')
    posList = id.split(' ')

    bookInfo=zip(idList,nameList,posList) #打包处理
    for bookItem in bookInfo:
        '''
        遍历图书信息进行存储
        '''
        dictInfo={'编号':bookItem[0],'书名':bookItem[1],'位置':bookItem[2]}
        books.append(dictInfo) #将字典对象添加到list容器中
        pass
    for item in books:
        print(item)

# printBookInfo()

# enumerate 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
# 一般用在 for 循环当中
listObj=['a','b','c']
# for index,item in enumerate(listObj,5):
#     print(index,item)
#     pass
dicObj={}
dicObj['name']='李易峰'
dicObj['hobby']='唱歌'
dicObj['pro']='艺术设计'
# print(dicObj)

for item in enumerate(dicObj):
    print(item)
# 这时只取了key  结果：
# (0, 'name')
# (1, 'hobby')
# (2, 'pro')



