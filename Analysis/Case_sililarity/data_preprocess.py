import re
from random import shuffle

# 标点符号和特殊字母
punctuation = '''，。、:；（）ＸX×xa"“”,<《》'''

# 对原始数据进行预处理
f1 = open("source.txt", "r", encoding='utf-8')
preprocessed_cases = []  # 存储处理过后的案件
for line in f1.readlines():
    try:
        location, content = line.strip().split("\t")        # 存储案件对应的地区、内容
    except ValueError:
        continue
    else:

        line2 = re.sub("[%s]+" % punctuation, "", content)  # 去除标点、特殊字母
        line3 = re.sub(                                     # 去除冗杂词汇
            "|中华人民共和国最高人民法院|刑事|裁定书|刑|事|裁|定|书|被告人|男|文化|出生|判处|复核|认定|意见|合法|宣告|审判长|最高人民法院|确实|于|书记员",
            "",
            line2)

        preprocessed_cases.append(location + '\t' + line3)
f1.close()

# 打乱数据
shuffle(preprocessed_cases)

# 将预处理后的案件写到文本中
f2 = open("other.txt", "w", encoding='utf-8')
for idx, preprocessed_case in enumerate(preprocessed_cases):
    f2.write(str(idx + 1) + "\t" + preprocessed_case + "\n")
f2.close()
