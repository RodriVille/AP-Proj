import pygame

pygame.init()

#---get width and height and set for diff aspect ratios---
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

#---lazer size---
lazer_width = 10
lazer_height = 50

from pygame.locals import (
    K_SPACE
)
class lazer(pygame.sprite.Sprite):
    def __init__(self):
        super(lazer, self).__init__()
        self.surf = pygame.Surface((lazer_width, lazer_height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (width/2, height/2))
            #---moves the rocket in a certain direction if a key is pressed---
    def update(self):
        self.rect.move_ip(0, -10)
        # Keep lazer on the screen
        if self.rect.top < 0:
            self.kill()
