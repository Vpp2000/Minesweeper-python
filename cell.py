from tkinter import Button
import random

import settings


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
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def right_click_actions(self, event):
        print(f'Right click... ${event}  ')

    @staticmethod
    def randomized_mines():
        picked_cells = random.sample(Cell.game_cells, settings.MINES_IN_GAME)

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def show_mine(self):
        self.cell_btn_object['text'] = 'MINE'
        self.cell_btn_object["bg"] = "red"

    def show_cell(self):
        self.cell_btn_object['text'] = self.surrounded_mines_length

    @property
    def surrounded_cells(self):
        surrounded_cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        surrounded_cells = [cell for cell in surrounded_cells if cell is not None]

        return surrounded_cells

    @property
    def surrounded_mines_length(self):
        return len([cell for cell in self.surrounded_cells if cell.is_mine])

    def get_cell_by_axis(self, x, y):
        for cell in Cell.game_cells:
            if cell.x == x and cell.y == y:
                return cell

    def __repr__(self):
        return f"Cell(y={self.y},x={self.x})"
