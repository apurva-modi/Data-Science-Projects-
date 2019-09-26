import  csv 
import numpy as numpy
from sklearn.svm import SVR
import matplotlib as plt

dates =[]
prices =[]

def getData(filename):
    with open(filename,'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return

