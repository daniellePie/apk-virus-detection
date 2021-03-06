# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from get_num import nor_num,virus_num,white_num

dataset=pd.read_csv("3_gram.csv")
print("dataset:",dataset.shape[0])

x=dataset.iloc[300:(nor_num+virus_num),:-1].values
y=dataset.iloc[300:(nor_num+virus_num),-1].values


from sklearn.model_selection import train_test_split
x_train, x_dev, y_train, y_dev = train_test_split(x, y, test_size = 0.2, random_state = 0)
print("x_train:",x_train.shape[0])
print("x_dev:",x_dev.shape[0])

# 特征量化
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_dev = sc.fit_transform(x_dev)

# SVM
# from sklearn.svm import SVC
# classifier = SVC(kernel = 'sigmoid', random_state = 0)

# knn
# from sklearn.neighbors import KNeighborsClassifier
# classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)

# RandomForest
from sklearn.ensemble import RandomForestClassifier as RF
classifier = RF(n_estimators=500, n_jobs=-1)

# 训练分类器
classifier.fit(x_train,y_train)

# 预测验证集
y_dev_pred = classifier.predict(x_dev)
print("-"*100)
print("y_dev_pred:",y_dev_pred)
print("y_dev:",y_dev)
print("dev_acc: ",classifier.score(x_dev,y_dev))

# 白测试集
x_testw=dataset.iloc[(virus_num+nor_num):(virus_num+nor_num+white_num),:-1].values
print("-"*100)
print(virus_num)
print(nor_num)
print(white_num)
print("x_test_white:",x_testw.shape[0])
y_test_predw = classifier.predict(x_testw)
print("y_test_pred_white:",y_test_predw)
print("test_pre_proba: ",classifier.predict_proba(x_testw))

# 黑测试集
x_testb=dataset.iloc[(virus_num+nor_num+white_num):,:-1].values
print("-"*100)
print("x_test_black:",x_testb.shape[0])
y_test_predb = classifier.predict(x_testb)
print("y_test_pred_black:",y_test_predb)
print("test_pre_proba: ",classifier.predict_proba(x_testb))