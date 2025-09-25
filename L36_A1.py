import pygame
import random

S_W,S_H = 500,400
M_S = 5
F_S = 72

pygame.init()

B_I = pygame.transform.scale(pygame.image.load("bg.jpg"),(S_W,S_H))

font = pygame.font.sysfont("Times New Roman",F_S)

class Sprite(pygame.sprite.sprite):

    def _init_(self,color,height,width):
        super()._init_()
        self.image.fill(pygame.color("dodgerblue"))
        pygame.draw.rect(self.image,color,pygame.rect(0,0,width,height))
