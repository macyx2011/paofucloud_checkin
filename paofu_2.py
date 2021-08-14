import requests

url = "https://paofu.cloud/user/checkin"

payload = "success"
headers = {'Cookie':'_ga=GA1.2.551594167.1628651838; _gid=GA1.2.598711326.1628651838; email=2724045612%40qq.com; expire_in=1629259344; ip=9b06a3e85818b82fcd9377c795c14ab4; key=0cf5fe9c46471f82c0e057ba4548dc0ef0628d29320d0; uid=166425',
#         'Accept':'application/json, text/javascript, */*; q=0.01',
        # 'Origin':'https://paofu.cloud',
        # 'Referer':' https://paofu.cloud/user',
        # 'Accept_Language':'zh-cn',
        # 'Host':'sign.cloud',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
        # 'Content-length':'0',
        # 'Accept_Encoding':'br,gzip,deflate',
        # 'Connection':'keep-alive',
        # 'X-Requestsd-With':'XMLHttpRequest'
           }


response = requests.request("POST", url = url, headers=headers, data = payload)
print(response.text)

# print(f"statusCode = {responseRes.status_code}")
# print(f"text = {responseRes.text}")