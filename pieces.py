import pygame

def load_image(path):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, (70, 70))
    img.set_colorkey((255, 0, 0))
    return img

black_pawn = load_image('data/black_pawn.png')
black_bishop = load_image('data/black_bishop.png')
black_knight = load_image('data/black_knight.png')
black_rook = load_image('data/black_rook.png')
black_queen = load_image('data/black_queen.png')
black_king = load_image('data/black_king.png')

white_pawn = load_image('data/white_pawn.png')
white_bishop = load_image('data/white_bishop.png')
white_knight = load_image('data/white_knight.png')
white_rook = load_image('data/white_rook.png')
white_queen = load_image('data/white_queen.png')
white_king = load_image('data/white_king.png')

black = [black_pawn, black_bishop, black_knight, black_rook, black_queen, black_king]

white = [white_pawn, white_bishop, white_knight, white_rook, white_queen, white_king]


class Piece:
    img = -1
    rect = (100, 10, 700, 700)
    startX = rect[0]
    startY = rect[1]
    rows = 8
    cols = 8
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []

    def change_pos(self, row, col, color):
        self.row = row
        self.col = col
        
    def isSelected(self):
        return self.selected

    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)
        
    def draw(self, win, color):
        if self.color == "w":
            draw_this = white[self.img]
            #win.blit(draw_this, (x, y))
        else:
            draw_this = black[self.img]
            #win.blit(draw_this, (x, y))


        y = int(self.row * 87.5) + 10 + int((87.5 - draw_this.get_width()) / 2)
        x = int(self.col * 87.5) + 100 + int((87.5 - draw_this.get_height()) / 2)
                
        win.blit(draw_this, (x, y))

        if self.selected and self.color == color:
            pygame.draw.rect(win, (80, 237, 255), (x - int((87.5 - draw_this.get_width()) / 2), y - int((87.5 - draw_this.get_height()) / 2), 87, 87), 3)

            moves = self.move_list
            for move in moves:
                x = int(move[1] * 87.5) + 100 + int(87.5 / 2)
                y = int(move[0] * 87.5) + 10 + int(87.5 / 2)
                pygame.draw.circle(win, (255, 0, 0), (x, y), 25)
            
class Pawn(Piece):
    img = 0

    def valid_moves(self, board):
        moves = []

        # For Color White--------------------------------------------------------------------#
        if self.color == 'w':
            # Double_Movement--------------------------#
            if self.row == 6:
                if board[self.row - 1][self.col] == 0:
                    moves.append([self.row - 1, self.col])
                if board[self.row - 2][self.col] == 0:
                    moves.append([self.row - 2, self.col])

            # Single Movements--------------------------#
            if self.row < 6:
                if board[self.row - 1][self.col] == 0:
                    moves.append([self.row - 1, self.col])

                # Capturing Pieces----------------------------#
            if 0 < self.col < 7:
                if board[self.row - 1][self.col - 1] != 0:
                    if board[self.row - 1][self.col - 1].color != self.color:
                        moves.append([self.row - 1, self.col - 1])
                if board[self.row - 1][self.col + 1] != 0:
                    if board[self.row - 1][self.col + 1].color != self.color:
                        moves.append([self.row - 1,self.col + 1])

            if self.col == 0:
                if board[self.row - 1][self.col + 1] != 0:
                    if board[self.row - 1][self.col + 1].color != self.color:
                        moves.append([self.row - 1,self.col + 1])

            if self.col == 7:
                if board[self.row - 1][self.col - 1] != 0:
                    if board[self.row - 1][self.col - 1].color != self.color:
                        moves.append([self.row - 1, self.col - 1])
                        
        if self.color == 'b':
            # Double_Movement--------------------------#
            if self.row == 1:
                if board[self.row + 1][self.col] == 0:
                    moves.append([self.row + 1, self.col])
                if board[self.row + 2][self.col] == 0:
                    moves.append([self.row + 2, self.col])

            # Single Movements--------------------------#
            if self.row > 1:
                if board[self.row + 1][self.col] == 0:
                    moves.append([self.row + 1, self.col])
                # Capturing Pieces----------------------------#
            if 0 < self.col < 7:
                if board[self.row + 1][self.col - 1] != 0:
                    if board[self.row + 1][self.col - 1].color != self.color:
                        moves.append([self.row + 1, self.col - 1])
                if board[self.row + 1][self.col + 1] != 0:
                    if board[self.row + 1][self.col + 1].color != self.color:
                        moves.append([self.row + 1,self.col + 1])

            if self.col == 0:
                if board[self.row + 1][self.col + 1] != 0:
                    if board[self.row + 1][self.col + 1].color != self.color:
                        moves.append([self.row + 1,self.col + 1])

            if self.col == 7:
                if board[self.row + 1][self.col - 1] != 0:
                    if board[self.row + 1][self.col - 1].color != self.color:
                        moves.append([self.row + 1, self.col - 1])

                
        return moves
            

