from tkinter import *

root = Tk(className='Checkers_TJA', useTk=1)
root.attributes('-fullscreen', True)
label = Label(root, text="Checkers coming...!")
label.pack()

base_size = 320

game_height = 3*base_size
game_width = 4*base_size

C = Canvas(root, bg="#9FAA9F",
           height=game_height, width=game_width)

rectangle = C.create_rectangle(0.75*base_size, 0.25*base_size, 3.25*base_size,
                   2.75*base_size, fill="#DDDDAA")


def create_row(y,fill_check=1): 
    i = 0
    while i < 2.5:
        fill_check += 1
        cells = C.create_rectangle((0.75+i)*base_size, (y)*base_size, (1.0625+i)*base_size,
                        (y+0.3125)*base_size,  fill="#BD9168" if fill_check%2 == 0 else "#DDDDAA")
        i += 0.3125

y = 0.25
fill_check = 1
while y < 2.5:
    create_row(y,fill_check)
    y +=0.3125
    fill_check += 1

C.pack()
root.mainloop()