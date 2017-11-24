#creating a "Map" library for the game board that will allow the player to move
#through out the map seamlessly
'''
Images Used
https://www.google.com/search?biw=1680&bih=920&tbm=isch&sa=1&ei=MYIUWsC7MMKQ0gL3sJa4DA&q=birds+eye+view+of+a+video+game+forest&oq=birds+eye+view+of+a+video+game+forest&gs_l=psy-ab.3...3222.6137.0.6486.11.11.0.0.0.0.58.500.11.11.0....0...1c.1.64.psy-ab..0.1.39...0.0.x4Rwwb4xXII#imgrc=CAgoy2SqS54O9M:
https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiVy7eYttHXAhWCslQKHW8_C0AQjRwIBw&url=http%3A%2F%2Fwww.tokkoro.com%2F398301-forest-background-hd.html&psig=AOvVaw1yrl2qqRqUs0TMSf1xhf-I&ust=1511398203146174
'''
#import Graphics library
from graphics import *
#define function


#define a class for the player
class player:
    def __init__(self,user):
        self.user = user
        self.healthscore = 5
        self.key = 0

    def hurtHealth(self):
        self.healthscore = self.healthscore - 1
        return self.healthscore

    def giveKey(self):
        self.key = self.key + 1
        return self.key

def riddle(character,characterPoint,playerName):
    #Get point of the character for location
    locationX = characterPoint.getX()
    locationY = characterPoint.getY()
    #if location is correct run the riddle
    if locationX == 3.5 and locationY == 4.5:
        answer = input("THIS IS AREA 1 type the number 1: ")
        if answer == "1":
            playerName.giveKey()
        else:
            playerName.hurtHealth()
    elif locationX == 4.5 and locationY == 6.5:
        answer = input("THIS IS AREA 2 type the number 2 : ")
        if answer == "2":
            playerName.giveKey()
        else:
            print("Wrong answer!")
            playerName.hurtHealth()
    elif locationX == 9.5 and locationY == 4.5:
        answer = input("THIS IS AREA 3 type the number 3: ")
        if answer == "3":
            playerName.giveKey()
        else:
            print("Wrong answer!")
            playerName.hurtHealth()
    elif locationX == 7.5 and locationY == 3.5:
        answer = input("THIS IS AREA 4 type the number 4: ")
        if answer == "4":
            playerName.giveKey()
        else:
            print("Wrong answer!")
            playerName.hurtHealth()
    elif locationX == 12.5 and locationY == 12.5:
        answer = input("THIS IS AREA 5 type the number 5: ")
        if answer == "5":
            playerName.giveKey()
        else:
            print("Wrong answer!")
            playerName.hurtHealth()
    elif locationX == 7.5 and locationY == 13.5:
        answer = input("THIS IS AREA 6 type the number 6: ")
        if answer == "6":
            playerName.giveKey()
        else:
            print("Wrong answer!")
            playerName.hurtHealth()
    elif locationX == 3.5 and locationY == 9.5:
        answer = input("THIS IS AREA 7 type the number 7: ")
        if answer == "7":
            playerName.giveKey()
        else:
            print("Wrong answer!")
            playerName.hurtHealth()
    elif locationX == 14.5 and locationY == 4.5:
        answer = input("THIS IS AREA 8 type the number 8: ")
        if answer == "8":
            playerName.giveKey()
        else:
            print("Wrong answer!")
            playerName.hurtHealth()
    elif locationX == 1.5 and locationY == 8.5:
        answer = input("THIS IS AREA 9 type the number 9: ")
        if answer == "9":
            playerName.giveKey()
        else:
            print("Wrong answer!")
            playerName.hurtHealth()
    elif locationX == 7.5 and locationY == 11.5:
        answer = input("THIS IS AREA 10 type the number 10: ")
        if answer == "10":
            playerName.giveKey()
        else:
            print("Wrong answer!")
            playerName.hurtHealth()

    return playerName

        


def map():
    #create Graphics window
    win = GraphWin("ZARTHIA",800,850)
    win.setCoords(0,16,16,0)
    #Creat title screen
    titleScreen = Image(Point(8,8),'Forest.png')
    #draw title screen
    titleScreen.draw(win)
    #load and draw title logo
    logo = Image(Point(8,3),'Title.png')
    logo.draw(win)
    #ask for user NAME
    playerName = input("Please Enter Your Name :")
    #create an object with the users name
    playerName = player(playerName)
    #this is for testing !!!!!!
    print(playerName.user,"HEALTH: ",playerName.healthscore,"KEYS",playerName.key)
    #Remove the title screen and logo
    titleScreen.undraw()
    logo.undraw()
    #Create and Display the map
    image = Image(Point(8,8.5),'ZarthiaMapImage.png')
    image.draw(win)
    #This will be moved when we figure out how to use text boxes at top
    healthDisplay = Text(Point(14,1), playerName.healthscore)
    healthDisplay.draw(win)
    #draw the grid lines. REMOVE WHEN DONE?????
    for column in range (0,16,1):
        vLine=Line(Point(column,1),Point(column,16))
        vLine.draw(win)
    for row in range(0,16,1):
        hLine = Line(Point(0,row),Point(16,row))
        hLine.draw(win)
    # Make our character appear
    character = Image(Point(.5,14.5),'CharacterHero.png')
    # Make a point under character for use with getting the coordinatates
    #Image has no function to get coordinates
    characterPoint = Point(.5,14.5)
    #Use image for creating house, compass
    house = Image(Point(6.5,6.5),'HouseFinal.png')
    compass = Image(Point(1.5,2.5),'CompassFinal.png')
    #Draw all the picture objects
    compass.draw(win)
    house.draw(win)
    characterPoint.draw(win)
    character.draw(win)
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

map()



    
                
    
