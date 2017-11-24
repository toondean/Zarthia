from graphics import *
from player import *
from riddle import *

class Game:
    def moveEast(self):
        character.move(1,0)
        characterPoint.move(1,0)
        riddle(character,characterPoint,playerName)
        print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)

    def moveNorth(self):
        character.move(0,-1)
        characterPoint.move(0,-1)
        riddle(character,characterPoint,playerName)
        print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)

    def moveWest(self):
        character.move(-1,0)
        characterPoint.move(-1,0)
        riddle(character,characterPoint,playerName)
        print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)

    def moveSouth(self):
        character.move(0,1)
        characterPoint.move(0,1)
        riddle(character,characterPoint,playerName)
        print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)

    def invalidDirection(self):
        print("Please enter a valid direction!")

    def createGraphicsWindow(self):
        #create Graphics self.window
        self.win = GraphWin("ZARTHIA",800,850)
        self.win.setCoords(0,16,16,0)

    def createTitleScreen(self):
        #Creat title screen
        self.titleScreena = Image(Point(8,8),'images/Forest.png')
        #draw title screen
        self.titleScreen.draw(self.win)
        #load and draw title logo
        logo = Image(Point(8,3),'images/Title.png')
        logo.draw(self.win)
    def destroyTitleScreen(self):
        #Remove the title screen and logo
        self.titleScreen.undraw()
        logo.undraw()

    def newPlayer(self):
        playerName = input("Please Enter Your Name :")
        #create an object with the users name
        playerName = Player(playerName)
        #this is for testing !!!!!!
        print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)

    def createMap(self):
        #Create and Display the map
        image = Image(Point(8,8.5),'images/ZarthiaMapImage.png')
        image.draw(self.win)
        #This will be moved when we figure out how to use text boxes at top
        healthDisplay = Text(Point(14,1), playerName.healthscore)
        healthDisplay.draw(self.win)
        #draw the grid lines. REMOVE WHEN DONE?????
        for column in range (0,16,1):
            vLine=Line(Point(column,1),Point(column,16))
            vLine.draw(self.win)
        for row in range(0,16,1):
            hLine = Line(Point(0,row),Point(16,row))
            hLine.draw(self.win)
        # Make our character appear
        character = Image(Point(.5,14.5),'images/CharacterHero.png')
        # Make a point under character for use with getting the coordinatates
        #Image has no function to get coordinates
        characterPoint = Point(.5,14.5)
        #Use image for creating house, compass
        house = Image(Point(6.5,6.5),'images/HouseFinal.png')
        compass = Image(Point(1.5,2.5),'images/CompassFinal.png')
        #Draw all the picture objects
        compass.draw(self.win)
        house.draw(self.win)
        characterPoint.draw(self.win)
        character.draw(self.win)

    def play(self):
        # #create Graphics self.window
        # self.win = GraphWin("ZARTHIA",800,850)
        # self.win.setCoords(0,16,16,0)
        # #Creat title screen
        # self.titleScreen = Image(Point(8,8),'images/Forest.png')
        # #draw title screen
        # self.titleScreen.draw(self.win)
        # #load and draw title logo
        # logo = Image(Point(8,3),'images/Title.png')
        # logo.draw(self.win)
        # #ask for user NAME
        # playerName = input("Please Enter Your Name :")
        # #create an object with the users name
        # playerName = Player(playerName)
        # #this is for testing !!!!!!
        # print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)
        # #Remove the title screen and logo
        # self.titleScreen.undraw()
        # logo.undraw()
        # #Create and Display the map
        # image = Image(Point(8,8.5),'images/ZarthiaMapImage.png')
        # image.draw(self.win)
        # #This will be moved when we figure out how to use text boxes at top
        # healthDisplay = Text(Point(14,1), playerName.healthscore)
        # healthDisplay.draw(self.win)
        # #draw the grid lines. REMOVE WHEN DONE?????
        # for column in range (0,16,1):
        #     vLine=Line(Point(column,1),Point(column,16))
        #     vLine.draw(self.win)
        # for row in range(0,16,1):
        #     hLine = Line(Point(0,row),Point(16,row))
        #     hLine.draw(self.win)
        # # Make our character appear
        # character = Image(Point(.5,14.5),'images/CharacterHero.png')
        # # Make a point under character for use with getting the coordinatates
        # #Image has no function to get coordinates
        # characterPoint = Point(.5,14.5)
        # #Use image for creating house, compass
        # house = Image(Point(6.5,6.5),'images/HouseFinal.png')
        # compass = Image(Point(1.5,2.5),'images/CompassFinal.png')
        # #Draw all the picture objects
        # compass.draw(self.win)
        # house.draw(self.win)
        # characterPoint.draw(self.win)
        # character.draw(self.win)
        print("Where would you like to go? Use n, e, s, w, :")
        #define movement placholder
        movement = ''
        #This will be used later to end the game
        game = True
        #while the game is still being played do this loop
        while game == True:
            #get direction
            movement = input("Enter Direction: ")
            #elif statements to move player arround and
            #call the funtions
            if movement == "east":
                character.move(1,0)
                characterPoint.move(1,0)
                riddle(character,characterPoint,playerName)
                print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)
            elif movement == "north":
                character.move(0,-1)
                characterPoint.move(0,-1)
                riddle(character,characterPoint,playerName)
                print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)
            elif movement == "west":
                character.move(-1,0)
                characterPoint.move(-1,0)
                riddle(character,characterPoint,playerName)
                print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)
            elif movement == "south":
                character.move(0,1)
                characterPoint.move(0,1)
                riddle(character,characterPoint,playerName)
                print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)
            else:
                print("Please enter a valid direction!")

    def reset(self):
        self.createGraphicsWindow()
        self.createTitleScreen()
        self.newPlayer()
        self.destroyTitleScreen()
        self.createMap()
        self.play()
