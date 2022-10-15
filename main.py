import pygame, sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Environment")

# defines frames per second game runs at
FPS = 60

#colors
WHITE = (255, 255, 255)

#user statistics
lives=3
score=0

# background images
ocean = pygame.image.load("images/ocean.jpeg")
ocean = pygame.transform.scale(ocean, (WIDTH, HEIGHT))
can = pygame.image.load(
    os.path.join('images', 'trash_can.png'))
can = pygame.transform.scale(can, (50, 70))
bag =  pygame.image.load("images/bag.png")
bag = pygame.transform.scale(bag, (50, 50))
heart = pygame.image.load("images/p_heart.png")
heart = pygame.transform.scale(heart, (25, 30))

#fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 25)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# sprite images
turtle = pygame.image.load("images/ocean.jpeg")
turtle = pygame.transform.scale(ocean, (WIDTH, HEIGHT))

class Turtle(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for num in range(1,18):
            self.sprites.append(pygame.image.load("images/turtle_sprite/turtle_{0}.png".format(num)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
    
    def animate(self):
        self.is_animating = True

    # update sprite animation (go to the next frame)
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.25

            # restart animation
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]


def draw_window():
    WIN.blit(ocean, (0, 0))
    WIN.blit(can, (30,40))
    WIN.blit(bag, (200,100))

    x,y = 10, 5
    i=0

    #health
    while i<lives:
        heart_rect = heart.get_rect()
        heart_rect.x = x + 30 * i
        heart_rect.y = y
        WIN.blit(heart, heart_rect)
        i = i+1

    #score
    score_text = HEALTH_FONT.render("SCORE: " + str(score), 1, WHITE)
    WIN.blit(score_text, (350, 10))
    
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
            if event.type == pygame.KEYDOWN:
                turtle.animate() # simulate turtle animating
        
        # drawing
        draw_window()
        moving_sprites.draw(WIN)
        moving_sprites.update()
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()

