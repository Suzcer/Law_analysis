import os
import os.path
from win32com import client as wc

c = []

rootdir = ["C:\\Users\\Dudu\\Desktop\\刑事判决书"]  # 以该路径为实验


def deal(j, c):
    word = wc.Dispatch('Word.Application')
    doc = word.Documents.Open(c[j])
    newname = c[j][:-4]
    print("进行：" + newname)
    doc.SaveAs(newname, 4)
    doc.Close()
    word.Quit()
    os.remove(c[j])

    # with open(c[j], "r") as f:
    #     CRFLexicalAnalyzer=JClass("com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer")
    #     analyzer=CRFLexicalAnalyzer()
    #     for line in f.readlines():
    #         line = line.strip('\n')  #去掉列表中每一个元素的换行符
    #         print(analyzer.analyze(line))


def wordt(c):  # 定义函数，进行筛选
    cnt = 0
    for j in range(0, len(c)):
        # if c[j][-4:] == ".doc":
        if c[j][-4:] == ".doc":
            deal(j, c)
            cnt = cnt + 1
            # if cnt==1:
            #     break
        else:
            pass
    print(cnt)


for i in rootdir:  # 定义函数，查找所有文件
    for parent, dirnames, filenames in os.walk(i):
        for filename in filenames:
            c.append(os.path.join(parent, filename))
wordt(c)
