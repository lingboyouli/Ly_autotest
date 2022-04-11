# 方法、函数
'''
与类和实例无绑定关系的function都属于函数（function）；
与类和实例有绑定关系的function都属于方法（method）。
'''

# 类、方法
import requests


class headers(object):
    def __init__(self):
        self.oauth_token = "tokenxx"
        self.oauth_uid = "uidxx"
        self.phone = 18911000000

        # 微博登录，获取headers

    def get_wbHeaders(self):
        data = {
            'oauth_token': self.oauth_token,
            'oauth_uid': self.oauth_uid
        }
        wburl = "xxx"
        headers = requests.post(wburl, data)
        return headers

    # 手机号登录，获取headers
    def get_Headers(self):
        data = {
            'phone': self.phone,
        }
        phoneurl = "xxx"
        headers = requests.post(phoneurl, data)
        return headers
