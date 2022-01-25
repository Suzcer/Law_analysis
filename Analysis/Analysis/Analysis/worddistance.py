from pyhanlp import *
CoreSynonymDictionary = JClass("com.hankcs.hanlp.dictionary.CoreSynonymDictionary")

word_array = [
    "确认",
    "坦白",
]
print("%-5s\t%-5s\t%-10s\t%-5s\n" % ("词A", "词B", "语义距离", "语义相似度"))
for a in word_array:
    for b in word_array:
        print("%-5s\t%-5s\t%-15d\t%-5.10f" % (a, b, CoreSynonymDictionary.distance(a, b),
            CoreSynonymDictionary.similarity(a, b)))
