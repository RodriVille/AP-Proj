import pygame
import random

pygame.init()

#---get width and height and set for diff aspect ratios---
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
class asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(asteroid, self).__init__()
        image = pygame.image.load('Asteroid.gif')
        self.surf = pygame.Surface((45, 100), pygame.SRCALPHA, 32)
        self.surf.blit(image, (0,0))
        self.rect = self.surf.get_rect(
            center=(random.randint(0, width),
                -random.randint(height + 30, height + 50),
            )                
        )
        self.speed = random.randint(1, 3)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.right < 0:
            self.kill()
  