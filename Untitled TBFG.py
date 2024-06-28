
#--- IMPORTS ---#
import os, random, time, sys

###Entry Point###
global userName
while True:
    userName = input("Please enter your name: ")
    if userName == "" or userName.isdigit():
        os.system("cls")
    else:
        break

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

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#--- the difference bewteen that this class is used to see if the character has reached the next level and if so, it will biring them to the next part. ---#
#--- I decided to make it two different classes because I didn't want to make the code too complex, and hard to read/comprhend. ---#
class progressionChecker:
    def __init__(progressionChecker, experience: int, progress: int, victories: int, first_Time_In_Light_Mage_Hideout: bool, entered_Light_Mage_Hideout: bool, first_time_entered_light_mage_library: bool, defeated_fire_dungeon: bool, defeated_earth_dungeon: bool, defeated_water_dungeon: bool, defeated_wind_dungeon: bool) -> None:
        progressionChecker.experience = experience
        progressionChecker.progress = progress
        progressionChecker.victories = victories
        progressionChecker.first_Time_In_Light_Mage_Hideout = first_Time_In_Light_Mage_Hideout
        progressionChecker.entered_Light_Mage_Hideout = entered_Light_Mage_Hideout
        progressionChecker.first_time_entered_light_mage_library = first_time_entered_light_mage_library
        progressionChecker.defeated_fire_dungeon = defeated_fire_dungeon
        progressionChecker.defeated_earth_dungeon = defeated_earth_dungeon
        progressionChecker.defeated_water_dungeon = defeated_water_dungeon
        progressionChecker.defeated_wind_dungeon = defeated_wind_dungeon
        

progressionChecker = progressionChecker(0, 0, 0, False, False, False, False, False, False, False)
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#--- PARENT FOR ALL CHARACTERS CLASS ---#
#--- I used to show my knowledge of inheritance in Python as, and i realised it would be better to create a parent class that all characters could inherit from also I like polymorphism. ---#
class universalCharaterStats:
    def __init__(universalCharaterStats, name: str, health: int, attack: int, defense : int) -> None:
        universalCharaterStats.name = name
        universalCharaterStats.health = health
        universalCharaterStats.attack = attack
        universalCharaterStats.defense = defense
        
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
    
    def __str__(weapon) -> str:
        return f'\n--------------------------------------------------------------------\nWeapon Name: {weapon.name}:\n--------------------------------------------------------------------\n\n\nDamage Range: {weapon.attack}\n--------------------------------------------------------------------\n\n\nSTYLE: {weapon.style}'

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--- CODE FOR ALL WEAPON DROPS ---#
gaunlets_damage = (200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250.)
gaunlets_description = ' Forged from the heart of an ancient mountain, these gauntlets were once said to imbue the wearer with immense strength and the power to create stone barriers and trigger minor earthquakes.'
gaunlets = weapon(name = 'Gaunlets', description = gaunlets_description, price = 0, level_requirement = 0, attack = gaunlets_damage, style = 'Blunt (GAUNLET)')

trident_of_souls_damage = (600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625.)
trident_of_souls_description = ('The Trident of Souls is a mystical weapon that harnesses the essence of departed souls, empowering its wielder with spectral abilities in combat.')
trident_of_souls = weapon(name = 'Trident of Souls', description = trident_of_souls_description, price = 0, level_requirement = 0, attack = trident_of_souls_damage, style = 'Slash Jab (TRIDENT)')


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
class defaultCharacter(universalCharaterStats):
    def __init__(player, name: str, level: int, attack: int, weapons_collection: list, armor_collection: list, buff_collection: list, light_attack: int, equipped_weapon: None, health: int, defense: int, equipped_armor: None, light_level: int, Xp: int, coins: int, victories: int, buff: any) -> None:
        super().__init__(name, health, attack, defense)
        player.weapons_collection = weapons_collection
        player.armor_collection = armor_collection
        player.buff_collection = buff_collection
        player.equipped_weapon = equipped_weapon
        player.light_attack = light_attack
        player.level = level
        player.light_level = light_level
        player.equipped_armor = equipped_armor
        player.Xp = Xp
        player.coins = coins
        player.victories = victories
        player.buff = None

player_damage = (30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43 ,44 ,45 ,46, 47, 48, 49, 50, 51, 52, 53, 55)

Player = defaultCharacter(name = {userName}, 
                          health = 750, 
                          attack = player_damage, 
                          defense = 300, 
                          Xp = 0, 
                          weapons_collection = [], 
                          armor_collection = [],
                          buff_collection = [],  
                          equipped_weapon = None, 
                          light_attack = 60, 
                          level = 0, 
                          light_level = 0, 
                          equipped_armor = None, 
                          coins = 1000, 
                          victories = 0,
                          buff = None)

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#--- CLASSES CODE FOR BOSSES AND MINIONS FOR DUNGEON --

#-- The difference bewteen bosses, and minions is that they have a loot they has a chance of droping
class elementalBoss(universalCharaterStats):
    def __init__(elementalBoss, name: str, attack: int, health: int, defense: int, loot: list) -> None:
        super().__init__(name, attack, health, defense)
        elementalBoss.loot = loot
        elementalBoss.name = name

weights = (70, 30)
nothing = 'Nothing'
winds_favor = ('A loot drop from Zephyrus')
#-- Zephyrus has a 70% chance of dropping a winds favor, and a 30% chance of dropping nothing ---#
wind_boss_description = ('Zephyrus is a swift and unpredictable master of the skies, capable of conjuring powerful storms and hurricanes. His control over the winds allows him to strike with lightning speed and disappear into the air.')
Zephyrus = elementalBoss(name = "Zephyrus", attack = 100 , health = 300, defense = 300, loot = [winds_favor, nothing])
random_loot_chance_zephyrus = random.choices([winds_favor, nothing], weights)

#-- Ignatius the Flame Tyrant has a 70% chance of dropping an emberheart amulet, and a 30% chance of dropping nothing ---#
fire_boss_description = ('WIP')
emberheart_amulet = ('A loot drop from Ignatius, the Flame Tyrant')
ignatius_the_flame_tyrant = elementalBoss(name = "Ignatius the Flame Tyrant", attack = 175, health = 400, defense = 450, loot = [emberheart_amulet, nothing])
random_loot_chance_ignatius = random.choices([emberheart_amulet, nothing], weights)

