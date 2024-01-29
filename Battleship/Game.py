from GameGrid import GameGrid
from Ship import Ship
from ScoreBoard import ScoreBoard
import random

class Game:
    humanPlayerGrid = GameGrid()
    shipyard = Ship()
    scoreboard = ScoreBoard()

    humanShipInventory = humanPlayerGrid.myGrid.shipGrid.shipInventory.copy()
    cpuShipInventory = humanPlayerGrid.yourGrid.shipGrid.shipInventory.copy()

    def __init__(self) -> None:
        pass


    def willYouPlayAgain(self):
        while True:
            playAgainPrompt = input("Would you like to play again? Y/N")
            if playAgainPrompt == "Y":
                return "Y"
            elif playAgainPrompt != "N":
                print("Sorry, I can't understand that, can you say it again please?")
                continue
            else:
                return "N"

    def gameReset(self):
        self.humanPlayerGrid.clearBothBoards()
        self.humanShipInventory = self.humanPlayerGrid.myGrid.shipGrid.shipInventory.copy()
        self.cpuShipInventory = self.humanPlayerGrid.yourGrid.shipGrid.shipInventory.copy()

    def playGame(self):
        print("Welcome to Battleship!\nFirst, place your ships. Then, guess where the opponent's ships are. First player to sink all of their opponent's ships wins!")
        self.gameReset()
        print(self.humanPlayerGrid)
        self.shipPlacementRound(randomEnabled=True)
        print(self.humanPlayerGrid)
        result = self.attackRound()
        return result

    def shipPlacementRound(self, randomEnabled=False):
        if randomEnabled:    
            while True:
                randomPrompt = input("Generate random ships? Y/N")
                if randomPrompt == "Y":
                    self.placeAllShipsTurn(isHuman=True, randomHuman=True)
                    self.placeAllShipsTurn(isHuman=False)
                    break
                elif randomPrompt == "N":
                    self.placeAllShipsTurn(isHuman=True)
                    self.placeAllShipsTurn(isHuman=False)
                    break
                else:
                    print("Not a valid answer, try again.")
                    continue

    def placeAllShipsTurn(self, isHuman, randomHuman=False):
        if isHuman:
            shipInventory = self.humanShipInventory
        else:
            print("CPU IS CHOOSING SHIPS.")
            shipInventory = self.cpuShipInventory
        while len(shipInventory) > 0:
            if isHuman:
                if randomHuman:
                    self.placeShipTurn(isHuman=True, randomHuman=True)
                else:
                    self.placeShipTurn(isHuman=True)
                    print(self.humanPlayerGrid.myGrid.shipGrid)
            else:
                self.placeShipTurn(isHuman=False)
                if len(shipInventory) == 0:
                    print("CPU HAS FINISHED CHOOSING SHIPS.")

    def placeShipTurn(self, isHuman, randomHuman=False):
        if isHuman:
            if randomHuman:
#               Human randomly selecting the ship
                selectedShip = random.choice(list(self.humanShipInventory.keys()))
#               Human placing the ship
                shipSpaces = self.getRandomShipSpaces(selectedShip, isHuman=True)
                self.humanPlayerGrid.myGrid.shipGrid.placeShip(shipSpaces, selectedShip, isHuman=True)
                self.humanShipInventory.pop(selectedShip)
                pass
            else:
    #           Selecting ship, location, and direction
                selectedShip = self.selectShip(isHuman)
                shipLength = self.shipyard.shipDict[selectedShip]
                shipStartingPosition = self.selectValidShipStartingPosition(isHuman, selectedShip)
                direction = self.selectValidShipDirection(isHuman, shipStartingPosition, selectedShip)
    #           Placing the ship
                shipSpaces = self.humanPlayerGrid.myGrid.shipGrid.getSpacesLine(space=shipStartingPosition, distance=shipLength, direction=direction)
                self.humanPlayerGrid.myGrid.shipGrid.placeShip(shipSpaces, selectedShip, True)
                print("Ship placed.")
        else:
#           CPU randomly selecting the ship
            selectedShip = random.choice(list(self.cpuShipInventory.keys()))
