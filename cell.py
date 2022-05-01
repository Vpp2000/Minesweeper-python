from tkinter import Button

class Cell:
    def __init__(self, text, is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object = None
        self.text = text

    def create_btn_object(self, parent_location):
        btn = Button(parent_location, text=self.text)
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(f'Left click... ${event}')

    def right_click_actions(self, event):
        print(f'Right click... ${event}')
