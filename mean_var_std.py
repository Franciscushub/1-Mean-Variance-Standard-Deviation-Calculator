import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
        
    calculations = {}
    numbers = np.array(list)
    numbers = numbers.reshape((3,3))
    meanl = mean(numbers)
    varl = variance(numbers)
    stdl = std_variation(numbers)
    maxl = max(numbers)
    minl = min(numbers)
    suml = sum(numbers)
    calculations = {'mean': meanl, 'variance': varl, 'standard deviation': stdl, 'max': maxl, 'min': minl, 'sum': suml}
    return calculations


def mean(numbers):
    # mean axis 1:
    meanax1 = numbers.mean(axis=0)
    meanax2 = numbers.mean(axis=1)
    meanflat = numbers.mean()
    meanl = []
    meanl.append(meanax1.tolist())
    meanl.append(meanax2.tolist())
    meanl.append(meanflat.tolist())
    return meanl

def variance(numbers):
    # mean axis 1:
    varax1 = numbers.var(axis=0)
    varax2 = numbers.var(axis=1)
    varflat = numbers.var()
    varl = []
    varl.append(varax1.tolist())
    varl.append(varax2.tolist())
    varl.append(varflat.tolist())
    return varl

def std_variation(numbers):
    stdax1 = numbers.std(axis=0)
    stdax2 = numbers.std(axis=1)
    stdflat = numbers.std()
    stdl = []
    stdl.append(stdax1.tolist())
    stdl.append(stdax2.tolist())
    stdl.append(stdflat.tolist())
    return stdl

def max(numbers):
    maxax1 = numbers.max(axis=0)
    maxax2 = numbers.max(axis=1)
    maxflat = numbers.max()
    maxl = []
    maxl.append(maxax1.tolist())
    maxl.append(maxax2.tolist())
    maxl.append(maxflat.tolist())
    return maxl

def min(numbers):
    minax1 = numbers.min(axis=0)
    minax2 = numbers.min(axis=1)
    minflat = numbers.min()
    minl = []
    minl.append(minax1.tolist())
    minl.append(minax2.tolist())
    minl.append(minflat.tolist())
    return minl

def sum(numbers):
    sumax1 = numbers.sum(axis=0)
    sumax2 = numbers.sum(axis=1)
    sumflat = numbers.sum()
    suml = []
    suml.append(sumax1.tolist())
    suml.append(sumax2.tolist())
    suml.append(sumflat.tolist())
    return suml