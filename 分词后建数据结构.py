import jieba
import jieba.analyse

#记录文件中有多少行标题 记录在count中
count=0
for line in open("jia.txt","r",encoding='utf-8'):
    count=count+1


#新建字典title_dict,键对应（1-5294）的数字，值是对应的新闻标题
    
title_dict={}

f=open("jia.txt","r",encoding='utf-8')
i=1
#将文字的每行标题存入字典
for line in open("jia.txt","r",encoding='utf-8'):
    #添加一个删除字符串末尾/n的操作
    title_dict[i]=line
    i=i+1
   # print(line)

#将字典title_dict中的值分别进行分词操作
seg_list={}
tags={}
#将分词存入tags字典，键为1-5294，值为对应的分词组成的列表
for j in range(1,count+1):
    #搜索引擎模式
    seg_list[j] =jieba.cut_for_search(title_dict.get(j))
    #精确模式
    #seg_list[j]=jieba.cut(title_dict.get(j),cut_all=True)
    tags[j]=jieba.analyse.extract_tags(title_dict.get(j), topK=40)
    
# print(tags)


#将分词后的结果存入词项字典
word_dict={}
for k in range(1,count+1):
    for z in range(0,int(len(tags.get(k))-1)):   #字典中每个值中，元素的个数
        word_dict.setdefault(tags.get(k)[z])
        if(word_dict.get(tags.get(k)[z])==None):
            word_dict[tags.get(k)[z]]=[]
            word_dict[tags.get(k)[z]].append(k)
        else:
            word_dict[tags.get(k)[z]].append(k)
            
        


#for i in range(1,count):
# title_dict['i']=
# title_dict.setdefault('i')
#for line in open("jia.txt","r",encoding='utf-8'):
    
