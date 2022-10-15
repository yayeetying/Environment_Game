import pygame, sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Environment")

# defines frames per second game runs at
FPS = 60

# background images
ocean = pygame.image.load("images/ocean.jpeg")
ocean = pygame.transform.scale(ocean, (WIDTH, HEIGHT))

# sprite images
turtle = pygame.image.load("images/ocean.jpeg")
turtle = pygame.transform.scale(ocean, (WIDTH, HEIGHT))

class Turtle(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        for num in range(1,18):
            self.sprites.append(pygame.image.load("images/turtle_sprite/turtle_{0}.png".format(num)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
    
    # update sprite animation (go to the next frame)
    def update(self):
        self.current_sprite += 1

        # restart animation
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]


def draw_window():
    WIN.blit(ocean, (0, 0))
    pygame.display.update()

# handles main loop of game
def main():
    clock = pygame.time.Clock()

    # creating the sprites and grouping them together
    moving_sprites = pygame.sprite.Group() # all sprites are grouped together
    turtle = Turtle(50,50,100,100)
    moving_sprites.add(turtle)

    run = True
    while run:
        clock.tick(FPS) # control speed of game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # drawing
        draw_window()
        moving_sprites.draw(WIN)
        moving_sprites.update()
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()

