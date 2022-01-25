import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import csv
import time

# f = open('LawDocument.csv', 'w', encoding='utf-8')
# csv_writer = csv.writer(f)
# L = [
#     [0, 3, 1, 22, 1, 0, 7.25, 0],
#     [1, 1, 0, 38, 1, 0, 71.28, 1],
#     [1, 3, 0, 26, 0, 0, 7.29, 0],
#     [1, 1, 0, 35, 1, 0, 53.1, 0],
#     [0, 3, 1, 35, 0, 0, 8.05, 0]
# ]
# csv_writer.writerow(["幸存", "Pclass", "性别", "年龄", "SibSp", "Parch", "Fare", "Embarked"])
# for i in range(len(L)):
#     csv_writer.writerow(L[i])


data = pd.read_csv(r'D:\PycharmProjects\djangoProject\LawDocument.csv', header=None)
data.columns = ["0", "1", "2", "3", "4", "5", "6"]  # 共有7项，6个因素

vec = DictVectorizer(sparse=False)
feature_name = ["title", "keyword", "verb", "noun", "adj", "other"]
# Xtrain = vec.fit_transform(feature.to_dict(orient='record'))

# print('show feature\n',feature)
# print('show vector\n',Xtrain)
# print('show vector name\n',vec.get_feature_names())
X = data.iloc[:, 1:]
Y = data['0']  # 判别
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.3)
#X,Y是特征和标签

import matplotlib.pyplot as plt

test = []
for i in range(10):
    clf = tree.DecisionTreeClassifier(criterion='gini', max_depth=i + 1)
    # clf=tree.DecisionTreeClassifier(criterion='entropy')
    clf.fit(Xtrain, Ytrain)
    score = clf.score(Xtest, Ytest)
    test.append(score)

# print(clf.score(Xtrain,Ytrain))
# print(*zip(feature_name, clf.feature_importances_))
plt.plot(range(1, 11), test, label="max_depth_LAWDoc",color="red")
plt.legend()
plt.show()
