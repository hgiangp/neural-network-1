import math 

num_features = 4 

def read_data(file_name): 
    r'''read data from iris dataset, normalize the data'''

    for line in open(file_name, 'r'):
        data = line.strip().split(',')[:num_features] # in string
        data = [float(xi) for xi in data] # convert to float 

        mean_data = math.sqrt(sum([xi ** 2 for xi in data])) # calculate eucludean distance mean = sqrt(sum (xi^2))  

        data = [xi*1.0 / mean_data for xi in data] # normalize data xi/mean 

        fmt = '{%.3f,%.3f,%.3f,%.3f},' % (data[0], data[1], data[2], data[3])
        print(fmt)

if __name__=='__main__':
    file_name = './data/iris.data'
    read_data(file_name)