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

    def draw(self, screen):
        pos = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(screen, self.color, pos, 5)

    def update(self):
        current_velocity = self.body.velocity
        velocity_change = (current_velocity - self.previous_velocity).length

        # Adjust these values based on your observations of typical velocity changes
        velocity_change_threshold = 50
        max_velocity_change = 500
        volume = min(1.0, velocity_change / max_velocity_change)

        # Directly manage the glowing effect based on velocity change
        if velocity_change > velocity_change_threshold:
            self.color = self.brighten_color(self.original_color)
            self.collision_sound.set_volume(volume)  # Set the volume based on impact
            self.collision_sound.play()  # Play the sound effect
            pygame.time.set_timer(pygame.USEREVENT, 100)  # Set timer to handle effect duration
        else:
            self.color = self.original_color

        # Update previous velocity for the next frame
        self.previous_velocity = current_velocity


    def brighten_color(self, color):
        r = min(255, color.r + 100)
        g = min(255, color.g + 100)
        b = min(255, color.b + 100)
        return pygame.Color(r, g, b)

    def handle_timer_event(self):
        # This method will be triggered by the USEREVENT from the pygame timer
        self.color = self.original_color
        pygame.time.set_timer(pygame.USEREVENT, 0)  # Reset the timer
