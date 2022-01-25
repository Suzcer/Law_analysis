# 裁判文书标注问题的研究报告

作者：CZY组

[TOC]



------

## 概述

### 团队成员及分工

| 姓名   | 学号      | 邮箱                       | 分工                                  |
| ------ | --------- | -------------------------- | ------------------------------------- |
| 陈鉴   | 201250091 | 201250091@smail.nju.edu.cn | 团队负责人、NLP、Django构建           |
| 张亦弛 | 201250088 | 201250088@smail.nju.edu.cn | 前端实现、NLP，图表制作               |
| 苏致成 | 201250104 | 201250104@smail.nju.edu.cn | NLP、Django构建、前端、爬虫、报告撰写 |

### 代码地址

代码尚未开源，请耐心等候。

GitHub Pages：https://github.com/Suzcer/susu-gif

### 其他

项目背景、项目需求、项目访问地址详见“裁判文书标注系统说明文档”；项目开发日志详见“项目开发日志”。



## 研究模型

### 词向量

#### 应用原因

​		裁判文书分词系统应当尽可能为用户（法律工作者）提供更佳的使用体验，因此，我们认为一个历史相似裁判文书的推荐是十分必要的，如此一来，用户能在历史相似案例标注的基础之上进行现有文书的标注，也会大大增加效率。

#### 流程概述

+ 文本预处理
+ 计算文本之间相似度

#### 文本预处理

+ 因为”刑事裁定书“遵从一定的书写规范，所以文本之间的相似度一般较高，为了将这种差异放大，我们选择了将文本共有特征进行适当的消除。如“中华人民共和国最高人民法院”、“审判员”这样的词在我们的剔除范围之内。
+ 利用**正则**匹配消除符号的影响。
+ 因其他实验利用pyhanlp，因此本实验亦依赖pyhanlp提供的**停用词表**。并且pyhanlp库支持CoreStopWordDictionary.apply（）方法支持去除停用词。

#### 模型建立

+ 首先对文书进行分词，获取每个单词对应的词向量
+ 然后将所有单词对应的词向量相加求均值，作为文书的向量
+ 最后计算文书的向量的夹角余弦值，作为它们之间的相似度

​		其中，求词向量的过程运用了Word2vec。训练模型主要代码如下：

```
sentences = word2vec.LineSentence('案件.txt')
model = word2vec.Word2Vec(sentences, hs=1, min_count=1, window=5, vector_size=64)
```

​		案件的来源即来源于数据库，取45份 “刑事裁定书” 作为一个超小型的语料库进行训练，待模型更为稳定后再适当考虑扩大语料库规模。参数中：window=5,意为训练窗口设置为5，即考虑一个单词的前后各5个；vector_size=64即将词向量的维度设置为64，因为笔者用以训练模型的语料库较小，故词向量亦较小。词向量维度的估算公式如下：
$$
n>8.33logN
$$
​		计算文书的夹角余弦值的结果如附录所示。尽管对文本的相似度作出了一定的削减，但就整体而言仍较高。即便如此，实验结果也有一定的参考价值。

​		因为笔者对词向量的原理仅有浅层了解，加之其中牵涉内容篇幅过大，因此对此不予过多解释。但就该实验而言，运用单词词向量加和求得文书词向量再求余弦值的方法还是较为科学可靠的。

#### 其他说明

+ 因为此实验和Django的解释器版本有不兼容的问题，因此尚未将本实验成果继承到项目主体框架中，因此目前用户也不能使用该功能。不过就理论而言，这项应用本身还是值得期待的！
+ 关于多案由裁判文书，模型的相似度预测值还有一定的改进空间
+ 改进思路：将裁判文书按案由予以分类，在相同案由的案件里面选择相似度较高的案件
+ word2vec原理主要是CBOW（continues bag of words）和skipgram。





### 条件随机场

#### 应用原因

​		我们项目的主要分词工作均由条件随机场即CRF完成，因为查阅原书之后对比相关的技术，我们认定，CRF在相关的各种情形下的分词结果更加出色。

