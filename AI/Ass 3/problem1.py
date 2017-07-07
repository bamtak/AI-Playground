import numpy as np
from numpy import array, dot, random, genfromtxt
from math import sin
import sys

step_function = lambda x: -1 if x < 0 else 1

inputfile = sys.argv[1]
outputfile = sys.argv[2]

data = genfromtxt(inputfile, delimiter=',')
num, d = np.shape(data)
training_data = data[:,:-1]
training_label = data[:,-1]
bias = np.zeros((num, 1))
bias.fill(1)
training_data = np.append(training_data,bias,axis=1)


w = np.zeros(d)
w_save = np.array([])
errors = True

while errors:
    errors = False
    for x, y in zip(training_data,training_label):
        error = y - step_function(dot(w, x))
        if error != 0:
            errors = True
        w += error * x
        if w_save.size == 0:
            w_save = w
        else:
            w_save = np.vstack((w_save,w))

np.savetxt(outputfile, w_save, delimiter=',')
