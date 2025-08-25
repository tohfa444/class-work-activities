import pygame

pygame.init()

S_W,S_H = 700,700

display_surface = pygame.display.set_mode((S_W,S_H))

pygame.display.set_caption("Adding image and backgroung image")

backgound_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (S_W,S_H)
)

penguin_image = pygame.transform.scale(
    pygame.image.load('penguin.png').convert_alpha(),
    (300,300)
)

penguin_rect = penguin_image.get_rect(ecter=(S_W // 2, S_H //2 - 30))

text = pygame.font.Font(None,36).render("Hello World, I am penguin",True,pygame.color("green"))

text

def game_loop():

    clock = pygame