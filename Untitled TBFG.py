
#--- IMPORTS ---#
import os, random, time, sys

###Entry Point###
global userName
userName = input("Please enter your name: ")
os.system("cls")

#--- DELAYING PRINT CODE ---#
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

#--- GLOBAL VARIABLES ---#
global attack_buff, health_buff, fire_level_buff, water_level_buff, Xp, Experience, storyExperience, starting_point

attack_buff = 0
health_buff = 0

Xp = 0




#This was to see if a person had compelted a part of the game if so it would skip some things.
storyExperience = 0

#Create 1 little mini boss of each element. Then create 3 little dungeon elemental mages

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#--- CODE FOR WEAPON CLASS ---#
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
#--- CODE FOR ALL SWORDS ---#
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
#--- CODE FOR ALL SCYTHES ---#
shadowsoul_requiem_damage = (1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250)
shadowsoul_requiem_description = ('Forged in secrecy by the solitary figure known only as the Shadowweaver, the Shadowsoul Requiem emerged from the depths of the forsaken realm. Once revered as a master of the arcane arts, the Shadowweavers name fell into obscurity when whispers of betrayal tainted their legacy. Driven by a desire to redeem their tarnished honor, the Shadowweaver delved into forbidden rituals, channeling dark magic to imbue the scythe with unearthly power. Each swing of the Shadowsoul Requiem carried the weight of forgotten heroes, echoing their silent cries for justice. As the dark clouds of war gathered on the horizon, the Shadowweaver emerged from the shadows, wielding the legendary scythe against the forces of darkness. Despite the worlds condemnation, the Shadowsoul Requiem became a beacon of hope for those who dared to challenge the tyranny of evil, forever etching its name into the annals of history as a symbol of redemption and defiance.')
shadowsoul_requiem = weapon(name = 'shadowsoul_requiem', description = shadowsoul_requiem_description, price = 15000, level_requirement = 50, attack = shadowsoul_requiem_damage, style = 'Mythical Sweeping, Slashing Weapon (SCYTHE)'  )

peasant_reaper_damage = (250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365)
peasant_reaper_description = ('The Peasant\'s Reaper is a formidable scythe-like weapon forged from repurposed farming tools. With its razor-sharp blade and sturdy handle, it embodies the resilience and defiance of the oppressed. Wielded by rebels, it strikes fear into oppressors and symbolizes the fight for freedom and justice.')
peasant_reaper = weapon(name = 'Peasants\' reaper', description = peasant_reaper_description, price = 3500, level_requirement = 10, attack = peasant_reaper_damage, style = 'Heavy Hitting Slashing (SCYTHE)')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--- CODE FOR ALL STAFFS ---#
celestial_staff_description = ('The Celestial Emberstaff: a divine oakwood staff adorned with celestial symbols, housing a radiant crystal. With it, wielders command the fury of flames, becoming beacons of celestial power, purging darkness with righteous fire.')
celestial_staff_damage = (350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600)
celestial_staff = weapon(name = 'Celestial Staff', description = celestial_staff_description, price = 4500, level_requirement = 20, attack = celestial_staff_damage, style = 'Stabbing Thrusting Weapon (STAFF)')

nova_nexus_description = ('The Nova Nexus, a revered artifact, channels celestial energies to empower wielders, shaping destinies with radiant spells infused with cosmic might. Crafted with arcane mastery, it stands as a beacon of cosmic awe, guiding seekers towards enlightenment through the mysteries of the universe.')
nova_nexus_damage = (600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825)
nova_nexus = weapon(name = 'Nova Nexus Staff', description = nova_nexus_description, price = 12500, level_requirement = 25, attack = nova_nexus_damage, style = 'Stabbing Thrusting Weapon (STAFF)')
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#--- CLASSES FOR ARMOR ---#
class armor:
    def __init__(armor, name: str, added_defense: int, level_requirement: int, description: str, price: int):
        armor.name = name
        armor.added_defense = added_defense
        armor.level_requirement = level_requirement
        armor.description = description
        armor.price = price

