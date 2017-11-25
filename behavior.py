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
            if command in ['north','east','west','south']:
                # the direction wasn't an applied behavior
                self.game.invalidDirection()
            else:
                # the command didn't match any behavior
                print('Unknown command, type "help" for list of commands')

    def north(self):
        return {'north':self.game.moveNorth}
    def east(self):
        return {'east':self.game.moveEast}
    def west(self):
        return {'west':self.game.moveWest}
    def south(self):
        return {'south':self.game.moveSouth}
    def help(self):
        return {"help":self.game.help}
    def keyNotFound(self):
        return {"get key":self.game.keyNotFound}
    def keyFound(self):
        return {"get key":self.game.keyFound}

    def createStandardBehavior(self):
        # create a standard set of
        standardBehavior = {}
        standardBehavior.update(self.help())
        standardBehavior.update(self.keyNotFound())
        return standardBehavior

    def createBehaviors(self):
        # create a dictionary of behaviors for each game square (16 by 16)
        gridSize = self.game.getGridSize()
        row = [self.createStandardBehavior() for i in range(gridSize['x'])]
        self.behaviors = [row for i in range(gridSize['y'])]

    def applyBehaviorsToCoords(self,x,y,behaviorsToApply):
        for behavior in behaviorsToApply:
            {**self.behaviors[x][y], **behavior()}

    def applyBehaviors(self):
        north = self.north
        east = self.east
        west = self.west
        south = self.south
        self.applyBehaviorsToCoords(0,14,[north,east,west,south])

        # this applies full movement to the first 5 square of the top row
        self.applyBehaviorsToCoords(0,0,[north,east,west,south])
        self.applyBehaviorsToCoords(0,1,[north,east,west,south])
        self.applyBehaviorsToCoords(0,2,[north,east,west,south])
        self.applyBehaviorsToCoords(0,3,[north,east,west,south])
        self.applyBehaviorsToCoords(0,4,[north,east,west,south])
        self.applyBehaviorsToCoords(14,0,[north,east,west,south])
        self.applyBehaviorsToCoords(14,1,[north,east,west,south])
        self.applyBehaviorsToCoords(14,2,[north,east,west,south])
        self.applyBehaviorsToCoords(14,3,[north,east,west,south])
        self.applyBehaviorsToCoords(14,4,[north,east,west,south])

    def __init__(self,game):
        self.game = game
        self.createBehaviors()
        self.applyBehaviors()
        print(game.getPlayerCoordinates())
