from pyhanlp import *
import json

chargeset = []
courtset = []
adjset = []
verbset = []
discardverbset = []
model = {}

defendent = ""
defendentgender = ""
defendentbirth = ""
defendentbirthplace = ""
defendentnation = ""
victims = set()
courts = set()
causesofAction = set()
adjs = set()
verbs = set()
term_list = []
vtime = ""
connecttext = ""

timetran = {'〇': "0", '一': "1", '二': "2", '三': "3", '四': "4", '五': "5", '六': "6", '七': "7", '八': "8", '九': "9"}
courtssuffix = ["人民法院", "检察院"]  # 定义法院和检察院后缀
CoreSynonymDictionary = JClass("com.hankcs.hanlp.dictionary.CoreSynonymDictionary")

'''

'''


def timetrans(str):
    global timetran
    ret = ""
    for i in range(len(str)):
        if str[i] in timetran.keys():
            ret = ret + timetran[str[i]]
            if str[i] == '十' and (str[i + 1] == '月' or str[i + 1] == '日'):
                ret = ret + "0"
    return ret


'''
    以下方法是预加载罪名文件的方法
'''


def preload():
    global chargeset
    f = open(r"D:\Documents\卷\Grade2_firstTerm\数据科学基础\大作业\语料库\罪名.txt", encoding="utf-8")
    texts = f.readlines()
    for each in texts:
        chargeset.append(each.strip("\n").strip(" "))

    f = open(r"D:\Documents\卷\Grade2_firstTerm\数据科学基础\大作业\语料库\中国中高级法院.txt", encoding="ansi")
    texts = f.readlines()
    for each in texts:
        courtset.append(each.strip("\n").strip(" "))

    f = open(r'D:\Documents\卷\Grade2_firstTerm\数据科学基础\大作业\语料库\形容词.txt', encoding="utf-8")
    texts = f.readlines()
    for each in texts:
        adjset.append(each.strip("\n").strip(" "))

    f = open(r'D:\Documents\卷\Grade2_firstTerm\数据科学基础\大作业\语料库\描述动词.txt', encoding="utf-8")
    texts = f.readlines()
    for each in texts:
        verbset.append(each.strip("\n").strip(" "))

    f = open(r"D:\Documents\卷\Grade2_firstTerm\数据科学基础\大作业\语料库\去除动词.txt", encoding="utf-8")
    texts = f.readlines()
    for each in texts:
        discardverbset.append(each.strip("\n").strip(" "))


'''
    处理函数的主逻辑
    1. 读取txt文件
    2. 用crf进行分词
    3. 进行各种所需内容的筛选
'''


def deal(filename):
    global defendentbirth, defendent, defendentgender, defendentnation, courts, term_list, connecttext
    reset_info()
    preload()
    with open(filename, "r") as f:
        CRFnewSegment = HanLP.newSegment("crf")
        texts = f.readlines()

        connecttext = connect(texts)
        term_list = CRFnewSegment.seg(connecttext)

        find_defendent()  # 节约查找，在其内调用搜索性别，出生年月，出生地
        find_step()
        find_time()

    # printout()
    save_as_json(filename)


'''
    优化代码结构，减少无意义重复
'''


def find_step():
    global term_list
    for i in range(len(term_list)):
        find_court(i)
        find_adj(i)
        find_verb(i)
        find_cause_of_Action(i)
        find_victim(i)


'''
    以下是找到被告人名字的方法
    直接简单粗暴地找被告人后面的一个名词
'''


def find_defendent():
    global defendent, term_list
    for i in range(len(term_list)):
        if (str(term_list[i].word) == "被告人"):
            for j in range(i + 1, i + 10):
                if str(term_list[j].word) == "，":
                    break
                defendent = defendent + str(term_list[j].word)
            find_defendent_gender(i)
            find_defendent_nation(i)
            return


'''
    以下是找到被告人性别的方法
    直接将最早看到的"男"、"女"词条当作被告人的性别
'''


