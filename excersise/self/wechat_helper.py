#coding: utf-8

import requests
import pandas as pd
import numpy  as np

import time
import datetime

today = datetime.datetime.today()

class WechatHelper(object):
    
    def set_appid(self ,appid="wxcceac8434f8108c3"):
        self.appid = appid
    def set_app_secret(self, app_secret="edebdf8ff6b07ebdf5b85bbc05e03380"):
        self.app_serret = app_secret


    def get_wechat_token(self):
        """获取公众号access_token
        """
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(self.appid, self.app_secret)
        answer = requests.get(url).json()
        if "access_token" not in answer:
            print(answer)
            return 
        return answer["access_token"]

    def get_wechat_userId(self, token, next_id):
        """获取关注用户的openId信息
        """
        if next_id:
            url = "https://api.weixin.qq.com/cgi-bin/user/get?access_token={}&next_openid={}".format(token, next_id)
        else:
            url = "https://api.weixin.qq.com/cgi-bin/user/get?access_token={}".format(token)
        answer = requests.get(url).json()
        try:
            next_openid = answer["data"]["next_openid"]
            batch_user = answer["data"]["openid"]
        except:
            print("已经没有了")
            batch_user, next_openid = None, None

        return batch_user, next_openid

    def get_wechat_user_info(self, token, openid_list):
        """获取用户具体信息
        """
        user_info = []
        url = "https://api.weixin.qq.com/cgi-bin/user/info/batchget?access_token={}".format(token)

        # 接口最多支持100个
        l = [i for i in range(0, len(openid_list), 100)]
        for i in range(len(l)):
            if i == len(l)-1:
                sub_list=openid_list[l[i]:]
            else:
                sub_list = openid_list[l[i]: l[i+1]]

            params = {
                "user_list": [{"openid": elem, "lang": "zh_CN"} for elem in sub_list]
            }
            answer = requests.post(url, body=params).json()
            user_info += answer["user_info_list"]
        
        return user_info


    def cook(self):
        # 获取服务token
        token = self.get_wechat_token()

        # 获取用户id,每批10000个
        next_openid = None
        users = []
        batch_user = []
        while batch_user is not None:
            batch_user, next_openid = self.get_wechat_userId(token, next_openid)
            users += batch_user
        
        # 获取用户相关信息
        user_info = self.get_wechat_user_info(token, users)

        return user_info


def get_gap_time(timestamp):
    """获取距离当天的日期差
    """
    src = datetime.datetime.fromtimestamp(timestamp)
    days = (today-src).days
    return days

def run(outpath):
    # 获取信息
    wechat_helper = WechatHelper()
    user_info = wechat_helper.cook()

    # 信息处理
    df = pd.DataFrame(user_info)
    # 关注事件转化成距离现在的事件
    df["gap_time"] = df["subscribe_time"].map(lambda x: get_gap_time(x))
    df.to_excel(outpath)

    df.describe(include=[np.number])



if __name__ == "__main__":
    run("./answer.xlsx")