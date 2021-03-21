# Loading data with python standart library
import csv
import numpy as np
path = r"G:\rauf\STEPBYSTEP\Data\iris.csv"
with open(path,'r') as f:
   reader = csv.reader(f,delimiter = ',')
   headers = next(reader)
   data = list(reader)
   data = np.array(data)
   print(headers)
   print("here our data loaded with python standart library \n")
   print(data.shape)
   print(data[:3])

# Loading data with numpy 
from numpy import loadtxt
path = r"G:\rauf\STEPBYSTEP\Data\pima-indians-diabetes.csv"
datapath= open(path, 'r')
data = loadtxt(datapath, delimiter=",")
print("here our data loaded with numpy \n")
print(data.shape)
print(data[:3])

# Loadinf data with pandas
from pandas import read_csv
path = r"G:\rauf\STEPBYSTEP\Data\iris.csv"
data = read_csv(path)
print("here our data loaded with pandas \n")
print(data.shape)
print(data[:3])
