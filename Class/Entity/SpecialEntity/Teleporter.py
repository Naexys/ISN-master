import pygame
from Class.HUD.LoadingBar import LoadingBar


class Teleporter():
    teleporter_hit = [pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)]
    teleporter_list = []

    def __init__(self, _x0, _y0, _x1, _y1):
        self._x0 = _x0
        self._y0 = _y0
        self._x1 = _x1
        self._y1 = _y1
        self._hitbox0 = pygame.Rect(_x0, _y0, 100, 25)
        self._hitbox1 = pygame.Rect(_x1, _y1, 100, 25)
        self._load0 = LoadingBar(_x=self._x0 + 35, _y=self._y0 - 10, _width=15, _height=10, _max_range=810, _dynamic_color=True)
        self._load1 = LoadingBar(_x=self._x1 + 35, _y=self._y1 - 10, _width=15, _height=10, _max_range=810, _dynamic_color=True)
        self._teleporter_loop = 0
        Teleporter.teleporter_list.append(self)
        self._f_append = False

    # Accessor and mutator of x0
    def _get_x0(self):
        return self._x0

    def _set_x0(self, value):
        self._x0 = value

    x0 = property(_get_x0, _set_x0)

    # Accessor and mutator of y0
    def _get_y0(self):
        return self._y0

    def _set_y0(self, value):
        self._y0 = value

    y0 = property(_get_y0, _set_y0)

    # Accessor and mutator of x1
    def _get_x1(self):
        return self._x1

    def _set_x1(self, value):
        self._x1 = value

    x1 = property(_get_x1, _set_x1)

    # Accessor and mutator of y1
    def _get_y1(self):
        return self._y1

    def _set_y1(self, value):
        self._y1 = value

    y1 = property(_get_y1, _set_y1)

    # Accessor of teleporter_loop
    def _get_teleporter_loop(self):
        return self._teleporter_loop

    teleporter_loop = property(_get_teleporter_loop)

    def draw(self, win):
        pygame.draw.rect(win, (0, 255, 255), (self._x0, self._y0, 50, 125), 0)
        pygame.draw.rect(win, (0, 255, 255), (self._x1, self._y1, 50, 125), 0)

    def delete(self):
        Teleporter.teleporter_list.pop(Teleporter.teleporter_list.index(self))
        del self

    def teleport(self):
        x = self._x0 - self._x1
        y = self._y0 - self._y1
        return x, y

    def life_cloak(self):
        if self._teleporter_loop <= 810:
            self._teleporter_loop += 1
        else:
            self.delete()

    def hitbox_update(self):
        if self._teleporter_loop <= 800:
            self._hitbox0 = pygame.Rect(self._x0, self._y0, 50, 125)
            self._hitbox1 = pygame.Rect(self._x1, self._y1, 50, 125)
        else:
            self._hitbox0 = pygame.Rect(0, 0, 0, 0)
            self._hitbox1 = pygame.Rect(0, 0, 0, 0)

        Teleporter.teleporter_hit[0] = self._hitbox0
        Teleporter.teleporter_hit[1] = self._hitbox1

    def scrolling_right(self, speed):
        self._x0 -= speed
        self._x1 -= speed
        self.hitbox_update()

    def scrolling_left(self, speed):
        self._x0 += speed
        self._x1 += speed
        self.hitbox_update()

    def scrolling_vertical(self, velocity):
        self._y0 += velocity
        self._y1 += velocity
        self.hitbox_update()

    def move(self, x, y):
        self._x0 -= x
        self._x1 -= x
        self._y0 -= y
        self._y1 -= y

    def hud(self, win):
        self._load0.update(win, self._teleporter_loop)
        self._load1.update(win, self._teleporter_loop)
        self._load0.x = self._x0 + 35
        self._load1.x = self._x1 + 35
        self._load0.y = self._y0 - 10
        self._load1.y = self._y1 - 10
        if self._teleporter_loop >= 809:
            self._load0.delete()
            self._load1.delete()

    def update(self, win):
        self.life_cloak()
        if self._teleporter_loop <= 809:
            self.hud(win)
        self.teleport()
        self.draw(win)