下图为“机器学习模型谱系图”。

> 图源《自然语言处理入门》，作者何晗。



<img src="C:\Users\Dudu\AppData\Roaming\Typora\typora-user-images\image-20220117195707672.png" alt="image-20220117195707672 " style="zoom:70%;" />

除此之外，作者还在书中列出这样的数据：

<img src="C:\Users\Dudu\AppData\Roaming\Typora\typora-user-images\image-20220119142723183.png" alt="image-20220119142723183" style="zoom:67%;" />

#### 其他说明

​		CRF算法与HMM的推导密不可分，牵涉内容过多，加之笔者并未涉及过多相关知识，因此不予展开。



### 分词结果评价

​		对于分词结果的评价，有精确率、召回率、F1值等等。

#### 混淆矩阵

| pred_label/true_label | Positive | Negative |
| --------------------- | -------- | -------- |
| Positive              | TP       | FP       |
| Negetive              | FN       | TN       |

​		仅以TP举例讲述类别的含义。TP（true positive）表示样本的真实类别为正，最后预测得到的结果也为正。即第一个T/F表示是否预测正确，第二个P/N表示预测的结果是什么。

#### 精确率/召回率

+ **精确率**表示预测结果中，预测为正样本的样本中，正确预测为正样本的概率
+ **召回率**表示在原始样本的正样本中，最后被正确预测为正样本的概率

二者用混淆矩阵计算如下：
$$
Precsion=\frac{TP}{TP+FP}\\Recall=\frac{TP}{TP+FN}
$$

#### F1-score

**F1-score**引入的原因是为了折中精确率和召回率。公式如下：
$$
F1-score=\frac{2×recall×precision}{recall+precision}
$$


#### TPR/TNR

TPR为敏感度（sensitivity）,TNR为特异度（specificity）

+ TPR：true positive rate，描述识别出的正例占所有正例的比例
+ TNR：true negative rate，描述识别出的负例占所有负例的比例

$$
TPR=\frac{TP}{TP+FN}
\\TNR=\frac{TN}{TN+FP}
$$

​		因为此模型和实际的二分类问题存在显著差异，因此对ROC曲线及之后的内容不加以阐述。

#### 应用评价

​		我们可以将如上分类问题应用到NLP的评价之中。对于一段文本，每个单词在文本中所对应的位置为[a,b]，那么标准答案中，所有单词的区间构成一个集合A，对于某一种切分规则，得到的分词结果的区间构成一个集合B。所以集合A是所有的正确样本，即A 为TP 和 FN的并集，而B是分词器认为的正确样本，即TP和FP的并集，那么 TP 即为 A和B的交集，公式表示如下：
$$
A=TP\bigcup FN
\\B=TP\bigcup FP
\\TP=A\bigcap B
$$
​		因此，可以将召回率和精确率的公式转为：
$$
Precision=\frac{TP}{TP+FP}=\frac{|A\bigcap B|}{|B|}
\\Recall=\frac{TP}{TP+FN}=\frac{|A\bigcap B|}{|A|}
$$
​		依据上述理论，笔者编写了相应的代码，并且手动分词分出“标准分词”作为对比。因为“标准分词”的数据难以获得，所以最终只进行了一篇裁判文书的精确率、召回率和F1-score的计算。此次实验详见提交的代码，文本已做预处理，测试的是pyhanlp分词的结果。计算结果如下：

+ Recall=0.7894
+ Precision=0.8679
+ F1-score=0.8266

​		笔者认为，此模式pyhanlp分词过细与人名识别功能较弱是其得分一般的主要原因。



### 决策树

#### 应用原因

​		决策树是机器学习的入门操作。因为我们目前的项目仅仅针对“刑事裁定书”进行有效分词标注（原因在于分割的代码中利用了刑事裁定书的格式要求），因此，对于如何甄别用户上传的文件或文字对本系统的**鲁棒性**格外重要。即便用简单的正则提取可能可以轻松解决，但是若用户上传文书时不规范（如复制粘贴了两遍）则决策树可以解决此类分类问题。

