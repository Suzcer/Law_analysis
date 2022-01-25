from pyhanlp import *

def phrase(filename):
    with open(filename, "r") as f:
        texts = f.readlines()
        connecttext = connect(texts)

        connecttext="".join(connecttext.split())
        #只有这样才能有效将所有的空字符串去除掉
        #可能含有空格、"\t","\n"，所以需要多多考虑处理

        phraseList = HanLP.extractPhrase(connecttext, 100)
        return phraseList

def dependency(filename):
    with open(filename, "r") as f:
        texts = f.readlines()
        connecttext = connect(texts)
        connecttext = "".join(connecttext.split())
        sentence = HanLP.parseDependency(connecttext)
        # 只有这样才能有效将所有的空字符串去除掉
        # 可能含有空格、"\t","\n"，所以需要多多考虑处理
        dependencylist=[]
        for word in sentence.iterator():  # 通过dir()可以查看sentence的方法
            item=word.LEMMA+" --( "+word.DEPREL+" )  --> "+ word.HEAD.LEMMA
            dependencylist.append(item)
        return dependencylist

def textrank(filename):
    with open(filename, "r") as f:
        texts = f.readlines()
        connecttext = connect(texts)
        connecttext = "".join(connecttext.split())
        textranklist = HanLP.extractSummary(connecttext, 12)
        return textranklist



def connect(texts):
    connecttext = ""
    for each in texts:
        connecttext = connecttext + each
    return connecttext
