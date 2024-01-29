from GridLayer import GridLayer
from ShipGrid import ShipGrid
from HitGrid import HitGrid

class PlayerGrid():


    def __init__(self, hiddenGrid) -> None:
        super().__init__()
        self.hiddenGrid = hiddenGrid
        if not hiddenGrid:
            self.shipGrid = ShipGrid()
            self.hitGrid = HitGrid()
            self.printGrid = GridLayer()
        else:
            self.shipGrid = ShipGrid(hiddenGrid=True)
            self.hitGrid = HitGrid(hiddenGrid=True)
            self.printGrid = GridLayer(hiddenGrid=True)

    def contrastGrids(self):
        differenceList = []
        for space in self.shipGrid.gridDict:
            if self.shipGrid.gridDict[space] != self.shipGrid.gridDict[space]:
                differenceList.append(space)
        return differenceList
    
    def checkIfSpaceEmptyInBothGrids(self, space):
        isEmpty = True
        if self.shipGrid.gridDict[space] != "empty" or self.hitGrid.gridDict[space] != "empty":
            isEmpty = False
        return isEmpty
    
    def checkIfSpaceBlankInBothGrids(self, space):
        isBlank = True
        if not self.checkIfSpaceEmptyInBothGrids(space) or self.hitGrid.gridDict[space] != "shipHidden":
            isBlank = False
        return isBlank

    def attack(self, space, hiddenGrid):
        if space not in self.shipGrid.gridListSingle:
            return "invalid move"
        if self.checkIfSpaceEmptyInBothGrids(space):
            self.hitGrid.miss(space)
            return "miss"
        elif self.shipGrid.detectShipSpace(space) and self.hitGrid.gridDict[space] == "empty":
            self.hitGrid.hit(space)
            return self.hitShips(space, hiddenGrid)
        else:
            return "invalid move"
    
    def transferHit(self, space, hiddenGrid):
        if hiddenGrid:
            self.shipGrid.gridDict[space] = "hit"
        else:
            self.shipGrid.gridDict[space] = "shipHit"
    
    def hitShips(self, space, hiddenGrid):
        hiddenGrid = self.hiddenGrid
        for ship in self.shipGrid.shipList:
            for location in ship.shipLocation:
                if space == location:
                    self.transferHit(space, hiddenGrid)
                    ship.shipHealth -= 1
                    if ship.shipHealth == 0:
                        print("Ship sunk!")
                        removeShip = self.shipGrid.removeShip(ship)
                        return removeShip
#   Clearing all boards
    def clearAllBoards(self):
        self.shipGrid.clearBoard()
        self.hitGrid.clearBoard()
        self.printGrid.clearBoard()

    def __str__(self) -> str:

#       Reset print grid        
        for space in self.printGrid.gridDict:
            self.printGrid.gridDict[space] = 'empty'

#       Populate print grid with non-empty spaces
        nonEmptyDict = {}
        for space in self.hitGrid.gridDict:
            spaceState = self.hitGrid.gridDict[space]
            if spaceState != "empty":
                nonEmptyDict[space] = spaceState
        for space in self.shipGrid.gridDict:
            if self.shipGrid.gridDict[space] != "empty":
                nonEmptyDict[space] = self.shipGrid.gridDict[space]
        for space in nonEmptyDict:
            self.printGrid.gridDict[space] = nonEmptyDict[space]
        return self.printGrid.__str__()