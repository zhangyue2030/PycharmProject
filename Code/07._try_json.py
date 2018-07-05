import requests
import  json

url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_free_stream/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=1530153164387"
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36",
           "referer": "https://m.douban.com/movie/watchonline"}
response = requests.get(url,headers=headers)
response_str = response.content.decode()
response_dict = json.loads(response_str)
print(response_dict)

with open("douban.txt","w",encoding="utf-8") as f:
    f.write(json.dumps(response_dict,ensure_ascii=False,indent=2))
    #ensure_ascii = False 数据不再以ascall码方式保存在本地，中文直接写入

