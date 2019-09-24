import pygame
from Assets.load_textures import *

class Block(object):
    block_list = []
    block_hit = []
    block_hit_right = []
    block_hit_left = []
    block_hit_top = []
    block_hit_bottom = []

    def __init__(self, _x, _y, _w, _h, _texture, _no_texture=False, _is_no_collision=False,
                 _is_trav_right=False, _is_trav_left=False, _is_trav_top=False, _is_trav_bottom=False, _resize=(False, 0), _parallaxe=(False, 0)):
        self._x = _x
        self._y = _y
        self._w = _w
        self._h = _h
        self._block_type = "Block"
        self._block_position = False
        self._color = (0, 255, 0)
        self._is_no_collision = _is_no_collision
        self._is_trav_right = _is_trav_right
        self._is_trav_left = _is_trav_left
        self._is_trav_top = _is_trav_top
        self._is_trav_bottom = _is_trav_bottom
        self._hitbox = pygame.Rect(self._x, self._y, self._w, self._h)
        self._hitbox_top = pygame.Rect(self._x, self._y, self._w, 10)
        self._hitbox_bottom = pygame.Rect(self._x, self._y + self._h, self._w, 10)
        self._hitbox_left = pygame.Rect(self._x, self._y + 10, 10, self._h)
        self._hitbox_right = pygame.Rect(self._x + self._w - 10, self._y + 10, 10, self._h)
        self._f_append = False
        Block.block_list.append(self)

        self._texture = _texture
        self._no_texture = _no_texture
        self._resize = _resize
        self._parallaxe = _parallaxe

    def _get_x(self):
        return self._x

    def _set_x(self, value):
        self._x = value

    x = property(_get_x, _set_x)

    def _get_y(self):
        return self._y

    def _set_y(self, value):
        self._y = value

    y = property(_get_y, _set_y)

    def _get_w(self):
        return self._w

    def _set_w(self, value):
        self._w = value

    w = property(_get_w, _set_w)

    def _get_h(self):
        return self._h

    def _set_h(self, value):
        self._h = value

    h = property(_get_h, _set_h)

    def _get_block_type(self):
        return self._block_type

    block_type = property(_get_block_type)

    def _get_block_position(self):
        return self._block_position

    block_position = property(_get_block_position)

    def hitbox_update(self):
        if not self._f_append:
            Block.block_hit.append(self._hitbox)
            Block.block_hit_bottom.append(self._hitbox_bottom)
            Block.block_hit_left.append(self._hitbox_left)
            Block.block_hit_right.append(self._hitbox_right)
            Block.block_hit_top.append(self._hitbox_top)
            self._f_append = True

        Block.block_hit.pop(Block.block_hit.index(self._hitbox))
        Block.block_hit_top.pop(Block.block_hit_top.index(self._hitbox_top))
        Block.block_hit_right.pop(Block.block_hit_right.index(self._hitbox_right))
        Block.block_hit_left.pop(Block.block_hit_left.index(self._hitbox_left))
        Block.block_hit_bottom.pop(Block.block_hit_bottom.index(self._hitbox_bottom))

        if not self._is_no_collision:
            if not self._is_trav_top:
                self._hitbox_top = pygame.Rect(self._x, self._y, self._w, 8)
            else:
                self._hitbox_top = pygame.Rect(0, 0, 0, 0)

            if not self._is_trav_bottom:
                self._hitbox_bottom = pygame.Rect(self._x, self._y + self._h, self._w, 8)
            else:
                self._hitbox_bottom = pygame.Rect(0, 0, 0, 0)

            if not self._is_trav_left:
                self._hitbox_left = pygame.Rect(self._x, self._y + 10, 8, self._h)
            else:
                self._hitbox_left = pygame.Rect(0, 0, 0, 0)

            if not self._is_trav_right:
                self._hitbox_right = pygame.Rect(self._x + self._w - 10, self._y + 10, 8, self._h)
            else:
                self._hitbox_right = pygame.Rect(0, 0, 0, 0)

            self._hitbox = pygame.Rect(self._x, self._y, self._w, self._h)
        else:
            self._hitbox = pygame.Rect(0, 0, 0, 0)
            self._hitbox_top = pygame.Rect(0, 0, 0, 0)
            self._hitbox_bottom = pygame.Rect(0, 0, 0, 0)
            self._hitbox_left = pygame.Rect(0, 0, 0, 0)
            self._hitbox_right = pygame.Rect(0, 0, 0, 0)

        Block.block_hit.append(self._hitbox)
        Block.block_hit_bottom.append(self._hitbox_bottom)
        Block.block_hit_left.append(self._hitbox_left)
        Block.block_hit_right.append(self._hitbox_right)
        Block.block_hit_top.append(self._hitbox_top)

    def delete(self):
        Block.block_hit_top.pop(Block.block_hit_top.index(self._hitbox_top))
        Block.block_hit_right.pop(Block.block_hit_right.index(self._hitbox_right))
        Block.block_hit_left.pop(Block.block_hit_left.index(self._hitbox_left))
        Block.block_hit_bottom.pop(Block.block_hit_bottom.index(self._hitbox_bottom))
        Block.block_list.pop(Block.block_list.index(self))
        del self

    def get_pos(self):
        return self._x, self._y

    def draw(self, win):
        #pygame.draw.rect(win, self._color, (self._x, self._y, self._w, self._h), 0)
        if self._resize[0]:
            self._texture = pygame.transform.scale(self._texture, (self._resize[1], self._resize[1]))
        if not self._no_texture:
            win.blit(self._texture, ((self._x, self._y)))
        else:
            pygame.draw.rect(win, self._color, (self._x, self._y, self._w, self._h), 0)

    def scrolling_right(self, speed):
        if self._parallaxe[0]:
            self._x -= speed/self._parallaxe[1]
        else:
            self._x -= speed

        self.hitbox_update()

    def scrolling_left(self, speed):
        if self._parallaxe[0]:
            self._x += speed / self._parallaxe[1]
        else:
            self._x += speed

        self.hitbox_update()

    def scrolling_vertical(self, velocity):
        self._y += velocity
        self.hitbox_update()

    def move(self, x, y):
        self._x -= x
        self._y -= y

    def update(self, win):
        self.draw(win)
