#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   girl_picture_ant.py
@Time    :   2020/01/21 08:28:29
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   美女图片爬虫程序

用最简单的urlib库，实现从网络上爬取美女图片，存到本地硬盘上

给定的是照片列表的url

# 影集的名称：name
# 影集的序号：girl_id
# 
# 照片的地址：https://mtl.gzhuibei.com/images/img/16725/37.jpg


提供的函数：
1. download_list(url)       根据列表url，分析所有影集信息，并生成 girls.json 文件
2. download_pic(json_files) 下载照片到制定目录


'''
import urllib.request
from bs4 import BeautifulSoup
import json
import os


# 全局参数配置
PIC_URL = 'https://mtl.gzhuibei.com/images/img/{girl_id}/{pic_id}.jpg'


class GirlPage:
    """
    美女影集对象
    """

    def __init__(self, url, girl_id, name, count):
        self.url = url
        self.girl_id = girl_id
        self.name = name
        self.count = count

    def __str__(self):
        return '{0} [{1}] {2}'.format(self.name, self.count, self.url)

    def get_pic_urls(self):
        """
        返回所有照片的地址
        """
        pic_urls = []
        for i in range(1, int(self.count)):
            url = PIC_URL.format(girl_id=self.girl_id, pic_id=i)
            pic_urls.append(url)
        return pic_urls


def down_pic(url):
    # https://mtl.gzhuibei.com/images/img/18215/1.jpg
    return None


def download_img(img_url, pic_file_path):
    """
    下载照片到本地

    Arguments:
        img_url {str} -- 照片的url地址
        pic_file_path {str} -- 本地存放地址

    Returns:
        [str] -- success | failed 下载成功与否
    """

    # header = {"Authorization": "Bearer " + api_token} # 设置http header
    # request = urllib.request.Request(img_url, headers=header)
    request = urllib.request.Request(img_url)
    try:
        response = urllib.request.urlopen(request)
        # img_name = "img.png"
        # filename = "C:\\temp\\" + img_name
        if (response.getcode() == 200):
            with open(pic_file_path, "wb") as f:
                f.write(response.read())    # 将内容写入图片
        # print('下载 ' + pic_file_path)
        return 'success'
    except Exception as err:
        print('下载照片出错，' + str(err))
        return "failed"


def download_list(url):
    """
    解析影集列表页面，形成含girls信息的json文件

    Arguments:
        url {[type]} -- [description]
    """

    # 下载url内容为html文件
    html_file = "C:\\temp\\girls.html"   # TODO 要改成规定的文件名
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)    
        if (response.getcode() == 200):
            with open(html_file, "w", encoding='utf-8') as f:
                soup = BeautifulSoup(response.read(), 'lxml')
                f.write(soup.prettify())
            print('生成html文件 ... ')
    except Exception as err:
        print('解析影集时出现问题，{0}'.format(str(err)))
        return None

    # 解析html文件，写入json文件
    girls = parse_list_html(html_file)
    # TODO 将对象写入文件， json
    dict_girls = {}
    for g in girls:
        g_dict = {}
        g_dict['id'] = g.girl_id
        g_dict['name'] = g.name
        g_dict['pics'] = g.get_pic_urls()
        dict_girls[g.girl_id] = g_dict
    with open(r'c:\temp\girls.json', mode='w', encoding='utf-8') as f:
        json.dump(dict_girls, f, ensure_ascii=False, indent=4)
    print('生成json文件 ... ')





# load_dict = json.load(load_f)


def parse_list_html(file):
    """解析列表html文件

    Arguments:
        file {[type]} -- [description]
    """
    with open(file, mode='r', encoding='utf-8') as f:
        html_str = f.read()

    soup = BeautifulSoup(html_str, 'lxml')
    # print(soup.prettify())

    # 找到列表清单
    lis = soup.select_one('.img').select('li')   # .find_all('li')
    girls_on_page = []
    for idx, li in enumerate(lis):
        # print('--{0}----------------'.format(idx))
        page_link = li.find('a')['href']
        girl_id = page_link[page_link.rfind('/')+1: page_link.rfind('.')]
        # print('girl_id = {0}'.format(girl_id))
        # print('page_link = {0}'.format(page_link))
        # [Beautyleg] No.1771 腿模Shacy - 黑丝美腿+无丝高跟写真[53]
        name_str = li.find('img')['alt']
        # print('name_str = {0}'.format(name_str))
        name = name_str[name_str.find(' '): name_str.rfind('-')]
        # print('name = {0}'.format(name))
        count = name_str[name_str.rfind('[')+1: name_str.rfind(']')]
        # print('count = {0}'.format(count))
        girl = GirlPage(url=page_link, girl_id=girl_id, name=name, count=count)
        girls_on_page.append(girl)
        # print(girl.get_pic_urls())

    print('共检索到{0}个照片合集'.format(len(girls_on_page)))
    
    return girls_on_page


def download_pic(json_file, down_dir=r'c:\temp\girls\\'):
    """
    读取json文件，并依次下载影集
    """
    # json.dump(dict_girls, f, ensure_ascii=False, indent=4)
    with open(json_file, mode='r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        # print(load_dict)

    for girl_id in load_dict.keys():
        # print(len(load_dict[girl_id]['pics']))
        girl_dir = down_dir + load_dict[girl_id]['name'].strip()
        # 创建目录:
        if not os.path.exists(girl_dir):
            os.makedirs(girl_dir)
            print('创建目录: ' + girl_dir)
        # 下载照片
        success_pics = 0
        for pic_url in load_dict[girl_id]['pics']:
            pic_file_name = girl_dir + '\\' + pic_url[pic_url.rfind('/')+1:]
            # print(pic_file_name)
            r = download_img(pic_url, pic_file_name)
            if r != 'failed':
                success_pics = success_pics+1
        print('共下载{0}个照片, 其中成功{1}'.format(len(load_dict[girl_id]['pics']), success_pics))    


if __name__ == "__main__":

    # url = 'https://www.meitulu.com/t/beautyleg/'  # https://www.meitulu.com/t/beautyleg/2.html
    # url = 'https://www.meitulu.com/t/luvian/'

    # url = 'https://www.meitulu.com/t/1319/'
    # url = 'https://www.meitulu.com/t/yiyang-elly/'
    url = 'https://www.meitulu.com/t/beautyleg/23.html'
    download_list(url)
    
    # json_file = r'c:\temp\girls.json'
    # download_pic(json_file, r'c:\temp\girls\\beautyleg_nana\\')

    # # --------------
    # json_file = r'c:\temp\girls.json'
    # for i in range(2, 14):
    #     url = 'https://www.meitulu.com/t/ligui/{0}.html'.format(i)
    #     # url = 'https://www.meitulu.com/t/beautyleg/{0}.html'.format(i)
    #     download_list(url)
    #     download_pic(json_file, r'c:\temp\girls\\丽柜_{0}\\'.format(i))

   