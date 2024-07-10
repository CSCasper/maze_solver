from gfx import Window, Line, Point, Cell

if __name__ == '__main__':
    win = Window(800, 600)
    cell_1 = Cell(win)
    cell_2 = Cell(win)

    cell_1.draw(100, 100, 20, 20)
    cell_2.draw(30, 30, 50, 50)
    
    win.wait_for_close()
