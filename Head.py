import pygame
import sys
from Enemy_Unit import Blob, Appell, Rain, moveing_way

pygame.init()
WIDTH = 900
HEIGHT = 600

BACKGROUND_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False
start_t = 0
clock = pygame.time.Clock()

blob = Blob()

appels_array = []

rain_array = []
for i in range(0, 600):
    rain_drop = Rain()
    rain_array.append(rain_drop)

jump_time = 0
frames = 0

while not game_over:
    screen.fill(BACKGROUND_COLOR)
    camera_move = -blob.blob_position_y + 450

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mause_x, mause_y = event.pos

    blob.update(jump_time)
    blob.drow_blob(screen)
    if frames % 30 == 0:
        ap = Appell()
        ap.last_x = 450  # mause_x
        ap.last_y = 0  # mause_y
        ap.path()
        appels_array.append(ap)
    frames += 1

    for ap in appels_array:
        #ap.apell_position_y -= camera_move
        ap.drow_apell(screen)

        if ap.apell_treff(blob):
            x_move, y_move = moveing_way(blob, ap)
            blob.blob_speed_y = y_move
            blob.blob_speed_x = x_move
            blob.blob_position_y += camera_move
            jump_time = -0.4
            appels_array.remove(ap)
            del ap

    jump_time += 0.02
    if blob.blob_speed_y > 0:
        blob.blob_speed_y -= 0.1

    if blob.blob_speed_x > 0:
        blob.blob_speed_x -= 0.1

    if blob.blob_speed_x < 0:
        blob.blob_speed_x += 0.1

    for rain_drop in rain_array:
        rain_drop.drow_drop(screen)

    #game_over = blob.end_game()
    clock.tick(30)
    pygame.display.flip()

print('end')
sys.exit()
