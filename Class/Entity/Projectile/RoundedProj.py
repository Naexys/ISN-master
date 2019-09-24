import pygame
from Class.Entity.Projectile.Projectile import Projectile
from intValues import *
from math import floor
from Class.Terrain.Block import Block
from Class.Entity.Enemy.Enemy import Enemy


class RoundedProj(Projectile):
    """Class for creating round shaped projectiles from the projectile class"""

    def __init__(self, _x, _y, _v, _radius, _orientationX, _orientationY, _damage):
        Projectile.__init__(self, _x, _y, _v, _damage)
        self._radius = _radius
        self._orientationX = _orientationX
        self._orientationY = _orientationY
        self._hitbox = pygame.Rect(self._x - self._radius, self._y - self._radius, self._radius * 2, self._radius * 2)

    # Method to draw the projectile
    def draw(self, win):
        pygame.draw.circle(win, (0, 255, 255), (floor(self._x), floor(self._y)), self._radius)

    # Method to actualised the hitbox
    def hitbox_update(self):
        self._hitbox = pygame.Rect(self._x - self._radius, self._y - self._radius, self._radius * 2, self._radius * 2)

    # Method to delete the projectile if he collide something
    def collide(self):
        if self._x > WIDTH + WIDTH / 2 or self._x < -WIDTH / 2 or self._y < - HEIGHT / 2 or self._y > HEIGHT + HEIGHT / 2:
            self.delete()

        if not self._hitbox.collidelist(Block.block_hit) == -1:
            self.delete()
        if not self._hitbox.collidelist(Enemy.enemy_hitlist) == -1:
            num = self._hitbox.collidelist(Enemy.enemy_hitlist)
            Enemy.enemy_list[num].health -= self._damage
            self.delete()

    # Methode to define the movement of the projectile across the map
    def movement(self):
        self._x += self._orientationX
        self._y -= self._orientationY

        self.hitbox_update()

    # Method to update all things
    def update(self, win):
        self.movement()
        self.collide()
        self.draw(win)
