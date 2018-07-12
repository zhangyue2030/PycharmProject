import json
from Code.parse import parse_url

class DoubanSpider:
    def __init__(self):
        #请求地址，将start的值换成{0}，在后面直接.format()即可
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_free_stream/items?os=ios&for_mobile=1&start={0}&count=18&loc_id=108288&_=1530153164387"

    '''
        提取数据
    '''
    def get_content_list(self,html_str):
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        #取total为了计算一共几页
        total = dict_data["total"]
        return content_list,total

    '''
    保存数据
    '''
    def save_content_list(self,content_list):
        with open("../../ResultFiles/douban.json","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self): #实现主要逻辑
        num = 0
        total = 1
        print(num ,total)
        while num<total+18:
            #1.构造当前url
            url = self.temp_url.format(num)
            print(url)
            #2.发送请求，获取响应
            html_str = parse_url(url)
            #3.提取数据
            content_list,total = self.get_content_list(html_str)
            #4.保存
            self.save_content_list(content_list)
            #5.计算下一页的url地址所需num，循环到结束
            num += 18

if __name__=="__main__":
    douban = DoubanSpider()
    douban.run()