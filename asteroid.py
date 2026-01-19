import pygame
from circleshape import *
from constants import LINE_WIDTH
##from constants import ASTEROID_KINDS
##from constants import ASTEROID_MAX_RADIUS
from constants import ASTEROID_MIN_RADIUS
##from constants import ASTEROID_SPAWN_RATE_SECONDS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,  LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        asteroid1_veloicty = self.velocity.rotate(angle)
        asteroid2_veloicty = self.velocity.rotate(-angle)
        asteroid1_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid2_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, asteroid1_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, asteroid2_radius)
        asteroid1.velocity = asteroid1_veloicty * 1.2
        asteroid2.velocity = asteroid2_veloicty * 1.2