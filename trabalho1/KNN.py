import pandas as p
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.preprocessing import MinMaxScaler


def knn(datafinal, classes):

    acc_1 = 0
    prec_1 = 0
    f1_1 = 0
    recall_1 = 0

    for repetir in range(10):

        X_train, X_test, y_train, y_test = train_test_split(
            datafinal, classes, test_size=0.2)

        # ‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute'
        knn = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
        knn.fit(X_train, y_train)

        print(knn.predict(X_test))

        previsao = knn.predict(X_test)

        acc = accuracy_score(y_test, previsao)
        f1 = f1_score(y_test, previsao, average='macro')
        prec = precision_score(y_test, previsao, average='macro')
        recall = recall_score(y_test, previsao, average='macro')

        acc_1 = acc + acc_1
        prec_1 = prec + prec_1
        f1_1 = f1 + f1_1
        recall_1 = recall + recall_1

    print("Acuracia: ", str(acc_1/10))
    print("Precisão: ", str(prec_1/10))
    print("F1: ", str(f1_1/10))
    print("Recall: ", str(recall_1/10))
