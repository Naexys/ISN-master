from Class.Entity.Character.Character import Character, pygame
from Class.Entity.Projectile.RoundedProj import RoundedProj
from Functions.Controls.Mouse.mouse_pressed import mouse_pressed
from Class.Entity.SpecialEntity.Teleporter import Teleporter


class Symmetra(Character):

    def __init__(self, _w, _h, _m, _g, _health, _speed, _shooting_rates):
        Character.__init__(self, _w, _h, _m, _g, _health, _speed, _shooting_rates)
        self._delay = 0

    def shooting(self):
        if self._shoot_loop >= 0:
            self._shoot_loop += 1
        if self._shoot_loop > self._shooting_rates:
            self._shoot_loop = self._shooting_rates

        if mouse_pressed() == "right" and len(RoundedProj.proj_list) <= 25 and self._shoot_loop == self._shooting_rates:
            RoundedProj(_x=self._g_point[0], _y=self._g_point[1], _v=3, _radius=10, _orientationX=(pygame.mouse.get_pos()[0] - self._g_point[0]) / 30,
                        _orientationY=-(pygame.mouse.get_pos()[1] - self._g_point[1]) / 30, _damage=50)
            self._shoot_loop = 0

    def portal(self):
        if mouse_pressed() == "left" and not len(Teleporter.teleporter_list) > 0 and self._delay == 0:
            if pygame.mouse.get_pos()[0] - self._g_point[0] >= 0 and pygame.mouse.get_pos()[1] - self._g_point[1] <= 0:
                Teleporter(_x0=(pygame.mouse.get_pos()[0]), _y0=(pygame.mouse.get_pos()[1]) - 125, _x1=self._g_point[0] - 25,
                           _y1=self._g_point[1] - 75)
            elif pygame.mouse.get_pos()[0] - self._g_point[0] <= 0 and pygame.mouse.get_pos()[1] - self._g_point[1] <= 0:
                Teleporter(_x0=(pygame.mouse.get_pos()[0]) - 50, _y0=(pygame.mouse.get_pos()[1]) - 125, _x1=self._g_point[0] - 25,
                           _y1=self._g_point[1] - 75)
            elif pygame.mouse.get_pos()[0] - self._g_point[0] >= 0 and pygame.mouse.get_pos()[1] - self._g_point[1] >= 0:
                Teleporter(_x0=(pygame.mouse.get_pos()[0]), _y0=(pygame.mouse.get_pos()[1]), _x1=self._g_point[0] - 25,
                           _y1=self._g_point[1] - 75)
            else:
                Teleporter(_x0=(pygame.mouse.get_pos()[0]) - 50, _y0=(pygame.mouse.get_pos()[1]), _x1=self._g_point[0] - 25,
                           _y1=self._g_point[1] - 75)
            self._delay = 100

        if not self._delay == 0:
            self._delay -= 1

    def update(self, win):
        self.portal()
        self.hud(win)
        self.movement()
        self.collisions()
        self.shooting()
        self.draw(win)
