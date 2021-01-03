import pygame
from pygame.locals import *
Black = (0, 0, 0)
bg=pygame.image.load(r'C:\Users\Acer\PyGDep\MenuBG.jpg')
def main_menu():
    pygame.init()
    pixf=pygame.font.SysFont("Calibri", 30)
    tela = pygame.display.set_mode((612,612))
    # tela.fill(WHITE)
    tela.blit(bg, (0, 0))
    pygame.display.set_caption("Game")
    tela.blit(pixf.render('Baixo Para Sair', True, Black), (100,100))
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                # sys.exit()
main_menu()