# The base layer for every grid. GridLayers are meant to be stacked and compared.

import numpy as np
import random

class GridLayer:
    
    numbersList = list(range(1,11))

    def __init__(self, hiddenGrid=False) -> None:
        #    Creating the grid list and matrix
        self.lettersList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

        self.gridList = []
        for number in self.numbersList:
            number = str(number)
            gridRow = []
            for letter in self.lettersList:
                gridRow.append(letter + number)
            self.gridList.append(gridRow)
        self.gridMatrix = np.array(self.gridList)
        
    #   Creating the grid dictionary
        self.spaceStatesDict = {"empty":" ", "selected":"#", "miss":"O", "hit":"X", "ship":"=", "shipHit":"≠", "shipHidden":" ",}
        self.gridListSingle = []
        for list in self.gridList:
            for AbcNum in list:
                self.gridListSingle.append(AbcNum)
        self.gridDict = {}
        for space in self.gridListSingle:
            self.gridDict[space] = "empty"
        self.validDirections = ["North", "South", "East", "West"]


#   Translating Xy coordinates([x,y]) into letter-number labels('xy') and vice versa
    def getXyFromAbcNum(self, AbcNum):
        return list(np.argwhere(self.gridMatrix == AbcNum)[0])

    def getAbcNumFromXy(self, xy):
        return self.gridMatrix[xy[0],xy[1]]

    def forceSpaceXY(self, space):
        if space in self.gridListSingle:
            return self.getXyFromAbcNum(space)
        else:
            return space
    
    def forceSpaceAbcNum(self, space):
        if space in self.gridListSingle:
            return space
        else:
            return self.getAbcNumFromXy(space)

#   Setting the state of the space(from spaceStatesDict)
    def setSpaceState(self, AbcNum, state):
        self.gridDict[AbcNum] = state


#   Getting a list of letter-number labels in any of 4 directions(from validDirections)
    def getSpacesLeft(self, space, distance):
        space = self.forceSpaceXY(space)
        try:
            if len(self.gridMatrix[(space[0] - distance):(space[0]), space[1]]) > 0:
                return self.gridMatrix[(space[0] - distance):(space[0]), space[1]]
            else:
                return []
        except IndexError:
            pass
        
    def getSpacesRight(self, space, distance):
        space = self.forceSpaceXY(space)
        if (space[0] + distance + 1) > len(self.lettersList):
            pass
        else:
            return self.gridMatrix[(space[0] + 1):(space[0] + distance + 1), space[1]]

    def getSpacesAbove(self, space, distance):
        space = self.forceSpaceXY(space)
        try:
            if len(self.gridMatrix[space[0], (space[1] - distance):space[1]]) > 0:
                return self.gridMatrix[space[0], (space[1] - distance):space[1]]
            else:
                return []
        except IndexError:
            return []

    def getSpacesBelow(self, space, distance):
        space = self.forceSpaceXY(space)
        if (space[1] + distance + 1) > len(self.numbersList):
            pass
        else:
            return self.gridMatrix[space[0], (space[1] + 1):(space[1] + distance + 1)]
    
    def getSpacesSide(self, space, distance, direction):
        if direction == self.validDirections[0]:
            return self.getSpacesAbove(space, distance)
        elif direction == self.validDirections[1]:
            return self.getSpacesBelow(space, distance)
        elif direction == self.validDirections[2]:
            return self.getSpacesLeft(space, distance)
        elif direction == self.validDirections[3]:
            return self.getSpacesRight(space, distance)

#   Getting spaces in a line, or a random line
    def getSpacesLine(self, space, distance, direction):
        spaceList = [space]
        for space in self.getSpacesSide(space, (distance - 1), direction):
            spaceList.append(space)
        return spaceList

    def getRandomSpacesLine(self, distance):
        space = random.choice(self.gridListSingle)
        direction = random.choice(self.validDirections)
        try:
            return self.getSpacesLine(space, distance, direction)
        except TypeError:
            return []        
        
#   Getting a cross of spaces of certain length around the space, including the first space
    def getSpacesCross(self, space, distance):
        space = self.forceSpaceXY(space)
        spacesList = [self.getAbcNumFromXy(space)]
        directionsList = []
        distance -= 1

        for item in self.getSpacesAbove(space, (distance)):
            spacesList.append(item)
        if len(self.getSpacesAbove(space, (distance))) > 0:
            directionsList.append(self.validDirections[0])
        for item in self.getSpacesBelow(space, (distance)):
            spacesList.append(item)
        if len(self.getSpacesBelow(space, (distance))) > 0:
            directionsList.append(self.validDirections[1])
        for item in self.getSpacesLeft(space, (distance)):
            spacesList.append(item)
        if len(self.getSpacesLeft(space, (distance))) > 0:
            directionsList.append(self.validDirections[2])
        for item in self.getSpacesRight(space, (distance)):
            spacesList.append(item)
        if len(self.getSpacesRight(space, (distance))) > 0:
            directionsList.append(self.validDirections[3])

        returnList = [spacesList, directionsList]
        return returnList        

#   Clear entire board
    def clearBoard(self):
        for space in self.gridListSingle:
            self.gridDict[space] = "empty"  

#   Showing the user the selected spaces
    def flashSelection(self, spaces):
        originalGrid = self.gridDict.copy()
        for space in spaces:
            self.gridDict[space] = "selected"
        print(self)
        self.gridDict = originalGrid
        pass

    def flashCross(self, space, distance):
        self.flashSelection(self.getSpacesCross(space, distance)[0])

#   Sorting list for printing
    def split_list(self, lst, chunk_size):
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

    def fullySortAbcNumList(self, listToSort, chunks):
        listByChunks = int((len(listToSort) / chunks ))
        splitByTen = self.split_list(listToSort, listByChunks)
        sortedList = []
        for subList in splitByTen:
            indexDict = {}
            for item in subList:
                indexDict[item] = int(item[1:])
            marklist = sorted(indexDict.items(), key=lambda x:x[1])
            sortdict = dict(marklist)
            for key in sortdict.keys():
                sortedList.append(key)
        return sortedList

    def __str__(self) -> str:
        gridPrintList = ["  "]
        spacesToGo = self.gridListSingle.copy()
        spacesToGo.sort()
        spacesToGo = self.fullySortAbcNumList(spacesToGo, len(self.lettersList))
        for number in self.numbersList:
            gridPrintList.append(" " + str(number) + " ")
        gridPrintList.append("\n")
        for letter in self.lettersList:
            gridPrintList.append(letter + " ")
            for number in self.numbersList:
                gridPrintList.append("[" + self.spaceStatesDict[self.gridDict[spacesToGo[0]]] + "]")
                spacesToGo.pop(0)
            gridPrintList.append("\n")
        gridPrintString = "".join(gridPrintList)
        return gridPrintString