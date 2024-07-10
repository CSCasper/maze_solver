from gfx import Window, Line, Point, Cell

if __name__ == '__main__':
    win = Window(800, 600)
    cell_1 = Cell(win)
    cell_2 = Cell(win)

    cell_1.draw(30, 30, 60, 60)
    cell_2.draw(60, 30, 90, 60)
    
    cell_1.draw_move(cell_2)
    
    win.wait_for_close()