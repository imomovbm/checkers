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

chess_square_address = {}

y = 0.25
for col in range(8,0,-1):
    i = 0
    for row , letter in enumerate(['a','b','c','d','e','f','g','h']):
        cells = C.create_rectangle((0.75+i)*base_size, (y)*base_size, (1.0625+i)*base_size,
                        (y+0.3125)*base_size,  fill="#DDDDAA" if (col+row)%2 == 0 else "#BD9168")
        chess_square_address[f'{letter}{col}'] = [(0.90625+i)*base_size, (y+0.15625)*base_size]
        i += 0.3125
    y +=0.3125
    
# chess board address coordinates print(chess_square_address)

def check_square_address(coordinate):
    half_square = 0.3125*base_size/2
    x,y = coordinate
    for piecePosition in chess_square_address:
        square_x,square_y = chess_square_address[piecePosition]
        if square_x-half_square < x < square_x+half_square and square_y - half_square < y < square_y + half_square:
            return piecePosition

pieces_address = {
    'a1': 1,'a2': 0,'a3': 1,'a4': 0,'a5': 0,'a6': 0,'a7': -1,'a8': 0,
    'b1': 0,'b2': 1,'b3': 0,'b4': 0,'b5': 0,'b6': -1,'b7': 0,'b8': -1,
    'c1': 1,'c2': 0,'c3': 1,'c4': 0,'c5': 0,'c6': 0,'c7': -1,'c8': 0,
    'd1': 0,'d2': 1,'d3': 0,'d4': 0,'d5': 0,'d6': -1,'d7': 0,'d8': -1,
    'e1': 1,'e2': 0,'e3': 1,'e4': 0,'e5': 0,'e6': 0,'e7': -1,'e8': 0,
    'f1': 0,'f2': 1,'f3': 0,'f4': 0,'f5': 0,'f6': -1,'f7': 0,'f8': -1,
    'g1': 1,'g2': 0,'g3': 1,'g4': 0,'g5': 0,'g6': 0,'g7': -1,'g8': 0,
    'h1': 0,'h2': 1,'h3': 0,'h4': 0,'h5': 0,'h6': -1,'h7': 0,'h8': -1,
}

def draw_piece(cx,cy,color):
    r = 0.1*base_size
    return C.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color)

def set_pieces():
    for address in pieces_address:
        x,y = chess_square_address[address]
        if pieces_address[address] == 1:
            color = 'white'
            pieces_address[address] = draw_piece(x,y, color)
        elif pieces_address[address] == -1:
            color = 'black'
            pieces_address[address] = draw_piece(x,y, color)

set_pieces()
# piece addresses print(pieces_address)

def check_click(event):
    x = event.x
    y = event.y
    # check the coordinate that was clicked    print(f"Clicked at: {event.x}, {event.y}")

    # check the chess board address that was clicked    print(check_square_address((x, y)))
    selected_piece = check_square_address(x,y)
    return selected_piece
     # C.delete(pieces_address[check_square_address((x, y))])
     # set_pieces()


C.pack()
C.bind("<Button-1>", check_click)


root.mainloop()