import requests
import re
import time
url = 'http://image.baidu.com/search/index?tn=baiduimage&word=皮卡丘'
urls = requests.get(url) # 打开链接
urltext =urls.text # 获取链接全部文本
urlre = re.compile('"objURL":"(.*?)"', re.S) # 书写正则表达式
urllist = urlre.findall(urltext) # 通过正则进行匹配

with open('Sources/baidupic/1.txt', 'w') as txt:     # 将匹配到的链接写入文件
    for i in urllist:
        txt.write(i + "\n")
i = 0

# 循环遍历列表并下载图片
for urlimg in urllist:
    time.sleep(3)   # 程序休眠三秒
    img = requests.get(urlimg, timeout = 5).content # 以二进制形式打开图片链接
    if img:
        with open("'Sources/baidupic/"+str(i) + '.jpg', 'wb') as imgs: # 新建一个jpg文件，以二进制写入
            print('正在下载第%s张图片 %s' % (str(i+1), urlimg) )
            imgs.write(img) # 将图片写入
            i += 1
        if i == 3: # 为了避免无限下载，在这里设定下载图片为3张
            break
    else:
        print('下载失败！')

print('下载完毕！')