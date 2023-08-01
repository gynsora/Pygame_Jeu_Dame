import pygame
from .constants import BLACK, ROWS,COLS ,RED , SQUARE_SIZE,WHITE
from .piece import Piece
class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None #piece selectionner dans l'échéquier
        self.red_left = self.white_left = 12 #nombre de pièces restant pour rouge et pour blanc, dans l'échequier
        self.red_kings = self.white_kings = 0 #nombre de roi présent pour rouge et pour blanc, dans l'échequier
        self.create_board()

    def draw_squares(self,win):
        win.fill(BLACK) #on remplit la surface du jeu "win" en noir
        for row in range(ROWS):
            for col in range(row % 2,COLS , 2): # permette de crée les cube rouge en alternant avec la couleur noir
                pygame.draw.rect(win,RED,(row*SQUARE_SIZE ,col*SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE)) # dessin d'un rectangle surface,couleur, x,y, width,height
    
    def create_board(self): #on crée les pieces de l'echequier
        for row in range(ROWS):
            self.board.append([])# on crée un liste pour chaque ligne de l'echéquier
            for col in range(COLS):
                if col %2  == ((row +1) % 2 ):# on dessine les piece de facon alternative comme dans le jeu de dame
                    if row < 3:# on crée les piece blanches sur les 3 premiere ligne du haut 0 1 2 
                        self.board[row].append(Piece(row , col, WHITE))
                    elif row > 4 :# on crée les piece rouge sur les 3 derniere ligne du bas 5 6 7
                        self.board[row].append(Piece(row , col, RED))
                    else:
                        self.board[row].append(0)# on ajoute aucune piece et on met un 0 
                else:
                    self.board[row].append(0)

    def draw(self,win): # dessine les squares (terrain rouge-noir) et les pieces (piece de dame)
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
