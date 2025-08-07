import numpy as np

w = np.array([1, 2, 3])
b = 4


def sigmoid(x):
    return 1 / (1 + np.exp(-(x * w + b)))


print(w, b)


print(sigmoid(np.random.randn(3)))
