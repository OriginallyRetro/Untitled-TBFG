
import os, random, time, sys

###Entry Point
global userName
userName = input("Please enter your name: ")
os.system("cls")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def fast_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

def afterMath_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)


global attack_buff, health_buff, fire_level_buff, water_level_buff, Xp, healthPotion, attackPotions, Experience, storyExperience, starting_point

attack_buff = 0
health_buff = 0
Xp = 0
healthPotion = 0
attackPotions = 0

itemsPossiblyGained = (healthPotion, attackPotions)



#This was to see if a person had compelted a part of the game if so it would skip some things.
global story_point, victories
Experience = 0
storyExperience = 0
story_point = 0
victories = 0

#Create 1 little mini boss of each element. Then create 3 little dungeon elemental mages

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
class defaultCharacter:
    def __init__(player, name, Xp: int, level: int, attack: int, health: int, defense: int, light_level: int, startingFight: int, victories: int, xp: int) -> None:
        player.name = name
        player.Xp = Xp
        player.level = level
        player.attack = attack
        player.health = health
        player.defense = defense
        player.light_level = light_level
        player.startingFight = startingFight
        player.victories = victories
        player.xp = xp
        
damage = (30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43 ,44 ,45 ,46, 47, 48, 49, 50, 51, 52, 53)
(random.choice(damage))

Player = defaultCharacter(name = {userName}, Xp = 0, level = 0, attack =(random.choice(damage)), health = 750, defense = 500, light_level = 0, startingFight = 0, victories = 0, xp = 0)


#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
class waterBoss:
    def __init__(waterBoss, attack: int, health: int) -> None:
        waterBoss.attack = attack
        waterBoss.health = health
class waterMinion:
    def __init__(waterMinion, attack: int, health:int) -> None:
        waterMinion.attack = attack
        waterMinion.health = health
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
class fireBoss:
    def __init__(fireBoss, attack: int, health: int) -> None:
        fireBoss.attack = attack
        fireBoss.health = health
class fireMinion:
    def __init__(fireMinion, attack: int, health:int) -> None:
        fireMinion.attack = attack
        fireMinion.health = health
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
class earthBoss:
    def __init__(earthBoss, attack: int, health: int) -> None:
        earthBoss.attack = attack
        earthBoss.health = health
class earthMinion:
    def __init__(earthMinion, attack: int, health:int) -> None:
        earthMinion.attack = attack
        earthMinion.health = health
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
class windBoss:
    def __init__(windBoss, attack: int, health:int) -> None:
        windBoss.attack = attack
        windBoss.health = health
class windMinion:
    def __init__(windMinion, name: str, attack: int, health: int, defense: int) -> None:
        windMinion.name = name
        windMinion.attack = attack
        windMinion.health = health
        windMinion.defense = defense

#This is to make it more like an actual fighting game the damage is random
windSpiritDamage = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17,)
(random.choice(windSpiritDamage))

firstWindSpirit = windMinion(name = "Wind Spirit", attack = (random.choice(windSpiritDamage)), health = 150, defense = 60)
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


def mainMenu():
    os.system("cls")
    if Experience > 3:
        print("[1] Endless Mode")
        print("[2] Story Mode")
        print("[3] Tutorial")
        print("[4] Inspiration")
        match input(f"Choose, {userName}: "):
            case ('1'):
                endlessMode()
            case ('2'):
                tutorialMode()
            case ('3'):
                storyMode()
            case _:
                os.system("cls")
                mainMenu()
    else:
        print("[1] Story Mode")
        print("[2] Tutorial")
        print("[3] Inspiration")
        print("[4] Progress")     
        match input(f"Choose, {userName}: "):
            case ('1'):
                storyMode()
            case ('2'):
                tutorialMode()
            case ('3'):
                inspiration()
            case ('4'):
                userProgression()
            case _:
                os.system("cls")
                mainMenu()


def inspiration():
    #Time to get serious lets be real all my friends that are playing this game by force
    #know that the entry/description to the story mode of that dungeon was made by known chatGPT
    #So dont sue me i gave credit, apprec it tho good job.


    ...
def endlessMode():
    ...
        

def tutorialMode():
    if storyExperience > 0:
        print("Well heres how the game works")
    else:
        match input("Go back to story mode. It'll explain it well. If you still dont understand then come back here.\nType 'm' to go to main menu."):
            case 'm':
                mainMenu()
            case _:
                os.system("cls")
                tutorialMode()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------






#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#First fight


