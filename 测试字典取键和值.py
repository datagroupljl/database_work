title_dict={}

f=open("jia.txt","r",encoding='utf-8')
i=1
#将文字的每行标题存入字典
for line in open("jia.txt","r",encoding='utf-8'):
    #添加一个删除字符串末尾/n的操作
    title_dict[i]=line
    i=i+1
   

title_dict.get(1)
