
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
class weapon:
    def __init__(weapon: str, name: str, description: str, price: int, level_requirement: int, attack: int, style: str) -> None:
        weapon.name = name
        weapon.description = description
        weapon.price = price
        weapon.level_requirement = level_requirement
        weapon.attack = attack
        weapon.style = style

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ALL SWORDS
stone_sword_damage = (60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 90)
stone_sword_description = 'The Stone Sword: a primal weapon, born from the earths core. With rugged charm and unwavering strength, it serves as a steadfast companion for those beginning their journey into the realm of combat.'

iron_sword_damage = (90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130)
iron_sword_description = 'The Iron Sword: forged in the heart of roaring flames, it bears the mark of resilience and strength. With its sleek design and formidable edge, it stands as a symbol of progress for fledgling warriors venturing into the fray.'

diamond_sword_damage = (130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175)
diamond_sword_description = 'The Diamond Sword: a gleaming beacon of power and prestige, crafted from the rarest of gems. Its radiant edge, sharp and unyielding, embodies the aspirations of champions-to-be as they embark on their quest for glory.'

stone_sword = weapon(name = 'Granite Edge', description = stone_sword_description, price = 500, level_requirement = 5, attack = stone_sword_damage, style = "Slashing (SWORD)")

iron_sword = weapon(name = 'Ironwill Scimitar', description = iron_sword_description, price = 1500, level_requirement = 8, attack = iron_sword_damage, style = "Slashing (SWORD)"  )

diamond_sword = weapon(name ='Gemfire Greatsword', description = diamond_sword_description, price = 3000, level_requirement = 15, attack = diamond_sword_damage, style = 'Heavy Hitting Slashing (SWORD)') 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ALL SCYTHES
shadowsoul_requiem_damage = (1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250)
shadowsoul_requiem_description = ('Forged in secrecy by the solitary figure known only as the Shadowweaver, the Shadowsoul Requiem emerged from the depths of the forsaken realm. Once revered as a master of the arcane arts, the Shadowweavers name fell into obscurity when whispers of betrayal tainted their legacy. Driven by a desire to redeem their tarnished honor, the Shadowweaver delved into forbidden rituals, channeling dark magic to imbue the scythe with unearthly power. Each swing of the Shadowsoul Requiem carried the weight of forgotten heroes, echoing their silent cries for justice. As the dark clouds of war gathered on the horizon, the Shadowweaver emerged from the shadows, wielding the legendary scythe against the forces of darkness. Despite the worlds condemnation, the Shadowsoul Requiem became a beacon of hope for those who dared to challenge the tyranny of evil, forever etching its name into the annals of history as a symbol of redemption and defiance.')
shadowsoul_requiem = weapon(name = 'shadowsoul_requiem', description = shadowsoul_requiem_description, price = 15000, level_requirement = 50, attack = shadowsoul_requiem_damage, style = 'Mythical Sweeping, Slashing Weapon (SCYTHE)'  )

peasant_reaper_damage = (250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365)
peasant_reapear_description = ('The Peasant\'s Reaper is a formidable scythe-like weapon forged from repurposed farming tools. With its razor-sharp blade and sturdy handle, it embodies the resilience and defiance of the oppressed. Wielded by rebels, it strikes fear into oppressors and symbolizes the fight for freedom and justice.')
peasant_reaper = weapon(name = 'Peasants\' reaper', description = peasant_reapear_description, price = 3500, level_requirement = 10, attack = peasant_reaper_damage, style = 'Heavy Hitting Slashing (SCYTHE)')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ALL STAFFS
celestial_staff_description = ('The Celestial Emberstaff: a divine oakwood staff adorned with celestial symbols, housing a radiant crystal. With it, wielders command the fury of flames, becoming beacons of celestial power, purging darkness with righteous fire.')
celestial_staff_damage = (350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600)
celestial_staff = weapon(name = 'Celestial Staff', description = celestial_staff_description, price = 4500, level_requirement = 20, attack = celestial_staff_damage, style = 'Stabbing Thrusting Weapon (STAFF)')

