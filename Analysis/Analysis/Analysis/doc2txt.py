# import os
# import docx
# spam=os.listdir('C:\\Users\\Dudu\\Desktop\\裁判文书网数据')#获取文件夹下的word文档列表
# print(spam)
# for i in spam:
#     doc=docx.Document('C:\\Users\\Dudu\\Desktop\\裁判文书网数据\\{}'.format(i))
#     doc.add_paragraph('world')
#     doc.save('C:\\Users\\Dudu\\Desktop\\裁判文书网数据1\\{}'.format(i))
#     #注意在已有的word文档中写入之后要保存
import os
import os.path
from win32com import client as wc

c=[]

rootdir=["C:\\Users\\Dudu\\Desktop\\裁判文书网282数据"]                #以该路径为实验
def txt(j,c):
     word = wc.Dispatch('Word.Application')
     doc = word.Documents.Open(c[j])
     newname=c[j][:-4]+"(translate txt)"
     doc.SaveAs(newname,4)
     doc.Close()
     word.Quit()
     os.remove(c[j])
     print("完成")

def wordt(c):                    #定义函数，进行筛选
    for j in range(0,len(c)):
        if c[j][-4:] == ".doc":  #寻找docx文件
            txt(j,c) #
        else:
            pass

for i in rootdir:                  #定义函数，查找所有文件
    for parent,dirnames,filenames in os.walk(i):
        for filename in filenames:
            c.append(os.path.join(parent,filename))

wordt(c)
