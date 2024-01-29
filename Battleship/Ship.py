class Ship:
    shipDict = {"Carrier": 5, "Battleship": 4, "Cruiser" : 3, "Submarine": 3, "Destroyer": 2}
    shipAbbrDict = {'Ca':"Carrier", "Ba":"Battleship", "Cr":"Cruiser", "Su":"Submarine", "De":"Destroyer"}
    shipType = ""
    shipHealth = 0
    shipLocation = []
    isSunk = False
    def __init__(self, type="Carrier") -> None:
        self.shipType = type
        self.shipHealth = self.shipDict[type]
        self.shipLocation = []
        pass
    
    def __str__(self) -> str:
        return self.shipType

