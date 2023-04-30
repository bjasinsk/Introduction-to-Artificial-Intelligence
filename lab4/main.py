import math
import pandas as pd


def frequencyDictionary(u):
    yValues = {}
    for x, y in u:
        if y not in yValues:
            yValues[y] = 1
        else:
            yValues[y] += 1
    return yValues

def entropy(u):
    yValues = frequencyDictionary(u)
    result = 0.0
    n = len(u)

    for value in yValues:
        v = yValues[value] / n
        result -= v * math.log2(v)
    return result


def leafMostFrequentClass(matrix, u):
    yValues = frequencyDictionary(u)

    maxValue = max(yValues.values())
    for y in yValues:
        if yValues[y] == maxValue:
            return leafWithClass(matrix, y)


def leafWithClass(matrix, y):
    selectedData = []
    for row in matrix:
        if row[-1] == y:
            selectedData.append(row)
    return selectedData


# Y  set of classes which we try to find
# D set of attributes, we use them to define nodes in decision tree
# U set of pairs which teach an algorithm, U can't be empty
def id3(matrix, y, d, u):
    yCount = frequencyDictionary(u)

    for ySimple in y:
        if ySimple in yCount and yCount[ySimple] == len(u):
            return leafWithClass(matrix, ySimple)

    if len(d) == 0:
        return leafMostFrequentClass(matrix, u)


if __name__ == '__main__':
    Y = {"not_recom", "recommend", "very_recom", "priority", "spec_prior"}
    D = {"parents, has_nurs, form, children, housing, finance, social, health"}

    df = pd.read_csv('nursery.data')
    matrix = df.values

    print(matrix)