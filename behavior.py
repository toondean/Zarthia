class Behavior():
    def receiveCommand(self,command):
        playerCoordinates = self.game.getPlayerCoordinates()
        x = playerCoordinates[0]
        y = playerCoordinates[1]
        availableBehaviors = self.behaviors[x][y]
        if command in list(availableBehaviors.keys()):
            actionFunc = availableBehaviors[command]
            actionFunc()
        else:
            print('Unknown command, type "help" for list of commands')

    def applyNorthMovement(self, coords):
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.behaviors[x][y]['north'] = self.game.moveNorth

    def applyEastMovement(self, coords):
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.behaviors[x][y]['east'] = self.game.moveEast

    def applyWestMovement(self, coords):
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.behaviors[x][y]['west'] = self.game.moveWest

    def applySouthMovement(self, coords):
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.behaviors[x][y]['south'] = self.game.moveSouth

    def createStandardBehavior(self):
        return {
            "help":self.game.help
        }

    def createBehaviors(self):
        gridSize = self.game.getGridSize()
        # create a dictionary of behaviors for each game square (16 by 16)
        row = [self.createStandardBehavior() for i in range(gridSize['x'])]
        self.behaviors = [row for i in range(gridSize['y'])]
        self.applyNorthMovement([[0,15]])
        self.applyEastMovement([[0,2], [1,2]])
        self.applySouthMovement([[0,2], [1,2]])
        self.applyWestMovement([[0,2], [1,2]])

    def __init__(self,game):
        self.game = game
        self.createBehaviors()
