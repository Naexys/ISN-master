import pygame


class Enemy(object):
    enemy_list = []
    enemy_hitlist = []

    def __init__(self, _x, _y, _w, _h, _walk_left, _walk_right, _path=(False, 0), _health=100, _gender="/Tiki/Rush"):
        self._x = _x
        self._y = _y
        self._w = _w
        self._h = _h
        self._path = _path
        self._health = _health
        self._walk_count = 0
        self._hitbox = pygame.Rect(_x, _y, _w, _h)
        Enemy.enemy_list.append(self)
        Enemy.enemy_hitlist.append(pygame.Rect(_x, _y, _w, _h))

        self._walk_left = _walk_left
        self._walk_right = _walk_right
        self._count = 0
        self._gender = _gender

        #   Init this way because you start by walking right, else you'll have the first animation which isn't loaded
        self._img_max = len(self._walk_right)

        #   Init an image
        self._enemy = pygame.image.load("Assets/enemy" + self._gender + "/WalkRight/" + self._walk_right[0])

    def _get_health(self):
        return self._health

    def _set_health(self, value):
        self._health = value

    health = property(_get_health, _set_health)

    def draw(self, win):
        #pygame.draw.rect(win, (255, 0, 0), (self._x, self._y, self._w, self._h), 0)

        self._enemy = self._enemy.convert_alpha()
        self._enemy = pygame.transform.scale(self._enemy, (200, 200))
        win.blit(self._enemy, (self._x, self._y))
    
    def hitbox_update(self):
        Enemy.enemy_hitlist.pop(Enemy.enemy_hitlist.index(self._hitbox))
        self._hitbox = pygame.Rect(self._x, self._y, self._w, self._h)
        Enemy.enemy_hitlist.append(self._hitbox)
    
    def movement(self):
        if self._path[0] and self._walk_count > 0:
            self._x += 1
            self._walk_count += 1

            ###
            self._img_max = len(self._walk_right)
            if self._count < self._img_max:
                self._enemy = pygame.image.load("Assets/enemy" + self._gender + "/WalkRight/" + self._walk_right[self._count])
                self._count += 1
            #   if he's walking, print the image
            else:
                self._count = 0
            ###

            if self._walk_count == self._path[1]:
                self._walk_count = -self._path[1]
        elif self._path[0] and self._walk_count <= 0:
            self._x -= 1
            self._walk_count += 1

            ###
            self._img_max = len(self._walk_left)
            if self._count < self._img_max:
                self._enemy = pygame.image.load("Assets/enemy" + self._gender + "/WalkLeft/" + self._walk_left[self._count])
                self._count += 1
            #   if he's walking, print the image
            else:
                self._count = 0
            ###



    def delete(self):
        Enemy.enemy_list.pop(Enemy.enemy_list.index(self))
        del self
    
    def scrolling_right(self, speed):
        self._x -= speed

    def scrolling_left(self, speed):
        self._x += speed

    def scrolling_vertical(self, velocity):
        self._y += velocity

    def move(self, x, y):
        self._x -= x
        self._y -= y
    
    def update(self, win):
        self.draw(win)
        self.movement()
        self.hitbox_update()
        #print(self._health)
        if self._health <= 0:
            self.delete()