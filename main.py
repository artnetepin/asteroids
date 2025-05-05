import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        updatables.update(dt)

        for asteroid in asteroids:
            has_collided = asteroid.collision_check(player)
            if has_collided:
                print('Game over!')
                sys.exit()

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
