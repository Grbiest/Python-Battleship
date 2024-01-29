# This is where I test random code.

import numpy as np

# array = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8],
#                   [9, 10, 11, 12]])

# solutions = np.argwhere(array == 2)
# print(solutions)
# print(array[(2 - 2):2, 2])

def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 5
chunks = split_list(numbers, chunk_size)


testList = ["a1", "a10", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "b1", "b10", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"]

listByTen = (len(testList) / 10 )
splitByTen = split_list(testList, 10)
print(testList)


sortedList = []
for subList in splitByTen:
    indexDict = {}
    for item in subList:
        indexDict[item] = int(item[1:])
    marklist = sorted(indexDict.items(), key=lambda x:x[1])
    sortdict = dict(marklist)
    for key in sortdict.keys():
        sortedList.append(key)
print(sortedList)