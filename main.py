from tkinter import *
import settings
import utils
from cell import Cell

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()

    root.configure(bg="black")
    root.geometry(settings.ROOT_GEOMETRY_STR)
    root.title("Minesweeper")
    root.resizable(False, False)

    top_frame = Frame(root, bg="red", width=settings.WIDTH, height=utils.height_prct(25))
    top_frame.place(x=0, y=0)

    left_frame = Frame(root, bg='blue', width=utils.width_prct(25), height=utils.height_prct(75))
    left_frame.place(x=0, y=utils.height_prct(25))

    center_fame = Frame(
        root,
        bg="black",
        width=utils.width_prct(75),
        height=utils.height_prct(75)
    )

    center_fame.place(x=utils.width_prct(25), y=utils.height_prct(25))

    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            cell = Cell(x=x, y=y, text=f"y={y} x={x}")
            cell.create_btn_object(center_fame)
            cell.cell_btn_object.grid(column=x, row=y)

    Cell.randomized_mines()
    Cell.create_cell_count_label(left_frame)
    Cell.cell_count_label_object.place(x=0, y=0)
    root.mainloop()
