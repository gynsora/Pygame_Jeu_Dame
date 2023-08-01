import pygame
from checkers.constants import WIDTH ,HEIGHT
from checkers.board import Board

FPS = 60
#WIN = window, ici on crée la taille de la fenetre du jeu
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#checkers = nom du jeu
pygame.display.set_caption('checkers')

def main():
    run = True
    #ici on crée un timer pour définir la vitesse de rafraichissement du jeu (FPS)
    clock = pygame.time.Clock()
    #on crée l'échequier
    board = Board()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # arret de la boucle du jeu, quand on quitte le jeu (on appuie sur la croix pour fermer le jeu)
                run = False 
            if event.type == pygame.MOUSEBUTTONDOWN : #event lorsque le joueur clique avec la souris
                pass 
        #dessin de l'échequier
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()


main()