#-- Nerus the Tidal Sovereign has a 70% chance of dropping a trident of souls, and a 30% chance of dropping nothing ---#
water_boss_description = ('WIP')
trident_of_souls = ('A loot drop from nerus_tidal_sovereign')
nereus_the_tidal_soverign = elementalBoss(name = "Nereus the Tidal Sovereign", attack = 200, health = 550, defense = 650, loot = [trident_of_souls, nothing])
random_loot_chance_nerus_ = random.choices([trident_of_souls, nothing], weights)

#--- Nerus the Gorah has a 70% chance of dropping gaulents, and a 30% chance of dropping nothing ---#
gorah = elementalBoss(name = "Gorah", attack = 250, health = 350 , defense = 325, loot = [gaunlets, nothing])
random_loot_chance_nerus_gorah = random.choices([gaunlets, nothing], weights)
#-- A legendary dragon scale has a 70% chance of dropping, and a 30% chance of dropping nothing ---#
dragon_scale_description = ('A rare and valuable piece of dragon scale, crafted from the scales of a legendary dragon. It offers great protection against all types of attacks.')
dragon_scale = 'Dragon Scale'
random_loot_chance_dragon = random.choices([dragon_scale, nothing], weights)
dragon = elementalBoss(name = "Mini Dragon", attack = 125, health = 500, defense = 300, loot = [dragon_scale, nothing])
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
    #--- If you have 5 pieces of dragonscale, you can create dragon armor! (FUTURE GAME IDEA) ---#
    #--- This code makes dragon_scale have a 70% chance to drop, and a 30% chance to drop nothing ---#


#-- I knoww that I could've just made it inherit no class because it doesnt have any extra methods or attributes. But just for the sake of understanding code better I decided to do this instead.---#
class elementalMinion(universalCharaterStats):
    def __init__(elementalMinion, name: str, attack: int, health: int, defense: int) -> None:
        super().__init__(name, attack, health, defense)
        elementalMinion.name = name
        elementalMinion.attack = attack
        elementalMinion.health = health
        elementalMinion.defense = defense


windSpiritDamage = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17,)
firstWindSpirit = elementalMinion(name = "Wind Spirit", attack = windSpiritDamage, health = 150, defense = 60)


#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#--- MAIN MENU ---#
def mainMenu():
    os.system("cls")
    if progressionChecker.progress > 3:
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
    elif progressionChecker.progress > 0:
        os.system("cls")      
        print("[1] (Continue) Story Mode")
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
    elif progressionChecker.entered_Light_Mage_Hideout == True:
        os.system("cls")      
        print("[1] (Continue) Story Mode")
        print("[2] Tutorial")
        print("[3] Inspiration")
        print("[4] Progress")     
        print("[5] Go to (Weapons) Inventory")
        print("[6] Go to (Armor) Inventory")	
        print("[7] Go to Light Mage Hideout")	
        match input(f"Choose, {userName}: "):
            case ('1'):
                storyMode()
            case ('2'):
                tutorialMode()
            case ('3'):
                inspiration()
            case ('4'):
                userProgression()
            case ('5'):
                weapon_system()
            case ('6'):
                armor_system()
            case ('7'):
                light_mages_hideout()
            case _:
                os.system("cls")
                mainMenu()
    else:
        os.system("cls")
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
    if Player.progress == 0:
       match input("Return to story mode for the full scoop. If you're still puzzled, swing by again. Press 'm' to warp to the main menu."):
            case 'm':
                mainMenu()
            case _:
                os.system("cls")
                tutorialMode()
    else:
        input("Alright, here's the rundown. In battle, you'll have three options: a Light Magic Attack for a guaranteed 60 DMGE, a regular fists attack (or basic attack for those without a weapon), and a weapon attack, whether it's with a sword, staff, or other.\nAfter each victory, you'll earn rewards like armor and weapons through story mode. So, gear up and embark on your adventure, light mage!")
        mainMenu()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