leather_tunic_description = ('A simple leather tunic, stitched together with basic craftsmanship. Provides basic protection against minor threats.')
leather_tunic = armor(name = "Leather Tunic", added_defense = 50, level_requirement = 1, description = leather_tunic_description, price = 800)

ironweaved_chainmail_armor_description = ("a sturdy and protective armor made from interlocking iron rings, offering both flexibility and defense.")
ironweaved_chainmail_armor = armor(name = "Iron Weaved Chainmail Armor", added_defense = 125, level_requirement = 5, description = ironweaved_chainmail_armor_description, price = 2500)

astral_armor_description = ('Woven from the fabric of the stars, this armor channels celestial energies to shield its wearer from harm. It radiates a mystical aura, embodying the essence of distant galaxies and granting its bearer a connection to the cosmic forces that govern the universe.')
astral_armor = armor(name = "Astral Armor", added_defense = 350, level_requirement = 10, description = astral_armor_description, price = 5000)

pheonix_armor_description = ('Crafted from the fiery feathers of the legendary phoenix, this armor offers exceptional protection against fire and embodies the spirit of resilience and renewal.')
pheonix_armor = armor(name = "Phenoix Armor", added_defense = 600, level_requirement = 15, description = pheonix_armor_description, price = 7500)

aetherial_armor_description = ('Woven from the radiant essence of the celestial spheres, this armor was gifted to mortals by Apollo after trials of ethereal valor. It emanates an otherworldly glow that shields its wearer from all harm, embodying the divine resilience and grace of the gods. Those who wear the Aetherial Radiance are revered as paragons of virtue and protectors of cosmic harmony.')
aetherial_armor = armor(name = "Ethereal armor", added_defense = 1250, level_requirement = 20, description = aetherial_armor_description, price = 11500)

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#-- DEFAULT CHARACTER CLASS {WIP} ---#
class defaultCharacter:
    def __init__(player, name, Xp: int, level: int, attack: int, light_attack: int, equipped_weapon, health: int, defense: int, equipped_armor, armor, light_level: int, startingFight: int, victories: int, xp: int, coins: int) -> None:
        player.name = name
        player.Xp = Xp
        player.level = level
        player.attack = attack
        player.light_attack = light_attack
        player.equipped_weapon = None
        player.health = health
        player.defense = defense
        player.equipped_armor = equipped_armor
        player.armor = None
        player.light_level = light_level
        player.startingFight = startingFight
        player.victories = victories
        player.xp = xp
        player.coins = coins
        
    #Code to have random amount of damage 30-53    
player_damage = (30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43 ,44 ,45 ,46, 47, 48, 49, 50, 51, 52, 53, 55)

Player = defaultCharacter(name = {userName}, Xp = 0, level = 0, attack = player_damage, light_attack = 60, equipped_weapon = None, health = 750, defense = 500, equipped_armor = None, armor = None, light_level = 0, startingFight = 0, victories = 0, xp = 0, coins = 0)

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#--- CLASSES CODE FOR BOSSES AND MINIONS FOR DUNGEON
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
    if Player.victories > 3:
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
    if Player.victories > 0:
        print("[1] (Continue)Story Mode")
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
    if Player.victories == 0:
       match input("Return to story mode for the full scoop. If you're still puzzled, swing by again. Press 'm' to warp to the main menu."):
            case 'm':
                mainMenu()
            case _:
                os.system("cls")
                tutorialMode()
    else:
        print("Alright, here's the rundown. In battle, you'll have three options: a Light Magic Attack for a guaranteed 60 DMGE, a regular fists attack (or basic attack for those without a weapon), and a weapon attack, whether it's with a sword, staff, or other.\nAfter each victory, you'll earn rewards like armor and weapons through story mode. So, gear up and embark on your adventure, light mage!")
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

#--- CODE FOR EQUIPPING WEAPON ---#
def equip_weapon(self, weapon):
    self.equipped_weapon = weapon
    print(f"{Player.name} has equipped {weapon.name}")

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------





