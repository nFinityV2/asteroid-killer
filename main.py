import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    
    dt = 0
    score = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    asteroid.split()
                    score += 1
                                    
            if asteroid.check_collisions(player):
                print("Game Over!")
                print(f"Score: {score}")
                sys.exit(1)
            
        pygame.Surface.fill(screen, "black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()