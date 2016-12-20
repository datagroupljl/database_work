from tkinter import *
import jieba
import jieba.analyse


#b1函数为 全部新闻显示页面
#b2函数为 检索页面 检索成功后，跳转另外一个页面
#b3函数为 跳转后的页面


def b1():  #全部新闻显示页面
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
            
        

    #gui部分
            
    root=Tk()
    root.title("上海理工大学新闻检索")
    root.geometry('800x500+200+100')
    sb=Scrollbar(root)
    sb.pack(side=RIGHT,fill=Y)

    #创建一个空列表
    theLB=Listbox(root,width=100,height=80,yscrollcommand=sb.set)

    count=0
    for line in open("jia.txt","r",encoding='utf-8'):
        count=count+1
    
    for a in range(1,count+1):
        theLB.insert(a,title_dict.get(a))

    theLB.pack(padx=20,pady=20,fill=BOTH)
    sb.config(command=theLB.yview)
    mainloop()


def b2():
    def compare():

        count=0
        for line in open("jia.txt","r",encoding='utf-8'):
            count=count+1
        title_dict={}
        f=open("jia.txt","r",encoding='utf-8')
        i=1
        for line in open("jia.txt","r",encoding='utf-8'):
            title_dict[i]=line
            i=i+1
        seg_list={}
        tags={}
        for j in range(1,count+1):
            seg_list[j] =jieba.cut_for_search(title_dict.get(j))
            tags[j]=jieba.analyse.extract_tags(title_dict.get(j), topK=40)
        word_dict={}
        for k in range(1,count+1):
            for z in range(0,int(len(tags.get(k))-1)):   
                word_dict.setdefault(tags.get(k)[z])
                if(word_dict.get(tags.get(k)[z])==None):
                    word_dict[tags.get(k)[z]]=[]
                    word_dict[tags.get(k)[z]].append(k)
                else:
                    word_dict[tags.get(k)[z]].append(k)






        
        user_input=a.get()
        for i in range(1,len(word_dict.keys())):
            if user_input==list(word_dict.keys())[i-1]:
                print("标题匹配成功\n")


                
                root=Tk()
                root.title("上海理工大学新闻检索")
                root.geometry('800x500+200+100')
                sb=Scrollbar(root)
                sb.pack(side=RIGHT,fill=Y)
                theLB=Listbox(root,width=100,height=80,yscrollcommand=sb.set)
                

                
                for k in range(1,len(word_dict[list(word_dict.keys())[i-1]])):
                    theLB.insert(k,title_dict[word_dict[list(word_dict.keys())[i-1]][k]])


                theLB.pack(padx=20,pady=20,fill=BOTH)
                sb.config(command=theLB.yview)
                mainloop()
                #print(title_dict[word_dict[list(word_dict.keys())[i-1]][k]])
                #print('\n')    # word_dict[list(word_dict.keys())[i-1]][k]
            else:
                pass
        
    root=Tk()
    root.title("上海理工大学新闻检索")
    #a是文本框，用于输入要检索的文字，按下回车或者单击Button按钮可以接受用户输入
    a=Entry(root,width=40,validate="focusout",validatecommand=compare)
    a.pack(side=LEFT,padx=40,pady=60)
    #s=a.get()

    #b=Button(root,text="检索",width=20,command=compare())
    #b.pack(side=RIGHT,padx=40,pady=60)

    mainloop()

def b3():
    pass


root=Tk()
root.title("上海理工大学新闻检索")

#插入一个图片
photo = PhotoImage(file="logo.gif")
Label(root,image=photo).grid(row=0,column=0,rowspan=3,padx=15,pady=10)
#标签的属性
Label(root,text="欢迎进入本系统",font=("华康少女字体",30),fg="red").grid(row=0,column=1,columnspan=3,padx=10,pady=10)
Label(root,text="请输入您要检索的内容：").grid(row=1,column=1)
#文本框
Entry(root).grid(row=1,column=2)

###

a = Button(root,text="查看所有内容",width=10,command=b1).grid(row=2,column=1,sticky=W,columnspan=2,padx=10,pady=5)

###a=Button(root,text="查看所有",width=40,command=b1)
###a.pack(padx=220,pady=60)
###
b = Button(root,text="检索",command=b2).grid(row=1,column=3,pady=5)
###b=Button(root,text="检索页面",width=40,command=b2)
###b.pack(padx=220,pady=60)
###
c = Button(root,text="退出",width=10,command=root.quit).grid(row=2,column=3,sticky=E,columnspan=2,padx=10,pady=5)
###c=Button(root,text="退出",width=15,command=root.quit)
###c.pack(padx=220,pady=60)

mainloop()




