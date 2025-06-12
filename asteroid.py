import pygame, random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt  
    
    def split(self):
        self.kill()
        if self.radius <= 2:
            return
        else:
            random_angle = random.uniform(20,50)
            random_velocity = self.velocity.rotate(random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast_one = Asteroid(self.position.x, self.position.y, new_radius)
            ast_one.velocity = random_velocity
            ast_two = Asteroid(self.position.x, self.position.y, new_radius)
            ast_two.velocity = -random_velocity