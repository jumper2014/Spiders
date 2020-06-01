'''
数据来源：东方财富网-行情中心
http://quote.eastmoney.com/center
'''

import requests
import re
import json



#用get方法访问服务器并提取页面数据
def get_stocks(page):
    url = "http://42.push2.eastmoney.com/api/qt/clist/get?cb=jQuery11240574199433107409_1590886830210&pn={0}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1590886830256".format(page)
    r = requests.get(url)
    # print(r.text)
    content = r.text.replace("jQuery11240574199433107409_1590886830210", "")
    content = content.replace(";", "")
    content = content[1:-1]
    content_dict = json.loads(content)
    print(content_dict)

    try:
        size = len(content_dict.get('data').get('diff'))
        for i in range(size+1):
            code = content_dict.get('data').get('diff')[i].get('f12')
            name = content_dict.get('data').get('diff')[i].get('f14')
            print(code, name)
            f.write("{0},{1}\n".format(code, name))
    except:
        pass


if __name__ == "__main__":
    f = open("data.csv", 'w')
    for page in range(200+1):
        get_stocks(page)

