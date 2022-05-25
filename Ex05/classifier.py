from logistic_regression import*

def classify(dsfile,modelfile):
     global ds
     ds =readDS(dsfile)
     t = [1,1,1]
     t = gradient_descent(function, derivative, 0.000001, 0.001, t)
     save_model(modelfile,t)
     file=open(dsfile,'w')

     for val in ds:
         val.append(classify(t, val))
         for i in val:
            file.write(str(i)+' ')
         file.write('\n')
     file.close()



classify("dataSet.txt","model.txt")
