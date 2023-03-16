import numpy as np 
from sklearn import datasets,ensemble 

datasets = datasets.load_diabetes()

X,y = datasets.data, datasets.target

X.shape

y.shape

x = X[:,5:6]

x.shape

x[0]

# Funcion hipostesis 
def h(x,theta_0,theta_1):
    return theta_0+theta_1*x

#arreglo de 1 columna
ones_column = np.ones((x.shape[0],1))

x = np.concatenate((ones_column,x),axis=1)

x.shape