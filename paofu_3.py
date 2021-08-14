import json
import requests
from bs4 import BeautifulSoup


def PaofuCloud():
    url = "https://paofu.cloud/"
    agent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

    def login(self, user, password) -> object:
        """

                    :rtype: object
                    """
        response = requests.post(url = 'https://paofu.cloud/auth/login',data = {
            # 'User-Agent':self.agent,
            'action': 'login',
            'email':user,
            'password':password,
            'token': 'bzHxy57jJIIU2FY6',
            'number': '753718'
        },headers = self.agent)
        html = BeautifulSoup(response.content,'lxml')
        print(html)

        # response_json = json.loads(response.text)
        # print(response_json)

def sign():
    paofu_session = requests.session()
    header = {
        'origin':'https://paofu.cloud',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
        'referer':'https://paofu.cloud/auth/login',
        'x-requested-with':'XMLHttpRequest'
        /
    }
    posturl = "https://paofu.cloud/auth/login"
    postdata = {
        'email':'2724045612@qq.com',
        'password':'yybeiyong1'
    }
    response = paofu_session.post(posturl,data = postdata,headers = header)
    print(response.text)
if __name__ == "__main__":
    # sign = PaofuCloud()
    # user = "bestyyhb@gmail.com"
    # password = "paofuyun-71"
    # sign.login(user = user,password = password)
    sign()



headers = {
    "origin": "https://paofu.cloud",
    "Referer": "https://paofu.cloud/auth/login",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}


def mafengwoLogin(account, password):
    # 马蜂窝模仿 登录
    print("开始模拟登录马蜂窝")

    postUrl = "https://paofu.cloud/auth/login"
    postData = {
        "email": account,
        "password": password,
    }

    responseRes = requests.Session().post(postUrl, data=postData, headers=headers)

    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    time.sleep(5)
    print(f"text = {responseRes.text}")


if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    mafengwoLogin("2724045612@qq.com","yybeiyong1")

