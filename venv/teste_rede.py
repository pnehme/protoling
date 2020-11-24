from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()
entradas = iris.data
saidas = iris.target
print(entradas)
print(saidas)
redeneural = MLPClassifier(verbose=True,
                           max_iter=10000,
                           tol=0.00001,
                           activation='logistic',
                           learning_rate_init=0.0001)
redeneural.n_layers_ = 400
redeneural.fit(entradas,saidas)