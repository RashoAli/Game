import pygame
import random


class Blob():
    def __init__(self):
        self.screen = [900, 600]

        self.blob_position_x = int(self.screen[0] / 2)
        self.blob_position_y = int(self.screen[1] / 2)

        self.blob_speed_x = 0
        self.blob_speed_y = 0
        self.blob_force = 1

    def update(self, time):
        self.blob_position_x = -self.blob_speed_x + self.blob_position_x

        self.blob_speed_y = time * self.blob_force + self.blob_speed_y
        self.blob_position_y = time * time * self.blob_force + time * self.blob_speed_y + self.blob_position_y

    def drow_blob(self, screen):
        x = int(self.blob_position_x)
        y = int(self.blob_position_y)
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 20, 2)

    def end_game(self):
        game_over = False
        if self.blob_position_x > self.screen[0] or self.blob_position_x < 0:
            game_over = True

        if self.blob_position_y > self.screen[1]:
            game_over = True

        return game_over


class Appell():
    def __init__(self):
        self.screen = [900, 600]

        self.apell_position_x = self.screen[0] / 2
        self.apell_position_y = self.screen[1]
        self.apell_speed = 20

        self.last_x = 0
        self.last_y = 0

        self.direction_x = self.last_x - self.apell_position_x
        self.direction_y = self.last_y - self.apell_position_y

        self.length = (self.direction_x * self.direction_x + self.direction_y * self.direction_y) ** (0.5)

    def apell_treff(self, chiken):
        treff = False
        x_abstand = self.apell_position_x - chiken.blob_position_x
        y_abstand = self.apell_position_y - chiken.blob_position_y

        abs_abstand = x_abstand * x_abstand + y_abstand * y_abstand
        if abs_abstand <= 2000:
            treff = True
        return treff

    def path(self):
        self.direction_x = self.last_x - self.apell_position_x
        self.direction_y = self.last_y - self.apell_position_y

        self.length = (self.direction_x * self.direction_x + self.direction_y * self.direction_y) ** (0.5)

    def update(self):
        self.apell_position_x = self.apell_position_x + self.direction_x * self.apell_speed / self.length
        self.apell_position_y = self.apell_position_y + self.direction_y * self.apell_speed / self.length

    def drow_apell(self, screen):
        self.update()
        x = int(self.apell_position_x)
        y = int(self.apell_position_y)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 10, 0)


class Rain():
    def __init__(self):
        self.x = random.randrange(900)
        self.y = random.randrange(-500, -10)
        self.z = random.randrange(0, 20)

    def update(self):
        self.y += self.z
        if self.y > 600:
            self.y = random.randrange(-50, -10)

    def drow_drop(self, screen):
        self.update()
        x = int(self.x)
        y = int(self.y)
        z = int(self.z)
        pygame.draw.line(screen, (138, 43, 226), (x, y), (x, y + z), 2)


def moveing_way(chiken, appel):
    x_move = -(chiken.blob_position_x - appel.apell_position_x)
    y_move = -(chiken.blob_position_y - appel.apell_position_y)

    length = (x_move * x_move + y_move * y_move) ** (0.5)

    x_move = x_move * 10 / length
    y_move = y_move * 20 / length
    return x_move, y_move
