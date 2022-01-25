from pyhanlp import *


def deal(querySet):
    # wordnature = ["n", "nt", "v", "vn", "a", "ad", "an", "b", "d"]
    # wordSet = set()
    # worddict1 = []
    # worddict2 = []
    # # 决策树，首先现将数据库中数据进行处理，进行词频统计
    # CRFnewSegment = HanLP.newSegment("crf")
    # for item in range(45):  # 选取前50份用作决策树
    #     tempdict = dict()
    #     term_list = CRFnewSegment.seg(
    #         querySet[item].vjson["原文"].replace("\n", ",").replace("\r", ",").replace(" ", ",").replace(u'\u3000',
    #                                                                                                    ',').replace("*",
    #                                                                                                                 ""))
    #     for i in range(len(term_list)):
    #         if str(term_list[i].nature) in wordnature:
    #             tempdict[term_list[i].word] = tempdict.get(term_list[i].word, 0) + 1
    #     tempdict_order = sorted(tempdict.items(), key=lambda x: x[1], reverse=True)[0:2]
    #     # print(tempdict_order)
    #     for i in range(len(tempdict_order)):
    #         wordSet.add(tempdict_order[i][0])
    #     worddict1.append(dict(tempdict_order))
    #
    #     # phraseList = HanLP.extractPhrase(querySet[item].vjson["原文"].replace("\n", ",").replace("\r", ",").replace(" ", ",").replace(u'\u3000',',').replace("*",""), 10)
    #     # print(phraseList)
    #
    #
    # rootdir = [r"D:\PycharmProjects\djangoProject\app01\Otherfile\刑事通知书file"]
    # c = []
    # for i in rootdir:  # 定义函数，查找所有文件
    #     for parent, dirnames, filenames in os.walk(i):
    #         for filename in filenames:
    #             c.append(os.path.join(parent, filename))
    # for j in range(0, len(c)):
    #     tempdict = dict()
    #     f = open(c[j], encoding="gbk")
    #     texts = f.readlines()
    #     connect = ""
    #     for each in texts:
    #         connect = connect + each
    #     connect = connect.replace("\n", ",").replace("\r", ",").replace(" ", ",").replace(u'\u3000', ',').replace("*",
    #                                                                                                               "")
    #     term_list = CRFnewSegment.seg(connect)
    #     for i in range(len(term_list)):
    #         if str(term_list[i].nature) in wordnature:
    #             tempdict[term_list[i].word] = tempdict.get(term_list[i].word, 0) + 1
    #     tempdict_order = sorted(tempdict.items(), key=lambda x: x[1], reverse=True)[0:2]
    #     # print(tempdict_order)
    #     for i in range(len(tempdict_order)):
    #         wordSet.add(tempdict_order[i][0])
    #     worddict2.append(dict(tempdict_order))
    #
    #
    # matrix = []
    # wordSet = list(wordSet)  # 其实现在已经成为一个不含重复元素的列表
    #
    #
    # for i in range(len(worddict1)):
    #     line = [0]  #属于刑事裁定书
    #     for item in wordSet:
    #         if item in worddict1[i]:
    #             line.append(worddict1[i][item])
    #         else:
    #             line.append(0)
    #     matrix.append(line)
    #
    # for i in range(len(worddict2)):
    #     line = [1] # 都属于第1类，也就是别的书
    #     for item in wordSet:
    #         if item in worddict2[i]:
    #             line.append(worddict2[i][item])
    #         else:
    #             line.append(0)
    #     matrix.append(line)
    #
    # # print(matrix)
    # for i in range(len(matrix)):
    #     print(matrix[i])
    # import csv
    # f = open('LawDocument.csv', 'w', encoding='utf-8')
    # csv_writer = csv.writer(f)
    #
    # for i in range(len(matrix)):
    #     csv_writer.writerow(matrix[i])
    #
    #
    #
    #
    #
    #

    # 以下是获取词频的代码
    # CRFnewSegment = HanLP.newSegment("crf")
    # wordnature = ["n", "nt", "v", "vn", "a", "ad", "an", "b", "d"]
    # tempdict = dict()
    # for item in range(len(querySet)):  # 对于每一份文书
    #     term_list = CRFnewSegment.seg(
    #         querySet[item].vjson["原文"].replace("\n", ",").replace("\r", ",").replace(" ", ",").replace(u'\u3000',
    #                                                                                                    "").replace("*",
    #                                                                                                                ""))
    #     for i in range(len(term_list)):  # 对于每一项词汇
    #         if str(term_list[i].nature) in wordnature:
    #             tempdict[str(term_list[i].word)] = tempdict.get(str(term_list[i].word), 0) + 1
    # # print(tempdict)
    # entities_order = sorted(tempdict.items(), key=lambda x: x[1], reverse=True)
    # # # 按字典集合中，每一个元组的第一个元素排列，相当于字典集合中遍历出来的一个元组。
    # print(entities_order)
    # dic = {i[0]: i[1] for i in entities_order}  # 列表转换为字典
    #
    #
    #
    #
    #
    #

    # 以下是按照分类进行降维的处理
    # datamap = {
    #     'title': ['中华人民共和国最高人民法院', '刑事', '裁定书'],
    #     'keyword': ['被告人', '出生', '文化', '暂住地', '复核', '合议庭', '开庭', '没收', '审判', '审判长', '审判员', '宣告', '书记员', '供认'],
    #     'verb': ['窃取', '尖刀', '反抗', '发现', '确认', '维持', '逮捕', '死亡', '裁定', '惩处', '同意', '指认', '逃离', '驳回', '检出'],
    #     'noun': ['财产', '死刑', '证人', '证据', '财物', '事实', '后果', '程序', '证言', '笔录', '法律', '血迹'],
    #     'adj': ['严重', '充分', '确实', '合法', '极其', '适当'],
    #     'other': ['故意杀人罪', '如下', '终身', 'DNA']
    # }
    #
    # cnt = 0
    # tempdict = dict()
    # wholeline = []
    # for i in datamap.keys():
    #     cnt += 1
    #     for j in datamap[i]:
    #         tempdict[j] = cnt
    # CRFnewSegment = HanLP.newSegment("crf")
    # for item in range(100):
    #     line = [0, 0, 0, 0, 0, 0, 0]  # 最前面的作为区分文本的标志
    #     term_list = CRFnewSegment.seg(
    #         querySet[item].vjson["原文"].replace("\n", ",").replace("\r", ",").replace(" ", ",").replace(u'\u3000',"").replace("*",""))
    #
    #     for i in range(len(term_list)):
    #         if str(term_list[i].word) in tempdict:
    #             line[tempdict[str(term_list[i].word)]] += 1
    #     wholeline.append(line)
    #
    # rootdir = [r"D:\PycharmProjects\djangoProject\app01\Otherfile\刑事通知书file"]
    # c = []
    # for i in rootdir:  # 定义函数，查找所有文件
    #     for parent, dirnames, filenames in os.walk(i):
    #         for filename in filenames:
    #             c.append(os.path.join(parent, filename))
    # for j in range(0, len(c)):
    #     f = open(c[j], encoding="gbk")
    #     texts = f.readlines()
    #     connect = ""
    #     for each in texts:
    #         connect = connect + each
    #     connect = connect.replace("\n", ",").replace("\r", ",").replace(" ", ",").replace(u'\u3000', ',').replace("*",
    #                                                                                                               "")
    #     term_list = CRFnewSegment.seg(connect)
    #     line = [1, 0, 0, 0, 0, 0, 0]
    #     for i in range(len(term_list)):
    #         if str(term_list[i].word) in tempdict:
    #             line[tempdict[str(term_list[i].word)]] += 1
    #     wholeline.append(line)
    #
    # rootdir = [r"D:\PycharmProjects\djangoProject\app01\Otherfile\民事裁定书file"]
    # c = []
    # for i in rootdir:  # 定义函数，查找所有文件
    #     for parent, dirnames, filenames in os.walk(i):
    #         for filename in filenames:
    #             c.append(os.path.join(parent, filename))
    # for j in range(0, len(c)):
    #     f = open(c[j], encoding="gbk")
    #     texts = f.readlines()
    #     connect = ""
    #     for each in texts:
    #         connect = connect + each
    #     connect = connect.replace("\n", ",").replace("\r", ",").replace(" ", ",").replace(u'\u3000', ',').replace("*",
    #                                                                                                               "")
    #     term_list = CRFnewSegment.seg(connect)
    #     line = [1, 0, 0, 0, 0, 0, 0]
    #     for i in range(len(term_list)):
    #         if str(term_list[i].word) in tempdict:
    #             line[tempdict[str(term_list[i].word)]] += 1
    #     wholeline.append(line)
    #
    # rootdir = [r"D:\PycharmProjects\djangoProject\app01\Otherfile\刑事判决书file"]
    # c = []
    # for i in rootdir:  # 定义函数，查找所有文件
    #     for parent, dirnames, filenames in os.walk(i):
    #         for filename in filenames:
    #             c.append(os.path.join(parent, filename))
    # for j in range(0, len(c)):
    #     f = open(c[j], encoding="gbk")
    #     texts = f.readlines()
    #     connect = ""
    #     for each in texts:
    #         connect = connect + each
    #     connect = connect.replace("\n", ",").replace("\r", ",").replace(" ", ",").replace(u'\u3000', ',').replace("*",
    #                                                                                                               "")
    #     term_list = CRFnewSegment.seg(connect)
    #     line = [1, 0, 0, 0, 0, 0, 0]
    #     for i in range(len(term_list)):
    #         if str(term_list[i].word) in tempdict:
    #             line[tempdict[str(term_list[i].word)]] += 1
    #     wholeline.append(line)
    #
    #
    #
    # import csv
    # f = open('LawDocument.csv', 'w', encoding='utf-8')
    # csv_writer = csv.writer(f)
    #
    # for i in range(len(wholeline)):
    #     csv_writer.writerow(wholeline[i])
    #
    #
    #
    #
    #

    # 处理crf的文本推荐的问题
    #
    #
    # CRFnewSegment = HanLP.newSegment("crf")
    # with open('a.txt', 'w', encoding='utf-8') as f:
    #     for item in range(100):  # 对于每一份文书
    #         term_list = CRFnewSegment.seg(
    #             querySet[item].vjson["原文"].replace("\n", ",").replace("\r", ",").replace(" ", ",").replace(u'\u3000',
    #                                                                                                        "").replace(
    #                 "*", ""))
    #
    #         newstr = ""
    #         for i in range(len(term_list)):  # 对于每一项词汇
    #             if str(term_list[i].word) not in ["，", "。", "×", "××", ",", "；", "、", "：", "中华人民共和国最高人民法院", "刑事", "裁定书",
    #                                               "刑", "事", "裁", "定", "书", "被告人", "男", "文化", "出生", "判处", "复核", "认定",
    #                                               "意见", "合法", "宣告", "审判长", "最高人民法院", "确实", "于", "书记员"]:
    #                 newstr = newstr + str(term_list[i].word) + " "
    #         f.write(newstr + "\n")
    return
