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
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            random_velocity_a = self.velocity.rotate(random_angle) 
            random_velocity_b = self.velocity.rotate(-random_angle) 
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            ast_one = Asteroid(self.position.x, self.position.y, new_radius)
            ast_one.velocity = random_velocity_a * 1.5
            ast_two = Asteroid(self.position.x, self.position.y, new_radius)
            ast_two.velocity = random_velocity_b * 1.8