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
