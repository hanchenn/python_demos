import requests
def get_ip_address(website,ip_str):
    try:            
        r = requests.get(website+ip_str)
        print(website+ip_str)
        print("r.status_code is:",r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[-500:])
    except:
        print("出错了")

if __name__ == '__main__':
    website = "http://www.ip138.com/ips138.asp?ip="
    ip_str = "202.204.80.112"
    get_ip_address(website,ip_str)

