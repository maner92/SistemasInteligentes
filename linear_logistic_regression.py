# Making the imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class LogisticRegression():

    def init(self) -> None:
        pass

    def fit(self, X, Y, learning_rate=0.000000001, epochs=1000, bias=True):
        n = int(len(X))  # numero de elementos de x
        y = Y.reshape(n, 1)  # convertimos y en un vector columna
        if bias:
            m = X.shape[1] + 1
            aux = np.ones((n, 1))
            X = np.concatenate((X, aux), axis=1)
        else:
            m = X.shape[1]
        thetas = np.zeros((m, 1))

        errores = []
        iteraciones = []

        # regresion logistica
        for i in range(epochs):
            h = 1 / (1 + np.exp(-X.dot(thetas)))
            error = h - y
            cost = np.sum(error**2) / (2 * n)
            gradient = (1 / n) * X.T.dot(error)
            thetas = thetas - learning_rate * gradient
            errores.append(cost)
            iteraciones.append(i)

        return iteraciones, errores