def find_defendent_gender(i):
    global defendentgender, term_list
    for j in range(i + 1, len(term_list)):
        if str(term_list[j].word) == "男" or str(term_list[j].word) == "女":
            defendentgender = str(term_list[j].word)
            find_defendent_birth(j)
            return


'''
    以下是找到被告人民族的方法
    直接将看到的第一个nz并且以"族"结尾的词当作被告人的民族
'''


def find_defendent_nation(sub):
    global defendentnation, term_list
    for i in range(sub, len(term_list)):
        if str(term_list[i].nature) == "nz" and str(term_list[i].word).endswith("族"):
            defendentnation = str(term_list[i].word)
            return


'''
    以下是找到被告人出生年月的方法
    将"出生"前的所有词性是t的分词全部连接作为出生年月
'''


def find_defendent_birth(sub):
    global defendentbirth, term_list
    for i in range(sub, len(term_list)):
        if str(term_list[i].word) == "出生":
            find_defendent_birthplace(i)
            for j in range(i - 1, -1, -1):
                if str(term_list[j].nature) == "t":
                    defendentbirth = str(term_list[j].word) + defendentbirth
                else:
                    return


'''
    以下是找到被告人出生地的方法
    直接将看到的第一个地点连缀起来当作被告人的出生地
'''


def find_defendent_birthplace(sub):
    global defendentbirthplace, term_list
    for j in range(sub + 2, len(term_list)):
        if str(term_list[j].nature) == "ns":
            defendentbirthplace = defendentbirthplace + str(term_list[j].word)
        else:
            return


'''
    以下是查找被害人的方法(如果存在的话)
'''


def find_victim(i):
    global victims, term_list
    if str(term_list[i].word) == "被害人":
        for j in range(i - 2, i + 3):
            if str(term_list[j].nature) == "nr":
                victims.add(str(term_list[j].word))


'''
    以下是找到各种法院和检察院的方法
    直接判断后缀,发现部分法院以结构团体名出现，因此也进行特殊判断
    应该找到全国所有法院的名称添加到语料库中更为实际，可以避免不必要的麻烦
'''


def find_court(i):
    global courts, term_list
    if str(term_list[i].word).endswith("法院") and str(term_list[i].word) in courtset:
        courts.add(str(term_list[i].word))

    # 下面是可选项,之后进行标注
    if str(term_list[i].word) in courtssuffix:
        court = str(term_list[i].word)
        for j in range(i - 1, -1, -1):
            if str(term_list[j].word) == "高级" or \
                    str(term_list[j].word) == "中级" or \
                    str(term_list[j].nature) == "ns":
                court = str(term_list[j].word) + court
            else:
                courts.add(court)
                break
    courts.discard("人民法院")
    courts.discard("高级人民法院")


'''
    以下是找到案由的方法
    实现的话是通过读取字典，匹配是否有罪名存在于字典中
    其实就是判处后面的话就可以了吧
'''


def find_cause_of_Action(i):
    global causesofAction, term_list
    if str(term_list[i].word) in chargeset:
        causesofAction.add(str(term_list[i].word).rstrip("罪"))

        # 案由就是可能犯下的罪
        # 因为词典的问题，这里判断可能会不足，因此需要进一步扩充罪名词典
        # 本地指路：D:\ChromeCoreDownloads\Anaconda3\envs\Lib\site-packages\pyhanlp\static\data\dictionary\custom\CustomDictionary.txt
    return causesofAction


'''
    简单来一版提取形容词,直接将所有形容词进行归入
'''


def find_adj(i):
    global adjs, term_list
    if str(term_list[i].nature) == "a" and len(str(term_list[i].word)) >= 2:
        for each in adjset:
            if CoreSynonymDictionary.similarity(str(term_list[i].word), each) > 0.99:
                # adj = ""
                # for j in range(i, -1, -1):
                #     if str(term_list[j].nature) == "w":  # 遇到符号就停止
                #         adjs.add(adj)
                #         break
                #     if str(term_list[j].nature) == "nr":
                #         break
                #     adj = str(term_list[j].word) + adj
                adjs.add(str(term_list[i].word))
                break