def fight(Player, firstWindSpirit)-> None:

    if firstWindSpirit.defense >= 0:
        firstWindSpirit.defense -= Player.attack
                    
            ### On the other hand if it is less than or equal to zero it'll attack the persons health
    if firstWindSpirit.defense <= 0:
            firstWindSpirit.defense = 0
            firstWindSpirit.health -= Player.attack

    if Player.defense >= 0:
        Player.defense -= firstWindSpirit.attack

    if Player.defense <= 0:
        Player.defense = 0
        Player.health -= firstWindSpirit.attack


        print("----------------------------------------------------------------")
        print(f"Wind spirit has dealt {random.choice(windSpiritDamage)} DAMAGE!\n{userName} has dealt {random.choice(damage)} DAMAGE!")
        print("----------------------------------------------------------------------")
        print(f"Wind Spirit health: {firstWindSpirit.health},\nWind Spirit defense: {firstWindSpirit.defense}\n----------\n")
        print(f"{userName} health: {Player.health},\n{userName} defense: {Player.defense}")

    if firstWindSpirit.health < 1:
        print("Wind spirit has died")
        input(firstAfterMath())
                    
    return story_point
                    

            

    # the 'f' and the 'd' stands for delay print and fast print
    # the reason that its like that because its faster to test when I 

def storyMode():
    if Player.victories == 0:
        os.system("cls")
        #fast
        print('     Narrator: "Within the foreboding depths of the Elemental Spirit Dungeon, darkness reigns supreme. Its twisted corridors are a ghastly tapestry of jagged stone and flickering torchlight, casting eerie shadows that seem to dance with malevolent intent.\nTraps lie in wait, eager to ensnare the unwary, while spectral entities haunt every corner, their mournful wails a constant reminder of the horrors that dwell within. Yet amidst the peril, there are treasures to be found and challenges to be overcome, for those brave or foolish enough to dare the dungeons depths.\nBut beware, for in the heart of darkness, even the most valiant souls may find themselves consumed by the abyss. Prepare for the unknown and prepare your heart, light mage..."\n\n\n     ')
        input()
        os.system("cls")
        #Delay
        print('  ???:\n"Hey! Get up, you alright, man?"   ')
        input('\n')
        #d
        print('  You:\n"Whats going on, Where am I?"  ')
        input('\n')
        #d
        print('  ???:\n "Thats not important, you got knocked out by a spirit, right now lets get through this dungeon!" ')
        input('\n')
        #d
        print('  "(Thinking to yourself): So, he ignored my question then answered it? This guy is a weirdo. Wait, a dungeon?!?! And a spirit too?"  ')
        input('\n')
        #f
        print('   ???:\n"Look a wind spirit, attack fend for you life!"  ')
        input('\n\n')
        os.system("cls")
        #f
        #This is to begin so when you press enter it doesnt automatticaly start the fight
        print("Wind spirit stats:\n--------------------\n")
        print(f"HLTH = {firstWindSpirit.health}")
        print(f"ATK =  8-17 DMGE")
        print(f"DEF = {firstWindSpirit.defense}")
        print("---------------------------------------------------")
        print(f"{userName} stats:\n--------------------\n")
        print(f"HLTH = {Player.health}")
        print(f"ATK =  8-17 DMGE")
        print(f"DEF = {Player.defense}")
        print(f"LIGHT MAG PWR = {Player.light_level}")
        input()
        while True:
            fight(Player, firstWindSpirit)
            input()
            os.system("cls")

    if Player.victories == 1:
        #f
        fast_print('   Narrator: "Emerging from the depths of the evil elemental spirit dungeon, You breathe a sigh of relief, your holy heart blazes with triumphant victory. The burden of darkness lifts, but a flicker of concern remains for the lingering shadows left behind. As you step into the light outside of the dungeon, victorious yet vigilant, the need for tranquillity resonates within..."   ')
        input('\n')
        print('  ???: "Good moves back there!"   ')
        input('\n')
        print('  You:  "What the hell was that back there?!"  ')
        input('\n')
        print('  ???: "That was a dungeon, full of treasure, scrolls and despair!"   ')
        input('\n')
        print('  You:  "What does that even mean"  ')
        input('\n')
        print('  ???: "Asumming you dont mean tresaure and despair scrolls are like magic spells that you can use it battle!"   ')
        input('\n')
        print('  You:  (To yourself) "THAT DOESNT MAKE SENSE EITHER!"  ')
        input('\n')
        print('  You:  "Why couldnt I use any earlier"  ')
        input('\n')
        print(' ???:   "Because you stupid- Just kidding you havent learned how to wield spells yet but ill teach you how." ')
        input('\n')
        print(' ???:   "Heres a map of our base ' )

        print("WIP")


    
def firstAfterMath():
        os.system("cls")
        afterMath_print("You beat the WINDSPIRIT! ")
        Player.xp += 100
        Player.level += 1
        Player.victories += 1
        afterMath_print(f"Level up! {Player.level} Total XP: {Player.xp} Items gained: None\n")
        input()
        mainMenu()
        



def userProgression():
    os.system("cls")
    print(f"{userName} Stats/Progression:")
    print(f"\n-------------------------\n")
    print(f"XP: {Player.xp}")
    print(f"Level: {Player.level}")
    print(f"Light Level: {Player.light_level}")
    print(f"Attack Strength: {Player.attack}")
    print(f"Health: {Player.health}\n")
    print(f"Number of victories: {victories}")
    match input("-------------------------------\nHeres is where you can view all your stats/inventory Type 'm' to go to main menu "):
        case 'm':
            mainMenu()
        case _:
            os.system("cls")
            userProgression()
                




        
mainMenu()








