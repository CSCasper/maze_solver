from tkinter import Tk, BOTH, Canvas

class Window():

    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, width=width, height=height)
        self._canvas.pack(fill=BOTH, expand=1)
        self._running = False

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)
        
    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color)

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
    def get_center(self):
        return ((self._x1+self._x2)//2, (self._y1+self._y2)//2)
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
            
    def draw_move(self, to_cell, undo=False):
        from_cell_center = self.get_center()
        to_cell_center = to_cell.get_center()
        
        color = "red" if undo is True else "gray"
        
        move_line = Line(
                    Point(from_cell_center[0], from_cell_center[1]),
                    Point(to_cell_center[0], to_cell_center[1])
                    )
        
        self._win.draw_line(move_line, fill_color=color)