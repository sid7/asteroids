import random
import pygame

from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, update_score):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return update_score(10)

        update_score(5)
        angle = random.uniform(20, 50)

        a = self.velocity.rotate(angle)
        b = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
