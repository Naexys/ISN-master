class Projectile(object):
    proj_list = []
    """Class allowing to define what a projectile is"""

    def __init__(self, _x, _y, _v, _damage=20):
        self._x = _x
        self._y = _y
        self._v = _v
        self._damage = _damage
        Projectile.proj_list.append(self)

    # Accessor and mutator of x
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

    # Accessor and mutator of velocity
    def _get_v(self):
        return self._v

    def _set_v(self, value):
        self._v = value

    v = property(_get_v, _set_v)

    def scrolling_right(self, speed):
        self._x -= speed

    def scrolling_left(self, speed):
        self._x += speed

    def scrolling_vertical(self, velocity):
        self._y += velocity

    # Method to delete the projectile
    def delete(self):
        Projectile.proj_list.pop(Projectile.proj_list.index(self))
        del self

    # Method to move the projectile across the map
    def move(self, x, y):
        self._x -= x
        self._y -= y
