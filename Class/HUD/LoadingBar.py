import pygame
from math import floor


class LoadingBar(object):
    loading_bar_list = []

    def __init__(self, _x, _y, _width, _height, _max_range=100, _dynamic_color=False, _thickness=1):
        self._x = _x
        self._y = _y
        self._width = _width
        self._height = _height
        self._max_range = _max_range
        self._dynamic_color = _dynamic_color
        self._thickness = _thickness
        LoadingBar.loading_bar_list.append(self)

    # Accessor and mutator of x0
    def _get_x(self):
        return self._x

    def _set_x(self, value):
        self._x = value

    x = property(_get_x, _set_x)

    # Accessor and mutator of y
    def _get_y(self):
        return self._y

    def _set_y(self, value):
        self._y = value

    y = property(_get_y, _set_y)

    def draw(self, win, progress_bar):
        red = floor(255 - ((progress_bar * 255) / self._max_range))
        green = floor((progress_bar * 255) / self._max_range)

        if not self._dynamic_color:
            pygame.draw.rect(win, (0, 255, 0),
                             (self._x + self._thickness, self._y, (progress_bar * (self._width - self._thickness)) / self._max_range, self._height),
                             0)
        else:
            pygame.draw.rect(win, (red, green, 0),
                             (self._x + self._thickness, self._y, (progress_bar * (self._width - self._thickness)) / self._max_range, self._height),
                             0)

        pygame.draw.rect(win, (255, 255, 255), (self._x, self._y, self._width, self._height), self._thickness)

    def delete(self):
        LoadingBar.loading_bar_list.pop(LoadingBar.loading_bar_list.index(self))
        del self

    def update(self, win, progress_bar):
        self.draw(win, progress_bar)
