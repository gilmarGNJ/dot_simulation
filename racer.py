import pymunk
import pygame

class Racer:
    def __init__(self, space, color, position):
        self.body = pymunk.Body(1, 100, pymunk.Body.DYNAMIC)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, 5)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5
        self.original_color = pygame.Color(*color)
        self.color = self.original_color
        self.shape.racer = self  # Link this racer to the shape for collision handling
        space.add(self.body, self.shape)
        self.colliding = False

    def draw(self, screen):
        pos = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(screen, self.color, pos, 5)

    def collide(self):
        if not self.colliding:
            self.color = pygame.Color(255, 255, 255)
            self.colliding = True
            pygame.time.set_timer(pygame.USEREVENT, 100)

    def update(self):
        if self.colliding:
            self.color = self.original_color
            self.colliding = False
            pygame.time.set_timer(pygame.USEREVENT, 0)  # Reset the timer

