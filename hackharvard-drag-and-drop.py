import pygame
import random

class Key(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, id):
        super(Key, self).__init__()
        self.image = pygame.image.load("button.png").convert()
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.clicked = False
        self.id = id
        self.linkReady = False
        self.links = []
#-------------------------------

Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)

pygame.init()

size = (700, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("This is a new window")

done = False
#----------------------------
clock = pygame.time.Clock()
#-----------------------------
key_list = pygame.sprite.Group()
#-------------------------------

# Main program loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        if event.button == 3:
            key_list.add(Key(x, y, len(key_list) + 1))
        elif event.button == 1:
            for key in key_list:
                if key.rect.collidepoint(pos):
                    key.clicked = True
        elif event.button == 2:
            for key in key_list:
                if key.rect.collidepoint(pos):
                    key.linkReady = True
                    count = 0
                    links = []
                    for key in key_list:
                        if key.linkReady == True:
                            count += 1
                            links.append(key.id)
                    if count == 2:
                        for key in key_list:
                            if key.linkReady == True:
                                key.linkReady = False
                                count += 1
                                key.links += links

        if event.type == pygame.MOUSEBUTTONUP:
            for key in key_list:
                key.clicked = False
            drag_id = 0
        #---------------------------------------

    #Game logic should go here
    for key in key_list:
        if key.clicked == True:
            pos = pygame.mouse.get_pos()
            key.rect.x = pos[0] - (key.rect.width/2)
            key.rect.y = pos[1] - (key.rect.height/2)
    #-------------------------------------------------
    #Drawing code here
    # First clear the screen to white. Do not put other drawing commands above this or they will be erased with the
    screen.fill(Black)

    #--------------------------------------------------
    key_list.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()