#--- CODE FOR FIGHT ---#

    
def fight(Player, target)-> None:
    def weapon_reponse_status(Player, target)-> None:
        print("\n------------------------------------\n")
        print(f"{userName}s' HLTH {Player.health}" )
        print(f"{userName}s' DEF {Player.defense}")
        print("\n------------------------------------\n")
        print(f"{target.name}s' HLTH {target.health}" )
        print(f"{target.name}s' DEF {target.defense}" )
        print("-------------------------------------")  
    def invalid_response_status(Player, target)-> None:
        print("\n------------------------------------\n")
        print(f"{userName}s' HLTH {Player.health}" )
        print(f"{userName}s' DEF {Player.defense}")
        print("\n------------------------------------\n")
        print(f"{target.name}s' HLTH {target.health}" )
        print(f"{target.name}s' DEF {target.defense}" )
        print("-------------------------------------")  
    def light_attack_status(Player, target)-> None:
        print(f"{target.name} DEALT {Rdamage}!")
        print("\n------------------------------------\n")
        print(f"{userName}s' HLTH {Player.health}" )
        print(f"{userName}s' DEF {Player.defense}" )
        print("\n------------------------------------\n")
        print(f"{userName} DEALT {Player.light_attack}!")
        print("\n------------------------------------\n")
        print(f"{target.name}s' HLTH {target.health}" )
        print(f"{target.name}s' DEF {target.defense}" )
        print("-------------------------------------")
    def status(Player, target)-> None:
    #--- CODE FOR STATUS UPDATES HEALTH
        print(f"{target.name} DEALT {Rdamage}!")
        print("\n------------------------------------\n")
        print(f"{userName}s' HLTH {Player.health}" )
        print(f"{userName}s' DEF {Player.defense}" )
        print("\n------------------------------------\n")
        print(f"{userName} DEALT {damage}!")
        print("\n------------------------------------\n")
        print(f"{target.name}s' HLTH {target.health}" )
        print(f"{target.name}s' DEF {target.defense}" )
        print("-------------------------------------")
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
    #--- Randomized word choice to keep the game from being bland --#
    global Rdamage, damage
    Haste = (f"With haste choose your next attack, {userName}: ")
    Wise = (f"Be wise with your next attack for it may be your last, {userName}: ")
    Regular = (f"Choose your next attack: ")
    fighting_words = (Haste, Wise, Regular)
    rcf = random.choice(fighting_words)
    #--- Code for randomized damage for more game authenticity ---#
    damage = random.choice(Player.attack)
    Rdamage = random.choice(target.attack)
    while True:
        print(f"---------{userName}s' Turn---------")
        print("1. Fists Attack")
        print("2. Light Magic Attack")
        print("3. Weapon Attack")
        print(f"\n")
        match input(f"{rcf}"):
            case '1':

                 #--- Game Logic attack the defense until its zero if it is zero then keep it there and attack at the health instead.
                 if target.defense >= 0:
                    target.defense -= damage
        
                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= damage
        
                    if Player.defense >= 0:
                        Player.defense -= Rdamage

                    if Player.defense <= 0:
                        Player.defense = 0
                        Player.health -= Rdamage

                    if target.health <= 0:
                        good_aftermath()

                    if Player.health <= 0:
                        bad_aftermath()

                    status(Player, target)
                    input()
            case '2':
                if target.defense >= 0:
                    target.defense -= Player.light_attack
        
                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= Player.light_attack
        
                    if Player.defense >= 0:
                        Player.defense -= Rdamage

                    if Player.defense <= 0:
                        Player.defense = 0
                        Player.health -= Rdamage

                    if target.health <= 0:
                        good_aftermath()

                    if Player.health <= 0:
                        bad_aftermath()
                    
                    light_attack_status(Player, target)
                    input()
            case '3':#Fix
                    if Player.equipped_weapon == diamond_sword:
                        
                        diamond_sword.attack = (random.choice(diamond_sword.attack))
                        if Player.equipped_weapon == diamond_sword:
                            target.health -= diamond_sword.attack
                            input(f"{target.health}")

                        weapon_reponse_status(Player, target)

                    else:
                        input(f"You have no weapon, [Seen as an invalid turn] {userName} loses turn [-10 HLTH and -10 DEF]")
                        print(f"{userName} takes 10 damage!")
                        Player.health -= 10

                    if Player.defense >= 0:
                        Player.defense -= 10

                    if Player.defense <= 0:
                        Player.defense = 0
                        Player.health -= 10

                    invalid_response_status(Player, target)
                    input()
            case _:
                Regular2 = (f"You've lost your turn {userName}!")
                Mean = (f"Look alive to stay alive {userName}!")
                Funny = (f"Bozo He hit you!")
                invalid_words = (Regular2, Mean, Funny)
                print(random.choice(invalid_words))
                print("\n[-10 HLTH and -10 DEF]")
                Player.health -= 10

                if Player.defense >= 0:
                    Player.defense -= 10

                if Player.defense <= 0:
                    Player.defense = 0
                    Player.health -= 10

                invalid_response_status(Player, target)
                input()

                            
