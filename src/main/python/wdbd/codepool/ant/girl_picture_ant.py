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
# 照片的地址：https://mtl.gzhuibei.com/images/img/16725/37.jpg


提供的函数：
1. download_img(x, y)       下载单个照片
2. download_single_listpage     下载单个列表页面的所有影集
3. download_multiple_listpage   下载多页的所有影集
4. show_gui     GUI显示程序
5. download_single          下载单个影集

辅助函数：
1. _parse_single_page 解析单一影集的内容
2. _parse_url_to_json 解析影集列表页面，形成含girls信息的json文件
3. _get_html_file   下载url内容为html文件

'''
import urllib.request
from bs4 import BeautifulSoup
import json
import os
from wdbd.codepool.ant.tl import log
import wdbd.codepool.ant.girl_ci as CI
import tkinter as tk
import tkinter.messagebox as tk_msg
import socket


class GirlPage:
    """
    影集对象，一个影集对应N个照片
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
        for i in range(1, int(self.count)+1):
            url = CI.PIC_URL.format(girl_id=self.girl_id, pic_id=i)
            pic_urls.append(url)
        return pic_urls


def download_single(url, down_dir=CI.DOWN_DIR):
    """下载单个影集

    Arguments:
        url {[type]} -- [description]

    Keyword Arguments:
        down_dir {[type]} -- [description] (default: {CI.DOWN_DIR})

    Return: 成功下载照片数量
    """
    # 解析：
    girl = _parse_single_page(url)
    if not girl:
        log.error('影集地址解析失败！ {0}'.format(url))
    down_dir = down_dir + girl.name + '\\'
    log.info('存放目录：{0}'.format(down_dir))

    try:
        if not os.path.exists(down_dir):
            os.makedirs(down_dir)
            log.info('新建文件夹: ' + down_dir)

        success = 0     # 成功下载的照片
        for pic_url in girl.get_pic_urls():
            pic_file_name = down_dir + '\\' + pic_url[pic_url.rfind('/')+1:]
            r = download_img(pic_url, pic_file_name)
            if r != 'failed':
                success += 1

        if os.path.exists(CI.TEMP_HTML):
            os.remove(CI.TEMP_HTML)

        log.info('下载完毕，{0} / {1}'.format(success, girl.count))
        return success
    except Exception as err:
        log.error('下载失败，{0}'.format(str(err)))
        return 0


def _parse_single_page(url):
    """解析单个影集url称GirlPage
    Arguments:
        url {[type]} -- [description]
    """
    html_file = _get_html_file(url)

    if not html_file:
        log.error('下载 影集列表页面 失败！ ' + url)
        return None
    else:
        with open(html_file, mode='r', encoding='utf-8') as f:
            html_str = f.read()
            soup = BeautifulSoup(html_str, 'lxml')
            # print(soup.prettify())

            # 解析内容：
            girl_id = _get_girlid_from_url(url)
            # 名称：
            name = soup.select_one('h1').text.strip()   # [YOUWU尤物馆] VOL.004 木木hanna - 性感蕾丝内衣写真
            # 照片张数
            count_str = soup.select_one('.c_l').select('p')
            count_str = count_str[2].text.strip()
            count_str = count_str[count_str.find('：')+1: count_str.find('张')].strip()     # 52

            girl = GirlPage(url=None, girl_id=girl_id, name=name, count=int(count_str))

            return girl


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
    if os.path.exists(pic_file_path):
        return 'success'

    try:
        request = urllib.request.Request(img_url)
        response = urllib.request.urlopen(request)
        if (response.getcode() == 200):
            with open(pic_file_path, "wb") as f:
                f.write(response.read())    # 将内容写入图片
        # log.debug('download {0} <= {1} '.format(pic_file_path, img_url))
        return 'success'
    except Exception as err:
        log.error('download pic error! ({0})'.format(str(err)))
        return "failed"


def _get_html_file(url, html_file=CI.TEMP_HTML):
    # 下载url内容为html文件
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        if (response.getcode() == 200):
            with open(html_file, "w", encoding='utf-8') as f:
                soup = BeautifulSoup(response.read(), 'lxml')
                f.write(soup.prettify())
        log.debug('解析页面: %s', url)
        return html_file
    except Exception as err:
        log.error('下载HTML时出现问题，{0}'.format(str(err)))
        return None


def _parse_url_to_json(url):
    """
    解析影集列表页面，形成含girls信息的json文件

    Arguments:
        url {[type]} -- [description]
    Returns:
        [str]: 生成的json文件地址
    """

    html_file = _get_html_file(url, html_file=CI.TEMP_HTML)

    if not html_file:
        log.error('下载 影集列表页面 失败！ ' + url)
    else:
        # 解析html文件，写入json文件
        girls = _parse_list_html(html_file)
        # 将对象写入文件， json
        dict_girls = {}
        for g in girls:
            g_dict = {}
            g_dict['id'] = g.girl_id
            g_dict['name'] = g.name
            g_dict['count'] = g.count
            g_dict['pics'] = g.get_pic_urls()
            dict_girls[g.girl_id] = g_dict
        log.debug('解析得到{0}个影集'.format(len(dict_girls)))
        with open(CI.TEMP_JSON, mode='w', encoding='utf-8') as f:
            json.dump(dict_girls, f, ensure_ascii=False, indent=4)
        log.debug('生成json文件 {0}'.format(CI.TEMP_JSON))
        return CI.TEMP_JSON


def _parse_list_html(file):
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
        girl_id = _get_girlid_from_url(page_link)
        # print('girl_id = {0}'.format(girl_id))
        # print('page_link = {0}'.format(page_link))
        # [Beautyleg] No.1771 腿模Shacy - 黑丝美腿+无丝高跟写真[53]
        name_str = li.find('img')['alt']
        # print('name_str = {0}'.format(name_str))
        # name = name_str[name_str.find(' '): name_str.rfind('-')]
        name = name_str[:name_str.rfind('[')]
        # print('name = {0}'.format(name))
        count = name_str[name_str.rfind('[')+1: name_str.rfind(']')]
        # print('count = {0}'.format(count))
        girl = GirlPage(url=page_link, girl_id=girl_id, name=name, count=count)
        girls_on_page.append(girl)
        # print(girl.get_pic_urls())

    # print('共检索到{0}个照片合集'.format(len(girls_on_page)))
    return girls_on_page


def _get_girlid_from_url(url):
    # 从url中找到美女id
    return url[url.rfind('/')+1: url.rfind('.')]


def download_single_listpage(list_page_url, down_dir=CI.DOWN_DIR):
    """下载单个列表页面

    比如：https://www.meitulu.com/t/1319/

    Arguments:
        list_page_url {[str]} -- HTTP url地址

    Keyword Arguments:
        down_dir {str} -- 下载目标目录 (default: CI.DOWN_DIR)

    Returns:
        [int] -- 成功下载的影集数量
    """
    log.info('下载列表 {0}'.format(list_page_url))
    girl_id = _get_girlid_from_url(list_page_url)
    down_dir = down_dir + girl_id + '\\'
    log.info('存放目录：{0}'.format(down_dir))

    try:
        if not os.path.exists(down_dir):
            os.makedirs(down_dir)
            log.info('新建文件夹: ' + down_dir)

        json_file = _parse_url_to_json(list_page_url)
        if not json_file:
            log.error('解析url失败，下载结束！ url = {0}'.format(list_page_url))
            return 0
        else:
            picset_count = _download_picset(json_file, down_dir)
            # 删除临时文件
            if os.path.exists(CI.TEMP_HTML):
                os.remove(CI.TEMP_HTML)
            if os.path.exists(CI.TEMP_JSON):
                os.remove(CI.TEMP_JSON)
            return picset_count
    except Exception as err:
        log.error('下载失败，{0}'.format(str(err)))
        return 0


def _download_picset(json_file, down_dir=r'c:\temp\girls\\'):
    """
    读取json文件，并依次下载影集
    """
    with open(json_file, mode='r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        # print(load_dict)

    count_all = len(load_dict)  # 总下载影集数量
    picset_id = 1
    for girl_id in load_dict.keys():
        try:
            # print(len(load_dict[girl_id]['pics']))
            log.info('【{0}/{1}】下载 {2}  ...'.format(picset_id,
                                                count_all, load_dict[girl_id]['name'].strip()))
            girl_dir = down_dir + load_dict[girl_id]['name'].strip()
            # 创建目录:
            if not os.path.exists(girl_dir):
                os.makedirs(girl_dir)
                log.debug('创建目录: ' + girl_dir)
            # 下载照片
            success_pics = 0
            for pic_url in load_dict[girl_id]['pics']:
                pic_file_name = girl_dir + '\\' + pic_url[pic_url.rfind('/')+1:]
                # print(pic_file_name)
                if CI.DOWN_PIC:
                    r = download_img(pic_url, pic_file_name)
                    if r != 'failed':
                        success_pics = success_pics+1
                else:
                    # 测试用，不真正下载
                    pass
            log.info('共下载{0}个照片, 其中成功{1}'.format(
                len(load_dict[girl_id]['pics']), success_pics))
            picset_id += 1
        except Exception as err:
            log.error('下载失败，{0}'.format(str(err)))
        
    return picset_id-1


def download_multiple_listpage(url, page_from=1, page_end=999, down_dir=CI.DOWN_DIR):
    """下载多页的影集

    Arguments:
        url {[type]} -- [description]

    Keyword Arguments:
        page_from {int} -- [description] (default: {1})
        page_end {int} -- [description] (default: {999})
        down_dir {[type]} -- [description] (default: {CI.DOWN_DIR})

    Returns:
        [type] -- [description]
    """
    url_list = []
    for page in range(page_from, page_end+1):
        if page == 1:
            # https://www.meitulu.com/t/ligui/1.html
            url_list.append(url[:url.rfind('/')])
        else:
            url_list.append(url.format(page))
    # print(url_list)

    count_all = 0
    for idx, url in enumerate(url_list):
        the_dir = down_dir + '_' + str(idx+1) + '\\'
        # print(the_dir)
        count_all += download_single_listpage(url, down_dir=the_dir)

    return count_all


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.title('美女影集爬虫')
        self.master.geometry('800x300+500+200')

    def create_widgets(self):
        # 影集下载:
        self.l_title = tk.Label(self, text='影集下载', width=30, height=2)
        self.l_title.grid(row=1, column=1)

        # Frame of 单个下载
        self.l_s_title = tk.Label(self, text='单页面下载：', width=30, height=2)
        self.l_s_title.grid(row=2, column=1)
        self.l_s_url = tk.Label(self, text='URL:', width=10, height=2)
        self.l_s_url.grid(row=3, column=1)
        url_addr = tk.StringVar(value='https://www.meitulu.com/t/1319/')
        self.e_s_url = tk.Entry(self, width=50, textvariable=url_addr)
        self.e_s_url.grid(row=3, column=2)
        self.btn_s_down = tk.Button(self, text='下载', width=10, height=1, command=self.btn_s_down_click)
        self.btn_s_down.grid(row=3, column=3)
        # Frame of 多个下载
        self.l_m_title = tk.Label(self, text='多页面下载：', width=30, height=2)
        self.l_m_title.grid(row=5, column=1)
        self.l_m_url = tk.Label(self, text='URL模板:', width=10, height=2)
        self.l_m_url.grid(row=6, column=1)
        url_addr = tk.StringVar(value='https://www.meitulu.com/t/ligui/{0}.html')
        self.e_m_url = tk.Entry(self, width=50, textvariable=url_addr)
        self.e_m_url.grid(row=6, column=2)
        self.l_m_sub = tk.Label(self, text='起始页码:', width=10, height=2)
        self.l_m_sub.grid(row=7, column=1)
        self.e_m_start = tk.Entry(self, width=3, textvariable=tk.StringVar(value='1'))
        self.e_m_start.grid(row=7, column=2)
        self.e_m_end = tk.Entry(self, width=3, textvariable=tk.StringVar(value='4'))
        self.e_m_end.grid(row=7, column=3)
        self.btn_m_down = tk.Button(self, text='下载', width=10, height=1, command=self.btn_m_down_click)
        self.btn_m_down.grid(row=8, column=2)

    def btn_s_down_click(self):
        """
        单个页面下载
        """
        url_str = self.e_s_url.get()
        if url_str == '':
            tk_msg.showwarning(title='Hi', message='请输入URL地址')
            self.e_s_url.focus_set()
        else:
            r = download_single_listpage(url_str)
            tk_msg.showwarning(title='下载完成', message='{0}个影集下载完成({1})'.format(r, CI.DOWN_DIR))

    def btn_m_down_click(self):
        """
        单个页面下载
        """
        url_str = self.e_m_url.get()
        start = int(self.e_m_start.get())
        end = int(self.e_m_end.get())
        if url_str == '':
            tk_msg.showwarning(title='Hi', message='请输入URL地址')
            self.e_m_url.focus_set()
        else:
            r = download_multiple_listpage(url_str, start, page_end=end)
            tk_msg.showwarning(title='下载完成', message='{0}个影集下载完成({1})'.format(r, CI.DOWN_DIR))


def show():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    socket.setdefaulttimeout(10)

    # url = 'https://www.meitulu.com/item/15267.html'
    # # g = _parse_single_page(url)
    # # print(g)
    # s = download_single(url)
    # print(s)

    # url = 'https://www.meitulu.com/t/beautyleg/3.html'
    # download_single_listpage(url)

    # url = 'https://www.meitulu.com/t/xiuren/{0}.html'
    # download_multiple_listpage(url, page_from=1, page_end=28, down_dir=CI.DOWN_DIR)

    url = 'https://www.meitulu.com/t/ningmengc-lemon/{0}.html'
    download_multiple_listpage(url, page_from=1, page_end=2, down_dir=CI.DOWN_DIR+'妲己_Toxic\\')