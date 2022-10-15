import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Environment")

# background images
ocean = pygame.image.load("images/ocean.jpeg")
ocean = pygame.transform.scale(ocean, (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(ocean, (0, 0))
    pygame.display.update()

# handles main loop of game
def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

