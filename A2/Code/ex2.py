import numpy as np
import matplotlib.pyplot as plt

X=np.array([
[1,1.0,1.0],
[1,0.9,1.0],
[1,0.9,0.875],
[1,0.7,0.75],
[1,0.6,0.875],
[1,0.6,0.875],
[1,0.5,0.75],
[1,0.5,0.8125],
[1,0.5,1.0],
[1,0.5,0.875],
[1,0.5,0.875]])

print(X)

y=np.array([[
1,
1,
1,
-1,
-1,
1,
-1,
-1,
1,
-1,
1
]]).T;

print(y)

w = np.ones((1,X.shape[1]))

#TODO
def error(x,y,w):
	return np.log(1 + np.exp(-y*np.matmul(x,w))) 

#TODO
def error_mean(X,y,w):
	errorSum = 0

	for i in range(0,X.shape[0]):
		errorSum += error(X[i],y[i],w[0])

	return errorSum / X.shape[0]

print(error_mean(X,y,w))