
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
Experience = 0
storyExperience = 0

#Create 1 little mini boss of each element. Then create 3 little dungeon elemental mages

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
class defaultCharacter:
    def __init__(player, name, Xp: int, level: int, attack: int, health: int, light_level: int, starting_point: int) -> None:
        player.name = name
        player.Xp = Xp
        player.level = level
        player.attack = attack
        player.health = health
        player.light_level = light_level
        player.starting_point = starting_point
        
Player = defaultCharacter(name = userName, Xp = 0, level = 0, attack = 30, health = 750, light_level = 0, starting_point = 0)


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
    def __init__(windMinion, name: str, attack: int, health:int) -> None:
        windMinion.attack = attack
        windMinion.health = health


firstWindSpirit = windMinion(name = "Wind Spirit", attack = 10, health = 150)
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




def storyMode():
    if Player.starting_point <= 0:
        os.system("cls")
        fast_print('     Narrator: "Within the foreboding depths of the Evil Spirit Dungeon, darkness reigns supreme. Its twisted corridors are a ghastly tapestry of jagged stone and flickering torchlight, casting eerie shadows that seem to dance with malevolent intent.\nTraps lie in wait, eager to ensnare the unwary, while spectral entities haunt every corner, their mournful wails a constant reminder of the horrors that dwell within. Yet amidst the peril, there are treasures to be found and challenges to be overcome, for those brave or foolish enough to dare the dungeons depths.\nBut beware, for in the heart of darkness, even the most valiant souls may find themselves consumed by the abyss. Prepare you heart for the unknown light mage...\n\n\n"     ')
        os.system("cls")
        delay_print('  "???:\n"Hey! Get up you alright, man?"   ')
        input('\n')
        delay_print('   "You:\n"Whats going on, Where am I?"  ')
        input('\n')
        delay_print('  ???:\n "Thats not important, you got knocked out by a spirit, right now lets get through this dungeon!" ')
        input('\n')
        delay_print('   "(Thinking to yourself): So, he ignored my question then answered it? This guy is a weirdo. Wait, a dungeon?!?! And a spirit too?"  ')
        input('\n')
        fast_print('  ???:\n"Look a wind spirit, attack fend for you life!')
        input()
        os.system("cls")
        input("Press ENTER get ready for battle!\n\n***Once you hit enter you will attack***")
        os.system("cls")

        while True:

            def firstFight (defaultCharacter, target) -> None:

                print(f"You attacked the wind spirit! dealt 30 DAMAGE!\n")
                target.health -= defaultCharacter.attack
                print(f"Wind Spirits health: {firstWindSpirit.health}\n------------\n")
                defaultCharacter.health -= target.attack
                print("Wind spirit dealt 10 DAMAGE!\n")
                print(f"Your health: {Player.health}")

            firstFight(Player, firstWindSpirit)

            if firstWindSpirit.health < 0:
                os.system("cls")

                firstAfterMath()

            input("")
            os.system("cls")

    if starting_point > 0:
        delay_print(' ???: "Come on lets blow this stand, we gotta get out of the dungeon!')
        input()
        fast_print("Narrator:\nSo as our two young heros fend for their lives against the wind Spirit.\n They leave in fear, not wanting to test their luck for another day.") 


def firstAfterMath():
        global Xp, level, storyExperience
        Xp = 0
        level = 0 #Try you beat the {target} with an f string perhapd?
        afterMath_print("You beat the WINDSPIRIT!")
        Xp += 100
        level += 1
        afterMath_print(f"Level up! {level} Total XP: {Xp} Items gained: None\n")
        afterMath_print(f"You beat the Wind Spirit!")
        storyExperience += 1
        mainMenu()



def userProgression():
    os.system("cls")
    print(f"{userName} Stats/Progression:\n")
    print(f"Stats:\n-------------------------\n")
    print(f"XP: {Player.Xp}")
    print(f"Level: {Player.level}")
    print(f"Light Level: {Player.light_level}")
    print(f"Attack Strength: {Player.attack}")
    print(f"Health: {Player.health}\n")
    match input("-------------------------------\nHeres is where you can view all your stats/inventory Type 'm' to go to main menu "):
        case 'm':
            mainMenu()
        case _:
            os.system("cls")
            userProgression()
                




        
mainMenu()








