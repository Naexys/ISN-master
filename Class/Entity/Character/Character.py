from intValues import *
from Functions.Controls.Keyboard.keyboard_pressed import keyboard_pressed
from Functions.Controls.Mouse.mouse_pressed import mouse_pressed
from Class.Terrain.Block import Block
from Class.Entity.Projectile import Projectile
from Class.Entity.SpecialEntity.Teleporter import Teleporter
from Class.HUD.LoadingBar import LoadingBar
from Class.Entity.Enemy.Enemy import Enemy
from Assets.load_textures import *
import time


# Class to create a character
class Character(object):
    """ Class defining the creation of a character taking as parameters:
    - width
    - height
    - velocity
    - mass
    - gravity
    - speed
    - shooting rates
    """
    charact_list = []
    charact_hitlist = []

    def __init__(self, _w, _h, _m, _g, _health, _speed, _shooting_rates, _gender="fireman/"):
        """Constructor of the Character class allowing to define the basic characteristics of a character"""

        self._x = X
        self._y = Y
        self._w = _w
        self._h = _h
        self._m = _m
        self._g = _g
        self._speed = _speed
        self._shooting_rates = _shooting_rates
        self._velocity = 1
        self._shoot_loop = 0
        self._wait_pressed = 0
        self._is_jump = False
        self._is_colliding = False
        self._g_point = (self._x + self._w / 2, self._y + self._h / 2)
        self._health = _health
        self._hitbox = pygame.Rect(X, Y, _w, _h)
        self._hitbox_top = pygame.Rect(self._x, self._y, self._w, 0)
        self._hitbox_bottom = pygame.Rect(self._x, self._y + self._h, self._w, 0)
        self._hitbox_left = pygame.Rect(self._x, self._y, 0, self._h)
        self._hitbox_right = pygame.Rect(self.x + self._w, self.y, 0, self._h)
        self._load = LoadingBar(_x=WIDTH / 2 + 35, _y=HEIGHT / 2 - 60, _width=15, _height=10, _max_range=100,
                                _dynamic_color=True)
        Character.charact_list.append(self)
        Character.charact_hitlist.append(self._hitbox)

        # create the self to load the image, the gender is the directory wile the name is for the loading object file

        self._gender = _gender
        self._count = 0
        self._img_max = 0
        self._img_max_attack = 0
        self._player = playerInit
        self._player_to_draw = nothing
        self._x_neg = 0
        self._y_neg = 0
        self._delta_x = 0
        self._delta_y = 0
        self._map = 1

    # Accessor and mutator of the name
    def _get_gender(self):
        return self._gender

    def _set_gender(self, value):
        self._gender = value
        self._count = 0

    # Accessor and mutator of the map
    def _get_map(self):
        return self._map

    def _set_map(self, value):
        self._map = value

    # Accessor and mutator of x
    def _get_x(self):
        return self._x

    x = property(_get_x)

    # Accessor and mutator of y
    def _get_y(self):
        return self._y

    y = property(_get_y)

    # Accessor and mutator of the width
    def _get_w(self):
        return self._w

    def _set_w(self, value):
        self._w = value

    w = property(_get_w, _set_w)

    # Accessor and mutator of the height
    def _get_h(self):
        return self._h

    def _set_h(self, value):
        self._h = value

    h = property(_get_h, _set_h)

    # Accessor and mutator of the mass
    def _get_m(self):
        return self._m

    def _set_m(self, value):
        self._m = value

    m = property(_get_m, _set_m)

    # Accessor and mutator of the constant of gravity
    def _get_g(self):
        return self._g

    def _set_g(self, value):
        self._g = value

    g = property(_get_g, _set_g)

    # Accessor and mutator of the health
    def _get_health(self):
        return self._health

    def _set_health(self, value):
        self._health = value

    health = property(_get_health, _set_health)

    # Accessor and mutator of the speed
    def _get_speed(self):
        return self._speed

    def _set_speed(self, value):
        self._speed = value

    speed = property(_get_speed, _set_speed)

    # Accessor and mutator of the velocity
    def _get_velocity(self):
        return self._velocity

    def _set_velocity(self, value):
        self._velocity = value

    velocity = property(_get_velocity, _set_velocity)

    # Accessor and mutator of the shoot_loop (To know the progress of the reloading of the shot)
    def _get_shoot_loop(self):
        return self._shoot_loop

    def _set_shoot_loop(self, value):
        self._shoot_loop = value

    shoot_loop = property(_get_shoot_loop, _set_shoot_loop)

    # Accessor and mutator of the boolean is_jump (To know if the character is in jump)
    def _get_is_jump(self):
        return self._is_jump

    def _set_is_jump(self, value):
        self._is_jump = value

    is_jump = property(_get_is_jump, _set_is_jump)

    # Accessor and mutator of g_point (center of the character)
    def _get_g_point(self):
        return self._g_point

    def _set_g_point(self, value):
        self._g_point = value

    g_point = property(_get_g_point, _set_g_point)

    #  Character movement method
    def movement(self):
        """Method for defining character movements"""

        # If the player is not in a collision, his fall continues
        if keyboard_pressed() == "space" and not self._is_jump:
            self._is_jump = True
            self.jump()
            if self._is_colliding:
                self._velocity = VELOCITYRESET
                self.jump()

        # Cheating part for flying
        if keyboard_pressed() == "f":
            self._velocity = 5

    # Character Collision Method
    def collisions(self):
        """Method for defining character movements"""

        # If the player is not in a collision, his fall continues until he reaches the ground
        if self._hitbox_bottom.collidelist(Block.block_hit_top) == -1:
            self.falling()
            self._is_colliding = False
            if not self._is_colliding:
                self._is_jump = True
                self.falling()
        # Otherwise it is that it is in collision, so it is no longer falling so its fall due to the jump is stopped
        else:
            if not keyboard_pressed() == "space":
                self._velocity = 0
            self._is_jump = False
            self._is_colliding = True

        # If there is no collision with the left side of a platform, then scrolling is done
        if self._hitbox_right.collidelist(Block.block_hit_left) == -1 and keyboard_pressed() == "right":
            for obj in Block.block_list:
                obj.scrolling_right(self._speed)
            for obj in Projectile.Projectile.proj_list:
                obj.scrolling_right(self._speed)
            for obj in Teleporter.teleporter_list:
                obj.scrolling_right(self._speed)
            for obj in Enemy.enemy_list:
                obj.scrolling_right(self._speed)

        # If there is no collision with the right side of a platform, then scrolling is done
        if self._hitbox_left.collidelist(Block.block_hit_right) == -1 and keyboard_pressed() == "left":
            for obj in Block.block_list:
                obj.scrolling_left(self._speed)
            for obj in Projectile.Projectile.proj_list:
                obj.scrolling_left(self._speed)
            for obj in Teleporter.teleporter_list:
                obj.scrolling_left(self._speed)
            for obj in Enemy.enemy_list:
                obj.scrolling_left(self._speed)

        # If there is no vertical collision, the vertical scrolling is updated according to the velocity
        if self._hitbox_top.collidelist(Block.block_hit_bottom) == -1:
            for obj in Teleporter.teleporter_list:
                obj.scrolling_vertical(self._velocity)
            for obj in Block.block_list:
                obj.scrolling_vertical(self._velocity)
            for obj in Projectile.Projectile.proj_list:
                obj.scrolling_vertical(self._velocity)
            for obj in Enemy.enemy_list:
                obj.scrolling_vertical(self._velocity)

        # Otherwise it is a collision with the underside of a platform, we push the character back then
        else:
            self._velocity = -0.3
            for obj in Block.block_list:
                obj.scrolling_vertical(self._velocity)
            for obj in Projectile.Projectile.proj_list:
                obj.scrolling_vertical(self._velocity)
            for obj in Teleporter.teleporter_list:
                obj.scrolling_vertical(self._velocity)
            for obj in Enemy.enemy_list:
                obj.scrolling_vertical(self._velocity)

        # If there is a collision between the moving platform and the player
        if not self._hitbox_bottom.collidelist(Block.block_hit_top) == -1 and Block.block_list[
            self._hitbox_bottom.collidelist(
                Block.block_hit_top)].block_type == "Moving_Block_Y":
            # If the player does not press on space and the platform in collision with it is climbing and does not move in X
            if not keyboard_pressed() == "space" and not Block.block_list[
                self._hitbox_bottom.collidelist(Block.block_hit_top)].block_position:
                self._velocity = 0.62
            # If the player does not press on space and the platform in collision with it is descending and does not move in X
            elif not keyboard_pressed() == "space" and Block.block_list[
                self._hitbox_bottom.collidelist(Block.block_hit_top)].block_position:
                self._velocity = -0.32
            self._is_jump = False
            self._is_colliding = True

        # If the top of the cube collides with the ladder and you press space, then the velocity increases to raise the character
        if not self._hitbox.collidelist(Block.block_hit) == -1 and Block.block_list[
            self._hitbox.collidelist(Block.block_hit)].block_type == "Ladders" and keyboard_pressed() == "space":
            self._is_jump = True
            self._velocity = 5

        if not self._hitbox.collidelist(
                Teleporter.teleporter_hit) == -1 and keyboard_pressed() == "tab" and self._wait_pressed == 0:
            x = Teleporter.teleporter_list[0].teleport()[0]
            y = Teleporter.teleporter_list[0].teleport()[1] - 93
            if self._hitbox.collidelist(Teleporter.teleporter_hit) == 0:
                x = -x
                y = -y - 186
            for obj in Block.block_list:
                obj.move(x, y)
            for obj in Teleporter.teleporter_list:
                obj.move(x, y)
            for obj in Projectile.Projectile.proj_list:
                obj.move(x, y)
            self._wait_pressed = 100

        if not self._hitbox.collidelist(Block.block_hit) == -1 and Block.block_list[
            self._hitbox.collidelist(Block.block_hit)].block_type == "BlockEnd":
            self._map +=1


        if not self._wait_pressed == 0:
            self._wait_pressed -= 1

    # Method defining the player's jump
    def jump(self):
        """
        Method to simulate the character's fall and send the information of this fall to the object
        platform to move the height of the platform according to the velocity of the character
        - self.velocity -= self.gravity × self.mass
        """
        if self._is_jump:
            # Changing the velocity
            self._velocity -= (self._g * self._m) / 512

            # Allows to avoid a too high velocity and to cross the platforms
            if self._velocity >= 7:
                self._velocity = 7
            elif self._velocity <= -7:
                self._velocity = -7

    # Character fall method
    def falling(self):
        """Method of continuing the fall if the player stops pressing the space key"""
        if self._is_jump:
            self.jump()

    # Character display method
    def draw(self, win):
        """Method for displaying the character"""
        #   Draw the hitbox
        # pygame.draw.rect(win, (255, 0, 0), (self._x, self._y, self._w, self._h), 0)

        if self._gender == "fireman/":

            if self._img_max_attack == 0:

                if mouse_pressed() == "right":
                    self._img_max_attack = len(attackFireman)

                if keyboard_pressed() == "right":
                    self._img_max = len(walkLeftFireman)

                    if self._count < self._img_max:
                        self._player = pygame.image.load("Assets/" + self._gender + "WalkRight/" + walkRightFireman[self._count])
                        self._count += 1
                    else:
                        self._count = 0

                if keyboard_pressed() == "left":
                    self._img_max = len(walkLeftFireman)

                    if self._count < self._img_max:
                        self._player = pygame.image.load(
                            "Assets/" + self._gender + "WalkLeft/" + walkLeftFireman[self._count])
                        self._count += 1
                    else:
                        self._count = 0

                if keyboard_pressed() == 0:
                    if self._velocity < 0:

                        self._img_max = len(fallFireman)
                        if self._count < self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Jump/" + fallFireman[self._count])
                            self._count += 1
                        elif self._count == self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Jump/" + fallFireman[self._img_max - 1])
                        else:
                            self._count = 0

                    elif self._velocity > 0:

                        self._img_max = len(jumpFireman)
                        if self._count < self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Jump/" + jumpFireman[self._count])
                            self._count += 1
                        elif self._count == self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Jump/" + jumpFireman[self._img_max - 1])
                        else:
                            self._count = 0

                    else:
                        self._img_max = len(afkFireman)
                        if self._count < self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Afk/" + afkFireman[self._count])
                            self._count += 1
                        else:
                            self._count = 0
            else:
                # this is the left button but my mate failed between left and right, screw him
                self._count += 1
                if self._count < self._img_max_attack:
                    self._player = pygame.image.load(
                        "Assets/" + self._gender + "Attack/" + attackFireman[self._count])
                    self._count += 1
                else:
                    self._count = 0
                    self._img_max_attack = 0
        if self._gender == "knight/":

            if self._img_max_attack == 0:

                if mouse_pressed() == "right":
                    self._img_max_attack = len(attackKnight)

                if keyboard_pressed() == "right":
                    self._img_max = len(walkRightKnight)

                    if self._count < self._img_max:
                        self._player = pygame.image.load(
                            "Assets/" + self._gender + "WalkRight/" + walkRightKnight[self._count])
                        self._count += 1
                    else:
                        self._count = 0

                if keyboard_pressed() == "left":
                    self._img_max = len(walkLeftKnight)

                    if self._count < self._img_max:
                        self._player = pygame.image.load(
                            "Assets/" + self._gender + "WalkLeft/" + walkLeftKnight[self._count])
                        self._count += 1
                    else:
                        self._count = 0

                if keyboard_pressed() == 0:
                    """""
                    if self._velocity < 0:

                        self._img_max = len(fallKnight)
                        if self._count < self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Jump/" + fallKnight[self._count])
                            self._count += 1
                        elif self._count == self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Jump/" + fallKnight[self._img_max - 1])
                        else:
                            self._count = 0

                    elif self._velocity > 0:

                        self._img_max = len(jumpKnight)
                        if self._count < self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Jump/" + jumpKnight[self._count])
                            self._count += 1
                        elif self._count == self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Jump/" + jumpKnight[self._img_max - 1])
                        else:
                            self._count = 0
                    """""
                    if True:
                        self._img_max = len(afkKnight)
                        if self._count < self._img_max:
                            self._player = pygame.image.load(
                                "Assets/" + self._gender + "Afk/" + afkKnight[self._count])
                            self._count += 1
                        else:
                            self._count = 0
            else:
                # this is the left button but my mate failed between left and right, screw him
                self._count += 1
                if self._count < self._img_max_attack:
                    self._player = pygame.image.load(
                        "Assets/" + self._gender + "Attack/" + attackKnight[self._count])
                    self._count += 1
                else:
                    self._count = 0
                    self._img_max_attack = 0

        self._player_to_draw = pygame.transform.scale(self._player, (200, 200))

        if self._gender == "fireman/":
            self._x_neg = 75
            self._y_neg = 52
            self._delta_x = self._x - self._x_neg
            self._delta_y = self._y - self._y_neg

        elif self._gender == "knight/":
            self._x_neg = 75
            self._y_neg = 52
            self._delta_x = self._x - self._x_neg
            self._delta_y = self._y - self._y_neg

        win.blit(self._player_to_draw, (self._delta_x, self._delta_y))

    # Character HUD method
    def hud(self, win):
        """"Method for displaying and update the HUD"""
        self._load.update(win, self._shoot_loop)

    # Character delete method
    def delete(self):
        """Method for removing the character"""
        Character.charact_list.pop(Character.charact_list.index(self))
        del self
