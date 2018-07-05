import requests

'''
请求一个网址获取响应 结果中的 <Response [200]> 即 Status Code:200 代表连通
'''
url = "http://www.baidu.com"
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36"}

response = requests.get(url,headers=headers)
print(response.content.decode())

#获取网页的html字符串
#response.encoding = "utf-8"
#print(response.text)

#content获取二进制的, decode转换为str
print(response.content.decode())

