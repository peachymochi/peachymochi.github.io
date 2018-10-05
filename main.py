"""
A simple story about Gordon Ramsay desiring an omellete.
Colorama is required for the full visual appeal of the game ("pip install colorama")
Simply type a response to play! You'll have to conform the the availible options though.
CREDITS: Grace Pak, Gavin Ceballos
"""



import time
from colorama import Fore, Back, Style, init

#For Colorama
init()

#Game is not ending until this value is True.
gameExit = False

while gameExit == True:
    break

def firstChoice():
    print("You are" + Fore.RED, Style.BRIGHT + "Gordon Ramsay" + Style.RESET_ALL +", and on this particular day you are craving an omellete.")
    print("You get out of bed, excited for the ensuing eggselence, only to find that you have no" + Fore.YELLOW, Style.BRIGHT + "eggs" + Style.RESET_ALL + " in the fridge.")
    print("This means that you will have to make the trip out to one of two grocery stores.")
    print(Fore.MAGENTA, Style.BRIGHT + "The Value Grocery" + Style.RESET_ALL + " store lies at the end of a forest with a lava floor.")
    print(Fore.CYAN, Style.BRIGHT + "The Premium Grocery" + Style.RESET_ALL + " store is accessible through a large waterside outside your house.")
    print("Both of these grocery stores have the eggs for your omellete.")
    choice = input("Which grocery store do you want to get the eggs from? (" + Fore.MAGENTA + "Value" + Style.RESET_ALL + " or " + Fore.CYAN + "Premium" + Style.RESET_ALL + "): ")
    
    if choice == "Value" or choice == "value":  #See "Value Route"
        lavaMonkey()
    elif choice == "Premium" or choice == "premium":    #See "Premium Route"
        waterSlide()
    else:   #Returns bad input
        print(Fore.MAGENTA, Back.WHITE + "You look around, but do not see a store by that name." + Style.RESET_ALL)
        time.sleep(1)
        firstChoice()
"""
Value Market Route (Start: lavaMonkey())
"""
def lavaMonkey():
    print("While staying away from the lava isn't particularly difficult, a " + Fore.BLACK + Back.RED + "lava monkey" + Style.RESET_ALL + " stands in the way between you and the eggs you seek.")
    print("Being the fantastic chef you are, you always carry a set of utensils with you at all times.")
    print("In order to get past the monkey, you consider using either the " + Fore.CYAN +  "Spoon" + Style.RESET_ALL + " or the " + Fore.RED + "Fork" + Style.RESET_ALL + " as a weapon.")
    weapon = input(Fore.CYAN + "Spoon" + Style.RESET_ALL +" or " + Fore.RED + "Fork?" + " " + Style.RESET_ALL)
    if weapon == "Spoon" or weapon == "spoon": #Lose choice
        loseSpoon()
    elif weapon == "Fork" or weapon == "fork": #Win choice
        fightGrandma()
    else:   #Returns bad input
        print(Fore.MAGENTA, Back.WHITE + "That is not a Fork or a Spoon." + Style.RESET_ALL)
        time.sleep(1)
        lavaMonkey()

#Lose Spoon
def loseSpoon():
    print("The monkey deftly slaps the spoon out of your hand.")
    print("You are sad, but the spoon wouldn't have done much anyways.")
    print("Weaponless and" + Fore.YELLOW, Style.BRIGHT + "eggless" + Style.RESET_ALL + ", you return home hungry.")
    print(Fore.RED, Back.WHITE, Style.BRIGHT + "You Lose!" + Style.RESET_ALL)
    exit = input("Do you wish to exit the game? (" + Fore.GREEN + "Yes" + Style.RESET_ALL + " or " + Fore.RED + "No" + Style.RESET_ALL + "): ")
    if exit == "Yes" or exit == "yes":
        gameExit = True
        return gameExit
    elif exit == "No" or exit == "no": #HOLD
        print ("Fine, then you can sit here.")
        input()
    else:   #Returns bad input    
        print(Fore.MAGENTA, Back.WHITE + "I'm going to assume that means you want to leave." + Style.RESET_ALL)
        time.sleep(3)
        gameExit = True
        return gameExit
        
