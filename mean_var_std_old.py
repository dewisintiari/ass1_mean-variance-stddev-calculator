from types import new_class
import numpy as np
from numpy.matrixlib.defmatrix import matrix

# computing mean
def mean(dataMatrix):
    data0 = np.mean(dataMatrix, axis=0)
    data1 = np.mean(dataMatrix, axis=1)
    data2 = np.mean(dataMatrix)
    dataMean = [data0, data1, data2]
    return dataMean

# computing variance
def variance(dataMatrix):
    data0 = np.std(dataMatrix, axis=0)
    data1 = np.std(dataMatrix, axis=1)
    data2 = np.std(dataMatrix)
    dataStdDev = [data0, data1, data2]
    return dataStdDev

# computing standard deviation
def stdDev(dataMatrix):
    data0 = np.var(dataMatrix, axis=0)
    data1 = np.var(dataMatrix, axis=1)
    data2 = np.var(dataMatrix)
    dataVar = [data0, data1, data2]
    return dataVar

# computing maximum
def max(dataMatrix):
    data0 = np.amax(dataMatrix, axis=0)
    data1 = np.amax(dataMatrix, axis=1)
    data2 = np.amax(dataMatrix)
    dataMax = [data0, data1, data2]
    print('type = ', type(dataMax))
    return dataMax

# computing minimum
def min(dataMatrix):
    data0 = np.amin(dataMatrix, axis=0)
    data1 = np.amin(dataMatrix, axis=1)
    data2 = np.amin(dataMatrix)
    dataMin = [data0, data1, data2]
    return dataMin

# computing sum
def sum(dataMatrix):
    data0 = np.sum(dataMatrix, axis=0)
    data1 = np.sum(dataMatrix, axis=1)
    data2 = np.sum(dataMatrix)
    dataSum = [data0, data1, data2]
    return dataSum

def calculate(dataList):
    if len(dataList) < 9:
        raise ValueError("List must contain nine numbers.")
    
    try:
        for item in dataList:
            float(item)
    except ValueError:
        raise ValueError("The input list must be a list of numbers.")

    arr = np.array(dataList)
    newArr = np.array_split(arr, 3) 
    dataMatrix = np.array([newArr[0], newArr[1], newArr[2]])

    dataStat = {
        'mean' : [], 
        'variance' : [], 
        'standard deviation' : [], 
        'max' : [], 
        'min' : [], 
        'sum' : []
        }

    dataMean = mean(dataMatrix)
    dataVar = variance(dataMatrix)
    dataStdDev = stdDev(dataMatrix)
    dataMax = max(dataMatrix)
    dataMin = min(dataMatrix)
    dataSum = sum(dataMatrix)

    dataStat['mean'].append(dataMean)
    dataStat['variance'].append(dataVar)
    dataStat['standard deviation'].append(dataStdDev)
    dataStat['max'].append(dataMax)
    dataStat['min'].append(dataMin)
    dataStat['sum'].append(dataSum)

    return dataStat