'''
    简单来一版提取动词，直接将所有动词进行归入
'''


def find_verb(i):
    global verbs, term_list
    if str(term_list[i].nature) == "v" and len(str(term_list[i].word)) >= 2:
        for each in verbset:
            if CoreSynonymDictionary.similarity(str(term_list[i].word), each) > 0.999:
                for one in discardverbset:
                    if CoreSynonymDictionary.similarity(str(term_list[i].word), one) > 0.9999:
                        return
                verbs.add(term_list[i].word)
                return


def find_time():
    global vtime, term_list
    for i in range(len(term_list) - 1, -1, -1):
        if str(term_list[i].nature) == "t":
            vtime = timetrans(str(term_list[i - 2].word))
            if len(timetrans(str(term_list[i - 1].word))) == 1:
                vtime = vtime + "0" + timetrans(str(term_list[i - 1].word))
            else:
                vtime = vtime + timetrans(str(term_list[i - 1].word))

            if len(timetrans(str(term_list[i].word))) == 1:
                vtime = vtime + "0" + timetrans(str(term_list[i].word))
            else:
                vtime = vtime + timetrans(str(term_list[i].word))
            return


'''
    将texts进行连接，防止出现跨行的现象
'''


def connect(texts):
    connecttext = ""
    for each in texts:
        connecttext = connecttext + each
    return connecttext


'''
    测试打印输出
'''


def printout():
    print("犯罪嫌疑人：" + defendent)
    print("出生年月：" + defendentbirth)
    print("性别：" + defendentgender)
    print("出生地：" + defendentbirthplace)
    print("民族：" + defendentnation)

    print("法院：", end="")
    for each in courts:
        print(each + "、 ", end="")
    print()

    print("案由：", end="")
    for each in causesofAction:
        print(each + "、 ", end="")
    print()

    print("被害人：", end="")
    for each in victims:
        print(each + "、 ", end="")
    print()

    print("形容词：", end="")
    for each in adjs:
        print(each + "、 ", end="")
    print()

    print("动词：", end="")
    for each in verbs:
        print(each + "、 ", end="")
    print()

    print("审判时间：", end="")
    print(vtime)
    print()

    print("\n")


def reset_info():
    global defendent, defendentgender, defendentbirth, \
        defendentbirthplace, defendentnation, victims, courts, \
        causesofAction, adjs, verbs, model
    defendent = ""
    defendentgender = ""
    defendentbirth = ""
    defendentbirthplace = ""
    defendentnation = ""
    model = {}
    victims = set()
    courts = set()
    causesofAction = set()
    adjs = set()
    verbs = set()


'''
    以json格式保存文件
'''


def save_as_json(filename):
    filename = filename.replace("upload_file", "json_file")[:-3] + "json"
    verblist = []
    adjlist = []
    causesofActionlist = []
    victimslist = []
    courtslist = []
    for i in verbs:
        verblist.append(i)
    for i in adjs:
        adjlist.append(i)
    for i in causesofAction:
        causesofActionlist.append(i)
    for i in victims:
        victimslist.append(i)
    for i in courts:
        courtslist.append(i)

    model["审判时间"] = vtime
    model["犯罪嫌疑人"] = defendent
    model["出生年月"] = defendentbirth
    model["出生地"] = defendentbirthplace
    model["民族"] = defendentnation
    model["性别"] = defendentgender
    model["案由"] = causesofActionlist
    model["形容词"] = adjlist
    model["动词"] = verblist
    model["被害人"] = victimslist
    model["法院"] = courtslist
    model["原文"] = connecttext

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(model, json_file, ensure_ascii=False)
