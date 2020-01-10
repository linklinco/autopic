import ctypes
import urllib.request
import json
import getpass
import time

def get_bing_photo():
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    res = urllib.request.urlopen(url)
    json_txt = res.read()
    txt = json.loads(json_txt)
    url = 'https://www.bing.com/' + txt['images'][0]['url']
    return url
def set_photo(url,num):
    photo = urllib.request.urlopen(url)
    d = photo.read()
    dizhi = "C:\\Users\\"+str(getpass.getuser())+"\\Pictures\\"+str(num)+".jpg"
    print(dizhi)
    f = open(dizhi, "wb")
    f.write(d)
    f.close()
    filepath = dizhi
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
if __name__ == "__main__":
    while True:
        #使用unsplash的随机高清图
        url = 'https://source.unsplash.com/random/4096x2160'
        #使用bing接口
        #url = get_bing_photo()
        #下载的图片保存地址
        f = open("C:\\Users\\"+str(getpass.getuser())+"\\Pictures\\tmp",'a+')
        f.seek(0)
        num = f.read()
        if num == '':
            num = '0'
        f.seek(0)
        f.truncate()
        num = int(num) + 1
        f.write(str(num))
        f.close()
        set_photo(url,num)
        #设置更改壁纸的时间,每隔100秒换一张
        time.sleep(100)