#--- ENTIRE STORY/DIALOUGE ---#
    # the 'f' and the 'd' stands for delay print and fast print
    # the reason that its like that because its faster to test when I go through it.
def storyMode():
    if Player.victories == 0:
        print('     Narrator: "Within the foreboding depths of the Elemental Spirit Dungeon, darkness reigns supreme.Twisted corridors of jagged stone stretch endlessly, flickering torchlight casting eerie shadows that dance with malevolent intent. Traps lie in wait, eager to ensnare the unwary, while spectral entities haunt every corner, their mournful wails a constant reminder of the horrors lurking within.\n\nBut amidst the peril, there are treasures to be found and challenges to be overcome, for those brave or foolish enough to dare the dungeon\'s depths. Yet, beware, for in the heart of darkness, even the most valiant souls may find themselves consumed by the abyss. Steel yourself, light mage, for your greatest trial begins now."\n\n\n')
        os.system("cls")
        print('  ???:\n"Hey! Wake up! Are you alright?"')
        input('\n')
        print('  You:\n"Ugh... What happened? Where am I?"')
        input('\n')
        os.system("cls")
        print('  ???:\n"There\'s no time to explain! You were knocked out by a spirit. We need to move, now, before it comes back!"')
        input('\n')
        print('  You (Thinking): "He’s dodging my questions. Who is this guy? And did he say a dungeon? And spirits?"')
        input('\n')
        print('  ???:\n"Focus! A wind spirit is approaching. Get ready to defend yourself!"')
        input('\n')
        os.system('cls')
        input('***Brace yourself for BATTLE!***\n\n')
        print('------------------------------------------------------------')
        print(f"Wind Spirits stats:\n--------------------\n")
        print(f"HLTH = {firstWindSpirit.health}")
        print(f"ATK =  8-17 DMGE")
        print(f"DEF = {firstWindSpirit.defense}")
        print("---------------------------------------------------")
        print(f"{userName} stats:\n--------------------\n")
        print(f"HLTH = {Player.health}")
        print(f"ATK =  30-53 DMGE")
        print(f"WPN = Fists")
        print(f"DEF = {Player.defense}")
        input()
        os.system("cls")
        if 1 == 1:
            while True:
                fight(Player, firstWindSpirit)
        input('\n')
        print('  You:\n"Seriously, who are you? And what’s going on here?"')
        input('\n')
        print('  ???:\n"Names later. Right now, survival is key. Follow my lead if you want to get out of here alive."')
        input('\n')
        os.system('cls')
        print('  You (Thinking): "This guy knows something he’s not telling me. I need to stay alert... and figure out what’s really happening here."')
        input('\n')
        print('  ???:\n""Great job in that fight! We need to get out of here now to keep you safe."')
        input
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
    #IMPROVE THE STORY PELASESEEEEE
    if Player.victories == 1:
        #f
        fast_print('   Narrator: "Emerging from the depths of the evil elemental spirit dungeon, You breathe a sigh of relief, your holy heart blazes with triumphant victory. The burden of darkness lifts, but a flicker of concern remains for the lingering shadows left behind. As you step into the light outside of the dungeon, victorious yet vigilant, the need for tranquillity resonates within..."   ')
        input('\n')
        print('  ???:\n"Good moves back there!"   ')
        input('\n')
        os.system("cls")
        print('  You:\n"What the hell was that back there?!"  ')
        input('\n')
        print('  ???:\n"That was a dungeon-full of treasure, scrolls and despair!"   ')
        input('\n')
        os.system("cls")
        print('  You:\n"What does that even mean"  ')
        input('\n')
        print('  ???:\n"I recommend getting armor next time you go through one though that fight looked a little rough"   ')
        input('\n')
        os.system("cls")
        print('  You:\n(To yourself) "Why does he keep ignoring my questions?"')
        input('\n')
        print('  You:\n(To yourself) "Hes most likely correct sadly..."  ')
        input('\n')
        print(' ???:\n"Here I might as well show you this, its a sketch of a larger more vital dungeon" ')
        input('\n')
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
        print(' ???:\n"The plan is to bassicaly just eradicate them from the face of the earth. Couldnt put it any simplier. They keep coming, back they feed and live off evil thoughts of men. I know what your thinking their dungeon looks like a cross how can they truly be evil right? To be honest we dont really know for certain there are a lot of theories out there to why that is but no one truly knows." ')
        input('\n')
        print(' ???:\n"Ill ignore the last part but...I assume up to us light mages to take care of em."')
        input('\n')
        os.system("cls")
        print(' ???:\n"Indeed" ')
        input('\n')
        print(' You:\n"So whats a light mage? Also do we get a super cool base or something?" ')
        input('\n')
        os.system("cls")
        print(' ???:\n"A light mage are people who fight against the darkness of evil, born with the gift of being able to use light magic abilities."')
        input('\n')
        print(' You:\n"Thats cool."')
        input('\n')
        os.system("cls")
        print(' ???:\n"Indudably my names Myles by the way but you can call me Isaiah" ')
        input('\n')
        print(' Isaiah:\n"Lets head back to our base ill explain more there" ')
        input('\n')
        os.system("cls")
        print(' Narrator: \n"Returning to your base, you walk side by side, your sudden found unity a beacon of hope in the ongoing struggle against the forces of darkness." ')
        input('\n')
        print(' Narrator:\n"Upon returning to your newfound base, the other light mages greeted you with a scene of bustling activity and camaraderie. Within the safety of their stronghold, you find not only weapons and provisions but also the warm embrace of fellow allies and friends. Amidst the flickering torchlight, laughter and conversation filled the air, a testament to the resilience of their bond forged in battle. Strengthened by their unity and fortified by the support of their companions, they prepared to face the challenges ahead with renewed determination and unwavering resolve. In this sanctuary of light and friendship, they found solace and strength to confront the darkness that loomed beyond their walls, united in their shared quest for peace and prosperity." ')
        input('\n')
        os.system("cls")
        print(' Isaiah:\n"Let me teach you the basics real quick on how to fight and get weapons and armor! First off to get weapons you can buy them from the shop and you can also switch weapons in your inventory. You get paid in coins when you defeat spirits, which you use to buy weapons, as well as armor. Your armor provides a boost of defense as well!" ') 
        input('\n')
        print(' Isaiah:\n"Here kid, I saved up some money to use for other purposes, but you seem like you\'re worth here heres 5000 coin. Dont spend it in one place! Lets head over to the shop and pick you out a fine weapon, and/or armor.!"')
        input('\n')
        os.system("cls")
        print(' (To yourself) "How can he tell me not to spend it all in one place when I can only spend it on weapons and armor, which are technically in the same place?"')
        Player.coins += 5000
        input()
        os.system("cls")
        shop()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- ENTRY POINT FOR SHOP ---#
