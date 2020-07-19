#爬虫1-3
#向360搜索引擎提交搜索关键字并得到搜索结果
import requests
def useSo():
    keyword = "Python"
    try:
        kv = {'q':keyword}
        r = requests.get("http://www.so.com/s",params=kv)
        print("r.status_code is:",r.status_code)#r.status_code is: 200
        print("r.request.url is:",r.request.url)#r.request.url is: https://www.so.com/s?q=Python
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return len(r.text)
    except:
        return "Somethin Wrong"


if __name__ == '__main__':
    print(useSo())#169497

##坑？？？##
#刚开始把keyword 写成了keywoed，一直运行不出来
