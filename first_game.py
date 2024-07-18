# Example file showing a circle moving on screen
import pygame

from object import object


# WORLD_SETTINGS
GRAVITY = 150  # m/s^2
RADIUS = 40
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
AIR_RESISTANCE = 3
DT_SPEED_UP_FACTOR = 20
# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# Put the object in the middle of the screen
init_obj_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
object1 = object(init_position=init_obj_pos,
                 init_velocity=[0.0, 0.0],
                 weight=1.0,
                 gravity=GRAVITY,
                 radius = RADIUS,
                 screen_height=SCREEN_HEIGHT,
                 screen_width=SCREEN_WIDTH,
                 air_resistance=AIR_RESISTANCE,
                 dt_speed_up_factor=DT_SPEED_UP_FACTOR)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    object1.update_dt(dt)

    pygame.draw.circle(screen, "red", object1.position, RADIUS)

    keys = pygame.key.get_pressed()
    object1.go_up = keys[pygame.K_w]
    object1.go_down = keys[pygame.K_s]
    object1.go_left = keys[pygame.K_a]
    object1.go_right = keys[pygame.K_d]

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()