nova_nexus_description = ('The Nova Nexus, a revered artifact, channels celestial energies to empower wielders, shaping destinies with radiant spells infused with cosmic might. Crafted with arcane mastery, it stands as a beacon of cosmic awe, guiding seekers towards enlightenment through the mysteries of the universe.')
nova_nexus_damage = ('601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824')
nova_nexus = weapon(name = 'Nova Nexus Staff', description = nova_nexus_description, price = 12500, level_requirement = 25, attack = nova_nexus_damage, style = 'Stabbing Thrusting Weapon (STAFF)')
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
class defaultCharacter:
    def __init__(player, name, Xp: int, level: int, attack: int, health: int, defense: int, light_level: int, startingFight: int, victories: int, xp: int,) -> None:
        player.name = name
        player.Xp = Xp
        player.level = level
        player.attack = attack
        player.health = health
        player.defense = defense
        player.equippied_weapon = None
        player.light_level = light_level
        player.startingFight = startingFight
        player.victories = victories
        player.xp = xp
        
    #Code to have random amount of damage 30-53    
player_damage = (30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43 ,44 ,45 ,46, 47, 48, 49, 50, 51, 52, 53, 55)

Player = defaultCharacter(name = {userName}, Xp = 0, level = 0, attack = player_damage, health = 750, defense = 500, light_level = 0, startingFight = 0, victories = 0, xp = 0)

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
class elemntalBoss:
    def __init__(elementalBoss, attack: int, health:int) -> None:
        elementalBoss.attack = attack
        elementalBoss.health = health
        
class elementalMinion:
    def __init__(elementalMinion, name: str, attack: int, health: int, defense: int) -> None:
        elementalMinion.name = name
        elementalMinion.attack = attack
        elementalMinion.health = health
        elementalMinion.defense = defense

#This is to make it more like an actual fighting game. The damaage is randomized.
windSpiritDamage = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17,)
firstWindSpirit = elementalMinion(name = "Wind Spirit", attack = windSpiritDamage, health = 150, defense = 60)
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

#--- MAIN MENU ---#
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

#--- INSPIRATION BEHIND GAME ---#
def inspiration():
    os.system("cls")
    match input(f"It's time to get serious.\nLet's be real, all my friends who are playing this game by force know that the entry/description to the story mode of that dungeon was authored by the renowned ChatGPT.\nAs well as some of the description to the weapons.\nI did edit them a little so its not entirely ChatGPT!\nSo, please don't sue me, I've given credit.\nI appreciate it though, good job ChatGPT.\nI hope you enjoy I just was kind of board of playing games and wanted to make one and i wanted to learn more about functions and OOP.\n\n\nType 'm' to go make to main menu."):
        case 'm':
            mainMenu()
        case _:
            inspiration()

#--- ENDLESS MODE WIP ---#
def endlessMode():
    print('WIP')
        

#--- EXPLAINS BASIC GAME MECHANICS ---#
def tutorialMode():
    if Player.victories > 0:
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

def equip_weapon(self, weapon):
    self.equipped_weapon = weapon
    print(f"{Player.name} has equipped {weapon.name}")




#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

