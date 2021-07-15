# os模块提供了多数操作系统的功能接口函数。
# 在python编程时，经常和文件、目录打交道，这时就离不了os模块
import os
import shutil
print(os.name)# 输出系统名字 Linux是posix  Windows是nt
# os.rename('Test.txt','Test_重命名.txt')
# os.remove('File_del.py') #删除文件 前提是文件必须存在
# os.mkdir('TestCJ') 创建文件夹
# os.rmdir('TestCJ') #删除文件夹 文件必须存在
# mkdir 创建一级目录
# os.mkdir('d:/Python编程/sub核心') #不允许创建多级
# 创建多级目录
# os.makedirs('d:/Python编程/sub核心/三级sub') #允许
# os.rmdir('d:/Python编程') #只能删除空目录
# 如果要删除非空目录的话 就需要调用shutil模块
# shutil.rmtree('d:/Python编程') #非空删除

# 获取当前的目录
# print(os.getcwd())

# 路径的拼接
# print(os.path)
# print(os.path.join(os.getcwd(),'venv'))

# 获取python中的目录列表
# listRs=os.listdir('d:/')  老版本的用法
# for dirname in listRs:
#     print(dirname)
# 使用现代版的写法
# scandir 和 with一起来使用  这样的话 上下文管理器会在迭代器遍历完成后自动
# 去释放资源
# with os.scandir('d:/') as entries:
#     for entry in entries:
#         print(entry.name)

# basePath='d:/'
# for entry in os.listdir(basePath):
#     # if os.path.isfile(os.path.join(basePath,entry)):
#     #     print(entry)
#     if os.path.isdir(os.path.join(basePath,entry)):
#         print(entry)
#         pass
