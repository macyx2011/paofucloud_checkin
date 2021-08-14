import requests
import time
import json
from bs4 import BeautifulSoup

def paofu():
    url = "https://paofu.cloud/user/checkin"
    head = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
        'Cookie':'_ga=GA1.2.357488741.1628834761; _gat_gtag_UA_90263540_5=1; _gid=GA1.2.1029803393.1628834761; email=yybeiyong1%40gmail.com; expire_in=1629439783; ip=a7049c85e0935d15b544353d9839ef5f; key=8a74139c3bb5051e58148bade6a9f95cb0fb9efb5890a; uid=166730'
    }
    # data = "success"
    #
    # sign_data = {
    #     'formhash':hash,
    #     'signsubmit':'true'
    # }
    req = requests.post(url,headers = head)
    html = BeautifulSoup(req.content,'lxml')
    print(html)


if __name__ == "__main__":
    paofu()