import urllib.request
import re
data="""onclick="searchlog(1,16891017063,7,2,'','flagsClk=1077936776')">
							<img width="220" height="220" class="err-product" data-img="1" src="//img13.360buyimg.com/n7/jfs/t8638/135/1980052220/499399/b4af97ab/59c236d5N79b002ee.jpg" />
</a>						<div data-catid="6254" data-venid="100724" data-presale="0"></div>
					</div>
					<div class="p-price">"""
pat1="src=\"//(img.*?jpg)"
url="https://search.jd.com/Search?keyword=%E7%8E%BB%E5%B0%BF%E9%85%B8%E9%B8%AD&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%8E%BB%E5%B0%BF%E9%85%B8%E9%B8%AD&stock=1&page=1"
data1=urllib.request.urlopen(url).read()
print(data1)
data1=data1.decode('utf-8')
text=re.compile(pat1).findall(data1,re.S)
print(text)