#--- CODE FOR FIGHT ---#

    
def fight(Player, target)-> None:
    Player.defense = 300
    Player.health = 750
    firstWindSpirit.health = 150
    firstWindSpirit.defense = 60

    if Player.equipped_armor is leather_tunic:
        Player.defense += leather_tunic.added_defense

    elif Player.equipped_armor is ironweaved_chainmail_armor:
        Player.defense += ironweaved_chainmail_armor.added_defense

    elif Player.equipped_armor is astral_armor:
        Player.defense += astral_armor.added_defense

    elif Player.equipped_armor is pheonix_armor:
        Player.defense += pheonix_armor.added_defense

    elif Player.equipped_armor is aetherial_armor:
        Player.defense += aetherial_armor.added_defense

    else:
        Player.defense = Player.defense  # No armor equipped, use default defense

    def weapon_reponse_status(Player, target)-> None:
        os.system("cls")
        print(f"{target.name} DEALT {Rdamage}!")
        print("\n------------------------------------\n")
        print(f"{userName} DEALT {EWD} USING {Player.equipped_weapon.name}!")
        print("\n------------------------------------\n")
        print(f"{userName}s' HLTH {Player.health}" )
        print(f"{userName}s' DEF {Player.defense}")
        print("\n------------------------------------\n")
        print(f"{target.name}s' HLTH {target.health}" )
        print(f"{target.name}s' DEF {target.defense}" )
        print("-------------------------------------")  
    def invalid_response_status(Player, target)-> None:
        os.system("cls")
        print("\n------------------------------------\n")
        print(f"{userName}s' HLTH {Player.health}" )
        print(f"{userName}s' DEF {Player.defense}")
        print("\n------------------------------------\n")
        print(f"{target.name}s' HLTH {target.health}" )
        print(f"{target.name}s' DEF {target.defense}" )
        print("-------------------------------------")  
    def light_attack_status(Player, target)-> None:
        os.system("cls")
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
        os.system("cls")
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
    Haste = (f"With haste choose your next attack, {userName}: ")
    Wise = (f"Be wise with your next attack for it may be your last, {userName}: ")
    Regular = (f"Choose your next attack: ")
    fighting_words = (Haste, Wise, Regular)
    rcf = random.choice(fighting_words)
    #--- Code for randomized damage for more game authenticity ---#
    global damage, Rdamage, DSG, SSD, ISD, PRD, SSRD, CSD, NND, EWD
    DSG = random.choice(diamond_sword_damage)
    SSD = random.choice(stone_sword_damage)
    ISD = random.choice(iron_sword_damage)
    PRD = random.choice(peasant_reaper_damage)
    SSRD = random.choice(shadowsoul_requiem_damage)
    CSD = random.choice(celestial_staff_damage)
    NND = random.choice(nova_nexus_damage)
    while True:
        print(f"---------{userName}s' Turn---------")
        print("1. Attack with Fists")
        print("2. Attack using Light Magic")
        print("3. Attack using Weapon")
        print(f"\n")
        match input(f"{rcf}"):
            case '1':

                 #--- Game Logic attack the defense until its zero if it is zero then keep it there and attack at the health instead. ---#
                 if target.defense >= 0:
                    damage = random.choice(Player.attack)
                    Rdamage = random.choice(target.attack)
                    target.defense -= damage
        
                    if target.defense <= 0:
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        target.defense = 0
                        target.health -= damage
        
                    if Player.defense >= 0:
                        Player.defense -= Rdamage

                    if Player.defense <= 0:
                        Player.defense = 0
                        Player.health -= Rdamage

                    if target.health <= 0:
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break

                    status(Player, target)
                    input()
            case '2':
                if target.defense >= 0:
                    target.defense -= Player.light_attack
        
                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= Player.light_attack
        
                    if Player.defense >= 0:
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.defense -= Rdamage

                    if Player.defense <= 0:
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.defense = 0
                        Player.health -= Rdamage

                    if target.health <= 0:
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break
                    
                    light_attack_status(Player, target)
                    input()
            case '3':
                if Player.equipped_weapon == diamond_sword:
                    EWD = DSG = random.choice(diamond_sword_damage)

                    if target.defense >= 0:
                        target.defense -= DSG

                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= DSG

                    if Player.defense >= 0:
                        Rdamage = random.choice(target.attack)
                        Player.defense -= Rdamage

                    if Player.defense <= 0:
                        Rdamage = random.choice(target.attack)
                        Player.defense = 0
                        Player.health -= Rdamage

                    if target.health <= 0:
                        Player.progress += 1
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break

                    weapon_reponse_status(Player, target)
                    input()

                elif Player.equipped_weapon == stone_sword:
                    EWD = SSD = random.choice(stone_sword_damage)

                    if target.defense >= 0:
                        target.defense -= SSD

                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= SSD

                    if Player.defense >= 0:
                        Rdamage = random.choice(target.attack)
                        Player.defense -= Rdamage
        
                    if Player.defense <= 0:
                        Player.defense = 0
                        Rdamage = random.choice(target.attack)
                        Player.health -= Rdamage
                    
                    if target.health <= 0:
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break

                    weapon_reponse_status(Player, target)
                    input()   

                elif Player.equipped_weapon == iron_sword:
                    EWD = SSD = random.choice(stone_sword_damage)

                    if target.defense >= 0:
                        target.defense -= ISD

                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= ISD

                    if Player.defense >= 0:
                        Rdamage = random.choice(target.attack)
                        Player.defense -= Rdamage
        
                    if Player.defense <= 0:
                        Player.defense = 0
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.health -= Rdamage

                    if target.health <= 0:
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break

                    weapon_reponse_status(Player, target)
                    input()   

                elif Player.equipped_weapon == peasant_reaper:
                    EWD = SSD = random.choice(peasant_reaper_damage)

                    if target.defense >= 0:
                        target.defense -= PRD

                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= PRD

                    if Player.defense >= 0:
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.defense -= Rdamage
        
                    if Player.defense <= 0:
                        Player.defense = 0
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.health -= Rdamage

                    if target.health <= 0:
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break

                    weapon_reponse_status(Player, target)
                    input()   
                
                elif Player.equipped_weapon == shadowsoul_requiem:
                    EWD = SSD = random.choice(shadowsoul_requiem_damage)

                    if target.defense >= 0:
                        target.defense -= SSRD

                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= SSRD

                    if Player.defense >= 0:
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.defense -= Rdamage
        
                    if Player.defense <= 0:
                        Player.defense = 0
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.health -= Rdamage
                    
                    if target.health <= 0:
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break

                    weapon_reponse_status(Player, target)
                    input()   
                
                elif Player.equipped_weapon == celestial_staff:
                    EWD = SSD = random.choice(celestial_staff_damage)

                    if target.defense >= 0:
                        target.defense -= CSD

                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= CSD

                    if Player.defense >= 0:
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.defense -= Rdamage
        
                    if Player.defense <= 0:
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.defense = 0
                        Player.health -= Rdamage
                    
                    if target.health <= 0:
                        Player.progress += 1
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break
                        
                    weapon_reponse_status(Player, target)
                    input()      

                elif Player.equipped_weapon == nova_nexus:
                    EWD = SSD = random.choice(nova_nexus_damage)

                    if target.defense >= 0:
                        target.defense -= NND

                    if target.defense <= 0:
                        target.defense = 0
                        target.health -= NND

                    if Player.defense >= 0:
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.defense -= Rdamage
        
                    if Player.defense <= 0:
                        damage = random.choice(Player.attack)
                        Rdamage = random.choice(target.attack)
                        Player.defense = 0
                        Player.health -= Rdamage

                    if target.health <= 0:
                        Player.progress += 1
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break

                    weapon_reponse_status(Player, target)
                    input()   

                else:
                    input(f"You have no weapon, [Seen as an invalid turn] {userName} loses turn [-10 HLTH and -10 DEF]")
                    print(f"{userName} takes 10 damage!")
                    Player.health -= 10

                    if Player.defense >= 0:
                        Player.defense -= 10

                    if Player.defense <= 0:
                        Player.defense = 0
                        Player.health -= 10

                    if target.health <= 0:
                        good_aftermath()
                        break

                    if Player.health <= 0:
                        bad_aftermath()
                        break
                            

                    invalid_response_status(Player, target)
                    input()
            case _:
                Regular2 = (f"You've lost your turn {userName}!")
                Mean = (f"Look alive to stay alive {userName}!")
                Funny = (f"Bozo He hit you!")
                invalid_words = (Regular2, Mean, Funny)
                input(("[-10 HLTH and -10 DEF]", ((random.choice(invalid_words)))))
                Player.health -= 10
                Player.defense -= 10

                if Player.defense <= 0:
                    Player.defense = 0
                

                if Player.health <= 0:
                    bad_aftermath()
                    break
                
                invalid_response_status(Player, target)
        
                            
