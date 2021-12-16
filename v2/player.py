import pygame

pygame.init()

#---get width and height and set for diff aspect ratios---
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

#---player size---
player_width = 80
player_height = 100


from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
    K_SPACE
)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        rocket = pygame.image.load('player.gif')
        self.surf = pygame.Surface((player_width, player_height), pygame.SRCALPHA, 32)
        self.surf.blit(rocket, (0,0))
        #self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (width/2, height/2))
            #---moves the rocket in a certain direction if a key is pressed---
    def movePlayer(self, keys):
        if keys[K_w]:
                self.rect.move_ip(0, -2)
        if keys[K_s]:
                self.rect.move_ip(0, 2)
        if keys[K_a]:
                self.rect.move_ip(-2, 0)
        if keys[K_d]:
                self.rect.move_ip(2, 0)
        #---Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = width-player_width
        if self.rect.right > width:
            self.rect.right = player_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
