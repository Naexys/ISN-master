import pygame
pygame.init()
win = pygame.display.set_mode((1, 1))
pygame.display.set_caption("Projet ISN")

playerInit = pygame.image.load("Assets/fireman/WalkRight/pixels_00.png")
playerInit = playerInit.convert_alpha()

fond = pygame.image.load("Assets/level/Map1.png")
fond = fond.convert_alpha()

fond2 = pygame.image.load("Assets/level/Map2.png")
fond2 = fond2.convert_alpha()

mountain = pygame.image.load("Assets/level/lilMountain.png")
mountain = mountain.convert_alpha()

tikiT = pygame.image.load("Assets/level/TikiTotem.png")
tikiT = tikiT.convert_alpha()

tree = pygame.image.load("Assets/level/tree.png")
tree = tree.convert_alpha()

tree2 = pygame.image.load("Assets/level/tree2.png")
tree2 = tree2.convert_alpha()

tree3 = pygame.image.load("Assets/level/tree3.png")
tree3 = tree3.convert_alpha()

spearLeft = pygame.image.load("Assets/enemy/Tiki/Items/SpearLeft.png")
spearLeft = spearLeft.convert_alpha()

spearRight = pygame.image.load("Assets/enemy/Tiki/Items/SpearRight.png")
spearRight = spearRight.convert_alpha()

fireball = pygame.image.load("Assets/other/fireball.png")
fireball = fireball.convert_alpha()

interogation = pygame.image.load("Assets/other/pixels_04.png")
interogation = interogation.convert_alpha()

blank = pygame.image.load("Assets/other/blank.png")
blank = blank.convert_alpha()

nothing = pygame.image.load("Assets/other/nothing.png")
nothing = nothing.convert_alpha()

ladderT = pygame.image.load("Assets/other/Ladder.png")
ladderT = ladderT.convert_alpha()


walkRightFireman = ["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png",
                    "pixels_05.png",
                    "pixels_06.png", "pixels_07.png",
                    "pixels_08.png", "pixels_09.png", "pixels_10.png", "pixels_11.png", "pixels_12.png",
                    "pixels_13.png",
                    "pixels_14.png", "pixels_15.png",
                    "pixels_18.png", "pixels_19.png", "pixels_20.png", "pixels_21.png", "pixels_00.png"]
walkLeftFireman = ["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png", "pixels_05.png",
                   "pixels_06.png", "pixels_07.png",
                   "pixels_08.png", "pixels_09.png", "pixels_10.png", "pixels_11.png", "pixels_12.png", "pixels_13.png",
                   "pixels_14.png", "pixels_15.png",
                   "pixels_18.png", "pixels_19.png", "pixels_20.png", "pixels_21.png", "pixels_00.png"]
jumpFireman = ["pixels_05.png", "pixels_06.png", "pixels_07.png", "pixels_08.png"]
fallFireman = ["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png"]
afkFireman = ["pixels_00.png", "pixels_00.png", "pixels_00.png", "pixels_00.png", "pixels_01.png", "pixels_01.png",
              "pixels_01.png", "pixels_01.png",
              "pixels_02.png", "pixels_02.png", "pixels_02.png", "pixels_02.png", "pixels_03.png", "pixels_03.png",
              "pixels_03.png", "pixels_03.png",
              "pixels_04.png", "pixels_04.png", "pixels_04.png", "pixels_04.png", "pixels_05.png", "pixels_05.png",
              "pixels_05.png", "pixels_05.png",
              "pixels_06.png", "pixels_06.png", "pixels_06.png", "pixels_06.png", "pixels_07.png", "pixels_07.png",
              "pixels_07.png", "pixels_07.png",
              "pixels_08.png", "pixels_08.png", "pixels_08.png", "pixels_08.png", "pixels_09.png", "pixels_09.png",
              "pixels_09.png", "pixels_09.png",
              "pixels_10.png", "pixels_10.png", "pixels_10.png", "pixels_10.png", "pixels_11.png", "pixels_11.png",
              "pixels_11.png", "pixels_11.png",
              "pixels_12.png", "pixels_12.png", "pixels_12.png", "pixels_12.png"]
