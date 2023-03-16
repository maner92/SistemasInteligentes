import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fit(X, Y, learning_rate=0.0001, epochs=10000, bias=True):
    n = int(len(X))  # Number of elements in X
    y = np.resize(Y, (n, 1))
    if bias:
        m = X.shape[1] + 1
        aux = np.ones((n, 1))
        X = np.concatenate((X, aux), axis=1)
    else:
        m = X.shape[1]
    thetas = np.zeros((m, 1))

    errores = []
    iter_ = []

    # Performing Gradient Descent
    for i in range(epochs):
        Y_pred = np.dot(X, thetas)  # The current predicted value of Y
        error = np.dot(X.T, (y - Y_pred))
        thetas = thetas - learning_rate * (-2/m) * error
        iter_.append(i)
        errores.append(mean_squared_error(y, Y_pred))
    print(thetas)
    return (iter_, errores)

# Making predictions


def mean_squared_error(actual, predicted):
    n = len(actual)
    mse = 0
    for i in range(n):
        mse += (predicted[i] - actual[i])**2
    mse /= n
    return mse

    # def plot(self):
    #     plt.rcParams['figure.figsize'] = (12.0, 9.0)
    #     # preprocessing input data
    #     data = pd.read_csv('data.csv')
    #     X = data.iloc[:, 0]
    #     Y = data.iloc[:, 1]
    #     plt.scatter(X, Y)
    #     plt.show()
