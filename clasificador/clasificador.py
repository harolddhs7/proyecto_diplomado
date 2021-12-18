from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import make_blobs
import numpy as np
import pandas as pd

df = pd.read_excel("../dataset.xlsx")
clf = GaussianNB()

df_etiqueta = df['Nivel de alerta']
df.drop(['Nivel de alerta'],axis=1,inplace=True)

#print(df, df_etiqueta)
clf.fit(df,df_etiqueta)

def clasificacion(lluvia,nivel):
    return clf.predict([[lluvia, nivel]])[0]

#print(clasificacion(1,2))

#X, y = make_blobs(n_samples = 10, centers =3, random_state = 6)

#print(X)
#print(y)
