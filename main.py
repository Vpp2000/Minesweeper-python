from tkinter import *
import settings
import utils

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

    root.mainloop()
