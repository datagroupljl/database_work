import requests
import re
import html
import time
import urllib.request

url="http://www.usst.edu.cn/s/1/t/517/p/2/i/381/list.htm"
r = requests.get(url)
content = r.text
title = re.findall("<font color=''>(.*?)</font>",content)
print(title)
