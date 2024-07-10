from gfx import Line, Point

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
        
        l_color = "black" if self.has_left_wall else "white"
        r_color = "black" if self.has_right_wall else "white"
        t_color = "black" if self.has_top_wall else "white"
        b_color = "black" if self.has_bottom_wall else "white"
        
        self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), l_color)
        self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), r_color)
        self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), t_color)
        self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), b_color)
        
    def draw_move(self, to_cell, undo=False):
        from_cell_center = self.get_center()
        to_cell_center = to_cell.get_center()
        
        color = "red" if undo is True else "gray"
        
        move_line = Line(
                    Point(from_cell_center[0], from_cell_center[1]),
                    Point(to_cell_center[0], to_cell_center[1])
                    )
        
        self._win.draw_line(move_line, fill_color=color)