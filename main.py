import pygame
from checkers.constants import WIDTH ,HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game

FPS = 60
#WIN = window, ici on crée la taille de la fenetre du jeu
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#checkers = nom du jeu
pygame.display.set_caption('checkers')


def get_row_col_from_mouse(pos): # permet de trouver la position de la souris dans l'échequier pos = tuple (x,y) (col,row)
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    #ici on crée un timer pour définir la vitesse de rafraichissement du jeu (FPS)
    clock = pygame.time.Clock()
    #on initialise le jeu
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # arret de la boucle du jeu, quand on quitte le jeu (on appuie sur la croix pour fermer le jeu)
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: #event lorsque le joueur clique avec la souris
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos) #cette fonction prend la position de la souris et la transforme position x,y dans l'échequier row,col sont les données renvoyé par la fonction
                game.select(row, col)
        #dessin de l'échequier
        game.update()
    
    pygame.quit()

main()
