import pygame
from .constants import BLACK, ROWS,COLS ,RED , SQUARE_SIZE,WHITE
from .piece import Piece
class Board:
    def __init__(self):
        self.board = []
        # #self.selected_piece = None #piece selectionner dans l'échéquier
        self.red_left = self.white_left = 12 #nombre de pièces restant pour rouge et pour blanc, dans l'échequier
        self.red_kings = self.white_kings = 0 #nombre de roi présent pour rouge et pour blanc, dans l'échequier
        self.create_board()
    
    def draw_squares(self, win): #permet de dessiner les case de l'échequier
        win.fill(BLACK)  #on remplit la surface du jeu "win" en noir
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2): # permette de crée les cube rouge en alternant avec la couleur noir
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        #ici on echange la position d'une piece dans le board avec le contenu de sa position d'arrivé (normalement toujours = 0)
        #self.board[piece.row][piece.col] = position actuelle de la piece
        #self.board[row][col] = position d'arrivé de la piece
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        #on change la position de la piece avec une position exact pour quelle puisse être redessiner correctement
        piece.move(row, col)

        if row == ROWS - 1 or row == 0: #si une des pieces à atteint la premiere ou dernière ligne (en haut pour les rouge et en bas pour les blanc) alors la piece devient un roi
            piece.make_king() #on transforme la piece en roi
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1 

    def get_piece(self, row, col):  #on récupere une piece de l'échequier en fonction de sa position
        return self.board[row][col]

    def create_board(self):  #on crée les pieces de l'echequier
        for row in range(ROWS):
            self.board.append([]) # on crée un liste pour chaque ligne de l'echéquier
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2): # on dessine les piece de facon alternative comme dans le jeu de dame
                    if row < 3: # on crée les piece blanches sur les 3 premiere ligne du haut 0 1 2 
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4: # on crée les piece rouge sur les 3 derniere ligne du bas 5 6 7
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)# on ajoute aucune piece et on met un 0 
                else:
                    self.board[row].append(0)
        
    def draw(self, win): # dessine les squares (terrain rouge-noir) et les pieces (piece de dame)
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None 
    
    def get_valid_moves(self, piece):
        moves = {} # (4,5): [(3,1)] la cle est un tuple 4,5 la liste de tuple contient les mouvement possible pour la clé (4,5)
        left = piece.col - 1  #on cherche la color de gauche par rapport à la pièce
        right = piece.col + 1 #on cherche la color de droite par rapport à la pièce
        row = piece.row       #on cherche la ligne ou se situe la piece

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves

    #start le debut de la boucle, stop la fin de la boucle, step pour savoir si la piece va vers le haut(-1) ou le bas(+1),
    #color représente la couleur de la piece, left represente le lieu on la piece arrive lors d'un saut de piece
    #skipped represente la liste des places ou les pieces peuvent bouger
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
