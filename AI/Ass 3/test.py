from numpy import array, dot, random
import numpy as np
from numpy import array, dot, random, genfromtxt
from math import sin
import matplotlib.pyplot as plt
from random import choice

step_function = lambda x: -1 if x < 0 else 1

training_data = [
    (array([0,0,1]), -1),
    (array([0,1,1]), 1),
    (array([1,0,1]), 1),
    (array([1,1,1]), 1),
]

errors = True
w = [0,0,0]

while errors:
    errors = False
    for x, y in training_data:
        error = y - step_function(dot(w, x))
        if error != 0:
            errors = True
        w += error * x

for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, step_function(result)))
