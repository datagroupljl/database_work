import requests
import re
import html
import time
import urllib.request

def spider(page=1):
    url="http://www.usst.edu.cn/s/1/t/517/p/2/i/"+str(page)+"/list.htm"
    r = requests.get(url)
    content = r.text
    content_treated1=content.replace('<b>','')
    content_treated=content_treated1.replace('</b>','')
    title = re.findall("<font color=''>(.*?)</font>",content_treated)

    print(title)
    for i in title:
        f.write(i)
        f.write("\n")
        
if __name__=='__main__':
    f=open("jia.txt","w",encoding='utf-8')
    count=0
    for i in range(1,380):
        spider(i)
    f.close()


    
