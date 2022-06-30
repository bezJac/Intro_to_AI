# Menachem Heller 305567943
# Bezalel Jacober  312033236

import math

'''
Computes the dot product of the vectors x and y (lists of numbers).
Assumes that x and y have the same length.
'''
ds = []


def readDS(filename):
    # read a data set of points and their classification into list
    # each row in data set is a point ,where last column is value of classification
    global ds
    file = open(filename, "r")  # open file
    s = file.readline()
    while s != "":  # read each row and add its values into a sublist in the main list
        s = s.split()
        l = []
        for val in s:
            l.append(int(val))
        ds.append(l)
        s = file.readline()
    file.close()
    return ds  # return list ci=ontaining lists of points and their classification


def save_model(filename, t):
    # save model calculated by a data set into file
    # each value of coefficient separated by a space
    file = open(filename, 'w')
    str1 = ""
    for val in t:
        str1 = str(val) + ' '
        file.write(str1)
    file.close()


def read_model(filename):
    # read a model of coefficients from a file
    # returns list with the values of the coefficients
    file = open(filename, 'r')
    res = []
    s = file.readline()
    s = s.split()
    for val in s:
        res.append(float(val))
    file.close()
    return res


def dot_prod(x, y):
    return sum([x[i] * y[i] for i in range(len(x))])


def sigmoid(t, x):
    return 1 / (1 + math.exp(-dot_prod(t, x)))


def gradient_descent(function, derivative, epsilon, alpha, x):
    f = function(x)
    prevf = f + 1 + epsilon
    while abs(prevf - f) > epsilon:
        x = [x[i] - alpha * derivative(i, x) for i in range(len(x))]
        prevf = f
        f = function(x)
    return x


def function(t):
    global ds
    return -sum([ds[i][-1] * math.log(sigmoid(t, [1] + ds[i][:-1])) + \
                 (1 - ds[i][-1]) * math.log(1 - sigmoid(t, [1] + ds[i][:-1])) \
                 for i in range(len(ds))]) / len(ds)


def derivative(j, t):
    global ds
    return sum([((sigmoid(t, [1] + ds[i][:-1])) - ds[i][-1]) * ([1] + ds[i])[j] \
                for i in range(len(ds))]) / len(ds)


def classify(t, x):
    return round(sigmoid(t, [1] + x))


'''
ds = [[1,1,0],[2,3,1],[3,2,1]]
t = [1,1,1]
t = gradient_descent(function, derivative, 0.000001, 0.001, t)
print (t)
print("+++++++++++++++++")
print (classify(t , [1,1]))
print (classify(t , [2,3]))
print (classify(t , [3,2]))
'''