class Bishop(Piece):
    img = 1

    def valid_moves(self, board):
        moves = []

        # For Downward Movement---------------------------#
            # For Left-----------------------#
        DLC = self.col

        for row in range(self.row + 1, self.rows):
            DLC += 1
            if -1 < DLC < self.cols:
                if board[row][DLC] == 0:
                    moves.append([row, DLC])
                else:
                    if board[row][DLC].color == self.color:
                        break
                    if board[row][DLC].color != self.color:
                        moves.append([row, DLC])
                        break

            # For Right-----------------------#
        DRC = self.col
        for row in range(self.row + 1, self.rows):
            DRC -= 1
            if self.cols > DRC > -1:
                if board[row][DRC] == 0:
                    moves.append([row, DRC])
                else:
                    if board[row][DRC].color == self.color:
                        break
                    if board[row][DRC].color != self.color:
                        moves.append([row, DRC])
                        break

        # For Upward Movement---------------------------#
            # For Left-----------------------#
        ULC = self.col
        for row in range(self.row - 1, -1, -1):
            ULC += 1
            if -1 < ULC < self.cols:
                if board[row][ULC] == 0:
                    moves.append([row, ULC])
                else:
                    if board[row][ULC].color == self.color:
                        break
                    if board[row][ULC].color != self.color:
                        moves.append([row, ULC])
                        break

            # For Right---------------------#
        URC = self.col
        for row in range(self.row - 1, -1, -1):
            URC -= 1
            if -1 < URC < self.cols:
                if board[row][URC] == 0:
                    moves.append([row, URC])
                else:
                    if board[row][URC].color == self.color:
                        break
                    if board[row][URC].color != self.color:
                        moves.append([row, URC])
                        break

        return moves


class Knight(Piece):
    img = 2

    def valid_moves(self, board):
        moves = []

        # DOWN LEFT
        if self.row < 6 and self.col > 0:
            if board[self.row + 2][self.col - 1] == 0:
                moves.append([self.row + 2, self.col - 1])
            elif board[self.row + 2][self.col - 1].color != self.color:
                moves.append([self.row + 2, self.col - 1])

        # UP LEFT
        if self.row > 1 and self.col > 0:
            if board[self.row - 2][self.col - 1] == 0:
                moves.append([self.row - 2, self.col - 1])
            elif board[self.row - 2][self.col - 1].color != self.color:
                moves.append([self.row - 2, self.col - 1])

        # DOWN RIGHT
        if self.row < 6 and self.col < 7:
            if board[self.row + 2][self.col + 1] == 0:
                moves.append([self.row + 2, self.col + 1])
            elif board[self.row + 2][self.col + 1].color != self.color:
                moves.append([self.row + 2, self.col + 1])

        # UP RIGHT
        if self.row > 1 and self.col < 7:
            if board[self.row - 2][self.col + 1] == 0:
                moves.append([self.row - 2, self.col + 1])
            elif board[self.row - 2][self.col + 1].color != self.color:
                moves.append([self.row - 2, self.col + 1])

        if self.row > 0 and self.col > 1:
            if board[self.row - 1][self.col - 2] == 0:
                moves.append([self.row - 1, self.col - 2])
            elif board[self.row - 1][self.col - 2].color != self.color:
                moves.append([self.row - 1, self.col - 2])

        if self.row > 0 and self.col < 6:
            if board[self.row - 1][self.col + 2] == 0:
                moves.append([self.row - 1, self.col + 2])
            elif board[self.row - 1][self.col + 2].color != self.color:
                moves.append([self.row - 1, self.col + 2])

        if self.row < 7 and self.col > 1:
            if board[self.row + 1][self.col - 2] == 0:
                moves.append([self.row + 1, self.col - 2])
            elif board[self.row + 1][self.col - 2].color != self.color:
                moves.append([self.row + 1, self.col - 2])

        if self.row < 7 and self.col < 6:
            if board[self.row + 1][self.col + 2] == 0:
                moves.append([self.row + 1, self.col + 2])
            elif board[self.row + 1][self.col + 2].color != self.color:
                moves.append([self.row + 1, self.col + 2])

        return moves
        

