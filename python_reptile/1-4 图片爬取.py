import requests
import os
def getImg():
    #图片的url路径
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec="\
          "1542993991904&di=739fd48f89fe5dff35fe2e72e58051dc&imgtype=0&src=http"\
          "%3A%2F%2Fimglf1.ph.126.net%2FEL41V1hr6QzSsKaaccug4Q%3D%3D%2F6630935824305511510.jpg"
    #设置root为图片存储的根目录
    root = "D://pics//"
    #定义path为图片的本地存储路径
    path = root + "123.jpg"
    try:
        if not os.path.exists(root):#如果根目录不存在，先创建
            os.mkdir(root)
        if not os.path.exists(path):#如果目标文件不存在，再从网上爬取
            r = requests.get(url)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)###这里r.content获取的是response数据的二进制形式（与r.text相对）
                f.close()
                print("文件保存成功")
        else:
            print("文件已经存在")
    except:
        print("爬取失败")
    
        
if __name__ == "__main__":
    getImg()

