class ScoreBoard:

    def __init__(self) -> None:
        self.cpuScore = 0
        self.humanScore = 0
        pass

    def __str__(self) -> str:
        return("------CPU: " + str(self.cpuScore) + "--Human:" + str(self.humanScore) + "------")