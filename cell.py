from tkinter import Button
import random


class Cell:
    game_cells = []

    def __init__(self, x, y, text, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.text = text
        self.x = x
        self.y = y

        Cell.game_cells.append(self)

    def create_btn_object(self, parent_location):
        btn = Button(parent_location, width=12, height=4, text=self.text)
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(f'Left click... ${event}')

    def right_click_actions(self, event):
        print(f'Right click... ${event}  ')

    @staticmethod
    def randomized_mines():
        TOTAL_CELLS_CHOSEN = 9
        picked_cells = random.sample(Cell.all, TOTAL_CELLS_CHOSEN)

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell(y={self.y},x={self.x})"
