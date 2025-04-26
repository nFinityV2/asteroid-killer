import pygame 
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, PLAYER_RADIUS)
    
    clock = pygame.time.Clock()
    dt = 0
    
    while screen:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, "black")
        dt = clock.tick(60) / 1000
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()