import random

from cell import Cell
from time import sleep

WAIT_TIME = 0.01

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        cur_cell = self._cells[i][j]
        cur_cell.visited = True
        
        if cur_cell == self._cells[self._num_cols-1][self._num_rows-1]:
            return True
        
        # left
        if i > 0 and not cur_cell.has_left_wall and not self._cells[i-1][j].visited:
            cur_cell.draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                cur_cell.draw_move(self._cells[i-1][j], True)
            
        # right
        if i < self._num_cols - 1 and not cur_cell.has_right_wall and not self._cells[i+1][j].visited:
            cur_cell.draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                cur_cell.draw_move(self._cells[i+1][j], True)
            
        # top
        if j > 0 and not cur_cell.has_top_wall and not self._cells[i][j-1].visited:
           cur_cell.draw_move(self._cells[i][j-1])
           if self._solve_r(i,j-1):
               return True
           else:
               cur_cell.draw_move(self._cells[i][j-1], True)
            
        # bottom
        if j < self._num_rows - 1 and not cur_cell.has_bottom_wall and not self._cells[i][j+1].visited:
            cur_cell.draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                cur_cell.draw_move(self._cells[i][j+1], True)
        
    def _create_cells(self):
        self._cells = [[Cell(self._win) for r in range(self._num_rows)] 
                       for c in range(self._num_cols)]
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j, wait=False):
        if self._win is None:
            return
        self._cells[i][j].draw(
            self._x1 + i*self._cell_size_x,
            self._y1 + j*self._cell_size_y,
            self._x1 + (i+1)*self._cell_size_x,
            self._y1 + (j+1)*self._cell_size_y
        )
        self._animate(wait)
        
    def _break_entrance_and_exit(self):
        if self._cells and self._cells[0]:
            self._cells[0][0].has_top_wall = False
            self._draw_cell(0, 0)
            self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
            self._draw_cell(self._num_cols - 1, self._num_rows - 1)
            
    def _break_walls_r(self, i, j):
        if self._cells and self._cells[0]:
            self._cells[i][j].visited = True
            while True:
                to_visit = []
                
                # left
                if i > 0 and not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j, 'l'))
                    
                # right
                if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j, 'r'))
                    
                # top
                if j > 0 and not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1, 't'))
                    
                # bottom
                if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1, 'b'))

                if len(to_visit) == 0:
                    self._draw_cell(i, j, wait=True)
                    return

                next_cell = to_visit[random.randrange(len(to_visit))]
                
                if next_cell[2] == 'r':
                    self._cells[i][j].has_right_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
                elif next_cell[2] == 'l':
                    self._cells[i][j].has_left_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
                elif next_cell[2] == 't':
                    self._cells[i][j].has_top_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
                elif next_cell[2] == 'b':
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_top_wall = False

                self._break_walls_r(next_cell[0], next_cell[1])          
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def _animate(self, wait=False, wait_time=WAIT_TIME):
        self._win.redraw()
        if wait:
            sleep(wait_time)