def shop():
    os.system("cls")
    print(f"Your current number of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print(' Ryker:\n"Welcome young lad! Havent seen you around here before welcome to my shop. ')
    match input("Avavaible weapons:\n'Swords', 'Scythes' 'Staffs' 'Armor' : "):
        case 'Swords':
            swords_shop()
        case 'Scythes' :
            scythes_shop()
        case 'Staffs':
            staffs_shop()
        case 'Armor':
            armor_shop()
        case _:
            input("Please enter a weapons name you would like to buy!")
            shop()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- ARMOR SHOP ---# WORK ON THE  SHOP #
def armor_shop():
    os.system("cls")
    print(f"Your current number of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print(f"[1] - NAME: {leather_tunic.name}: ADDED DEF: +{leather_tunic.added_defense}\nDescription: {leather_tunic.description}\nPrice: {stone_sword.price}\n\n ")
    print(f"[2] - NAME: {ironweaved_chainmail_armor.name} ADDED DEF: +{ironweaved_chainmail_armor.added_defense}\nDescription: {ironweaved_chainmail_armor.description}\nPrice: {ironweaved_chainmail_armor.price}\n\n ")
    print(f"[3] - NAME: {astral_armor.name}: ADDED DEF: +{astral_armor.added_defense}\nDescription: {astral_armor.description}\nPrice: {astral_armor.price}\n\n ")
    print(f"[4] - NAME: {pheonix_armor.name}: ADDED DEF: +{pheonix_armor.added_defense}\nDescription: {pheonix_armor.description}\nPrice: {pheonix_armor.price}\n\n ")
    print(f"[5] - NAME: {aetherial_armor.name}: ADDED DEF: +{aetherial_armor.added_defense}\nDescription: {aetherial_armor.description}\nPrice: {aetherial_armor.price}\n\n ")
    print("\n\n\nType m to go to main menu")
    match input("Which weapon would you like lad?"):
        case '1':
            if Player.coins < leather_tunic.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                scythes_shop() 
            elif leather_tunic.level_requirement > Player.level:
                input(f"You need to be at least level {leather_tunic.level_requirement} to wear {leather_tunic.name}.")
                scythes_shop()
            else:
                Player.equipped_armor = leather_tunic
                Player.coins -= leather_tunic.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {leather_tunic.name}. Press ENTER to continue.")
                scythes_shop()
        case '2': 
            if Player.coins < ironweaved_chainmail_armor.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                scythes_shop() 
            elif ironweaved_chainmail_armor.level_requirement > Player.level:
                input(f"You need to be at least level {ironweaved_chainmail_armor.level_requirement} to wear {ironweaved_chainmail_armor.name}.")
                scythes_shop()
            else:
                Player.equipped_armor = ironweaved_chainmail_armor
                Player.coins -= ironweaved_chainmail_armor.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {ironweaved_chainmail_armor.name}. Press ENTER to continue.")
                scythes_shop()
        case '3': 
            if Player.coins < astral_armor.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                scythes_shop() 
            elif astral_armor.level_requirement > Player.level:
                input(f"You need to be at least level {astral_armor.level_requirement} to wear {astral_armor.name}.")
                scythes_shop()
            else:
                Player.equipped_armor = astral_armor
                Player.coins -= astral_armor.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {astral_armor.name}. Press ENTER to continue.")
                scythes_shop()
        case '4':
            if Player.coins < pheonix_armor.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                scythes_shop() 
            elif pheonix_armor.level_requirement > Player.level:
                input(f"You need to be at least level {pheonix_armor.level_requirement} to wear {pheonix_armor.name}.")
                scythes_shop()
            else:
                Player.equipped_armor = pheonix_armor
                Player.coins -= pheonix_armor.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {pheonix_armor.name}. Press ENTER to continue.")
                scythes_shop()
        case '5':
            if Player.coins < aetherial_armor.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                scythes_shop() 
            elif aetherial_armor.level_requirement > Player.level:
                input(f"You need to be at least level {aetherial_armor.level_requirement} to wear {aetherial_armor.name}.")
                scythes_shop()
            else:
                Player.equipped_armor = aetherial_armor
                Player.coins -= aetherial_armor.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {aetherial_armor.name}. Press ENTER to continue.")
                scythes_shop()
        case _:
            armor_shop()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- SWORDS WEAPON SHOP ---#
def swords_shop():
    os.system("cls")
    print(f"Your current number of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print(f"[1] - NAME: {stone_sword.name}: DMGE: 60-90.\nDescription: {stone_sword.description}\nPrice: {stone_sword.price}\n\n")
    print(f"[2] - NAME: {iron_sword.name}: DMGE: 90-130.\nDescription: {iron_sword.description}\nPrice: {iron_sword.price}\n\n")
    print(f"[3] - NAME: {diamond_sword.name}: DMGE: 90-130.\nDescription: {diamond_sword.description}\nPrice: {diamond_sword.price}\n\n")
    print("\n\n\nType 'm' to go to main menu")
    match input("Which weapon would you like lad?"):
        case '1':
            if Player.coins < stone_sword.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                input()
                swords_shop()
            elif stone_sword.level_requirement > Player.level:
                print(f"You need to be at least level {stone_sword.level_requirement} to wield {stone_sword.name}.")
                input()
                swords_shop()
            else:
                Player.equipped_weapon = stone_sword
                Player.coins -= stone_sword.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {stone_sword.name}. Press Enter to continue.")
                swords_shop()
        case '2':
            if Player.coins < iron_sword.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
            elif iron_sword.level_requirement > Player.level:
                input(f"Ryker:\nYou need to be at least level {iron_sword.level_requirement} to wield {iron_sword.name}.")
                swords_shop()
            else:
                Player.equipped_weapon = iron_sword
                Player.coins -= iron_sword.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {iron_sword.name}. Press ENTER to continue.")
                swords_shop()
        case '3':
            if Player.coins < diamond_sword.price:
                print("You dont have enough money young man. You try to scam the legendary Ryker?")
                swords_shop()
                if diamond_sword.level_requirement > Player.level:
                    input(f"You have to be at least level {diamond_sword.level_requirement} to buy this weapon!")
                    swords_shop()
            else:
                Player.equipped_weapon = diamond_sword
                Player.coins -= 3000
                print("Pleasure doin business with you ya bo-yo!")
                input(f"You have equipped a {diamond_sword.name}")
                swords_shop()
        case 'm':
            mainMenu()
        case _:
            input(random.choice(choose_words))
            swords_shop()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------        
global choose_words, Already, Hurry
Already = "Ryker:\n'Hurry up we dont got all day we got a line going young man."
Hurry = "Ryker:\n'Get on with it kid."
choose_words = (Already, Hurry)
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- SCYTHES WEAPON SHOP ---#
def scythes_shop():
    os.system("cls")
    print(f"Your current # of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print(f"[1] - NAME: {peasant_reaper.name} DMGE: 250-365.\nDescription: {peasant_reaper_description}\nPrice: {peasant_reaper.price}\n\n")
    print(f"[2] - NAME: {shadowsoul_requiem.name} DMGE: 1000-1250.\nDescription: {shadowsoul_requiem_description}\nPrice: {shadowsoul_requiem.price}\n\n")
    print("\n\n\nType 'm' to go to main menu")
    match input("Which weapon would you like lad?"):
        case '1':
            if Player.coins < peasant_reaper.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                scythes_shop() 
            elif peasant_reaper.level_requirement > Player.level:
                input(f"You need to be at least level {peasant_reaper.level_requirement} to wield {peasant_reaper.name}.")
                scythes_shop()
            else:
                Player.equipped_weapon = peasant_reaper
                Player.coins -= peasant_reaper.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {peasant_reaper.name}. Press ENTER to continue.")
                scythes_shop()
        case '2':
            if Player.coins < shadowsoul_requiem.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                scythes_shop()  
            elif shadowsoul_requiem.level_requirement > Player.level:
                print(f"You need to be at least level {shadowsoul_requiem.level_requirement} to wield {shadowsoul_requiem.name}.")
                scythes_shop()
            else:
                Player.equipped_weapon = shadowsoul_requiem
                Player.coins -= shadowsoul_requiem.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {shadowsoul_requiem.name}. Press ENTER to continue.")
                scythes_shop() 
        case 'm':
            mainMenu()
        case _:
            input(random.choice(choose_words))
            scythes_shop()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- STAFFS WEAPON SHOP ---#
def staffs_shop():
    os.system("cls")
    print(f"Your current # of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print(f"[1] - NAME: {celestial_staff.name} DMGE: 600-825.\nDescription: {celestial_staff_description}\nPrice: {celestial_staff.price}\n\n")
    print(f"[2] - NAME: {nova_nexus.name} DMGE: 600-825.\nDescription: {nova_nexus_description}\nPrice: {nova_nexus.price}\n\n")
    print("\n\n\nType 'm' to go to main menu")
    match input("Which weapon would you like lad?"):
        case '1':
            # Check if the player has enough coins to buy the celestial_staff
            if Player.coins < celestial_staff.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                staffs_shop() 
            # Check if the player meets the level requirement for the stone_sword
            elif celestial_staff.level_requirement > Player.level:
                input(f"You have to be at least level {celestial_staff.level_requirement} to buy this weapon!")
                staffs_shop() 
            else:
                # Player meets both money and level requirements
                Player.equipped_weapon = celestial_staff
                Player.coins -= celestial_staff.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {celestial_staff.name}. Press ENTER to continue.")
                staffs_shop()
        case '2':
            if Player.coins < nova_nexus.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                staffs_shop()
            elif nova_nexus.level_requirement > Player.level:
                print(f"You need to be at least level {nova_nexus.level_requirement} to wield {nova_nexus.name}.")
                staffs_shop()
            else:
                Player.equipped_weapon = nova_nexus
                Player.coins -= nova_nexus.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {nova_nexus.name}. Press ENTER to continue.")
                staffs_shop()
        case 'm':
            mainMenu()
        case _:
            input(random.choice(choose_words))
            staffs_shop()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- CUSTOM AFTERMATH WORDS SO THAT THE GAME DOESNT FEEL BLAND ---#
Day = "Another day another victory! "
Easy = "That wasnt so bad, nice victory light mage!"
victory_words = (Day, Easy)

def good_aftermath():    
    os.system("cls")
    fast_print(random.choice(victory_words))
    Player.xp += 100
    Player.level += 5
    Player.light_level += 3
    if Player.light_level > 3:
        Player.light_attack + 35
    Player.victories += 1
    Player.coins += 750
    fast_print(f"Level up! {Player.level} Total XP: {Player.xp} Items gained: None\n")
    input()
    mainMenu()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
Regular = "You have fallen in battle! No rewards"
Rough = "Better luck next time eh? No rewards for you!"
loser_words = (Regular, Rough)  
def bad_aftermath():       
    os.system("cls")
    input()
    fast_print(random.choice(loser_words))
    mainMenu()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- USERS PROGRESSION TO SHOW HOW FAR THE PLAYER HAS CAME ---#
def userProgression():
    os.system("cls")
    print(f"{userName} Stats/Progression:")
    print(f"\n-------------------------\n")
    print(f"XP: {Player.xp}")
    print(f"Level: {Player.level}")
    print(f"Light Level: {Player.light_level}")
    print(f"Attack Strength: {Player.attack}")
    print(f"Health: {Player.health}\n")
    print(f"Number of Victories: {Player.victories}")
    print(f"Number of Coins: {Player.coins}")
    print(f"Weapon {Player.equipped_weapon}")
    print(f"Armor {Player.equipped_armor}")
    match input("-------------------------------\nHeres is where you can view all your stats/inventory Type 'm' to go to main menu "):
        case 'm':
            mainMenu()
        case _:
            os.system("cls")
            userProgression()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

mainMenu()





