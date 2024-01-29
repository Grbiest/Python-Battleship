from GridLayer import GridLayer

class HitGrid(GridLayer):
    
    def __init__(self, hiddenGrid=False) -> None:
        self.hiddenGrid=hiddenGrid
        super().__init__()

    def miss(self, space):
        self.gridDict[space] = "miss"
    
    def hit(self, space):
        self.gridDict[space] = "hit"