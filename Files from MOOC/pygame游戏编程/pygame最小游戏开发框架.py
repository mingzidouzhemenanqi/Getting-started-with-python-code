import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame游戏之旅")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
