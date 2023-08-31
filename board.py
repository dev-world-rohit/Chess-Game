import pygame
from pieces import Piece
from pieces import Pawn
from pieces import Bishop
from pieces import Knight
from pieces import Rook
from pieces import Queen
from pieces import King

class Board:
    prev = [-1, -1]
    changed = False
    
    def __init__(self, rows, cols, color):
        self.rows = rows
        self.cols = cols
        self.color = color
        self.selected = False
        
        self.board = []
        self.create_board()

        self.board[0][0] = Rook(0, 0, "b")
        self.board[0][1] = Knight(0, 1, "b")
        self.board[0][2] = Bishop(0, 2, "b")
        self.board[0][3] = Queen(0, 3, "b")
        self.board[0][4] = King(0, 4, "b")
        self.board[0][5] = Bishop(0, 5, "b")
        self.board[0][6] = Knight(0, 6, "b")
        self.board[0][7] = Rook(0, 7, "b")

        self.board[1][0] = Pawn(1, 0, "b")
        self.board[1][1] = Pawn(1, 1, "b")
        self.board[1][2] = Pawn(1, 2, "b")
        self.board[1][3] = Pawn(1, 3, "b")
        self.board[1][4] = Pawn(1, 4, "b")
        self.board[1][5] = Pawn(1, 5, "b")
        self.board[1][6] = Pawn(1, 6, "b")
        self.board[1][7] = Pawn(1, 7, "b")

        self.board[7][0] = Rook(7, 0, "w")
        self.board[7][1] = Knight(7, 1, "w")
        self.board[7][2] = Bishop(7, 2, "w")
        self.board[7][3] = Queen(7, 3, "w")
        self.board[7][4] = King(7, 4, "w")
        self.board[7][5] = Bishop(7, 5, "w")
        self.board[7][6] = Knight(7, 6, "w")
        self.board[7][7] = Rook(7, 7, "w")

        self.board[6][0] = Pawn(6, 0, "w")
        self.board[6][1] = Pawn(6, 1, "w")
        self.board[6][2] = Pawn(6, 2, "w")
        self.board[6][3] = Pawn(6, 3, "w")
        self.board[6][4] = Pawn(6, 4, "w")
        self.board[6][5] = Pawn(6, 5, "w")
        self.board[6][6] = Pawn(6, 6, "w")
        self.board[6][7] = Pawn(6, 7, "w")
        

    def create_board(self):
        self.board = []
        for row in range(8):
            self.board.append([])
            for col in range(8):
                self.board[row].append(0)
                
    def draw_images(self, win, color):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != 0:
                    self.board[row][col].draw(win, color)
                    
    
    def reset_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False

    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)

                    
    def move(self, row, col, color):

        if self.changed == True:
            self.changed = False

        if self.selected == False:
            if self.board[row][col] != 0:
                if self.board[row][col].color == color:
                    self.prev = [row, col]
                    self.board[row][col].selected = True
                    self.selected = True
                    self.changed = False
                    self.update_moves()
        else:
            if self.selected == True and self.changed == False:
                coor = self.prev
                valid_moves = self.board[coor[0]][coor[1]].valid_moves(self.board)
                if [row, col] in valid_moves:
                    self.board[coor[0]][coor[1]].change_pos(row, col, color)
                    self.board[row][col] = self.board[coor[0]][coor[1]]
                    self.board[coor[0]][coor[1]] = 0
                    self.selected = False
                    self.board[row][col].selected = False
                    self.changed = True
                    self.prev = [-1, -1]
                else:
                    self.reset_selected()
                    if self.board[row][col] != 0:
                        self.changed = False
                        self.prev = [row, col]
                        self.board[row][col].selected = True
                        self.selected = True
                    
                
        return self.changed
