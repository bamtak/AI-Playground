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

while error < 0:
    error = 1
    count += 1
    for x,y in zip(training_data,training_label):
        prediction = step_function(sin(dot(w,x)))
        l_error = prediction * y
        print prediction,y
        if l_error < 0:
            error = l_error
            n = 0
            while l_error < 0 and n < d:
                w[n] = w[n] + (l_error * x[n] * y*1.0)
                l_error = step_function(sin(dot(w,x))) * y
                n +=1
                print w
