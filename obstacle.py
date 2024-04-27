import pymunk
import pygame
import random
import math

class Obstacle:
    def __init__(self, space):
        x = random.randint(100, 1100)  # Ensure these values are within the visible area
        y = random.randint(100, 700)
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = x, y
        self.shape = pymunk.Poly.create_box(self.body, (500, 5))
        self.shape.elasticity = 0.5
        self.shape.friction = 1.0
        angle_in_degrees = random.randint(-10, 10)  # Generate a random angle between 0 and 90 degrees
        self.body.angle = math.radians(angle_in_degrees)  # Convert the angle to radians and set it
        space.add(self.body, self.shape)

    def draw(self, screen):
        points = [self.body.local_to_world(v) for v in self.shape.get_vertices()]
        points = [(int(v.x), int(v.y)) for v in points]
        pygame.draw.polygon(screen, (255, 255, 255), points)
