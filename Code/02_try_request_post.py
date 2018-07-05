import requests

url = "http://fanyi.baidu.com/basetrans"

data = {"from": "en",
        "to": "zh",
        "query": "Parse" }
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36"}
response = requests.post(url, data=data, headers=headers)
print(response)
response.encoding = "unicode_escape"
print(response.text)
#print(response.content.decode('unicode_escape'))
