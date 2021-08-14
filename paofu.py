import requests
import json
import time
from bs4 import BeautifulSoup
from requests import Response


class Paofu():
    def __init__(self):
        self.agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"
        self.log_url = "https://paofu.cloud/auth/login"
        self.user_url = "https://paofu.cloud/user"
        self.check_url = "https://paofu.cloud/user/checkin"

    def login(self,email,password):
        if time.strftime('%H',time.localtime()) == "14":
            # try:
            session = requests.session()
            # log_cookie = requests.get(self.log_url, headers = {'user-agent':self.agent})
            # print(log_cookie.text)
            headers = {
                'user-agent':self.agent,
                # 'cookie':log_cookie,
                'accept':'application/json, text/javascript, */*; q=0.01',
                # 'accept-encoding':'gzip,deflate,br',
                # 'cache-contro':'max-age=0',
                'referer':self.log_url
            }
            data = {
                'email':email,
                'passwd':password
            }
            response_login = session.post(url = self.log_url,data = data,headers = headers)
            cookie_dir = requests.utils.dict_from_cookiejar(response_login.cookies)
            cookie_str = []
            for key,value in cookie_dir.items():
                addd = str(key)+'='+str(value)
                cookie_str.append(addd)
            print(cookie_str)
            cookie = ";".join(cookie_str)
            response_user = session.get(url = self.user_url,headers = {
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent':self.agent
            })
            return cookie

    def cookie(self,email,cookie):
        cookie = requests.utils.dict_from_cookiejar(self.login(email = email,cookie = cookie))

            
            # user_page = BeautifulSoup(response_user.content,'lxml')
            # print(user_page)
            # return log_cookie,req,user_page,user_cookie

    def checkin(self, cookie: object) -> object:
        """
        :return:
        <html>
        <body>
        success:<p>{"msg":"\u4f60\u83b7\u5f97\u4e86 603 MB\u6d41\u91cf","ret":1}</p>
        false:<p>{"ret":0,"msg":"\u60a8\u4f3c\u4e4e\u5df2\u7ecf\u7b7e\u5230\u8fc7\u4e86..."}</p>
        </body>
        </html>
        :type cookie: object
        """
        # assert isinstance(object, cookie)
        checkin: Response = requests.post(self.check_url,headers = {
            'user-agent':self.agent,
            'cookie':cookie
        })
        return checkin.text

    def split(self,checkin:str) -> type:
        # print(self.checkin(paofu.login(email = 'bestyyhb@gmail.com',password = 'paofuyun-71')))
        megabyte = checkin.split(' ')[1]
        """
        :rtype string
        """
        # checkin_status = 'True' if megabyte == True else checkin_status = 'False'
        print(megabyte)
        # if megabyte == True:
        #     checkin_status = True
        # else:
        #     checkin_status = False
        # print(checkin_status)

if __name__ == "__main__":
    paofu = Paofu()
    email = "xx@xx.com"
    password = "xxx"
    print(paofu.login(email,password))
    paofu.split(paofu.checkin(paofu.login(email = email,password = password)))