#### 流程概述

+ 获取数据集：刑事裁定书数据为数据库中数据，与之对比手动下载了民事裁定书与刑事通知书
+ 数据降维与特征提取（特征工程）
+ 模型训练
+ 模型评估



#### 降维处理

​		对于文本而言，特征项往往是其中的词频，而若将全部词语均作为特征项计入会导致运算异常缓慢并且容易出现过拟合的风险，因此需要进行数据降维。

##### 弃用方案

+ 我们认为 **TF-IDF** 进行关键词提取的数据衡量和本实验中相悖，因为TF-IDF会认为在各文本中共同出现的词的权重应该较低，但是在本实验中，例如“刑事”这样的字眼在任何“刑事裁定书”都会出现，但是我们实际要求其权重应该较高。

+ 而 pyhanlp 内置的`extractkeyWord`函数（用的是 **Textrank** 算法）进行单文本处理。而结果中会将许多该文本独有的短语如  “*被告人刘肱钻*”  提取出来作为特征数据，而此类数据显然不能作为判断标准。

+ 因此我们选择手写相关的逻辑代码，思路如下：将文本中出现的词频降序排列，并且词性属于特定类别（如形容词、动词）我们才将其纳入考虑，即便如此，对于总量为 45份刑事裁定书+20份民事裁定书+20份刑事通知书，每份文本提取前10词频的词语，那么词语的总量依然高达300+，不可谓达到了降维的目的。因此我们选择了减少样本的数量来求出更轻便的数据集。结果如附录所示。



##### 标签化

+ 特征选取的方法有：文档频率、信息增益、互信息、卡方拟合检验(CHI)等。在此我们选择朴素的文档频率的方法，并且我们认为，高频词对低频词对文档特征的贡献大。

+ 我们选择了对数据进行**标签化**的处理，标签化的依据即为已有文本中词频较高的并且有意义的词汇。这些词汇在按照词频的优先次序的情况下由我们组员进行筛选。刑事裁定书的词频降序如附录所示。

​		我们挑选的分类如下，挑选工作仍在继续，以下仅做展示处理。

![image-20220118193551787](C:\Users\Dudu\AppData\Roaming\Typora\typora-user-images\image-20220118193551787.png)





#### 模型训练

​		本着不要重复造轮子的原则，我们选取了sklearn作为实现决策树的工具。

> 决策树有多种不同的建造方式，如id3，C4.5，cart，本次实现的是id3（entrophy作为参数）和cart（gini作为参数）

代码如下：

```
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

data=pd.read_csv('data/LawDocument.csv',header=None)
with open('./djangoProject/app01/Test/LawDocumentTitle','r',encoding='utf8')as fp:
    columns = json.load(fp)
data.columns=columns["title"]
vec=DictVectorizer(sparse=False)
feature=data[columns[:-1]]				#最后一列是分类列，需要去除


Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.3)
clf=tree.DecisionTreeClassifier(criterion='gini')		#基尼不纯度（课上没讲）
#clf=tree.DecisionTreeClassifier(criterion='entropy')#两种，信息增益比（课上讲了信息增益）
#X对Y的信息增益率是X对Y的信息增益和X的熵的比值。
#按照信息增益率的降序排序，依次选择具有“较高决定权”的特征项。
clf.fit(Xtrain,Ytrain)
```

#### 模型评估

​		评估代码如下：

```
score=clf.score(Xtest,Ytest)
```

​		若测试未采取标签化的数据，则评分在0.8左右徘徊；采取标签化的数据，模型评分达到0.95左右。

> 之所以没有列出一个确定值，是与sklearn的实现有关，每次训练集和测试集都是随机挑选，因此每次模型不一样都属于正常现象。

​		在加入25份“刑事判决书”之后，上述模型的评分略有下降，解释为：刑事判决书和刑事裁定书的内容较为相似。若选取基尼不纯度选项，则时间上相较信息增益比的模式耗时更多（约10%），与直觉解释相悖。可以解释为：因为样本太少，所以运算速度可能产生误差。