attackFireman = [
            "pixels_00.png", "pixels_00.png", "pixels_00.png", "pixels_00.png", "pixels_00.png",
            "pixels_01.png", "pixels_01.png", "pixels_01.png", "pixels_01.png", "pixels_01.png",
            "pixels_02.png", "pixels_02.png", "pixels_02.png", "pixels_02.png", "pixels_02.png",
            "pixels_03.png", "pixels_03.png", "pixels_03.png", "pixels_03.png", "pixels_03.png",
            "pixels_04.png", "pixels_04.png", "pixels_04.png", "pixels_04.png", "pixels_04.png",
            "pixels_05.png", "pixels_05.png", "pixels_05.png", "pixels_05.png", "pixels_05.png",
            "pixels_06.png", "pixels_06.png", "pixels_06.png", "pixels_06.png", "pixels_06.png",
            "pixels_07.png", "pixels_07.png", "pixels_07.png", "pixels_07.png", "pixels_07.png",
            "pixels_08.png", "pixels_08.png", "pixels_08.png", "pixels_08.png", "pixels_08.png",
            "pixels_09.png", "pixels_09.png", "pixels_09.png", "pixels_09.png", "pixels_09.png",
            "pixels_10.png", "pixels_10.png", "pixels_10.png", "pixels_10.png", "pixels_10.png",
            "pixels_11.png", "pixels_11.png", "pixels_11.png", "pixels_11.png", "pixels_11.png",
            "pixels_12.png", "pixels_12.png", "pixels_12.png", "pixels_12.png", "pixels_12.png",
            "pixels_13.png", "pixels_13.png", "pixels_13.png", "pixels_13.png", "pixels_13.png",
            "pixels_14.png", "pixels_14.png", "pixels_14.png", "pixels_14.png", "pixels_14.png",
            "pixels_15.png", "pixels_15.png", "pixels_15.png", "pixels_15.png", "pixels_15.png",
            "pixels_16.png", "pixels_16.png", "pixels_16.png", "pixels_16.png", "pixels_16.png",
            "pixels_17.png", "pixels_17.png", "pixels_17.png", "pixels_17.png", "pixels_17.png",
            "pixels_18.png", "pixels_18.png", "pixels_18.png", "pixels_18.png", "pixels_18.png",
            "pixels_19.png", "pixels_19.png", "pixels_19.png", "pixels_19.png", "pixels_19.png",
            "pixels_20.png", "pixels_20.png", "pixels_20.png", "pixels_20.png", "pixels_20.png",
            "pixels_21.png", "pixels_21.png", "pixels_21.png", "pixels_21.png", "pixels_21.png",
            "pixels_22.png", "pixels_22.png", "pixels_22.png", "pixels_22.png", "pixels_22.png",
            "pixels_23.png", "pixels_23.png", "pixels_23.png", "pixels_23.png", "pixels_23.png",

            "pixels_00.png", "pixels_00.png", "pixels_00.png", "pixels_00.png", "pixels_00.png",
                 ]

walkRightKnight = ["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png", "pixels_05.png",
                   "pixels_06.png", "pixels_07.png", "pixels_08.png", "pixels_09.png", "pixels_10.png", "pixels_11.png",
                   "pixels_12.png", "pixels_13.png"]
walkLeftKnight = ["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png", "pixels_05.png",
                   "pixels_06.png", "pixels_07.png", "pixels_08.png", "pixels_09.png", "pixels_10.png", "pixels_11.png",
                   "pixels_12.png", "pixels_13.png"]
jumpKnight = ["pixels_06.png", "pixels_07.png", "pixels_08.png", "pixels_09.png", "pixels_10.png", "pixels_11.png",
              "pixels_12.png", ]
fallKnight = ["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png", "pixels_05.png",
              "pixels_06.png"]
afkKnight = ["pixels_00.png", "pixels_00.png", "pixels_00.png", "pixels_00.png", "pixels_01.png", "pixels_01.png",
              "pixels_01.png", "pixels_01.png",
              "pixels_02.png", "pixels_02.png", "pixels_02.png", "pixels_02.png", "pixels_03.png", "pixels_03.png",
              "pixels_03.png", "pixels_03.png",
              "pixels_04.png", "pixels_04.png", "pixels_04.png", "pixels_04.png", "pixels_05.png", "pixels_05.png",
              "pixels_05.png", "pixels_05.png",
              "pixels_06.png", "pixels_06.png", "pixels_06.png", "pixels_06.png", "pixels_07.png", "pixels_07.png",
              "pixels_07.png", "pixels_07.png",
              "pixels_08.png", "pixels_08.png", "pixels_08.png", "pixels_08.png", "pixels_09.png", "pixels_09.png",
              "pixels_09.png", "pixels_09.png",
              "pixels_10.png", "pixels_10.png", "pixels_10.png", "pixels_10.png", "pixels_11.png", "pixels_11.png",
              "pixels_11.png", "pixels_11.png",
              "pixels_12.png", "pixels_12.png", "pixels_12.png", "pixels_12.png" ,"pixels_13.png","pixels_13.png",
             "pixels_13.png","pixels_13.png"]
attackKnight = ["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png", "pixels_05.png",
                "pixels_06.png", "pixels_07.png", "pixels_08.png", "pixels_09.png"]

tikiWalkRightRush =["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png",
                    "pixels_05.png",
                    "pixels_06.png", "pixels_07.png",
                    "pixels_08.png", "pixels_09.png"]
tikiWalkLeftRush =["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png",
                    "pixels_05.png",
                    "pixels_06.png", "pixels_07.png",
                    "pixels_08.png", "pixels_09.png"]

tikiWalkRightThrow =["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png",
                    "pixels_05.png",
                    "pixels_06.png", "pixels_07.png",
                    "pixels_08.png", "pixels_09.png"]
tikiWalkLeftThrow =["pixels_00.png", "pixels_01.png", "pixels_02.png", "pixels_03.png", "pixels_04.png",
                    "pixels_05.png",
                    "pixels_06.png", "pixels_07.png",
                    "pixels_08.png", "pixels_09.png"]
