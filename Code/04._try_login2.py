import requestsurl = "https://mail.163.com/js6/main.jsp?sid=nCrREhOGJuZvOaYLACGGJxXcALXyiMTa&df=mail163_letter"headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36"}cookies = "xxx"cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookies.split("; ")} #先以"; "【分号加空格切割】再以逗号为切割 区前面的为name后面的为valueprint(cookie_dict)response = requests.get(url,headers=headers,cookies=cookie_dict)with open("163mail2.html","w",encoding="utf-8") as f:    f.write(response.content.decode())