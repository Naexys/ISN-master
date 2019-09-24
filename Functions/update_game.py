import pygame
from math import floor
from intValues import *
from Objects.objects_init import *
from Class.Entity.Character.Character import Character
from Class.Entity.Projectile.Projectile import Projectile
from Class.Terrain.Block import Block
from Class.Entity.SpecialEntity.Teleporter import Teleporter
from Objects.Entity.Enemy.Enemy import *
from Functions.Controls.Mouse.mouse_position import mouse_position
from Functions.change_heroes import *
if raspberry:
    from Functions.Server.client import *
load_objects()


def update_game(win, count):
    win.fill((0, 0, 0))

    pygame.draw.circle(win, (28, 28, 28), (floor(Character.charact_list[0].g_point[0]), floor(Character.charact_list[0].g_point[1])), MOUSER, 0)

    for obj in Projectile.proj_list:
        obj.update(win)
    for obj in Block.block_list:
        obj.update(win)
    for obj in Teleporter.teleporter_list:
        obj.update(win)
    for obj in Enemy.enemy_list:
        obj.update(win)
    for obj in Character.charact_list:
        obj.update(win)


    mouse_position()
    switch_heroes()




    #   update each second
    if raspberry:
        if count == 120:
            msgx = "actu"
            Sock.send(msgx.encode())






    pygame.display.update()
