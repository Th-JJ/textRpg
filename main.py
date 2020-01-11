from characters.charBase import charBase
import os
import colored
from colored import stylize

def creatPlayer(charName, charMaxLife):
    player = charBase(charName, charMaxLife)
    return player
def credites():
    os.system('cls')
    print("CREATED BY TH")
    inp = input("Press Any key To Back: ")
    if inp != "":
        menu()
        os.system('cls')

def game():
    pname = input("Set Player Name: ")
    player = creatPlayer(pname, 100)
    
    while(player.dead == False):
        print("Player: " + player.name)
        print("HP: " + str(player.currentLife))
        print("-----------------------")
        inputAction = input("Action: ")
        if(inputAction != ""):
            print(inputAction)
        
        
  
def menu():
    os.system('cls')
    print(stylize('WELCOME THE ADVENTURE TEXT', colored.fg("green")))
    print("Press to:")
    print("[1] Play")
    print("[2] Credits")
    print("[3] OUT")
    print("-----------------------")
    inputMenu = input("Input: ")
    if inputMenu == '1':
        os.system('cls')
        game()
    elif inputMenu == '2':
        credites()
    elif inputMenu == '3':
        exit
menu()
    
    
    
    