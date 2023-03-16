from sklearn import datasets
import linear_logistic_regression as linear
from matplotlib import pyplot as plt

data_set = datasets.load_breast_cancer()
X = data_set['data']
X.shape
y = data_set['target']
y.shape
ll = linear.LogisticRegression()
iteraciones, errores = ll.fit(X, y)

plt.plot(iteraciones, errores)
plt.show()