#--- ENTIRE STORY/DIALOUGE ---#
    # the 'f' and the 'd' stands for delay print and fast print
    # the reason that its like that because its faster to test when I go through it.
def storyMode():
    if progressionChecker.progress == 0:
        os.system("cls")
        print('  Narrator: "Within the foreboding depths of the Elemental Spirit Dungeon, darkness reigns supreme.\nTwisted corridors of jagged stone stretch endlessly, flickering torchlight casting eerie shadows that dance with malevolent intent.\nTraps lie in wait, eager to ensnare the unwary, while spectral entities haunt every corner, their mournful wails a constant reminder of the horrors lurking within.\nBut amidst the peril, there are treasures to be found and challenges to be overcome, for those brave or foolish enough to dare the dungeon\'s depths.\nYet, beware, for in the heart of darkness, even the most valiant souls may find themselves consumed by the abyss.\nSteel your heart, light mage, for your trials and tribulations begin now..."\n\n\n')
        input('\n')
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
        while True:
            fight(Player, firstWindSpirit)
            break
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
    #IMPROVE THE STORY PELASESEEEEE
        os.system("cls")
        input('\n')
        print('  You:\n"Seriously, who are you? And what’s going on here?"')
        input('\n')
        print('  ???:\n"Names later. Right now, survival is key. Follow my lead if you want to get out of here alive."')
        input('\n')
        os.system('cls')
        print('  You (Thinking): "This guy knows something he’s not telling me. I need to stay alert... and figure out what’s really happening here."')
        input('\n')
        print('  ???:\n""Great job in that fight though! We need to get out of here now to keep you safe."')
        input('\n')
        os.system('cls  ')
        print(' Narrator:\n"The wind spirit that you defeated slowly disappears, into thin air, leaving behind a trail of darkness.\nYou feel the urge to leave this place. So, you run out of the dungeon."')
        input('\n')
        os.system("cls")
        print('   Narrator:\n"Emerging from the depths of the evil elemental spirit dungeon, You breathe a sigh of relief, your holy heart blazes with triumphant victory. The burden of darkness lifts, but a flicker of concern remains for the lingering shadows left behind. As you step into the light outside of the dungeon, victorious yet vigilant, the need for tranquillity resonates within..."   ')
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
        print('  You:\n(Thinking) "Why does he keep ignoring my questions?"')
        input('\n')
        print('  You:\n(Thinking) "Hes most likely correct sadly..."  ')
        input('\n')
        os.system("cls")
        print(' ???:\n"If we went any deeper you would\'ve certainly died. Still good job for a newbie..." ')
        input('\n')
        print(' Narrator:\n"With that thought it gets quiet in the conversation bewteen you two." ')
        input('\n')
        os.system("cls")
        print(' You:\n"Well that doesnt sound good." ')
        input('\n')
        print(' ???:\n"The plan is to bassicaly just eradicate them from the face of the earth. Couldnt put it any simplier. They keep coming, back they feed and live off evil thoughts of men." ')
        input('\n')
        print(' ???:\n"Ill ignore the last part but...I assume its up to us light mages to take care of em."')
        input('\n')
        os.system("cls")
        print(' ???:\n"Indeed" ')
        input('\n')
        print(' You:\n"So whats a light mage? Also, do we get a super cool base or something?" ')
        input('\n')
        os.system("cls")
        print(' ???:\n"I suppose you could call it that... Anywho, A light mage are people who fight against the darkness of evil, born with the gift of being able to use light magic abilities."')
        input('\n')
        print(' You:\n"Thats cool."')
        input('\n')
        os.system("cls")
        print(' ???:\n"Indudably my names Myles by the way but you can call me Isaiah." ')
        input('\n')
        print(' Isaiah:\n"Lets head back to our base I\'ll explain more there." ')
        input('\n')
        os.system("cls")
        print(' Narrator: \n"going to your base, you walk side by side, your sudden found unity a beacon of hope in the ongoing struggle against the forces of darkness." ')
        input('\n')
        os.system("cls")
        print(' Narrator:\n"Upon going to your newfound base, the other light mages greeted you with a scene of bustling activity and camaraderie. Within the safety of their stronghold, you find not only weapons and provisions but also the warm embrace of fellow allies and friends. Amidst the flickering torchlight, laughter and conversation filled the air, a testament to the resilience of their bond forged in battle. Strengthened by their unity and fortified by the support of their companions, they prepared to face the challenges ahead with renewed determination and unwavering resolve. In this sanctuary of light and friendship, they found solace and strength to confront the darkness that loomed beyond their walls, united in their shared quest for peace and prosperity." ')
        input('\n')
        os.system("cls")
        print(' Isaiah:\n"The light mages have come together to defeat the darkness and restore peace to the world. It is truly a sacred place to remember for generations to come." ')
        input('\n')
        os.system("cls")
        progressionChecker.entered_light_mage_hideout = True
        light_mages_hideout()


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- ENTRY POINT FOR SHOP ---#
def shop():
    os.system("cls")
    print(f"Your current number of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print(' Ryker:\n"Welcome young lad! Please choose the item(s) you would like to buy." )')
    match input("Avavaible weapons/armor:\n'Swords', 'Scythes' 'Staffs' 'Armor' : "):
        case 'Swords':
            os.system("cls")
            swords_shop()
        case 'Scythes' :
            os.system("cls")
            scythes_shop()
        case 'Staffs':
            os.system("cls")
            staffs_shop()
        case 'Armor':
            os.system("cls")
            armor_shop()
        case _:
            input("\nPlease enter a weapons name you would like to buy!")
            os.system("cls")
            shop()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- ARMOR SHOP ---#
def armor_shop():
    os.system("cls")
    print(f"Your current number of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print(f"[1] - NAME: {leather_tunic.name}: ADDED DEF: +{leather_tunic.added_defense}\nDescription: {leather_tunic.description}\nPrice: {stone_sword.price}\n\n ")
    print(f"[2] - NAME: {ironweaved_chainmail_armor.name} ADDED DEF: +{ironweaved_chainmail_armor.added_defense}\nDescription: {ironweaved_chainmail_armor.description}\nPrice: {ironweaved_chainmail_armor.price}\n\n ")
    print(f"[3] - NAME: {astral_armor.name}: ADDED DEF: +{astral_armor.added_defense}\nDescription: {astral_armor.description}\nPrice: {astral_armor.price}\n\n ")
    print(f"[4] - NAME: {pheonix_armor.name}: ADDED DEF: +{pheonix_armor.added_defense}\nDescription: {pheonix_armor.description}\nPrice: {pheonix_armor.price}\n\n ")
    print(f"[5] - NAME: {aetherial_armor.name}: ADDED DEF: +{aetherial_armor.added_defense}\nDescription: {aetherial_armor.description}\nPrice: {aetherial_armor.price}\n\n ")
    print("\n\n\nType m to go to main menu\n\n\nType s to go back to the shop: ")
    match input("Which armor set would you like lad?:"):
        case '1':
            if Player.coins < leather_tunic.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                scythes_shop() 
            elif leather_tunic.level_requirement > Player.level:
                input(f"You need to be at least level {leather_tunic.level_requirement} to wear {leather_tunic.name}.")
                armor_shop()
            else:
                Player.equipped_armor = leather_tunic
                Player.armor_collection.append(leather_tunic)
                Player.coins -= leather_tunic.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {leather_tunic.name}. Press ENTER to continue.")
                armor_shop()
        case '2': 
            if Player.coins < ironweaved_chainmail_armor.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                scythes_shop() 
            elif ironweaved_chainmail_armor.level_requirement > Player.level:
                input(f"You need to be at least level {ironweaved_chainmail_armor.level_requirement} to wear {ironweaved_chainmail_armor.name}.")
                armor_shop()
            else:
                Player.equipped_armor = ironweaved_chainmail_armor
                Player.armor_collection.append(ironweaved_chainmail_armor)
                Player.coins -= ironweaved_chainmail_armor.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {ironweaved_chainmail_armor.name}. Press ENTER to continue.")
                armor_shop()
        case '3': 
            if Player.coins < astral_armor.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                armor_shop() 
            elif astral_armor.level_requirement > Player.level:
                input(f"You need to be at least level {astral_armor.level_requirement} to wear {astral_armor.name}.")
                armor_shop()
            else:
                Player.armor_collection.append(astral_armor)
                Player.equipped_armor = astral_armor
                Player.coins -= astral_armor.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {astral_armor.name}. Press ENTER to continue.")
                armor_shop()
        case '4':
            if Player.coins < pheonix_armor.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                armor_shop() 
            elif pheonix_armor.level_requirement > Player.level:
                input(f"You need to be at least level {pheonix_armor.level_requirement} to wear {pheonix_armor.name}.")
                armor_shop()
            else:
                Player.equipped_armor = pheonix_armor
                Player.armor_collection.append(pheonix_armor)
                Player.coins -= pheonix_armor.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {pheonix_armor.name}. Press ENTER to continue.")
                armor_shop()
        case '5':
            if Player.coins < aetherial_armor.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                armor_shop() 
            elif aetherial_armor.level_requirement > Player.level:
                input(f"You need to be at least level {aetherial_armor.level_requirement} to wear {aetherial_armor.name}.")
                armor_shop()
            else:
                Player.equipped_armor = aetherial_armor
                Player.armor_collection.append(aetherial_armor)
                Player.coins -= aetherial_armor.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {aetherial_armor.name}. Press ENTER to continue.")
                armor_shop()
        case 'm':
            mainMenu()
        case 's':
            shop()
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
    print("\n\n\nType 'm' to go to main menu\n\n\nType s to go back to the shop: ")
    match input("Which weapon would you like lad?"):
        case '1':
            if Player.coins < stone_sword.price:
                print("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                input()
                os.system("cls")
                swords_shop()
            elif stone_sword.level_requirement > Player.level:
                print(f"You need to be at least level {stone_sword.level_requirement} to wield {stone_sword.name}.")
                input()
                os.system("cls")
                swords_shop()
            else:
                Player.equipped_weapon = stone_sword
                Player.weapons_collection.append(stone_sword)
                Player.coins -= stone_sword.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {stone_sword.name}. Press ENTER to continue.")
                swords_shop()
        case '2':
            if Player.coins < iron_sword.price:
                input("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                os.system("cls")
                swords_shop()
            elif iron_sword.level_requirement > Player.level:
                input(f"Ryker:\nYou need to be at least level {iron_sword.level_requirement} to wield {iron_sword.name}.")
                os.system("cls")
                swords_shop()
            else:
                Player.equipped_weapon = iron_sword
                Player.weapons_collection.append(iron_sword)
                Player.coins -= iron_sword.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {iron_sword.name}. Press ENTER to continue.")
                os.system("cls")
                swords_shop()
        case '3':
            if Player.coins < diamond_sword.price:
                input("You dont have enough money young man. You try to scam the legendary Ryker?")
                os.system("cls")
                swords_shop()
            elif diamond_sword.level_requirement > Player.level:
                input(f"You have to be at least level {diamond_sword.level_requirement} to buy this weapon!")
                os.system("cls")
                swords_shop()
            else:
                Player.equipped_weapon = diamond_sword
                Player.weapons_collection.append(diamond_sword)
                Player.coins -= diamond_sword.price
                print("Pleasure doin business with you ya bo-yo!")
                input(f"You have equipped a {diamond_sword.name}")
                os.system("cls")
                swords_shop()
        case 'm':
            mainMenu()
        case 's':
            shop()
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
#--- SCYTHES WEAPON SHOP ---# Make a attribute that says if first time int he shop delcare global variable weapons_tuple = (). same thing for armors
def scythes_shop():
    os.system("cls")
    print(f"Your current # of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print(f"[1] - NAME: {peasant_reaper.name} DMGE: 250-365.\nDescription: {peasant_reaper_description}\nPrice: {peasant_reaper.price}\n\n")
    print(f"[2] - NAME: {shadowsoul_requiem.name} DMGE: 1000-1250.\nDescription: {shadowsoul_requiem_description}\nPrice: {shadowsoul_requiem.price}\n\n")
    print("\n\n\nType 'm' to go to main menu\n\n\nType s to go back to the shop: ")
    match input("Which weapon would you like lad?"):
        case '1':
            if Player.coins < peasant_reaper.price:
                input("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                os.system("cls")
                scythes_shop() 
            elif peasant_reaper.level_requirement > Player.level:
                input(f"You need to be at least level {peasant_reaper.level_requirement} to wield {peasant_reaper.name}.")
                os.system("cls")
                scythes_shop()
            else:
                Player.equipped_weapon = peasant_reaper
                Player.weapons_collection.append(peasant_reaper)
                Player.coins -= peasant_reaper.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {peasant_reaper.name}. Press ENTER to continue.")
                os.system("cls")
                scythes_shop()
        case '2':
            if Player.coins < shadowsoul_requiem.price:
                input("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                os.system("cls")
                scythes_shop()  
            elif shadowsoul_requiem.level_requirement > Player.level:
                print(f"You need to be at least level {shadowsoul_requiem.level_requirement} to wield {shadowsoul_requiem.name}.")
                os.system("cls")
                scythes_shop()
            else:
                Player.equipped_weapon = shadowsoul_requiem
                Player.weapons_collection.append(shadowsoul_requiem)
                Player.coins -= shadowsoul_requiem.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {shadowsoul_requiem.name}. Press ENTER to continue.")
                os.system("cls")
                scythes_shop() 
        case 'm':
            mainMenu()
        case 's':
            shop()
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
    print("\n\n\nType 'm' to go to main menu\n\n\nType s to go back to the shop: ")
    match input("Which weapon would you like lad?"):
        case '1':
            if Player.coins < celestial_staff.price:
                input("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                os.system("cls")
                staffs_shop() 
            elif celestial_staff.level_requirement > Player.level:
                input(f"You have to be at least level {celestial_staff.level_requirement} to buy this weapon!")
                os.system("cls")
                staffs_shop() 
            else:
                Player.equipped_weapon = celestial_staff
                Player.weapons_collection.append(celestial_staff)
                Player.coins -= celestial_staff.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {celestial_staff.name}. Press ENTER to continue.")
                os.system("cls")
                staffs_shop()
        case '2':
            if Player.coins < nova_nexus.price:
                input("Ryker:\nYou don't have enough money, young man. You trying to scam the legendary Ryker?")
                staffs_shop()
            elif nova_nexus.level_requirement > Player.level:
                print(f"You need to be at least level {nova_nexus.level_requirement} to wield {nova_nexus.name}.")
                os.system("cls")
                staffs_shop()
            else:
                Player.equipped_weapon = nova_nexus
                Player.weapons_collection.append(nova_nexus)
                Player.coins -= nova_nexus.price
                print("Ryker:\nPleasure doing business with you, ya bo-yo!")
                input(f"You have equipped {nova_nexus.name}. Press ENTER to continue.")
                os.system("cls")
                staffs_shop()
        case 'm':
            mainMenu()
        case 's':
            shop()
        case _:
            input(random.choice(choose_words))
            staffs_shop()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--- CUSTOM AFTERMATH WORDS SO THAT THE GAME DOESNT FEEL BLAND ---#
Day = "Another day another victory! "
Easy = "That wasnt so bad, nice victory light mage! "
victory_words = (Day, Easy)

def good_aftermath():    
    os.system("cls")
    fast_print(random.choice(victory_words))
    Player.Xp += 100
    Player.level += 5
    Player.light_level += 3
    if Player.light_level > 3:
        Player.light_attack + 35
    progressionChecker.progress += 1
    progressionChecker.victories += 1
    Player.coins += 750
    fast_print(f"Level up! {Player.level} Total XP: {Player.Xp} Items gained: None\n")
    input()
    mainMenu()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
Regular = "You have fallen in battle! No rewards "
Rough = "Better luck next time eh? No rewards for you! "
loser_words = (Regular, Rough)  
def bad_aftermath():       
    os.system("cls")
    fast_print(random.choice(loser_words))
    input()
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
    print(f"Number of Vctories: {Player.victories}")
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
def light_mages_hideout():
    os.system("cls")
    if progressionChecker.first_Time_In_Light_Mage_Hideout == 0:
        os.system("cls")
        #break this into small peices of text with a delay print
        print(' Narrator:\n"Hidden within a sacred mountain and concealed by an illusionary rock face, the Ancient Light Hideout was once a refuge for a mystical order of light-wielding mages.\nInside, the walls are embedded with luminous crystals that emit a soft, ambient light, creating an atmosphere of calm and serenity.\nThe architecture is elegant and ethereal, with high vaulted ceilings, sweeping archways, and intricate carvings depicting scenes of light’s triumph over darkness.\nThe central area of the hideout is a large, circular chamber with a domed ceiling featuring a grand mosaic of a radiant sun, serving as a gathering place and housing a central altar for light-based rituals.\nUnderneath the mosaic is a fireplace. Branching off from the main chamber are living quarters with simple, comfortable furnishings, and a vast library filled with ancient texts detailing the secrets of light magic.\nAdditionally, there is a spacious training hall with mirrored walls for practicing light magic, and an indoor garden illuminated by sunlight channeled through crystal prisms, filled with bioluminescent plants and flowers.\nGuarding the hideout are ethereal light spirits and ancient statues that come to life in times of need. There are also meaning intruging things around that seem to peak your curiosity \nAll of this makes up the Ancient Light Hideout a place of mystery, light, and adventure.')
        input('\n')
        os.system("cls")
        print(' Narrator:\n"As you make your way through the Ancient Light Hideout, you come to see a training hall full of light mages practicing their light magic. Isaiah then pulls you aside to tell you a few things...')
        input('\n')
        os.system("cls")
        print(' Isaiah:\n"Let me teach you the basics real quick on how to fight and get weapons and armor! First off to get weapons you can buy them from the shop and you can also switch weapons in your inventory. You get paid in coins when you defeat spirits, which you use to buy weapons, as well as armor. Your armor provides a boost of defense as well!" ') 
        input('\n')
        os.system("cls")
        print(' Narrator:\n"Isaiah then hands you a medium sized bag filled with coins. He also recommends you go buy some armor again. "Dont spend it all in the small place" He adds with a smirk.')
        input('\n')
        print(' (To yourself) "How can he tell me not to spend it all in one place when I can only spend it on weapons and armor, which are technically in the same place?"')
        input('\n')
        os.system("cls")
        entry_point_light_mage_hideout()
def entry_point_light_mage_hideout():    
        os.system("cls")
        print("******************************************************")
        print("Welcome to the Light Mage Hideout!")
        print(f"\n-------------------------\n")
        print("[1] Go to the shop to get some weapons and armor.")
        print("[2] Go to the fireplace to warm up.")
        print("[3] Wander around the hideout to find some cool things.")
        print("[4] Go to bed/rest. ")
        match input(f"Choose your action, {userName}: "):
            case '1':
                shop()
            case '2':
                fire_place()
            case '3':
                wander_around_hideout()
            case '4':
                players_room()
            case _:
                print("Invalid input, please try again.")
                entry_point_light_mage_hideout()
    
#--- This code is going to be replaced with actual code. ---#    
def wander_around_hideout():
    os.system("cls")
    print("  You wander around the hideout, trying to find anything inturging you find a large board with papers on it.")
    input('\n')
    print(' ???:\n"You seem new around here, my names Voithos pronuced Vee-thos. This is a board full of quests you can take."')
    input('\n')
    print('  Voithos\n"These quests can be very rewarding. If you complete a quest you will receive coins, but beware for they are also dangerous..."')
    input('\n')
    os.system("cls")
    print("[1] Inspect the quest board")
    print("[2] Ignore")
    match input(f"Choose your action: {userName}: "):
        case '1':
            os.system("cls")
            print("  Narrator:\nYou inspect the quest board. There are many different quests, some of which are very dangerous.")
            input('\n')
            print(' "You decide to go for a small quest for now thinking later you will choose to go for the biggers ones it says: Defeat the fire spirit and his minions."')
            input('\n')
            os.system("cls")
            print(' Isaiah comes back after his fight with the dragon a little scathed but with a new weapon thats draws all eyes around him. Isaiah:\n"I see you found a quest you should get some rest first lets get you to bed tough guy."')
            input('\n')
            print(' Narrator:\n"After a day of being woken up to a stranger, and fighting a windspirit you go to bed. You follow Isaiah to a small chamber and find a room.')
            input('\n')
            os.system("cls")
            print(' Narrator:\n"As you step into your room, sunlight pours through the large windows, illuminating the space with a soft, warm glow.\nCrystal chandeliers and floating orbs cast a gentle light, while pastel furnishings and enchanted plants create an atmosphere of serene, magical beauty.')
            input('\n')
            print(' You:\n"If we are underground how is there sunlight in this room?"')
            input('\n')
            os.system("cls")
            print(' Isaiah smurks and says:\n"Thats magic. What you dont like it?"')
            input('\n')
            print(' You trying not to be rude respond with:\nNo, its super cool never seen anything like it before. I\'m going to go get some rest. Then do the quest in the morning."')
            os.system("cls")
            print(' Isaiah:\n"Alright, I will go get some rest aswell. You can take your rest now. I\'ll escort you to your quest in the morning."')
            input('\n')
            os.system("cls")
            print("WIP")
        case '2':
            print("You decide to continue your wandering around the hideout.")
            light_mages_hideout()
        case _:
            print("Invalid input, please try again.")
                            
def fire_place():
    os.system("cls")
    input('\n')
    print('  Narrator:\n"As you step closer to the fireplace, you feel a newfound sense of peace forgetting about all your worries. You hear and feel the fireplace whispers to you, ancient secrets. You hear the sound of a battle and the laughter almost, frighting but also endearing in a way.\nAs if a long lost friend is trying to tell you a story."')
    input('\n')
    print('  ???:\n"You\'ve seem to find the fireplace intriuging eh? Well my names Anagnostis, pronuced Ah-nah-gnoh-stees. When I first came here I found it intruging aswell. If you would like to go to the library to get some books on our anciet history, I\'d be happy to show you where it is."')
    input('\n')
    print("[1] Go to the library")
    print("[2] Continue your wandering around the hideout.")
    match input(f"Choose your action, {userName}: "):
        case '1':
            light_mages_library()
        case '2':
            print("You decide to continue your wandering around the hideout.")
            input('\n')
            entry_point_light_mage_hideout()
        case _:
            print("Invalid input, please try again.")
            input()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#WIP
def light_mages_library():
    os.system("cls")
    if progressionChecker.first_time_entered_light_mage_library == True:
        print("[1] Find books about War")
        print("[2] Find books about Magic")
        print("[3] Find books about History")
        print("[4] Find books about Prophecy")
        print("[4] Go to Room")
        match input(f"Choose your action: {userName}"):
            case '1':
                print("You pick up a book about war heres what it says:")
                print("TITLE: The Prophecy of the Tratior")
                print("Author: There is said to ")
                input()
                light_mages_library()
            case '2':
                print("You find books about magic.")
                input()
                light_mages_library()
            case '3':
                print("You find books about history.")
                input()
                light_mages_library()
            case '4':
                print("You find books about prophecy.")
                input()
                light_mages_library()
            case '5':
                print("You Go to your room.")
                input()
                light_mages_library()
    if progressionChecker.first_time_entered_light_mage_library == False:
        progressionChecker.first_time_entered_light_mage_library = True
        print("\n-------------------------\n")
        print("Anagnostis:\n"'"The library is a place where you can learn about history, magic, and war. It has many books on all things. I recommend staying here and learning some things."')
        input('\n')
        print("[1] Find books about War")
        print("[2] Find books about Magic")
        print("[3] Find books about History")
        print("[4] Find books about Prophecy")
        print("[4] Go to Room")
        match input(f"Choose your action: {userName}"):
            case '1':
                print("You pick up a book about war. Here's what it says:")
                input()
                os.system("cls")
                print("TITLE: The Prophecy of Shadows")
                print("Author: UNKNOWN SAGE")
                print("Story:")
                print("Within these pages unfolds a haunting prophecy of the Shadows.")
                input('\n')
                print("As the forces of light battle against darkness, the Shadows appear defeated.")
                input('\n')
                print("Yet amidst this conflict, a traitor may emerge.")
                input('\n')
                print("The line between friend and foe will blur.")
                input('\n')
                print("We, wise sages of ages past, cannot foresee the future.")
                input('\n')
                print("But we wish you luck.") 
                #The traitor shall be one you know, you would not wish to fight him as you do want to kill neither a friend nor a foe.
                print("Proditor erit quis novisti, nec pugnare vis cum eo, nam neque amicum neque inimicum interficere cupis.")
                input('\n')
                print("  Narrator:\nYou put the book down feeling uneasy.")
                input()
                light_mages_library()
            case '2':
                print("You find a bookk about magic.")
                input()
                print("TITLE: Radiance Unveiled: The Genesis of Light Magic")
                #name means light of fire
                print("Author: Lucius Ignis")
                input('\n')
                print("In the dawn of ancient times, when darkness threatened to engulf the world, wise sages sought a beacon of hope.")
                input('\n')
                print("Through years of study and meditation, they discovered the radiant essence woven into the fabric of the cosmos.")
                input('\n')
                print("Harnessing this ethereal light, they forged the art of light magic, weaving spells of illumination and protection.")
                input('\n')
                print("With each generation, the knowledge grew, passed down through scrolls and whispered in the halls of mystical academies.")
                input('\n')
                print("Today, light magic stands as a testament to the enduring spirit of enlightenment and the eternal battle against the shadows.")
                input()
                print("You put the book down.")
                light_mages_library()
            case '3':
                print("You find books about history.")
                input()
                light_mages_library()
            case '4':
                print("You find books about prophecy.")
                input()
                light_mages_library()
            case '5':
                print("You Go to your room.")
                input()
                light_mages_library()
            case _:
                print("Invalid input, please try again.")
                input()
                light_mages_library()

        
def players_room():
    print("[1] Go to bed")
    print("[2] Go to the shop")
    print("[3] Go to the library")
    print("[4] Go to find mission")
    match input(f"Where do you head off to now? {userName}: "):
        case '1':
            print("You go to bed fully rested.")
            input()
            players_room()
        case '2':
            print("You go to the shop.")
            input()
            shop()
        case '3':
            print("You go to the library.")
            input()
            light_mages_library()
        case '4':
            print("You go to find a mission heading towards to mission board.")
            input()
            find_mission_area()
        case _:
            print("Invalid input, please try again.")
            input()
            players_room()


def find_mission_area():
    print("[1] Defeat the fire spirit and his minions (FIRE DUNGEON) [Cost: 550 coins to attempt].")
    print("[2] Defeat the wind spirit and his minions (WIND DUNGEON). [Cost: 300 coins to attempt].")
    print("[3] Defeat the earth spirit and his minions. (EARTH DUNGEON) [Cost: 450 coins to attempt].")
    print("[4] Go to the water spirit and his minions. (WATER DUNGEON). [Cost: 1250 coins to attpment]")
    print("[5] Go back to room to ponder about what choice you should make..")
    match input (f"Choose your action: {userName}"):
        case '1':
            if progressionChecker.defeated_fire_dungeon == True:
                print("You have already defeated the fire dungeon cannot go again.")
            elif Player.coins <= 549:
                print("You do not have enough coins to attempt the fire dungeon.")
                find_mission_area()
            else:
                print("You decide to venture to the fire dungeon.")
                fire_dungeon()
        case '2':
            if progressionChecker.defeated_wind_dungeon == True:
                print("You have already defeated the wind dungeon cannot go again.")
            elif Player.coins <= 299:
                print("You do not have enough coins to attempt the wind dungeon.")
                find_mission_area()
            else:
                print("You decide to venture to the wind dungeon.")
                wind_dungeon()
        case '3':
            if progressionChecker.defeated_earth_dungeon == True:
                print("You have already defeated the earth dungeon cannot go again.")
            elif Player.coins <= 449:
                print("You do not have enough coins to attempt the earth dungeon.")
                find_mission_area()
            else:
                print("You decide to venture to the earth dungeon.")
                earth_dungeon()
        case '4':
            if progressionChecker.defeated_water_dungeon == True:
                print("You have already defeated the water dungeon cannot go again.")
            elif Player.coins <= 1249:
                print("You do not have enough coins to attempt the water dungeon.")
                find_mission_area()
            else:
                print("You decide to venture to the water dungeon.")
                water_dungeon()
        case '5':
            print("You decide to return to the room to ponder about what choice you should make.")
            input()
            players_room()

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
def armor_system():
    os.system("cls")
    print(f"Your current number of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print("Equipped Armor: " + Player.equipped_armor.name if Player.equipped_armor else "No armor equipped")
    print("\nArmors:")
    for i, armor in enumerate(Player.armor_collection, start=1):
        print(f"[{i}] Armor Name: {armor.name}: Added Defense: +{armor.added_defense}\n======================================================================================================================\n")
    print("\n\n\nType 'm' to go to main menu")
    choice = input("What would you like to do?: ")
    match choice:
        case 'm':
            mainMenu()
        case choice:
            if choice.isdigit():
                user_input = int(choice) - 1
                if 0 <= user_input < len(Player.armor_collection):
                    Player.equipped_armor = Player.armor_collection[user_input]
                    fast_print(f"You have equipped {Player.equipped_armor.name}.")
                    input()
                    armor_system()
                else:
                    print("Invalid option. Press ENTER to continue.")
                    input()
                    armor_system()
            else:
                print("Invalid option. Press ENTER to continue.")
                input()
                armor_system()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
def weapon_system():
    os.system("cls")
    print(f"Your current number of coins: {Player.coins}\n-------------------------------------------------------------------------------------------------------------------------------\n")
    print("Equipped Weapon: " + Player.equipped_weapon.name if Player.equipped_weapon else "No weapon equipped")
    print("\nWeapons:")
    for i, weapon in enumerate(Player.weapons_collection, start=1):
        print(f"[{i}] Weapon Name: {weapon.name}: Range of Damage: {weapon.attack}\n======================================================================================================================\n")
    print("\n\n\nType 'm' to go to main menu")
    choice = input("What would you like to do?: ")
    match choice:
        case 'm':
            mainMenu()
        case choice:
            if choice.isdigit():
                user_input = int(choice) - 1
                if 0 <= user_input < len(Player.weapons_collection):
                    Player.equipped_weapon = Player.weapons_collection[user_input]
                    fast_print(f"You have equipped {Player.equipped_weapon.name}.")
                    input()
                    weapon_system()
                else:
                    print("Invalid option. Press ENTER to continue.")
                    input()
                    weapon_system()
            else:
                print("Invalid option. Press ENTER to continue.")
                input()
                weapon_system()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

def fire_dungeon():
    ...
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

def water_dungeon():
    ...
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
def wind_dungeon():
    ...
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
def earth_dungeon():    
    ...
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
def loot_trade_hub():
    ...
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------


mainMenu()