#Win Spoon
def fightGrandma():
    print("The lava monkey does not like being poked, and he returns to his treetop home opening the way forward.")
    print("You make it inside the Value Grocery store, but by the time you make it to the eggs, a normal grocery store grandma has taken the " + Fore.GREEN + "last" + Style.RESET_ALL + " dozen!")
    print("You " + Fore.RED + "REALLY" + Style.RESET_ALL + " want that omellete, but would you fight a grandma for it?")
    fight = input("(" + Fore.GREEN + "Yes" + Style.RESET_ALL + " or " + Fore.RED + "No" + Style.RESET_ALL + "): ")
    if fight == "Yes" or fight == "yes": #Win Choice
        valueEggs()
    elif fight == "No" or fight == "no": #Lose Choice
        loseGrandma()
    else:   #Returns bad input
        print(Fore.MAGENTA, Back.WHITE + "Please answer either Yes or No or you cannot go on." + Style.RESET_ALL)
        time.sleep(1)
        fightGrandma()

#Lose Grandma 
def loseGrandma():
    print("Although it is tempting to snatch the eggs away from grandma, you decide to let her keep the eggs.")
    print("The Grandma notices your sad face and gives you a lolipop for letting her keep the eggs.")
    print("With a lolipop in your hand, you return to your eggsless home.")
    print(Fore.RED, Back.WHITE, Style.BRIGHT + "You Lose!" + Style.RESET_ALL)
    exit = input("Do you wish to exit the game? (" + Fore.GREEN + "Yes" + Style.RESET_ALL + " or " + Fore.RED + "No" + Style.RESET_ALL + "): ")
    if exit == "Yes" or exit == "yes":
        gameExit = True
        return gameExit
    elif exit == "No" or exit == "no": #HOLD
        print ("Fine, then you can sit here.")
        input()
    else:   #Returns bad input    
        print(Fore.MAGENTA, Back.WHITE + "I'm going to assume that means you want to leave." + Style.RESET_ALL)
        time.sleep(3)
        gameExit = True
        return gameExit

#Win Grandma
def valueEggs():
    print("The grandma puts up a tough fight, but you manage to wrangle the eggs away from her.")
    print("You " + Fore.RED +  "(Gordon Ramsay)" + Style.RESET_ALL + " have successfully aquired eggs from the Value Market and have made yourself a delicious omellete!")
    print("Since you fought a grandma for eggs in a grocery store, I'm unsure you can call this a moral victory, but you won either way.")
    print(Fore.GREEN, Back.WHITE, Style.BRIGHT + "You Win!" + Style.RESET_ALL)
    exit = input("Do you wish to exit the game? (" + Fore.GREEN + "Yes" + Style.RESET_ALL + " or " + Fore.RED + "No" + Style.RESET_ALL + "): ")
    if exit == "Yes" or exit == "yes":
        gameExit = True
        return gameExit
    elif exit == "No" or exit == "no": #HOLD
        print ("Fine, then you can sit here.")
        input()
    else:   #Returns bad input    
        print(Fore.MAGENTA, Back.WHITE + "I'm going to assume that means you want to leave." + Style.RESET_ALL)
        time.sleep(3)
        gameExit = True
        return gameExit

"""
Premium Market Route (Start: waterSlide())
"""
def waterSlide():
    print("You approach the waterslide, expecting a quick journey, only to find that it is completely dry!")
    print("Being the fantastic chef you are, You are carrying a full stick of butter with you.")
    print("At this point you can either butter yourself up for the slide, or run down it barefoot (to avoid slipping).")
    slide = input(Fore.GREEN + "Butter" + Style.RESET_ALL + " or " + Fore.RED + "Run? " + Style.RESET_ALL)
    if slide == "Butter" or slide == "butter": #Win choice
        butter()
    elif slide == "Run" or slide == "run": #Lose Choice
        run()
    else:   #Returns bad input
        print(Fore.MAGENTA, Back.WHITE + "Gordon's inability to decide will get him nowhere!" + Style.RESET_ALL)
        time.sleep(1)
        waterSlide()