class Rook(Piece):
    img = 3

    def valid_moves(self, board):
        moves = []

        # For Down------------------------------#
        UC = self.col
        for row in range(self.row + 1, self.rows):
            if board[row][UC] == 0:
                moves.append([row, UC])
            else:
                if board[row][UC].color != self.color:
                    moves.append([row, UC])
                    break
                else:
                    break

        # For Up------------------------------#
        UD = self.col
        for row in range(self.row - 1, -1, -1):
            if board[row][UD] == 0:
                moves.append([row, UD])
            else:
                if board[row][UD].color != self.color:
                    moves.append([row, UD])
                    break
                else:
                    break

        # For Left------------------------------#
        LC = self.row
        for col in range(self.col + 1, self.cols):
            if board[LC][col] == 0:
                moves.append([LC, col])
            else:
                if board[LC][col].color != self.color:
                    moves.append([LC, col])
                    break
                else:
                    break

        # For Right------------------------------#
        RC = self.row
        for col in range(self.col - 1, -1, -1):
            if board[RC][col] == 0:
                moves.append([RC, col])
            else:
                if board[RC][col].color != self.color:
                    moves.append([RC, col])
                    break
                else:
                    break

        return moves
class Queen(Piece):
    img = 4

    def valid_moves(self, board):
        moves = []

        # For Downward Movement---------------------------#
            # For Left-----------------------#
        DLC = self.col

        for row in range(self.row + 1, self.rows):
            DLC += 1
            if -1 < DLC < self.cols:
                if board[row][DLC] == 0:
                    moves.append([row, DLC])
                else:
                    if board[row][DLC].color == self.color:
                        break
                    if board[row][DLC].color != self.color:
                        moves.append([row, DLC])
                        break

            # For Right-----------------------#
        DRC = self.col
        for row in range(self.row + 1, self.rows):
            DRC -= 1
            if self.cols > DRC > -1:
                if board[row][DRC] == 0:
                    moves.append([row, DRC])
                else:
                    if board[row][DRC].color == self.color:
                        break
                    if board[row][DRC].color != self.color:
                        moves.append([row, DRC])
                        break

        # For Upward Movement---------------------------#
            # For Left-----------------------#
        ULC = self.col
        for row in range(self.row - 1, -1, -1):
            ULC += 1
            if -1 < ULC < self.cols:
                if board[row][ULC] == 0:
                    moves.append([row, ULC])
                else:
                    if board[row][ULC].color == self.color:
                        break
                    if board[row][ULC].color != self.color:
                        moves.append([row, ULC])
                        break

            # For Right---------------------#
        URC = self.col
        for row in range(self.row - 1, -1, -1):
            URC -= 1
            if -1 < URC < self.cols:
                if board[row][URC] == 0:
                    moves.append([row, URC])
                else:
                    if board[row][URC].color == self.color:
                        break
                    if board[row][URC].color != self.color:
                        moves.append([row, URC])
                        break

        # For Down------------------------------#
        UC = self.col
        for row in range(self.row + 1, self.rows):
            if board[row][UC] == 0:
                moves.append([row, UC])
            else:
                if board[row][UC].color != self.color:
                    moves.append([row, UC])
                    break
                else:
                    break

        # For Up------------------------------#
        UD = self.col
        for row in range(self.row - 1, -1, -1):
            if board[row][UD] == 0:
                moves.append([row, UD])
            else:
                if board[row][UD].color != self.color:
                    moves.append([row, UD])
                    break
                else:
                    break

        # For Left------------------------------#
        LC = self.row
        for col in range(self.col + 1, self.cols):
            if board[LC][col] == 0:
                moves.append([LC, col])
            else:
                if board[LC][col].color != self.color:
                    moves.append([LC, col])
                    break
                else:
                    break

        # For Right------------------------------#
        RC = self.row
        for col in range(self.col - 1, -1, -1):
            if board[RC][col] == 0:
                moves.append([RC, col])
            else:
                if board[RC][col].color != self.color:
                    moves.append([RC, col])
                    break
                else:
                    break
                
        return moves

