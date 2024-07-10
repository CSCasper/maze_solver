from gfx import Window
from maze import Maze

WIN_W = 805
WIN_H = 605

MAZE_OFFSET = 5

CELL_SIZE = 50

NUM_ROWS = (WIN_W - MAZE_OFFSET) // CELL_SIZE
NUM_COLS = (WIN_H - MAZE_OFFSET) // CELL_SIZE

if __name__ == '__main__':
    win = Window(WIN_W, WIN_H)
        
    maze = Maze(MAZE_OFFSET, MAZE_OFFSET, NUM_COLS, NUM_ROWS, CELL_SIZE, CELL_SIZE, win)
    
    win.wait_for_close()