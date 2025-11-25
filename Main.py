import pygame
from characters import *

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((900, 750))

background = pygame.image.load("assets/background_layer_1.png")
foreground1 = pygame.image.load("assets/foreground_layer_1.png")

width = 250
height = 250
character_image = pygame.Surface((width, height))
player = Character(450, 375)

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
    screen.fill("black") #empty screen with black color

    background = pygame.transform.scale(background, (900, 750))
    foreground1 = pygame.transform.scale(foreground1, (900, 750))
    screen.blit(background, (0, 0)) #draw background
    screen.blit(foreground1, (0, 0)) #draw foreground

    screen.blit(player.image, player.rect) #draw character at center

    keys = pygame.key.get_pressed()
    player.update(None) #update character position and animation

    pygame.display.update() #update the display
    pygame.time.Clock().tick(60) #limit to 60 FPS