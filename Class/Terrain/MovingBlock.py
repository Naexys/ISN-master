from Class.Terrain.Block import Block
from Assets.load_textures import *


class MovingBlock(Block):
    def __init__(self, _x, _y, _w, _h, _texture, _is_moving_x=(False, 0), _is_moving_y=(False, 0)):
        Block.__init__(self, _x, _y, _w, _h, _texture)
        self._is_moving_x = _is_moving_x
        self._is_moving_y = _is_moving_y
        self._walk_count = 0
        if _is_moving_x[0]:
            self._block_type = "Moving_Block_X"
        else:
            self._block_type = "Moving_Block_Y"
            self._is_trav_bottom = True
            self._is_trav_right = True
            self._is_trav_left = True

    def movement(self):
        if self._is_moving_y[0] and self._walk_count >= 0:
            self._y += 0.5
            self._walk_count += 1
            self._block_position = True
            if self._walk_count == self._is_moving_y[1]:
                self._walk_count = -self._is_moving_y[1]
        elif self._is_moving_y[0] and self._walk_count < 0:
            self._y -= 0.5
            self._walk_count += 1
            self._block_position = False

        if self._is_moving_x[0] and self._walk_count > 0:
            self._x += 0.5
            self._walk_count += 1
            if self._walk_count == self._is_moving_x[1]:
                self._walk_count = -self._is_moving_x[1]
        elif self._is_moving_x[0] and self._walk_count <= 0:
            self._x -= 0.5
            self._walk_count += 1

    def update(self, win):
        self.movement()
        self.hitbox_update()
        self.draw(win)
