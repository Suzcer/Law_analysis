## README

+ ana.py 是pyhanlp的简单使用，用于文本整体的词性的分析
+ ana02.py 是依赖于pyhanlp的对文本进行分析的过程，并且将内容生成为json文件
+ doc2txt.py 和 doc2txt02.py 是因为爬虫下载的doc转txt的代码，方便进行后续处理
+ textrank.py 是依赖于 textrank4zh 的进行关键词提取的代码，主要参考《裁判文书关键词提取的改进方法研究》文章，文章认为，textrank4zh 比常见的 Word2Vec 效果更优秀，因此选择其进行实验。但因为缺乏前期对文本的训练，所以导致类似"中华人民共和国"等对甄别文本内容意义不大的词条，因此暂时效果不如直接利用 pyhanlp 进行词性分析进而提取的效果
+ txttrip.py 是试验内容，尝试将txt中尾部空格消去，实际上没有使用该方法
+ worddistance.py 是运用 pyhanlp 进行词距分析的代码，已经使用到 ana02.py 的主体分析代码中