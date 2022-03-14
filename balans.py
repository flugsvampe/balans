from microbit import *
import time

player_x = 2.0
player_y = 2.0

while True:

    old_x = player_x
    old_y = player_y

    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    player_x = player_x + (x / 1000)
    player_y = player_y + (y / 1000)

    if player_x < 0.0:
        player_x = 0.0

    if player_x > 4.0:
        player_x = 4.0

    if player_y < 0.0:
        player_y = 0.0

    if player_y > 4.0:
        player_y = 4.0

    if old_x != player_x or old_y != player_y:
        display.set_pixel(int(old_x), int(old_y), 0)

    display.set_pixel(int(player_x), int(player_y), 9)

    print((x, 0))

    time.sleep(0.05)
