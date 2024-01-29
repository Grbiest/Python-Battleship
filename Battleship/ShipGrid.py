from GridLayer import GridLayer
from Ship import Ship

class ShipGrid(GridLayer):


  

    def __init__(self, hiddenGrid=False) -> None:
        super().__init__()
#       A different instance of Ship for each ship 
        self.carrier = Ship("Carrier")
        self.battleship = Ship("Battleship")
        self.cruiser = Ship("Cruiser")
        self.submarine = Ship("Submarine")
        self.destroyer = Ship("Destroyer")
        self.shipList = [self.carrier, self.battleship, self.cruiser, self.submarine, self.destroyer]
        self.shipListStr = [self.carrier.__str__(), self.battleship.__str__(), self.cruiser.__str__(), self.submarine.__str__(), self.destroyer.__str__()]

        self.hiddenGrid = hiddenGrid
        self.shipInventory = self.carrier.shipDict.copy()
        self.shipLocations = {}
        self.shipsAreAlive = True 

    def getShipFromType(self, shipType):
        for ship in self.shipList:
            if ship.shipType == shipType:
                return ship

    def checkForShipPlacement(self, shipType, space):
        shipLength = self.carrier.shipDict[shipType]
        shipCross = self.getSpacesCross(space, shipLength)
        for space in shipCross:
            if self.gridDict[space] != "empty":
                shipCross.pop(space)
        if len(shipCross) == (1 + 4 * (shipLength - 1)):
            return True
        else:
            return False
        pass

    def placeShip(self, spacesList, shipType, isHuman=True):
        self.shipLocations[shipType] = spacesList
        shipInstance = self.getShipFromType(shipType)
        shipInstance.shipLocation = spacesList
        for space in spacesList:
            if isHuman:
                self.gridDict[space] = "ship"
            else:
                self.gridDict[space] = "shipHidden"
        
        pass

    def removeShip(self, ship=Ship):
        ship.isSunk = True
        self.shipListStr.remove(ship.shipType)
        if len(self.shipListStr) == 0:
            return "Fleet annihilated."
        else:
            return self.shipListStr

    def damageShip(self, ship=Ship):
        pass
        

    def detectShipSpace(self, space):
        if self.gridDict[space] == "ship" or self.gridDict[space] == "shipHidden":
            return True
        else:
            return False
    
    def armadaHealthCheck(self):
        if len(self.currentShips) == 0:
            self.shipsAreAlive = False
        return self.currentShips 