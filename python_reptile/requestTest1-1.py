#1-1 爬取指定网页的信息
import requests
def getInfo(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "异常！"
    
if __name__=="__main__":
    url = "https://item.jd.com/35080250383.html"
    print(getInfo(url))


