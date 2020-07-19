#爬虫1-3
#向百度搜索引擎提交搜索关键字并得到搜索结果
import requests
def use_Baidu():
    keyword = "Python"
    try:
        kv = {'wd':keyword}
        r = requests.get("http://www.baidu.com/s",params=kv)#注意：/s 的有无会造成查询结果的差异
        print("r.request.url:",r.request.url) #r.request.url: http://www.baidu.com/s?wd=Python
        print("r.status_code is:",r.status_code)#r.status_code is: 200
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return len(r.text)
    except:
        return "Something Wrong!"

if __name__ == '__main__':
    print(use_Baidu())#395665
    
