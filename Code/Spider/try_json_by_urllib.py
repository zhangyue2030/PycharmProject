'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
1. 打开F12
2. 尝试输入单词girl，发现每敲一个字母后都有请求
3. 请求地址是 http://fanyi.baidu.com/sug
4. 利用NetWork-All-Hearders，查看，发现FormData的值是 kw:girl
5. 检查返回内容格式，发现返回的是json格式内容==>需要用到json包
'''

from urllib import request, parse
# 负责处理json格式的模块
import json
import chardet

'''
大致流程是：
1. 利用data构造内容，然后urlopen打开
2. 返回一个json格式的结果
3. 结果就应该是girl的释义
'''

baseurl = 'http://fanyi.baidu.com/sug'


# 存放用来模拟form的数据一定是dict格式
data = {
    # girl是翻译输入的英文内容，应该是由用户输入，此处使用硬编码
    'kw': 'refactor'
}

# 需要使用parse模块对data进行编码
data = parse.urlencode(data).encode("utf-8")

#print(type(data))
#  我们需要构造一个请求头，请求头部应该至少包含传入的数据的长度
# request要求传入的请求头是一个dict格式

headers = {
    # 因为使用post，至少应该包含content-length 字段
    'Content-Length':len(data)
}


# 可以直接尝试发出请求
# rsp = request.urlopen(baseurl, data=data)

# 或通过request发送带headers的请求
# 这是构造一个Request的实例
req = request.Request(url=baseurl, data=data, headers=headers)
# req.add_header("User-Agent","````") #注：可以通过add_header()添加头

# 因为已经构造了一个Request的请求实例，则所有的请求信息都可以封装在Request实例中
# urlopen可以打开URL 而URL，可以是字符串或Request对象
rsp = request.urlopen(req)

json_data = rsp.read()

# 利用 chardet自动检测
cs = chardet.detect(json_data)
#print(type(cs))
#print(cs)

json_data = json_data.decode(cs.get("encoding", "utf-8"))

#print( type(json_data))
#print(json_data)


# 把json字符串转化成字典
json_data = json.loads(json_data)
#print(type(json_data))
#print(json_data)


for item in json_data['data']:
    print(item['k'], "--", item['v'])
