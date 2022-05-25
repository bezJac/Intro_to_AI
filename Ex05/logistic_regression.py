import math

'''
Computes the dot product of the vectors x and y (lists of numbers).
Assumes that x and y have the same length.
'''

def readDS(filename):
    global ds
    file=open(filename,"r")
    ds=[]
    s=file.readline()
    while s!="":
        s=s.split()
        l=[]
        for val in s:
            l.append(int(val))
        ds.append(l)
        s=file.readline()
    file.close()
    return ds

def save_model(filename, t):
    file= open(filename,'w')
    str1=""
    for val in t:
        str1=str(val)+' '
    file.write(str1)
    file.close()

def dot_prod(x ,y):
    return sum([x[i]*y[i] for i in range(len(x))])

def sigmoid(t, x):
    return 1 / (1 + math.exp(-dot_prod(t ,x)))

def gradient_descent(function, derivative, epsilon, alpha, x):
    f = function(x)
    prevf = f + 1 + epsilon
    while abs(prevf-f) > epsilon:
        x = [x[i] - alpha*derivative(i,x) for i in range(len(x))]
        prevf = f
        f = function(x)
    return x

def function(t):
    global ds
    return -sum([ds[i][-1]*math.log(sigmoid(t,[1] + ds[i][:-1])) + \
                 (1-ds[i][-1])*math.log(1-sigmoid(t,[1] + ds[i][:-1]))\
                      for i in range(len(ds))]) / len(ds)

def derivative(j ,t):
    global ds
    return sum([((sigmoid(t,[1] + ds[i][:-1])) - ds[i][-1]) * ([1] + ds[i])[j] \
            for i in range(len(ds))]) / len(ds)

def classify(t, x):
    return round(sigmoid(t, [1]+x))


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