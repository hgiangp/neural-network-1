import math 
import numpy as np 

num_features = 4 

def read_data(file_name): 
    r'''read data from iris dataset, normalize the data'''
    iris_data = []

    for line in open(file_name, 'r'):
        data = line.strip().split(',')[:num_features] # in string
        data = [float(xi) for xi in data] # convert to float 
        iris_data.append(np.asarray(data))
    
    iris_data = np.asarray(iris_data)
    mu = np.mean(iris_data, axis=0) 
    sigma = np.std(iris_data, axis=0)
    iris_data = (iris_data - mu)/(sigma + 0.001)
    
    for data in iris_data:
        fmt = '{%.3f,%.3f,%.3f,%.3f},' % (data[0], data[1], data[2], data[3])
        print(fmt)

if __name__=='__main__':
    file_name = './data/iris.data'
    read_data(file_name)