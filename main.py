from malcom import Snake, Food, Poison
from tkinter import *

#CONSTANTS
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50

ROWS = int(GAME_HEIGHT/SPACE_SIZE)
COLS = int(GAME_WIDTH/SPACE_SIZE)

SPEED = 150
BODY_PARTS = 3
SNAKE_COLOR = '#000000'
FOOD_COLOR ='#00FF00'
POISON_COLOR = "#FFFF00"
BG_COLOR = '#FFFFFF'

score = 0

def initialize_board(canvas): ### RAYNARD
        board = []

        for i in range(ROWS):
            for j in range(COLS):
               board.append((i, j))

        for i in range(ROWS):
             canvas.create_line(
                  i * GAME_WIDTH / ROWS, 0, i * GAME_WIDTH / ROWS, GAME_WIDTH,
                  )

        for i in range(COLS):
             canvas.create_line(
                  0, i * GAME_HEIGHT / COLS, GAME_HEIGHT, i * GAME_HEIGHT / COLS,
                  )

def next_turn(snake, food, poison):     ### HARITHA
     pass

def change_direction(new_direction):    ### DARRYL
     pass
     
def check_collision(snake):   ### DARRYL
     pass

def game_over(): ### JADEN
     print('gg')
     

def play_again():   ### JADEN
     pass

def mouse_input(event):  ### JADEN
     pass



# initialise game window
window = Tk()
window.title("Makan Time")
window.resizable(False, False)


direction = 'down'

label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
play_again()
canvas.pack()
window.update()


### RAYNARD
# Centralize game window
## get game dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()

## get screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

## get coordinate of where game screen should be
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

## set game window
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# bind keyboard controls
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

window.mainloop()