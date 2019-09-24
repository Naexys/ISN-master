import math
import pygame
from intValues import *


def mouse_position():
    mouses = pygame.mouse.get_pressed()
    if not mouses[1]:
        # Permet de calculer la distance entre la souris et le milieu de l'écran
        lenXToMouse = pygame.mouse.get_pos()[0] - WIDTH / 2
        lenYToMouse = pygame.mouse.get_pos()[1] - HEIGHT / 2

        # Permet de calculer l'angle former entre la souris et le milieu de l'écran
        dirToMouse = math.atan2(lenYToMouse, lenXToMouse)

        # Permet d'attribuer la position X et Y de la souris sur le cercle
        mouseXPos = WIDTH / 2 + MOUSER * math.cos(dirToMouse)
        mouseYPos = HEIGHT / 2 + MOUSER * math.sin(dirToMouse)

        # Redefinie la position de la souris sur le cercle
        pygame.mouse.set_pos(mouseXPos, mouseYPos)
