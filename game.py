from graphics import *
from player import *
from riddle import *
from behavior import *
class Game:
    def getGridSize(self):
        return {'x':16,'y':15}

    # INITAILIZATION
    ################
    def createGraphicsWindow(self):
        #create Graphics self.window
        self.win = GraphWin("ZARTHIA",800,850)
        self.win.setCoords(0,16,16,0)

    def createTitleScreen(self):
        #Creat title screen
        self.titleScreen = Image(Point(8,8),'images/Forest.png')
        #draw title screen
        self.titleScreen.draw(self.win)
        #load and draw title self.logo
        self.logo = Image(Point(8,3),'images/Title.png')
        self.logo.draw(self.win)

    def destroyTitleScreen(self):
        #Remove the title screen and self.logo
        self.titleScreen.undraw()
        self.logo.undraw()

    def newPlayer(self):
        playerName = input("Please Enter Your Name :")
        #create an object with the users name
        self.player = Player(playerName)
        #this is for testing !!!!!!
        print(self.player.user,"HEALTH: ",self.player.healthscore,"KEYS",self.player.key)

    def getPlayerCoordinates(self):
        x = int(self.characterPoint.x - 0.5)
        y = int(self.characterPoint.y)
        return [x,y]

    def createMap(self):
        #Create and Display the map
        image = Image(Point(8,8.5),'images/ZarthiaMapImage.png')
        image.draw(self.win)
        #This will be moved when we figure out how to use text boxes at top
        healthDisplay = Text(Point(14,1), self.player.healthscore)
        healthDisplay.draw(self.win)
        #draw the grid lines. REMOVE WHEN DONE?????
        for column in range (0,16,1):
            vLine=Line(Point(column,1),Point(column,16))
            vLine.draw(self.win)
        for row in range(0,16,1):
            hLine = Line(Point(0,row),Point(16,row))
            hLine.draw(self.win)
        # Make our self.character appear
        self.character = Image(Point(.5,14.5),'images/CharacterHero.png')
        # Make a point under self.character for use with getting the coordinatates
        #Image has no function to get coordinates
        self.characterPoint = Point(.5,14.5)
        #Use image for creating house, compass
        house = Image(Point(6.5,6.5),'images/HouseFinal.png')
        compass = Image(Point(1.5,2.5),'images/CompassFinal.png')
        #Draw all the picture objects
        compass.draw(self.win)
        house.draw(self.win)
        self.characterPoint.draw(self.win)
        self.character.draw(self.win)

    # DIRECTIONS
    ############
    def move(self,x,y):
        self.character.move(x,y)
        self.characterPoint.move(x,y)

    def moveEast(self):
        self.move(1,0)
        riddle(self.character,self.characterPoint,self.player)
        print(self.player.user,"HEALTH: ",self.player.healthscore,"KEYS",self.player.key)

    def moveNorth(self):
        self.move(0,-1)
        riddle(self.character,self.characterPoint,self.player)
        print(self.player.user,"HEALTH: ",self.player.healthscore,"KEYS",self.player.key)

    def moveWest(self):
        self.move(-1,0)
        riddle(self.character,self.characterPoint,self.player)
        print(self.player.user,"HEALTH: ",self.player.healthscore,"KEYS",self.player.key)

    def moveSouth(self):
        self.move(0,1)
        riddle(self.character,self.characterPoint,self.player)
        print(self.player.user,"HEALTH: ",self.player.healthscore,"KEYS",self.player.key)

    def invalidDirection(self):
        print("You hit an immovable object. You do not move.")

    # GAMEPLAY

    def play(self):
        print("Where would you like to go? Use n, e, s, w, :")
        #This will be used later to end the game
        self.game = True
        behavior = Behavior(self)
        #while the game is still being played do this loop
        while self.game == True:
            #get direction
            command = input("Enter Direction: ")
            behavior.receiveCommand(command)

    def reset(self):
        self.createGraphicsWindow()
        self.createTitleScreen()
        self.newPlayer()
        self.destroyTitleScreen()
        self.createMap()
        self.play()

    def help(self):
        print('Put help here')
