import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((840,650))

bg = pygame.image.load('images/bg.png')
bg_num = 0

bg_sound = pygame.mixer.Sound('sounds\The_Black_Eyed_Peas_-_Pump_It_OST_Taksi_4_(SkySound.cc).mp3')
bg_sound.play()

player1 = pygame.image.load('images/car2-removebg-preview (1).png')
player2 = pygame.image.load('images/car3-removebg-preview.png')



running = True
while running:
    
    screen.blit(bg,(0,bg_num))  
    screen.blit(bg, (0,bg_num - 650))
    screen.blit(player1,(100,300))
    screen.blit(player2,(100,90))

    bg_num += 2
    if bg_num == 650:
        bg_num = 0
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        


    