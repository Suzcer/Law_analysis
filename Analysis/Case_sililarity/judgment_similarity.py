import logging
from gensim.models import word2vec
import numpy as np
from scipy import linalg
'''
        计算案件之间的相似度
        首先对句子分词，然后获取每个单词对应的词向量
        然后将所有单词对应的词向量相加求平均值，作为句子的向量
        最后，计算句子的向量的夹角余弦值，作为它们之间的相似度
'''
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)

# 使用gensim中的word2vec模块
sentences = word2vec.LineSentence('案件.txt')
model = word2vec.Word2Vec(sentences, hs=1, min_count=1, window=5, vector_size=64)


# req_count = 5
# for key in model.wv.similar_by_word('被告人', topn=100):
#     if len(key[0]) == 3:
#         req_count -= 1
#         print(key[0], key[1])
#         if req_count == 0:
#             break


def sentence_vector(s):
    '''
    将所有单词的词向量相加求平均值，得到的向量即为句子的向量

    '''
    words = s.split(" ")
    v = np.zeros(64)
    for word in words:
        if word !="":
            v += model.wv[word]
    v /= len(words)
    return v


def vector_similarity(s1, s2):
    '''
    计算两个句子之间的相似度:将两个向量的夹角余弦值作为其相似度
    '''
    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    return np.dot(v1, v2) / (linalg.norm(v1) * linalg.norm(v2))


with open("案件.txt", "r", encoding="utf-8") as f:
    contents = f.readlines()
    matrix = np.zeros((len(contents), len(contents)))
    for i in range(len(contents)):
        for j in range(len(contents)):
            # 使用矩阵存储所有案件之间的相似度
            matrix[i][j] = vector_similarity(
                contents[i].strip(), contents[j].strip())

    f1 = open("result.txt", "w", encoding="utf-8")
    for j in range(len(contents)):
        # 获取最为相似的案件
        # 注意：每个案件与自己的相似度为1，因此获取的是相似度第二大的案件
        index = np.argsort(matrix[j])[-2]

        f1.writelines("案件" + str(j + 1) + ":" + '\t')
        f1.writelines(contents[j])
        f1.writelines("案件" + str(index + 1) + ":" + '\t')
        f1.writelines(contents[index])
        f1.writelines("相似度： " + str(matrix[j][index]) + '\n\n')
