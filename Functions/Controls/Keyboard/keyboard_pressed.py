import pygame


def keyboard_pressed():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        return "left"

    elif keys[pygame.K_d]:
        return "right"

    elif keys[pygame.K_w]:
        return "top"

    elif keys[pygame.K_s]:
        return "bottom"

    elif keys[pygame.K_SPACE]:
        return "space"

    elif keys[pygame.K_TAB]:
        return "tab"

    elif keys[pygame.K_f]:
        return "f"

    elif keys[pygame.K_F1]:
        return "F1"

    elif keys[pygame.K_F2]:
        return "F2"

    else:
        return 0


