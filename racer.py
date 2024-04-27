import pygame
import pymunk

class Racer:
    def __init__(self, space, color, position):
        self.body = pymunk.Body(1, 100, pymunk.Body.DYNAMIC)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, 5)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5
        self.original_color = pygame.Color(*color)
        self.color = self.original_color
        space.add(self.body, self.shape)
        self.previous_velocity = self.body.velocity  # Store the initial velocity
        self.collision_sound = pygame.mixer.Sound('marbles.wav')  # Load the sound file
        self.trail_positions = []  # List to store the positions for the trail
        self.max_trail_length = 10  # Maximum length of the trail

    def remove_from_space(self, space):
        space.remove(self.body, self.shape)

    def draw(self, screen):
        # Draw the trail with fading alpha and reducing radius
        num_positions = len(self.trail_positions)
        for i, pos in enumerate(reversed(self.trail_positions)):
            alpha = int(255 * (1 - i / num_positions))  # Decrease alpha along the trail
            radius = 5 * (1 - i / num_positions)  # Decrease radius along the trail
            trail_color = self.original_color + pygame.Color(0, 0, 0, alpha)
            pygame.draw.circle(screen, trail_color, pos, int(radius))

        # Draw the racer
        pos = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(screen, self.color, pos, 5)

    def update(self):
        current_velocity = self.body.velocity
        velocity_change = (current_velocity - self.previous_velocity).length

        velocity_change_threshold = 50
        max_velocity_change = 500
        volume = min(1.0, velocity_change / max_velocity_change)

        if velocity_change > velocity_change_threshold:
            self.color = self.brighten_color(self.original_color)
            self.collision_sound.set_volume(volume)
            self.collision_sound.play()
            pygame.time.set_timer(pygame.USEREVENT, 100)
        else:
            self.color = self.original_color

        # Update previous velocity for the next frame
        self.previous_velocity = current_velocity

        # Update trail positions
        self.trail_positions.append((int(self.body.position.x), int(self.body.position.y)))
        if len(self.trail_positions) > self.max_trail_length:
            self.trail_positions.pop(0)

    def brighten_color(self, color):
        r = min(255, color.r + 100)
        g = min(255, color.g + 100)
        b = min(255, color.b + 100)
        return pygame.Color(r, g, b)

    def handle_timer_event(self):
        self.color = self.original_color
        pygame.time.set_timer(pygame.USEREVENT, 0)
