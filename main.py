import pygame
from constants import *
from player import *
from asteroidfield import * 
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT / 2
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    player = Player(x, y)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        for object in updateable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game Over!")
                return
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()