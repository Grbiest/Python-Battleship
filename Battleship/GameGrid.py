# Both the hidden and visible game boards, formatting them in an easily readable string.

from PlayerGrid import PlayerGrid

class GameGrid():


    def __init__(self, isHuman=True) -> None:
        self.yourGrid = PlayerGrid(hiddenGrid=True)
        self.myGrid = PlayerGrid(hiddenGrid=False)

#   Wiping both boards clean.    
    def clearBothBoards(self):
        self.yourGrid.clearAllBoards()
        self.myGrid.clearAllBoards()
        print("Clearing both boards")

    def __str__(self) -> str:
        return ("Opponent's Grid:\n" + self.yourGrid.__str__() + "\nHuman's Grid:\n" + self.myGrid.__str__())