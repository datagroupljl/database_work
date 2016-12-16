import requests
import re
import html
import time
import urllib.request

def spider(page=1):
    url="http://www.usst.edu.cn/s/1/t/517/p/2/i/"+str(page)+"/list.htm"
    r = requests.get(url)
    content = r.text

    title = re.findall("<font color=''>(.*?)</font>",content)

    print(title)
    for i in title:
        f.write(i)
        f.write("\n")
        
if __name__=='__main__':
    f=open("liu.txt","w",encoding='utf-8')
    count=0
    for i in range(1,381):
        spider(i)
    f.close()


    
