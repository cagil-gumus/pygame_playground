# Example file showing a circle moving on screen
import pygame

from object import object


# WORLD_SETTINGS
GRAVITY = 150
RADIUS = 40
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
AIR_RESISTANCE = 3
DT_SPEED_UP_FACTOR = 10
COLLISION_LOSS = 0.8

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
WHITE = (255, 255, 255)


# Put the object in the middle of the screen
init_obj_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


object_list = []


# Sprites
all_sprites = pygame.sprite.Group()

object_to_add = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_0]:
        object_list.append(object(init_position=init_obj_pos,
                    init_velocity=[0.0, 0.0],
                    weight=1.0,
                    gravity=GRAVITY,
                    radius = RADIUS,
                    screen_height=SCREEN_HEIGHT,
                    screen_width=SCREEN_WIDTH,
                    air_resistance=AIR_RESISTANCE,
                    dt_speed_up_factor=DT_SPEED_UP_FACTOR,
                    collision_loss=COLLISION_LOSS))
        all_sprites.add(object_list[object_to_add])
        object_to_add += 1

   # Update all sprites
    all_sprites.update(dt)

    # Clear the screen
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()