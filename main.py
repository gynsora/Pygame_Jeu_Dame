import pygame
from checkers.constants import WIDTH ,HEIGHT, SQUARE_SIZE
from checkers.game import Game

FPS = 60
#WIN = window, ici on crée la taille de la fenetre du jeu
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#checkers = nom du jeu
pygame.display.set_caption('checkers')

def get_row_col_mouse(pos):# permet de trouver la position de la souris dans l'échequier pos = tuple (x,y) (col,row)
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col


def main():
    run = True
    #ici on crée un timer pour définir la vitesse de rafraichissement du jeu (FPS)
    clock = pygame.time.Clock()
    #on initialise le jeu
    game = Game(WIN)
    #on crée l'échequier
    # # board = Board()
    #piece = board.get_piece(0,1)
    #board.move(piece, 4, 3)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # arret de la boucle du jeu, quand on quitte le jeu (on appuie sur la croix pour fermer le jeu)
                run = False 
            if event.type == pygame.MOUSEBUTTONDOWN : #event lorsque le joueur clique avec la souris
                pos = pygame.mouse.get_pos() 
                row , col = get_row_col_mouse(pos) #cette fonction prend la position de la souris et la transforme position x,y dans l'échequier row,col sont les données renvoyé par la fonction
                # #piece = board.get_piece(row, col)   
                # #if piece != 0 : 
                    # #board.move(piece, 4, 3)   
        #dessin de l'échequier
        game.update()
        # #board.draw(WIN)
        # #pygame.display.update()
    pygame.quit()


main()