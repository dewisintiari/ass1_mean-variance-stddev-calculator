from types import new_class
import numpy as np
from numpy.matrixlib.defmatrix import matrix

# computing mean
def mean(dataMatrix):
    dataMean = []
    dataMean.append(np.mean(dataMatrix, axis=0).tolist())
    dataMean.append(np.mean(dataMatrix, axis=1).tolist())
    dataMean.append(np.mean(dataMatrix).tolist())
    return dataMean

# computing variance
def variance(dataMatrix):
    dataVar = []
    dataVar.append(np.var(dataMatrix, axis=0).tolist())
    dataVar.append(np.var(dataMatrix, axis=1).tolist())
    dataVar.append(np.var(dataMatrix).tolist())
    return dataVar

# computing standard deviation
def stdDev(dataMatrix):
    dataStdDev = []
    dataStdDev.append(np.std(dataMatrix, axis=0).tolist())
    dataStdDev.append(np.std(dataMatrix, axis=1).tolist())
    dataStdDev.append(np.std(dataMatrix).tolist())
    return dataStdDev

# computing maximum
def max(dataMatrix):
    dataMax = []
    dataMax.append(np.amax(dataMatrix, axis=0).tolist())
    dataMax.append(np.amax(dataMatrix, axis=1).tolist())
    dataMax.append(np.amax(dataMatrix).tolist())
    return dataMax

# computing minimum
def min(dataMatrix):
    dataMin = []
    dataMin.append(np.amin(dataMatrix, axis=0).tolist())
    dataMin.append(np.amin(dataMatrix, axis=1).tolist())
    dataMin.append(np.amin(dataMatrix).tolist())
    return dataMin

# computing sum
def sum(dataMatrix):
    dataSum = []
    dataSum.append(np.sum(dataMatrix, axis=0).tolist())
    dataSum.append(np.sum(dataMatrix, axis=1).tolist())
    dataSum.append(np.sum(dataMatrix).tolist())
    return dataSum

def calculate(dataList):
    try:
        dataMatrix = np.reshape(dataList, (3,3))
    except:
        raise ValueError("List must contain nine numbers.")

    dataMean = mean(dataMatrix)
    dataVar = variance(dataMatrix)
    dataStdDev = stdDev(dataMatrix)
    dataMax = max(dataMatrix)
    dataMin = min(dataMatrix)
    dataSum = sum(dataMatrix)

    dataStat = {
        'mean' : dataMean, 
        'variance' : dataVar, 
        'standard deviation' : dataStdDev, 
        'max' : dataMax, 
        'min' : dataMin, 
        'sum' : dataSum
        }

    return dataStat