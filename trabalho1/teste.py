from KNN import knn
from MLP import mlp
from SVM import Svm
import pandas as p
from sklearn.preprocessing import MinMaxScaler

dados = p.read_csv("student.csv")

classes = dados['GRADE']

dados.loc[dados.GRADE <= 3, 'GRADE'] = 0
dados.loc[dados.GRADE >= 4, 'GRADE'] = 1

dados_df = p.DataFrame(dados, columns=[
    'AGE', 'GENDER', 'HS_TYPE', 'SCHOLARSHIP', 'WORK', 'ACTIVITY',
    'PARTNER', 'SALARY', 'TRANSPORT', 'LIVING', 'MOTHER_EDU', 'FATHER_EDU',
    '#_SIBLINGS', 'KIDS', 'MOTHER_JOB', 'FATHER_JOB', 'STUDY_HRS',
    'READ_FREQ', 'READ_FREQ_SCI', 'ATTEND_DEPT', 'IMPACT', 'ATTEND',
    'PREP_STUDY', 'PREP_EXAM', 'NOTES', 'LISTENS', 'LIKES_DISCUSS',
    'CLASSROOM', 'CUML_GPA', 'EXP_GPA', 'COURSE ID', 'GRADE'
])

dados_df = p.concat(
    [p.DataFrame(dados_df), p.DataFrame(classes)], axis=1)

datafinal = p.DataFrame(dados, columns=[
    'AGE', 'GENDER', 'HS_TYPE', 'SCHOLARSHIP', 'WORK', 'ACTIVITY',
    'PARTNER', 'SALARY', 'TRANSPORT', 'LIVING', 'MOTHER_EDU', 'FATHER_EDU',
    '#_SIBLINGS', 'KIDS', 'MOTHER_JOB', 'FATHER_JOB', 'STUDY_HRS',
    'READ_FREQ', 'READ_FREQ_SCI', 'ATTEND_DEPT', 'IMPACT', 'ATTEND',
    'PREP_STUDY', 'PREP_EXAM', 'NOTES', 'LISTENS', 'LIKES_DISCUSS',
    'CLASSROOM', 'CUML_GPA', 'EXP_GPA', 'COURSE ID'
])

scaler = MinMaxScaler()
scaler.fit(datafinal)
datafinal = scaler.transform(datafinal)

print('========= MLP =========')
print(mlp(datafinal, classes))
print()
print('========= KNN =========')
print(knn(datafinal, classes))
print()
print('========= SVM =========')
print(Svm(datafinal, classes))

