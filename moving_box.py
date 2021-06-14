# script for creating a moving box game in tkinter
# created: 10 April 2021 author: Alfie Grace

import tkinter as tk
from PIL import ImageTk, Image

# define window variables
window_size = 700
box_width = window_size/10

# define the sensitivity of movement keys, make larger for smaller movements or larger for bigger
move_step_size = 30

# define start location for the box
global grid_x
grid_x = window_size/2
grid_y = window_size*0.527

class moving_box():
    # -------------------------------------
    # initialization functions
    # -------------------------------------
    def __init__(self):
        # create the window and generate a title
        self.window = tk.Tk()
        self.window.title('Moving Box')

        # create the canvas
        self.draw_canvas()

        # create the box
        self.draw_new_box()

        # bind arrow keys to movement
        self.window.bind('<Right>', self.move_right)
        self.window.bind('<Left>', self.move_left)

    def import_images(self):
        # import the background
        global background
        background = Image.open('background.jpg')
        background = background.resize((window_size + 50, window_size + 100), Image.ANTIALIAS)
        background = ImageTk.PhotoImage(background)

    def main_loop(self):
        # trigger the main loop
        self.window.mainloop()

    # -------------------------------------
    # drawing functions
    # -------------------------------------
    def draw_canvas(self):
        # create the canvas and pack
        self.canvas = tk.Canvas(self.window, width=window_size, height=window_size)
        self.canvas.pack()
        self.canvas.config(bg='black')

        # import the images
        self.import_images()

        # create background
        self.canvas.create_image(window_size/2, window_size/2, image=background)

    def draw_new_box(self):
        # create_line(start_x, start_y, end_x, end_y
        x_location, y_location = grid_x, grid_y

        # create the box
        global box
        box = self.canvas.create_rectangle(x_location - box_width/2, y_location - box_width/2, x_location + box_width/2,
                                           y_location + box_width/2, fill = 'mistyrose2')

    # -------------------------------------
    # logical functions
    # -------------------------------------
    def move_right(self, event=None):
        global grid_x
        grid_x = grid_x + window_size/move_step_size
        self.canvas.delete(box)
        self.draw_new_box()

    def move_left(self, event=None):
        global grid_x
        grid_x = grid_x - window_size/move_step_size
        self.canvas.delete(box)
        self.draw_new_box()

if __name__ == '__main__':
    # start the game
    game_instance = moving_box()
    game_instance.main_loop()
