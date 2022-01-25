import os
import os.path

fileset = []
rootdir = [r"C:\Users\Dudu\Desktop\刑事裁定书数据未处理"]  # 以该路径为实验
def main():
    for i in rootdir:  # 定义函数，查找所有文件
        for parent, dirnames, filenames in os.walk(i):
            for filename in filenames:
                fileset.append(os.path.join(parent, filename))
    mydeal(fileset)  # screen的意思是筛选

def mydeal(allfiles):
    for each in range(0, len(allfiles)):
        if os.path.exists(allfiles[each]) and allfiles[each].endswith(".txt"):
            os.remove(allfiles[each])
            os.remove(allfiles[each].replace("txt","doc"))
        else:
            print(allfiles[each])


if __name__ == '__main__':
    main()

