import numpy as np
X = np.array([[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,0,1],[1,0,1],[0,1,1],[1,1,1]])
Y = np.array([[0,0,0,0,0,0,0,1]]).T
W = np.random.random((3,1))
for i in range(10000):
    z = np.dot(X,W)
    O = 1 / (1 + np.exp(-z))
    W -= np.dot(X.T,(O-Y) * O * (1-O))
print(W)
