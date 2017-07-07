import numpy as np
from numpy import array, dot, random, genfromtxt
from math import sin
import matplotlib.pyplot as plt

step_function = lambda x: -1 if x < 0 else 1

data = genfromtxt('input1.csv', delimiter=',')
num, d = np.shape(data)
training_data = data[:,:-1]
training_label = data[:,-1]
bias = np.zeros((num, 1))
bias.fill(1)
training_data = np.append(training_data,bias,axis=1)


w = np.zeros(d)
error = -1
count = 0

colors = np.array([(lambda x: 'r' if x < 1 else 'g' )(x) for x in training_label])
plt.scatter(training_data[:,1],training_data[:,0], c = colors)
plt.show()