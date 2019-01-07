import pygame

class Player:
    def __init__(self):
        self.x_p = 0
        self.y_p = 0


        self.color = (225, 225, 225)
        self.player_speed = 20
        self.Lives = 3

    def pressed_kay_type(self):
        keys = pygame.key.get_pressed()

        pressed_kay = 'N'
        if sum(keys) == 1:
            if keys[pygame.K_LEFT]:
                pressed_kay = 'L'
            elif keys[pygame.K_RIGHT]:
                pressed_kay = 'R'
            elif keys[pygame.K_UP]:
                pressed_kay = 'U'
            elif keys[pygame.K_DOWN]:
                pressed_kay = 'D'

        if sum(keys) == 2:
            if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
                pressed_kay = 'RU'
            elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:
                pressed_kay = 'LU'
            elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
                pressed_kay = 'LD'
            elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
                pressed_kay = 'RD'

        return pressed_kay

    def player_M(self, pressed_kay, WIDTH, HEIGHT):

        if pressed_kay == 'D':
            self.y_p += self.player_speed
        elif pressed_kay == 'R':
            self.x_p += self.player_speed
        elif pressed_kay == 'L':
            self.x_p -= self.player_speed
        elif pressed_kay == 'U':
            self.y_p -= self.player_speed

        elif pressed_kay == 'LU':
            self.x_p -= self.player_speed
            self.y_p -= self.player_speed

        elif pressed_kay == 'RD':
            self.x_p += self.player_speed
            self.y_p += self.player_speed

        elif pressed_kay == 'RU':
            self.y_p -= self.player_speed
            self.x_p += self.player_speed

        elif pressed_kay == 'LD':
            self.x_p -= self.player_speed
            self.y_p += self.player_speed

        if 0 > self.x_p:
                self.x_p += self.player_speed
        if self.x_p > WIDTH:
                self.x_p -= self.player_speed
        if 0 > self.y_p:
                self.y_p += self.player_speed
        if self.y_p > HEIGHT:
                self.y_p -= self.player_speed

    def drow(self, screen):
        color = self.color
        x = self.x_p
        y = self.y_p
        pygame.draw.circle(screen, color, (x, y), 20, 2)
