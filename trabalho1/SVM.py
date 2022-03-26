from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import pandas as p
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC


def Svm(datafinal, classes):

    acc_1 = 0
    prec_1 = 0
    f1_1 = 0
    recall_1 = 0
    clf = None

    for repetir in range(10):

        X_train, X_test, y_train, y_test = train_test_split(
            datafinal, classes, test_size=0.5)

        paramet = [{'kernel': ["poly", 'rbf', 'sigmoid', 'linear']}]

        svm = SVC()
        clf = GridSearchCV(svm, paramet, cv=5)
        clf.fit(X_train, y_train)

        previsao = clf.predict(X_test)
        acc = accuracy_score(y_test, previsao)
        f1 = f1_score(y_test, previsao, average='macro')
        prec = precision_score(y_test, previsao, average='macro')
        recall = recall_score(y_test, previsao, average='macro')

        acc_1 = acc + acc_1
        prec_1 = prec + prec_1
        f1_1 = f1 + f1_1
        recall_1 = recall + recall_1

    print(clf.best_params_)
    print("Acuracia: ", str(acc_1/10))
    print("Precisão: ", str(prec_1/10))
    print("F1: ", str(f1_1/10))
    print("Recall: ", str(recall_1/10))
