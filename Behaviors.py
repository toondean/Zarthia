class MapGridBehavior():
   def __init__(self,game):
       self.game = game
       self.gridBehaviors = []
        createBehavior(0,2,{"south":game.moveSouth, "north":game.invalidDirection})

    def createBehavior(self):