#Win Slide
def butter():
    print("You quickly whip out your stick of fresh " + Fore.YELLOW + "butter " + Style.RESET_ALL + "and begin to cover yourself in a thick layer of butter.")
    print("Now that you're all buttered up, you get on the slide and start cruising down to the market.")
    print("You finally arrive to the Premium Market and grab the glorious eggs, BUT you realize you don't have enough money!")
    print("Would you steal the eggs for your precious omellete?")
    steal = input("Do you wish to steal the eggs? (" + Fore.GREEN + "Yes" + Style.RESET_ALL + " or " + Fore.RED + "No" + Style.RESET_ALL + "): ")
    if steal == "Yes" or steal == "yes": #Win Choice
        yesSteal()
    elif steal == "No" or steal == "no": #Lose Choice
        noSteal()
    else:   #Returns bad input
        print(Fore.MAGENTA, Back.WHITE + "Please say either Yes or No if you want to go on." + Style.RESET_ALL)
        time.sleep(1)
        butter()
        
#Lose Slide
def run():
    print("You take off your shoes in order to run down the hot, burning, plastic slide.")
    print("As you run down the slide, you're in agonizing pain because you burned you feet.")
    print("Suddenly the slide begins to work properly again and a gush of water begins to flow down the slide!")
    print("You slip and begin to enjoy the ride until the slide makes you miss the " + Fore.CYAN +  "Premium Grocery" + Style.RESET_ALL + " and you are separated from your precious" + Fore.YELLOW, Style.BRIGHT + "eggs." + Style.RESET_ALL)
    print(Fore.RED, Back.WHITE, Style.BRIGHT + "You Lose!" + Style.RESET_ALL)
    exit = input("Do you wish to exit the game? (" + Fore.GREEN + "Yes" + Style.RESET_ALL + " or " + Fore.RED + "No" + Style.RESET_ALL + "): ")
    if exit == "Yes" or exit == "yes":
        gameExit = True
        return gameExit
    elif exit == "No" or exit == "no": #HOLD
        print ("Fine, then you can sit here.")
        input()
    else:   #Returns bad input    
        print(Fore.MAGENTA, Back.WHITE + "I'm going to assume that means you want to leave." + Style.RESET_ALL)
        time.sleep(3)
        gameExit = True
        return gameExit

#Win Steal
def yesSteal():
    print("You look around aisle to see if anyone is around before carefully hiding the eggs under your jacket.")
    print("As you walk closer and closer to the exit, you dash immediately out of the store after one of your eggs fell on the floor!")
    print("The security guard begins chasing after you, but you manage to get away from him and safely return home.")
    print("Now that you have the eggs, you make the most delicious " + Fore.YELLOW + "omellete" + Style.RESET_ALL + " ever and enjoy your meal.")
    print(Fore.GREEN, Back.WHITE, Style.BRIGHT + "You Win!" + Style.RESET_ALL)
    exit = input("Do you wish to exit the game? (" + Fore.GREEN + "Yes" + Style.RESET_ALL + " or " + Fore.RED + "No" + Style.RESET_ALL + "): ")
    if exit == "Yes" or exit == "yes":
        gameExit = True
        return gameExit
    elif exit == "No" or exit == "no": #HOLD
        print ("Fine, then you can sit here.")
        input()
    else:   #Returns bad input    
        print(Fore.MAGENTA, Back.WHITE + "I'm going to assume that means you want to leave." + Style.RESET_ALL)
        time.sleep(3)
        gameExit = True
        return gameExit
    
#Lose Steal
def noSteal():
    print("You decide not to steal the eggs because it's the wrong thing to do and you don't want to go to jail.")
    print("You return to your eggless home and decide to just cook some omellete flavored cup noodles instead.")
    print(Fore.RED, Back.WHITE, Style.BRIGHT + "You Lose!" + Style.RESET_ALL)
    exit = input("Do you wish to exit the game? (" + Fore.GREEN + "Yes" + Style.RESET_ALL + " or " + Fore.RED + "No" + Style.RESET_ALL + "): ")
    if exit == "Yes" or exit == "yes":
        gameExit = True
        return gameExit
    elif exit == "No" or exit == "no": #HOLD
        print ("Fine, then you can sit here.")
        input()
    else:   #Returns bad input    
        print(Fore.MAGENTA, Back.WHITE + "I'm going to assume that means you want to leave." + Style.RESET_ALL)
        time.sleep(3)
        gameExit = True
        return gameExit
    
#Game is started by calling firstChoice()    
firstChoice()