import jieba
seg_list = jieba.cut("上海市动力工程多相流动与传热重点实验室筹建验收会在我校格致堂108会议室举行",cut_all=True)
list1=list(seg_list)
print(list1)

