# Readme

[TOC]



## 结构如下（可以跳过）

├─Analysis
│  └─Analysis
│      ├─.idea
│      │  ├─dataSources
│      │  └─inspectionProfiles
│      ├─Analysis
│      │  └─__pycache__
│      ├─Other
│      │  ├─Case_sililarity
│      │  ├─CRF
│      │  ├─HMM
│      │  └─NLP-evaluate
│      └─venv
│          ├─Include
│          ├─Lib
│          │  └─site-packages
│          └─Scripts
├─djangoProject
│  ├─.idea
│  │  ├─dataSources
│  │  │  └─d1e7f6d1-2060-4665-b8d0-9e671d2b03d2
│  │  │      └─storage_v2
│  │  │          └─_src_
│  │  │              └─schema
│  │  └─inspectionProfiles
│  ├─app01
│  │  ├─json_file
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  ├─Otherfile
│  │  │  ├─刑事判决书file
│  │  │  ├─刑事通知书file
│  │  │  └─民事裁定书file
│  │  ├─Test
│  │  ├─upload_file
│  │  └─__pycache__
│  ├─djangoProject
│  │  └─__pycache__
│  ├─static
│  │  ├─bootstrap-5.1.3-dist
│  │  │  ├─css
│  │  │  └─js
│  │  ├─css
│  │  ├─element
│  │  ├─FileSaver.js-master
│  │  │  └─FileSaver.js-master
│  │  │      ├─.github
│  │  │      ├─dist
│  │  │      └─src
│  │  ├─icon
│  │  ├─iconfont
│  │  │  ├─add_file
│  │  │  ├─cloud
│  │  │  ├─court
│  │  │  ├─defendent
│  │  │  ├─download
│  │  │  ├─Github
│  │  │  ├─save
│  │  │  ├─saveDB
│  │  │  ├─search
│  │  │  ├─spider
│  │  │  └─upload
│  │  ├─img
│  │  ├─jquery-1.7.2
│  │  │  └─jquery-1.7.2
│  │  └─js
│  ├─templates
│  └─__pycache__
├─sklearn
│  └─sklearn
│      └─.idea
│          └─inspectionProfiles
├─参考资料
└─语料库



## Analysis

### Analysis

Analysis中ana03进行数据的分词；doc2txt2进行格式转化

### Other

Case_similarity进行案件相似度的检查；

NLP-evaluate进行NLP分词效果的判断；

HMM为隐马尔科夫的分词训练



## Djangoproject

### app01

json_file：json数据（已分词）

Otherfile：刑事判决书、民事裁定书

Test：命名实体识别、tf-idf

upload_file:txt数据

static：前端依赖

templates：前端页面



## sklearn

：决策树判断裁判文书





## 裁判文书网爬虫

getdata/getdata_safe：爬虫













