import pygame

from .constants import RED , WHITE, BLUE, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected: #si on a selectionné une piece à nous avant (self.selected != None)
            result = self._move(row, col) #on tente de changer la position de la piece selectionné vers la nouvelle position choisi
            if not result: # si le movement est invalidé on deselectionne la piece pour tenté d'en reprendre une autre
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col) # on selection dans le board la piece avec les coordonées correspondante dans l'échequier
        if piece != 0 and piece.color == self.turn: # si la piece appratient au joueur du tour en cour et que l'emplacement contient bien une piece
            self.selected = piece #on selectionne la piece
            self.valid_moves = self.board.get_valid_moves(piece) #et on regarde quels sont ces mouvement possible
            return True # on renvoi vrai si la zone selectionner contient une piece qu'on peut bouger
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:  # si piece = a une case vide valide on bouge la piece selectionné(self.selected)
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False #sinon on retourne faux (mouvement invalide)

        return True #si tout se passe bien on retourne vrai (mouvement valide)

    def draw_valid_moves(self, moves): # dessine tout les mouvement possible lorsqu'on selectionne une piece nous apparetenant
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
