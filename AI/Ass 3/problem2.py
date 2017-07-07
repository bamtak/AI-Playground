
import numpy as np
from numpy import array, dot, random, genfromtxt
from math import sin
import sys, os


def preprocess(X):
    return np.divide((X - np.mean(X)),np.std(X))

def fit(X, y, iter = 100, alpha = 0.3):
    temp = sys.stdout
    f = open(outputfile,'a')
    sys.stdout = f
    X_norm = preprocess(X)
    num, d = np.shape(X_norm)
    bias = np.zeros((num, 1))
    bias.fill(1)
    X_norm = np.append(bias,X_norm,axis=1)
    num, d = np.shape(X_norm)
    beta = np.zeros(d)
    for i in xrange(iter):
        f_x = np.dot(beta,np.transpose(X_norm))
        error = f_x - y
        der = alpha * (1.0/num) * np.dot(error, X_norm)
        #print np.dot(error,error)
        print 'beta :{} and der {}'.format(beta, der)
        beta = beta - der
    print '{},{},{},{},{}'.format(alpha,iter,beta[0],beta[1],beta[2])
    sys.stdout = temp
    f.close()

def main(X, y, alphas):
    beta_save = np.array([])
    for alpha in alphas:
        fit(X,y,alpha = alpha)
    fit(X, y, iter = 300, alpha = 0.78)


if __name__ == "__main__":
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    try:
        os.remove(outputfile)
    except OSError:
        pass
    alphas = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]
    data = genfromtxt(inputfile, delimiter=',')
    num, d = np.shape(data)

    # Let split our data to training and label sets
    training_data = data[:,:-1]
    training_label = data[:,-1]

    main(training_data,training_label, alphas)
