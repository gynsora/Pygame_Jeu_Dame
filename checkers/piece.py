import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY

class Piece:
    PADDING = 15
    OUTLINE = 2
    def __init__(self, row , col, color): #on définir un ligne, une cologne (position de la piece) et un couleur pour chaque pièce de l'échéquier
        self.row = row
        self.col = col
        self.color = color
        self.king = False # pour savoir si notre piece s'est transformé en roi

        #le pièce vont vers le haut si elle sont rouge donc direction = -1 sinon elle descend et direction = +1
        #rappel les coordonées en y sont inversé le 0 se situe en haut de l'écran 
        self.direction  = -1 if self.color == RED else 1 
        #if self.color == RED:
            #self.direction = -1
        #else:
            #self.directionirection = 0
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self): # permet de calculer la position centrale dans laquel la piece sera
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king(self): # permet de transformer une piece en roi
        self.king = True

    def draw(self, win): # permet de dessiner la piece dans l'échequier on dessine 2 cercle supperposé de taille différente pour faire 1 pièce
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win,GREY, (self.x,self.y), radius +self.OUTLINE )
        pygame.draw.circle(win,self.color, (self.x,self.y), radius )
    
    def __repr__(self): # permet de représanter une piece, utile pour le debug
        return str(self.color)