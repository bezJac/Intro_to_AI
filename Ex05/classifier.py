from logistic_regression import *


# set and write to file classification for points provided from database file
def classifier(dsfile, modelfile):
    global ds
    ds = readDS(dsfile)  # read points from file with original classification
    t = [1, 1, 1]
    t = gradient_descent(function, derivative, 0.000001, 0.001, t)  # calculate model
    save_model(modelfile, t)  # write model to separate file
    model = read_model(modelfile)  # read model from file ti variable
    file = open(dsfile, 'w')  # add to database file points, classification value calculated with model
    for val in ds:  # calculate classification for each point
        val.append(classify(model, val))
        for i in val:  # write to file point with added new classification
            file.write(str(i) + ' ')
        file.write('\n')
    file.close()


classifier("DataSet.txt", "model.txt")
