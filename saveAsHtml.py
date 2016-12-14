from urllib.request import urlopen

html = urlopen("http://consumer.huawei.com/minisite/worldwide/privacy-policy/cn/index.htm").read()

with open("enPolicy"+".html", "wb") as f:
    f.write(html)