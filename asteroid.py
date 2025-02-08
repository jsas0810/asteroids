import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        dir1 = self.velocity.rotate(angle)
        dir2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        ast2 = Asteroid(self.position[0], self.position[1], new_radius)
        ast1.velocity = dir1 * 1.2
        ast2.velocity = dir2 * 1.2
        asteroids.add(ast1, ast2)