import os
import os.path

fileset=[]
rootdir=["C:\\Users\\Dudu\\Desktop\\20211112下载"]

def nnnn(allfiles,each):
    with open(allfiles[each],"r") as f:
        texts=f.readlines()
        file=open("C:\\Users\\Dudu\\Desktop\\20211112下载\\罪名change.txt","w")
        for ii in texts:
            if ii=="\n":
                continue
            file.write(ii)

'''
    以下是进行筛选的函数，边筛选边处理
'''
def screen(allfiles):
    cnt=0
    for each in range(0,len(allfiles)):
        if allfiles[each][-4:]==".txt":
            if cnt>=1:
                break
            nnnn(allfiles,each)
            cnt=cnt+1
        else:
            pass


def main():
    global fileset
    for i in rootdir:                  #定义函数，查找所有文件
        for parent,dirnames,filenames in os.walk(i):
            for filename in filenames:
                allfiles.append(os.path.join(parent,filename))
    screen(allfiles)                   #screen的意思是筛选

if __name__ == '__main__':
    main()

