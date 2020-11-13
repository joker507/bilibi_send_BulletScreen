## 基于requests包发送

详细请看send.py

1. 抓包：

   发送信息,参数 这里需要在网页里面查找，

   检查元素

   -> 网络 

   -> 发送一次弹幕 

   -> 更新 

   -> 找到post(含有send关键字) 

   -> 请求

   得到信息配置信息

   

   ```python
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
   ```

2. 