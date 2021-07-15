import urllib.request
import os
# import platform
'''
1   download中目标网址page_url
2   find_image中前缀
3   find_image中查找类型
4   save_image中有时需要前缀
'''
def url_open(url):
    '''
    打开这个URL
    :param url:
    :return:
    '''
    # # 生成一个request对象 为了给它能添加一个文件头 让它看上去更像浏览器访问而不是爬虫
    # req = urllib.request.Request(url)
    # req.add_header('')

    response = urllib.request.urlopen(url)# 打开这个url
    html = response.read()
    return html
    pass
def get_page(url):

    pass

def find_image(html):

    # 前缀
    fore = 'src="'

    a = html.find(fore)
    img_addres = []# 列表，存放图片的地址
    while a != -1:
        b = html.find('.jpg',a,a+255)# 查找.jpg 字符串 从a开始 至a+255截至
        if b != -1:
            img_addres.append(html[a+46:b+4])
        else:
            b=a+48
        a=html.find(fore,b)

    # for each in img_addres:# 输出所有此次从抓取的数据的列表
    #     # print(each)
    #     print(1)

    return img_addres
    pass

def save_image(img_addrs_list,i):
    count = 0
    for each in img_addrs_list:
        # save需要前缀：
        #img_addrs_list_1 = 'https://img.viptoon.cc/static/upload/book/' + str(each)
        # save不需要前缀：
        img_addrs_list_1 =str(each)

        # filename = each.split('/')[-1]# split 取最后一个作filename
        # with open(filename,'wb') as f:
        #     # img = url_open(img_addrs_list_1)
        #     img = url_open(each)
        #     f.write(img)

        # 序列作名字
        filename = str(i)+'.'+each.split('.')[-1]
        print('正在写入：',filename)
        with open(filename, 'wb') as f:# wb模式打开？？？？？
            img = url_open(img_addrs_list_1)
            f.write(img)
            count += 1
            pass
        i += 1
    return count
    pass

# def download(floder,pages,page_num):# 传入文件夹名 想爬的页个数
def download():# 传入文件夹名 想爬的页个数
    floder = str(input('存储文件名'))
    pages = int(input('爬取页码数量'))
    page_num = int(input('起始页'))

    os.mkdir(floder)# 创建文件夹floder
    os.chdir(floder)# 对文件的工作路径切换到folder

    # -------------------------多页
    url = str(input('爬取的网址：'))
    ## page_num = int(get_page(url))# 获得当前url最新页码
    i = 1
    j = 1
    while i <= pages:
        print('正获取第{}页'.format(page_num))
        page_url = url + str(page_num) + '.html'
        html = url_open(page_url).decode('utf-8')
        # 获取网页里图片的地址
        img_addrs_list = find_image(html)
        j += save_image(img_addrs_list,j)
        page_num += 1
        i +=1
    pass
    # -------------------------

    # # -------------------------只一网页：
    # page_url = ''
    # html = url_open(page_url).decode('utf-8')
    # print(2)
    # # 获取网页里图片的地址并写入
    # img_addrs_list = find_image(html)
    # save_image(img_addrs_list,1)
    # # -------------------------

    # 打开文件夹
    path = r'C:\Users\Keasar\Desktop\day程序\\' + str(floder)
    os.startfile(path)

if __name__=='__main__':# 若是本文件运行 则执行 若是调用此文件则不执行
    download()