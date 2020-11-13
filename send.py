# -*- coding: utf-8 -*-
# @Time : 2020/8/18 19:19
# @Author : XXX
# @Site : 
# @File : 抓包.py
# @Software: PyCharm

import requests
import random
import time


def send_Barrage(msg=''):
    '''
    发送弹幕核心函数
    1，抓包：url,data,header
    2，配置信息
    3. 发送
    :return:
    '''

    #抓包：
    #发送信息,参数 这里需要在网页里面查找，检查元素-> 网络 -> 发送一次弹幕 -> 更新 -> 找到post(含有send关键字) -> 请求
    postdata = {
        "color": "16777215",
        "fontsize": "25",
        "mode": "1",
        "msg": msg,
        "rnd": "1597750331",
        "roomid": "923833",
        "bubble": "0",
        "csrf_token": "0b193e3c0492064ec8880c09342c37fa",
        "csrf": "0b193e3c0492064ec8880c09342c37fa"
    }

    #解决账号未登录，请求头，cookie 记录了账号信息：请求头
    request_headers = {
    "Accept":"application / json, text / javascript, * / *; q = 0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh - CN, zh;q = 0.8, zh - TW;q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2",
    "Connection": "keep-alive",
    "Content-Length":"161",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"xxx-复制你的cookie",#登录信息
    "Host": "api.live.bilibili.com",
    "Origin":"https://live.bilibili.com",
    "Referer": "https://live.bilibili.com/923833",
    "TE":"Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0" # 防止爬虫
    }
    #寻找处理信息头的程序，手动太难了


    url = 'https://api.live.bilibili.com/msg/send'
    #发送请求、获取响应 get post
    response = requests.post(url,data = postdata, headers = request_headers)
    print(response.text)

def randomWord():
    '''
    随机选择发送
    :return:
    '''
    words = [
        '请大佬喝茶',
        '666',
        '恕我直言，在坐的各位都是帅哥，美女'
    ]
    word = random.choice(words)
    print(word)
    return word

def timing(function):
    '''
    实现定时功能，延时
    :return:
    '''
    while 1:
        time.sleep(3)
        pass#程序

def scheduler():
    '''
    是心啊调度器来调度程序运行吗 每隔几执行程序
    APScheduler使用。。。
    调度器使用定时框架， IP池 定时框架 定时任务
    :return: 
    '''
    pass

if __name__ == '__main__':
    word = randomWord()
    send_Barrage(msg=word)

