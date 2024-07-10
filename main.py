from gfx import Window, Line, Point

if __name__ == '__main__':
    win = Window(800, 600)
    line_1 = Line(Point(10, 10), Point(20, 20))
    line_2 = Line(Point(30, 20), Point(40, 100))
    win.draw_line(line_1)
    win.draw_line(line_2, "red")
    win.wait_for_close()
