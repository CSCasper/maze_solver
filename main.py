from gfx import Window
from cell import Cell

if __name__ == '__main__':
    win = Window(800, 600)
    cell_1 = Cell(win)
    cell_2 = Cell(win)
    cell_3 = Cell(win)

    cell_1.draw(30, 30, 60, 60)
    cell_2.draw(60, 30, 90, 60)
    cell_3.draw(60, 60, 90, 90)
    
    cell_1.draw_move(cell_2)
    cell_2.draw_move(cell_3, True)
    
    win.wait_for_close()