import pygame


def mouse_pressed():
    mouses = pygame.mouse.get_pressed()

    if mouses[2]:
        return "left"
    elif mouses[0]:
        return "right"

    else:
        return 0


