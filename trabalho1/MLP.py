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
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


def mlp(datafinal, classes):

    acc_1 = 0
    prec_1 = 0
    f1_1 = 0
    recall_1 = 0
    grid = None

    for repetir in range(10):

        X_train, X_test, y_train, y_test = train_test_split(
            datafinal, classes, test_size=0.2)

        paramet = [{'activation': ['identity', 'logistic', 'tanh', 'relu'],
                    'hidden_layer_sizes':[(3, 3), (5, 5), (7, 7)],
                    'learning_rate_init':[0.0001, 0.001, 0.01], 'max_iter':[3000]}]

        mlp = MLPClassifier()
        grid = GridSearchCV(mlp, paramet, cv=5)
        grid.fit(X_train, y_train)

        previsao = grid.predict(X_test)
        acc = accuracy_score(y_test, previsao)
        f1 = f1_score(y_test, previsao, average='macro')
        prec = precision_score(y_test, previsao, average='macro')
        recall = recall_score(y_test, previsao, average='macro')

        acc_1 = acc + acc_1
        prec_1 = prec + prec_1
        f1_1 = f1 + f1_1
        recall_1 = recall + recall_1

    #print(grid.get_params)
    print("Acuracia: ", str(acc_1/10))
    print("Precisão: ", str(prec_1/10))
    print("F1: ", str(f1_1/10))
    print("Recall: ", str(recall_1/10))
