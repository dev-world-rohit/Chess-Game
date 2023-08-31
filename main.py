import pygame, random
from board import Board

# Pygame/Window Setup----------------------------------------------#
pygame.init()

screen_width, screen_height = (900, 720)
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chess')

# Images-----------------------------------------------------#
board_img = pygame.transform.scale(pygame.image.load('data/board.png'), (700, 700)).convert()

def find_pos(pos):
    rect = (100, 10, 700, 700)
    if 100 < pos[0] < 800 and 10 < pos[1] < 710:
        row = int((pos[0] - rect[0]) // 87)
        col = int((pos[1] - rect[1]) // 87)
    else:
        row, col = None, None

    return row, col

def turn_effect(color):
    if color == 'w':
        pygame.draw.rect(win, (50, 237, 255), (810, 365, 80, 175))
        pygame.draw.rect(win, (100, 100, 100), (810, 180, 80, 175))
            
    else:
        pygame.draw.rect(win, (50, 237, 255), (810, 180, 80, 175))
        pygame.draw.rect(win, (100, 100, 100), (810, 365, 80, 175))


        
# Main Loop------------------------------------------------------#
def main():

    run = True
    clock = pygame.time.Clock()
    fps = 30
    color = 'w'

    rect_effect = []
    
    board = Board(8, 8, color)
    while run:

        win.fill((0, 0, 0))

        turn_effect(color)
        pygame.draw.rect(win, (255, 0, 0), (100, 10, 700, 700), 5)
        win.blit(board_img, (100, 10))
        board.draw_images(win, color)

                    
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = find_pos(pos)
                if row != None and col != None:
                    board.update_moves()
                    moved = board.move(row, col, color)
                    if moved:
                        if color == 'b':
                            color = 'w'
                        else:
                            color = 'b'
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
main()