#### 模型调优

​		模型调优主要通过剪枝参数调优实现。sklearn的决策树中提供剪枝参数如下：

+ max_depth：控制决策树最大深度
+ min_samples_leaf：不能有小于此参数的叶子节点
+ min_samples_split：控制最小分支（大于该参数才能拥有子节点)
+ max_featrues：限制特征个数
+ min_impurity_decrease：限制信息增益大小

​		本实验中，进行单独设置max_depth=9、min_samples_leaf=5、min_samples_split=10之后，评估分数均有所增加。此外，还利用了`matplotlib`进行绘制max_depth和score的关系图，如下图所示：

<img src="C:\Users\Dudu\AppData\Roaming\Typora\typora-user-images\image-20220119114211155.png" alt="image-20220119114211155" style="zoom:67%;" />



​		可以看出，当最大深度为9的时候，该模型达到得分最佳。此外，决策树还提供如下参数：

+ class_weight：完成样本标签平衡的参数



#### TF-IDF简述

TF指词频，即该词条在文本中出现的频率
$$
公式:tf_{ij}=\frac{n_{i,j}}{\Sigma_{k}n_{k,j}}
$$
IDF指逆向文本频率，即总文件数目除以包含该词语的文件数目(或+1），得到的商再取对数。
$$
公式：idf_{i}=log\frac{|D|}{1+|\{j:t_{i}\in d_{j}\}|}
$$

$$
TF-IDF=TF*IDF
$$

TF-IDF倾向于过滤掉常见词语，保留重要的词语，因此在特征项的选择中并不适用。

#### TextRank简述

$$
公式：WS(V_{i})=(1-d)+d*\sum_{j\in In(V_{i})}\frac{w_{ji}}{\sum_{V_{k}\in Out(V_{j})}w_{jk}}WS(V_{j})
$$

其中，d用于平滑，PR（Vi）表示结点Vi的rank，In（Vi）表示结点Vi的前驱节点的集合，Out（Vj）表示结点Vj的后继节点的集合。考虑到词语之间可能会有共现，因此增加一项权重Wji。（笔者亦知其然不知其所以然）



#### 其他说明

+ 项目暂时并没有选上择将决策树可视化。
+ 决策树是一种“贪心”的算法，因为不可能枚举所有的连续可能组合，因此每次产生的模型都可能不一样。



### Demo说明

​		此处仅仅是给予标注系统中的Demo页面进行简要说明，详细原理请阅读《自然语言处理入门》，作者何晗。

#### 短语提取

​		按照何晗的说法，首先利用互信息提取，其次用信息熵提取，最后将互信息和左熵、右熵加和结果作为衡量结果。

> 注：何晗为Hanlp的作者



#### 自动摘要

​		按照何晗的说法，首先根据TextRank公式（上文已展示），可以计算每一个句子的权重。而TextRank比PageRank多出的参数wji就需要用到 BM25 算法进行评分。最后按照句子权重降序可以得到自动摘要。

> 原文：[TextRank算法自动摘要的Java实现-码农场 (hankcs.com)](http://www.hankcs.com/nlp/textrank-algorithm-java-implementation-of-automatic-abstract.html)



#### 依存句法分析

​		详见原书。





## 附录

1. 利用词向量进行文本相似性分析，仅截取部分。<img src="C:\Users\Dudu\AppData\Roaming\Typora\typora-user-images\image-20220119141003402.png" alt="image-20220119141003402" style="zoom:67%;" />

2. 刑事裁定书的词频统计，仅截取部分。

   <img src="C:\Users\Dudu\AppData\Roaming\Typora\typora-user-images\image-20220118211507270.png" alt="image-20220118211507270" style="zoom:50%;" />

3. 决策树构建特征项，按照词频的方式则特征项数量巨大。（仅截取部分）

<img src="C:\Users\Dudu\AppData\Roaming\Typora\typora-user-images\image-20220118152552397.png" alt="image-20220118152552397 " style="zoom: 33%;" />