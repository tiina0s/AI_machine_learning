# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:21:48 2018

@author: Lenovo
"""

import pandas
import logging
logging.basicConfig(filename='classificationlogs.log',level=logging.DEBUG)


# veergude nimed võetud kirjeldusest
features = ["buying", "maint", "doors", "persons", "lug_boot", "safety"]        
                                                                                
car_data = pandas.read_csv("car.data.txt",                                          
    header=None,                                                                
    names=features + ["class"]) 

X_text = car_data.loc[:, features]

X = pandas.get_dummies(X_text)                                                   
#print(X.columns)                                                                

y = car_data["class"]

from sklearn.model_selection import train_test_split

# no shuffling
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, shuffle=False)


from sklearn import tree
dtc=tree.DecisionTreeClassifier()
dtc.fit(X_train, y_train)

dtc.score(X_test, y_test)
logging.info("Otsustuspuu")

logging.info("Testandmete klassifitseerimine juhul, kui andmed on sorteeritud ning treeningandmed erinevad testandmetest:")
logging.info(dtc.score(X_test, y_test))


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)

# puu on treenitud, vaatame kiirelt, kui hästi ta testandmeid klassifitseerib:
dtc.score(X_test, y_test)
print(dtc.score(X_test, y_test))

logging.info("Testandmete klassifitseerimine juhul, kui andmed on segatud ning treening- ja testandmed on sarnasemad:")
logging.info(dtc.score(X_test, y_test))

from sklearn.metrics import precision_recall_fscore_support

y_predicted = dtc.predict(X_test)
precision, recall, _, _ = precision_recall_fscore_support(                          
        y_predicted, y_test, average=None, labels=["vgood"])

#print("precision, kui palju autosid 'vaga hea' olid oigesti klassifitseeritud:")
#print(precision)
#print("recall, nr, kui suur osa 'vaga haid' yles leiti:")
#print(recall)
logging.info("Precision: Kui palju autosid, mille kohta otsustuspuu ütles 'väga hea', olid õigesti klassifitseeritud:")
logging.info(precision)
logging.info("Recall: Kui suur osa 'väga häid' autosid kogu testandmestikust üles leiti:")
logging.info(recall)
logging.info("Närvivõrk")


from sklearn import neural_network
nnc = neural_network.MLPClassifier(hidden_layer_sizes=(10,))
nnc.fit(X_train, y_train)
nnc.score(X_test, y_test)

nnc = neural_network.MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)

n_features = X_train.shape[1]
nnc_shape = (n_features, n_features, 10)
nnc = neural_network.MLPClassifier(hidden_layer_sizes=nnc_shape, max_iter=1000)

logging.info("Testandmete klassifitseerimine närvivõrguga:")
# no shuffling
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, shuffle=False)
logging.info("Testandmete klassifitseerimine juhul, kui andmed on sorteeritud ning treeningandmed erinevad testandmetest:")
nnc.fit(X_train, y_train)

logging.info(nnc.score(X_test, y_test))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)

logging.info("Testandmete klassifitseerimine juhul, kui andmed on segatud ning treening- ja testandmed on sarnasemad:")
nnc.fit(X_train, y_train)
logging.info(nnc.score(X_test, y_test))

y_nnc = nnc.predict(X_test)
precision, recall, _, _ = precision_recall_fscore_support(y_nnc, y_test, average=None, labels=["vgood"])


X1 = X_train[y_train == "unacc"]
X2 = X_train[y_train == "acc"]
X3 = X_train[y_train == "good"]
X4 = X_train[y_train == "vgood"]
y1 = y_train[y_train == "unacc"]
y2 = y_train[y_train == "acc"]
y3 = y_train[y_train == "good"]
y4 = y_train[y_train == "vgood"]

from sklearn.utils import resample

biggest_class = X1.shape[0]

X2r, y2r = resample(X2, y2, n_samples=biggest_class)
X3r, y3r = resample(X3, y3, n_samples=biggest_class)
X4r, y4r = resample(X4, y4, n_samples=biggest_class)


X_balanced = pandas.concat([X1, X2r, X3r, X4r])
y_balanced = pandas.concat([y1, y2r, y3r, y4r])

y_predicted = nnc.predict(X_balanced)
precision, recall, _, _ = precision_recall_fscore_support(                          
        y_predicted, y_balanced, average=None, labels=["vgood"])

logging.info("*_balanced andmed ning score meetod:")
logging.info(nnc.score(X_balanced, y_balanced))
logging.info("*_balanced andmed ning 'vgood' leidmine:")
logging.info("Precision: Kui palju autosid, mille kohta otsustuspuu ütles 'väga hea', olid õigesti klassifitseeritud:")
logging.info(precision)
logging.info("Recall: Kui suur osa 'väga häid' autosid kogu testandmestikust üles leiti:")
logging.info(recall)

#nnc.score(X_balanced, y_balanced)