class King(Piece):
    img = 5

    def valid_moves(self, board):
        moves = []
        
        # For All Directions------------------------#
        if 0 < self.row < self.rows - 1:
            if 0 < self.col < self.cols - 1:
     
                # For Up----------------------#
                if board[self.row - 1][self.col] == 0:
                    moves.append([self.row - 1, self.col])
                else:
                    if board[self.row - 1][self.col].color != self.color:
                        moves.append([self.row - 1, self.col])
                    else:
                        pass

                # For Down----------------------#
                if board[self.row + 1][self.col] == 0:
                    moves.append([self.row + 1, self.col])
                else:
                    if board[self.row + 1][self.col].color != self.color:
                        moves.append([self.row + 1, self.col])
                    else:
                        pass

                # For Right--------------------#
                if board[self.row][self.col - 1] == 0:
                    moves.append([self.row, self.col - 1])
                else:
                    if board[self.row][self.col - 1].color != self.color:
                        moves.append([self.row, self.col - 1])
                    else:
                        pass

                # For Left--------------------#
                if board[self.row][self.col + 1] == 0:
                    moves.append([self.row, self.col + 1])
                else:
                    if board[self.row][self.col + 1].color != self.color:
                        moves.append([self.row, self.col + 1])
                    else:
                        pass

                # For DL--------------------#
                if board[self.row + 1][self.col - 1] == 0:
                    moves.append([self.row + 1, self.col - 1])
                else:
                    if board[self.row + 1][self.col - 1].color != self.color:
                        moves.append([self.row + 1, self.col - 1])
                    else:
                        pass

                # For DR--------------------#
                if board[self.row + 1][self.col + 1] == 0:
                    moves.append([self.row + 1, self.col + 1])
                else:
                    if board[self.row + 1][self.col + 1].color != self.color:
                        moves.append([self.row + 1, self.col + 1])
                    else:
                        pass

                # For UL--------------------#
                if board[self.row - 1][self.col - 1] == 0:
                    moves.append([self.row - 1, self.col - 1])
                else:
                    if board[self.row - 1][self.col - 1].color != self.color:
                        moves.append([self.row - 1, self.col - 1])
                    else:
                        pass

                # For UR--------------------#
                if board[self.row - 1][self.col + 1] == 0:
                    moves.append([self.row - 1, self.col + 1])
                else:
                    if board[self.row - 1][self.col + 1].color != self.color:
                        moves.append([self.row - 1, self.col + 1])
                    else:
                        pass

        # At Corners--------------------------#
            # At UL---------------#
        if self.row == 0 and self.col == 0:
            if board[self.row][self.col + 1] == 0:
                    moves.append([self.row, self.col + 1])
            else:
                if board[self.row][self.col + 1].color != self.color:
                    moves.append([self.row, self.col + 1])
                else:
                    pass

            if board[self.row + 1][self.col + 1] == 0:
                    moves.append([self.row + 1, self.col + 1])
            else:
                if board[self.row + 1][self.col - 1].color != self.color:
                    moves.append([self.row + 1, self.col + 1])
                else:
                     pass

            if board[self.row + 1][self.col] == 0:
                    moves.append([self.row + 1, self.col])
            else:
                if board[self.row + 1][self.col].color != self.color:
                    moves.append([self.row + 1, self.col])
                else:
                    pass

            # At UR---------------#
        if self.row == 0 and self.col == self.cols - 1:
            if board[self.row + 1][self.col] == 0:
                    moves.append([self.row + 1, self.col])
            else:
                if board[self.row + 1][self.col].color != self.color:
                    moves.append([self.row + 1, self.col])
                else:
                    pass

            if board[self.row + 1][self.col - 1] == 0:
                    moves.append([self.row + 1, self.col - 1])
            else:
                if board[self.row + 1][self.col - 1].color != self.color:
                    moves.append([self.row + 1, self.col - 1])
                else:
                    pass

            if board[self.row][self.col - 1] == 0:
                    moves.append([self.row , self.col - 1])
            else:
                if board[self.row][self.col - 1].color != self.color:
                    moves.append([self.row, self.col - 1])
                else:
                    pass
            # At DL---------------#
        if self.row == self.rows - 1 and self.col == 0:
            if board[self.row][self.col + 1] == 0:
                    moves.append([self.row, self.col + 1 ])
            else:
                if board[self.row][self.col + 1].color != self.color:
                    moves.append([self.row, self.col + 1])
                else:
                    pass

            if board[self.row - 1][self.col + 1] == 0:
                    moves.append([self.row - 1, self.col + 1])
            else:
                if board[self.row - 1][self.col + 1].color != self.color:
                    moves.append([self.row - 1, self.col + 1])
                else:
                    pass

            if board[self.row - 1][self.col] == 0:
                    moves.append([self.row - 1, self.col])
            else:
                if board[self.row - 1][self.col].color != self.color:
                    moves.append([self.row - 1, self.col])
                else:
                    pass

                # At DR---------------#
        if self.row == self.rows - 1 and self.col == self.cols - 1:
            if board[self.row][self.col - 1] == 0:
                    moves.append([self.row, self.col - 1 ])
            else:
                if board[self.row][self.col - 1].color != self.color:
                    moves.append([self.row, self.col - 1])
                else:
                    pass

            if board[self.row - 1][self.col - 1] == 0:
                    moves.append([self.row - 1, self.col -+ 1])
            else:
                if board[self.row - 1][self.col - 1].color != self.color:
                    moves.append([self.row - 1, self.col - 1])
                else:
                    pass

            if board[self.row - 1][self.col] == 0:
                    moves.append([self.row - 1, self.col])
            else:
                if board[self.row - 1][self.col].color != self.color:
                    moves.append([self.row - 1, self.col])
                else:
                    pass
            
            
        # For Other Locations--------------------#
        if self.row == 0:
            if 0 < self.col < self.cols - 1:
                # For Down-------------------#
                if board[self.row + 1][self.col] == 0:
                    moves.append([self.row + 1, self.col])
                else:
                    if board[self.row + 1][self.col].color != self.color:
                        moves.append([self.row + 1, self.col])
                    else:
                        pass

                # For Right--------------------#
                if board[self.row][self.col - 1] == 0:
                    moves.append([self.row, self.col - 1])
                else:
                    if board[self.row][self.col - 1].color != self.color:
                        moves.append([self.row, self.col - 1])
                    else:
                        pass

                # For Left--------------------#
                if board[self.row][self.col + 1] == 0:
                    moves.append([self.row, self.col + 1])
                else:
                    if board[self.row][self.col + 1].color != self.color:
                        moves.append([self.row, self.col + 1])
                    else:
                        pass

                # For DL--------------------#
                if board[self.row + 1][self.col - 1] == 0:
                    moves.append([self.row + 1, self.col - 1])
                else:
                    if board[self.row + 1][self.col - 1].color != self.color:
                        moves.append([self.row + 1, self.col - 1])
                    else:
                        pass

                # For DR--------------------#
                if board[self.row + 1][self.col + 1] == 0:
                    moves.append([self.row + 1, self.col + 1])
                else:
                    if board[self.row + 1][self.col + 1].color != self.color:
                        moves.append([self.row + 1, self.col + 1])
                    else:
                        pass
                    
        if self.row == self.rows - 1:
            if 0 < self.col < self.cols - 1:
                # For Up-------------------#
                if board[self.row - 1][self.col] == 0:
                    moves.append([self.row - 1, self.col])
                else:
                    if board[self.row - 1][self.col].color != self.color:
                        moves.append([self.row - 1, self.col])
                    else:
                        pass

                # For Right--------------------#
                if board[self.row][self.col - 1] == 0:
                    moves.append([self.row, self.col - 1])
                else:
                    if board[self.row][self.col - 1].color != self.color:
                        moves.append([self.row, self.col - 1])
                    else:
                        pass

                # For Left--------------------#
                if board[self.row][self.col + 1] == 0:
                    moves.append([self.row, self.col + 1])
                else:
                    if board[self.row][self.col + 1].color != self.color:
                        moves.append([self.row, self.col + 1])
                    else:
                        pass

                # For UL--------------------#
                if board[self.row - 1][self.col - 1] == 0:
                    moves.append([self.row - 1, self.col - 1])
                else:
                    if board[self.row - 1][self.col - 1].color != self.color:
                        moves.append([self.row - 1, self.col - 1])
                    else:
                        pass

                # For UR--------------------#
                if board[self.row - 1][self.col + 1] == 0:
                    moves.append([self.row - 1, self.col + 1])
                else:
                    if board[self.row - 1][self.col + 1].color != self.color:
                        moves.append([self.row - 1, self.col + 1])
                    else:
                        pass

        if self.col == 0:
            if 0 < self.row < self.rows - 1:
                    # For Up----------------------#
                if board[self.row - 1][self.col] == 0:
                     moves.append([self.row - 1, self.col])
                else:
                    if board[self.row - 1][self.col].color != self.color:
                        moves.append([self.row - 1, self.col])
                    else:
                        pass

                        # For Down----------------------#
                if board[self.row + 1][self.col] == 0:
                    moves.append([self.row + 1, self.col])
                else:
                    if board[self.row + 1][self.col].color != self.color:
                        moves.append([self.row + 1, self.col])
                    else:
                        pass

                        # For Right--------------------#
                if board[self.row][self.col + 1] == 0:
                    moves.append([self.row, self.col + 1])
                else:
                    if board[self.row][self.col + 1].color != self.color:
                        moves.append([self.row, self.col + 1])
                    else:
                        pass
                        
                        # For UR--------------------#
                if board[self.row - 1][self.col + 1] == 0:
                    moves.append([self.row - 1, self.col + 1])
                else:
                    if board[self.row - 1][self.col + 1].color != self.color:
                        moves.append([self.row - 1, self.col + 1])
                    else:
                        pass

                        # For DR--------------------#
                if board[self.row + 1][self.col + 1] == 0:
                    moves.append([self.row + 1, self.col + 1])
                else:
                    if board[self.row + 1][self.col + 1].color != self.color:
                        moves.append([self.row + 1, self.col + 1])
                    else:
                        pass

        if self.col == self.cols - 1:
            if 0 < self.row < self.rows - 1:
                    # For Up----------------------#
                if board[self.row - 1][self.col] == 0:
                     moves.append([self.row - 1, self.col])
                else:
                    if board[self.row - 1][self.col].color != self.color:
                        moves.append([self.row - 1, self.col])
                    else:
                        pass

                        # For Down----------------------#
                if board[self.row + 1][self.col] == 0:
                    moves.append([self.row + 1, self.col])
                else:
                    if board[self.row + 1][self.col].color != self.color:
                        moves.append([self.row + 1, self.col])
                    else:
                        pass

                        # For Left--------------------#
                if board[self.row][self.col - 1] == 0:
                    moves.append([self.row, self.col - 1])
                else:
                    if board[self.row][self.col - 1].color != self.color:
                        moves.append([self.row, self.col - 1])
                    else:
                        pass
                        
                        # For UR--------------------#
                if board[self.row - 1][self.col - 1] == 0:
                    moves.append([self.row - 1, self.col - 1])
                else:
                    if board[self.row - 1][self.col - 1].color != self.color:
                        moves.append([self.row - 1, self.col - 1])
                    else:
                        pass

                        # For DR--------------------#
                if board[self.row + 1][self.col - 1] == 0:
                    moves.append([self.row + 1, self.col - 1])
                else:
                    if board[self.row + 1][self.col - 1].color != self.color:
                        moves.append([self.row + 1, self.col - 1])
                    else:
                        pass
                
        return moves

        