#--- CODE FOR FIRST FIGHT ---#
def fight(Player, target)-> None:
    damage = random.choice(Player.attack)
    WSdamage = random.choice(target.attack)

    if target.defense >= 0:
        target.defense -= damage
            
            ### On the other hand if it is less than or equal to zero it'll attack the persons health
    if target.defense <= 0:
        target.defense = 0
        target.health -= damage

    if Player.defense >= 0:
        Player.defense -= WSdamage

    if Player.defense <= 0:
        Player.defense = 0
        Player.health -= WSdamage


    print("----------------------------------------------------------------")
    print(f"Wind spirit has dealt {WSdamage} DAMAGE!\n{userName} has dealt {damage} DAMAGE!")
    print("----------------------------------------------------------------------")
    print(f"Wind Spirit health: {target.health},\nWind Spirit defense: {target.defense}\n----------\n")
    print(f"{userName} health: {Player.health},\n{userName} defense: {Player.defense}")

    if target.health < 1:
        Player.victories +=1
        print("Wind spirit has died")
        input(firstAfterMath())
                    
                    

            

    # the 'f' and the 'd' stands for delay print and fast print
    # the reason that its like that because its faster to test when I go through it.

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
        input('***Brace yourself for BATTLE!***\n\n')
        #f
        #This is to begin so when you press enter it doesnt automatticaly start the fight
        print('------------------------------------------------------------')
        print("Wind spirit stats:\n--------------------\n")
        print(f"HLTH = {firstWindSpirit.health}")
        print(f"ATK =  8-17 DMGE")
        print(f"DEF = {firstWindSpirit.defense}")
        print("---------------------------------------------------")
        print(f"{userName} stats:\n--------------------\n")
        print(f"HLTH = {Player.health}")
        print(f"ATK =  30-53 DMGE")
        print(f"WPN = Fists")
        print(f"DEF = {Player.defense}")
        print(f"LIGHT MAG PWR = {Player.light_level}")
        input()
        os.system("cls")
        while True:
            fight(Player, firstWindSpirit)
            input()
    

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
        print(' ???:   "Because you stupid- Just kidding you havent learned how to wield spells yet but i\'ll teach you how. While were at it heres a sketch of the dungeon." ')
        input('\n')
        os.system("cls")
        input()
        #FAST PRINT ALL OF THIS
        print("                                    WATER BOSS                                                    ")
        print("                                   |           |                                                   ")
        print("                                   |           |                                                   ")
        print("                                   |           |                                                   ")
        print("                                   |           |                                                   ")
        print("                                   |           |                                                   ")
        print("           ________________________|           |________________________                           ")
        print("                                                                                                  ")
        print("   FIRE BOSS                                                           EARTH BOSS       ")
        print("           ________________________            ________________________                           ")
        print("                                   |           |                                                    ")
        print("                                   |           |                                                    ")
        print("                                   |           |                                                    ")
        print("                                   |           |                                                    ")
        print("                                   |           |                                                    ")
        print("                                   |           |                                                    ")
        print("                                   |           |                                                    ")
        print("                                     WIND BOSS                                                             ")
        print("                                                                                                  ")
        print("                                                                                                  ")
        input()
        os.system("cls")
        #d
        print(' ???:  "The plan is to bassicaly just eradicate them from the face of the earth. Couldnt put it any simplier. They keep coming, back they feed and live off evil thoughts of men." ')
        input('\n')
        print(' ???:  "So its up to us light mages to take care of em."')
        input('\n')
        print(' You:  "So whats a light mage? Also do we get a super cool base or something?" ')
        input('\n')
        print(' ???:  "A light mage are people who fight against the darkness of evil born with the gift of being able to use light magic abilities."')
        input('\n')
        print(' You:  "Thats cool."')
        input('\n')
        print(' ???: "Indudably my names Myles by the way but you can call me Isaiah" ')
        input('\n')
        print(' Isaiah: "Lets head back to our base ill explain more there" ')
        input('\n')
        print(' Narrator: " Returning to your base, you light mages walk side by side, your sudden found unity a beacon of hope in the ongoing struggle against the forces of darkness." ')
        input('\n')
        os.system('cls')
        print(' Narrator: " Upon returning to your newfound base, the other light mages greeted you with a scene of bustling activity and camaraderie. Within the safety of their stronghold, you find not only weapons and provisions but also the warm embrace of fellow allies and friends. Amidst the flickering torchlight, laughter and conversation filled the air, a testament to the resilience of their bond forged in battle. Strengthened by their unity and fortified by the support of their companions, they prepared to face the challenges ahead with renewed determination and unwavering resolve. In this sanctuary of light and friendship, they found solace and strength to confront the darkness that loomed beyond their walls, united in their shared quest for peace and prosperity." ')
        input('\n')
        print(' Isaiah: "Let me teach you the basics real quick. (talk bout shop ability to change weapons how when you buy a weapon you equip it automatticaly you get paid in coins which u can use to buy weapons, and how to use your light magic)"')



def firstAfterMath():    
    os.system("cls")
    afterMath_print("You beat the WINDSPIRIT! ")
    Player.xp += 100
    Player.level += 1
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
    print(f"Number of victories: {Player.victories}")
    match input("-------------------------------\nHeres is where you can view all your stats/inventory Type 'm' to go to main menu "):
        case 'm':
            mainMenu()
        case _:
            os.system("cls")
            userProgression()
                




        
mainMenu()







