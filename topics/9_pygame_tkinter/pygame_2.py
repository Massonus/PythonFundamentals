# підключаємо модуль
import pygame

# визначаємо константу затримки кадрів
# та інші константи 
FPS = 60

WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)

DISPLAY_WIDTH = 400
DISPLAY_HEIGH = 400

# ініціалізація та створення об'єктів
pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

# gameDisplay=pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

clock = pygame.time.Clock()

# якщо необхідно до циклу відобразити об'єкти на екрані
pygame.display.update()

# головний цикл
while True:

    # затримка кадрів
    clock.tick(FPS)

    # цикл обробки подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # ######################
    # зміна об'єктів та інше
    # ######################
    gameDisplay.fill(ORANGE)
    # обновлення екрану
    pygame.display.update()