#           CPU placing the ship
            shipSpaces = self.getRandomShipSpaces(selectedShip, isHuman=False)
            self.humanPlayerGrid.yourGrid.shipGrid.placeShip(shipSpaces, selectedShip, isHuman=False)
            self.cpuShipInventory.pop(selectedShip)
                        



    def selectShip(self, isHuman):
        selectedShip = ""
        while True:
            if isHuman:
                shipAbbr = input("Which ship will you place? Ca(Carrier) Ba(Battleship) Cr(Cruiser) Su(Submarine) or De(Destroyer)?")
                if shipAbbr not in self.shipyard.shipAbbrDict.keys():
                    print("Abbreviation invalid. Please select another.")
                    continue
                else:
                    selectedShip = self.shipyard.shipAbbrDict[shipAbbr]
                    if selectedShip not in self.humanShipInventory:
                        print("You have already placed that ship. Please select another.")
                        print("Remaining ships:", list(self.humanShipInventory.keys()))
                    else:
                        self.humanShipInventory.pop(selectedShip)
                        break
            else:
                pass
        return selectedShip

    def selectValidShipStartingPosition(self, isHuman, _selectedShip):
        while True:
            if isHuman:
                print(self.humanPlayerGrid.myGrid.shipGrid)
                shipSpace = input("Please select the starting space you would like to place the ship.")
                if shipSpace not in self.humanPlayerGrid.myGrid.shipGrid.gridListSingle:
                    print("Sorry, {} is not a coordinate on this grid. Please try again.".format(shipSpace))
                    continue
                elif not self.humanPlayerGrid.myGrid.checkIfSpaceEmptyInBothGrids(shipSpace):
                    print("Sorry, {} is not empty. Please try again.".format(shipSpace))
                    continue
                else:
                    break
            else:
                pass
        return shipSpace

    def selectValidShipDirection(self, isHuman, AbcNum, selectedShip):
        print(self.shipyard.shipDict)
        shipLength = self.shipyard.shipDict[selectedShip]
        self.humanPlayerGrid.myGrid.shipGrid.gridDict[AbcNum] = "selected"
        while True:
            if isHuman:
                print(self.humanPlayerGrid.myGrid.shipGrid)
                chosenDirection = input("Please select one of the four cardinal directions to place your ship: North, South, East, or West.")
                if chosenDirection not in self.humanPlayerGrid.myGrid.shipGrid.getSpacesCross(space=AbcNum, distance=shipLength)[1]:
                    print("Invalid direction. Please select another.")
                    continue
                else:
                    break
            else:
                pass
        return chosenDirection
    
    def getRandomShipSpaces(self, shipType, isHuman):
        shipLength = self.shipyard.shipDict[shipType]
        shipSpaces = []
        while True:
            shipSpaces = self.humanPlayerGrid.yourGrid.shipGrid.getRandomSpacesLine(shipLength)
            if len(shipSpaces) != shipLength:
                continue
            else:
                validPlacement = True
                for space in shipSpaces:
                    if isHuman:
                        if not self.humanPlayerGrid.myGrid.checkIfSpaceEmptyInBothGrids(space):
                            validPlacement = False
                    else:
                        if not self.humanPlayerGrid.yourGrid.checkIfSpaceEmptyInBothGrids(space):
                            validPlacement = False
                if not validPlacement:
                    continue
                else:
                    return shipSpaces
    
    def attackRound(self):
        while True:
            humanAttack = self.attackTurn(isHuman=True)
            if humanAttack == "Turn finished.":
                cpuAttack = self.attackTurn(isHuman=False)
                if cpuAttack == "Turn finished.":
                    continue
                else:
                    print("CPU Victory!")
                    return ("CPU Victory")
            else:
                print("Congratulations! You've won!")
                return("Player Victory")
            

    def attackTurn(self, isHuman, wrangleOverride=True):
        if isHuman:
            while True:
                chosenAttack = input("Select a space to fire upon!")
                attackResult = self.humanPlayerGrid.yourGrid.attack(chosenAttack, hiddenGrid=True)
                if attackResult == "invalid move":
                    print(chosenAttack + " is an invalid move. Please select another space.")
                    continue
                else:
                    print(self.humanPlayerGrid.yourGrid.hitGrid.gridDict[chosenAttack])
                    if attackResult == "Fleet annihilated.":
                        return "Player victory"
                    else:
                        print(self.humanPlayerGrid)
                        return "Turn finished."
        else:
            while True:
                if wrangleOverride:
                    chosenAttack = input("Input CPU move")
                else:
                    chosenAttack = random.choice(self.humanPlayerGrid.myGrid.shipGrid.gridListSingle)
                attackResult = self.humanPlayerGrid.myGrid.attack(chosenAttack, hiddenGrid=False)
                if attackResult == "invalid move":
                    continue
                else:
                    print("CPU ATTACKING AT", chosenAttack)
                    print(self.humanPlayerGrid.myGrid.hitGrid.gridDict[chosenAttack])
                    if attackResult == "Fleet annihilated.":
                        return "CPU victory"
                    else:
                        print(self.humanPlayerGrid)
                        return "Turn finished."

                
            
