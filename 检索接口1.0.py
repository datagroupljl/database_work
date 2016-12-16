from tkinter import *

root = Tk()
root.title("上海理工大学新闻检索")

#插入一个图片
photo = PhotoImage(file="logo.gif")
Label(root,image=photo).grid(row=0,column=0,rowspan=3,padx=15,pady=10)
#
Label(root,text="欢迎进入本系统",font=("华康少女字体",30),fg="red").grid(row=0,column=1,columnspan=3,padx=10,pady=10)
Label(root,text="请输入您要检索的内容：").grid(row=1,column=1)

Entry(root).grid(row=1,column=2)

a = Button(root,text="检索").grid(row=1,column=3,pady=5)
b = Button(root,text="查看所有内容",width=10).grid(row=2,column=1,sticky=W,columnspan=2,padx=10,pady=5)
c = Button(root,text="退出",width=10).grid(row=2,column=3,sticky=E,columnspan=2,padx=10,pady=5)



mainloop()
