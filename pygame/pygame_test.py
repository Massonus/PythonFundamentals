import pygame

FPS = 60

WIDTH_DISPLAY = 640
HEIGHT_DISPLAY = 400

pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.



gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption("Test pygame")


clock = pygame.time.Clock()

while True:

    # затримка кадрів
    clock.tick(FPS)

    # цикл обробки подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    pygame.display.update()
