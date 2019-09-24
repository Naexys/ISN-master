import pygame, time, sys
from intValues import *
from pygame.locals import *
from Functions.update_game import update_game
from Objects.objects_init import load_objects
if raspberry:
    from Functions.Server.client import *

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projet ISN")

count = 0

# Mainloop
run = True

# HORLOGE
clock = pygame.time.Clock()



while run:



    clock.tick(TICKRATES)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT or keys[pygame.K_END] or keys[pygame.K_DELETE]:
            run = False

    update_game(win, count)
    #   update server each second
    if count >= 120:
        count = 0
    else:
        count += 1



if raspberry:
    time.sleep(1)
    msgx="escape"
    Sock.send(msgx.encode())

pygame.quit()
sys.exit()
