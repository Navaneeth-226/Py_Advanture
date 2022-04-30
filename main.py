import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) # creat displa with width and height
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)# arg-(font-type,font-size)


sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game',False,'Black') #arg-(text,Anti Aliansing,color)AA used to smooth the edges of the text

snail_surface = pygame.image.load('graphics/snail1.png').convert_alpha() #removing the alpha values
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))


while True:
    # drow all our elements
    # update everything to display
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()


    screen.blit(sky_surface,(0,0)) # blits(s) for displaying one surface on top of another       
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800
    screen.blit(snail_surface,(snail_rect))

    player_rect.left += 2
    if player_rect.left > 850: 
        player_rect.left = 0
    screen.blit(player_surf,(player_rect))

    if player_rect.colliderect(snail_rect):  # print False / True
        print("collision")
    pygame.display.update()
    clock.tick(60) # set maximum frm rate to 60frm per second