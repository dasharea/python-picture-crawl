import urllib.request
import re
import urllib.error
def crawl(url,page):
    data=urllib.request.urlopen(url).read()
    pat1 = 'img width="220" height="220" class="err-product" data-img="1" src=\"//(img.*?jpg)'
    data=data.decode("utf-8")
    result=re.compile(pat1).findall(data,re.S)
    x=len(result)
    for i in range (0,x-1):
        imagename="F:/pythoncrawl/image/"+str(page)+str(i)+".jpg"
        imageurl="http://"+result[i]
        try:
            urllib.request.urlretrieve(imageurl,imagename)
        except urllib.error.URLError as e:
            i+=0
for page in range (1,11,2):
    url="https://search.jd.com/Search?keyword=%E7%8E%BB%E5%B0%BF%E9%85%B8%E9%B8%AD&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%8E%BB%E5%B0%BF%E9%85%B8%E9%B8%AD&stock=1&page="+str(page)
    crawl(url,page)
