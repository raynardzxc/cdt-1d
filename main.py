from tkinter import *
import random

# -------------------------------------------------
# Global Constants
# -------------------------------------------------

# Setting the size of the board

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50

# Getting rows and columns from the board size for objects (eg. snake)

ROWS = int(GAME_HEIGHT/SPACE_SIZE)
COLS = int(GAME_WIDTH/SPACE_SIZE)

# Initializing the characteristics of the game

SPEED = 150
BODY_PARTS = 3
SNAKE_COLOR = '#ADC2A9'
SNAKE_OUTLINE_COLOR = '#125C13'
GREEN_COLOR ='#9AE66E'
DARK_GREEN_COLOR = '#105652'
YELLOW_COLOR = "#FBF46D"
ORANGE_COLOR = '#FF4848'
BG_COLOR = '#F9F3DF'
TEXT_COLOR = "#7BC043"
BLACK_COLOR = "#000000"

class MakanTime:
     # -------------------------------------------------
     # Init Functions
     # -------------------------------------------------

     # DARRYL
     def __init__(self):
          ## create window settings
          self.window = Tk()
          self.window.title("Makan-Time")
          self.window.resizable(False, False)

          ## create canvas
          self.canvas = Canvas(self.window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
          self.canvas.pack()
          
          ## binding sser input
          self.window.bind("<Key>", self.key_input)
          self.window.bind("<Button-1>", self.mouse_input)
          self.play_again()
          self.begin = False
     
     # DARRYL
     def initialize_board(self):
          self.board = []

          ## obj list used to generate display
          self.poison_obj = []
          self.food_obj = []
          self.wall_obj = []

          ## cell list used to identify coordinate of obj
          self.old_poison_cell = []
          self.old_food_cell = []
          self.previous_wall_cells = []

          ## create board
          for i in range(ROWS):
               for j in range(COLS):
                    self.board.append((i, j))

          ## draw lines to create grid
          for i in range(ROWS):
               self.canvas.create_line(
                    i * GAME_WIDTH / ROWS, 0, i * GAME_WIDTH / ROWS, GAME_WIDTH,
                    )

          for i in range(COLS):
               self.canvas.create_line(
                    0, i * GAME_HEIGHT / COLS, GAME_HEIGHT, i * GAME_HEIGHT / COLS,
                    )
     
     # DARRYL
     def initialise_snake(self):
          self.snake = []
          self.crashed = False
          self.heading = "Down"
          self.last_key = self.heading

          ## create dict of forbidden actions
          ## prevent snake from eating itself
          self.forbidden_actions = {}
          self.forbidden_actions["Up"] = "Down"
          self.forbidden_actions["Down"] = "Up"
          self.forbidden_actions["Right"] = "Left"
          self.forbidden_actions["Left"] = "Right"

          self.snake_objects = []
          for i in range(BODY_PARTS):
               self.snake.append((0, i))

     # HARITHA
     def play_again(self):
          self.canvas.delete("all")
          self.initialize_board()
          self.initialise_snake()
          self.place_food()
          self.place_poison()
          self.display_snake(mode="init")

     # HARITHA
     def mainloop(self):
          while True:
               self.window.update()
               if self.begin:
                    if not self.crashed:
                         self.window.after(SPEED, self.update_snake(self.last_key))
                    else:
                         self.begin = False
                         self.display_gameover()
     
     # -------------------------------------------------
     # Display Functions
     # -------------------------------------------------
     
     # HARITHA
     def display_gameover(self):
          score = len(self.snake)
          self.canvas.delete("all")
          score_text = "Score:\n"

          self.canvas.create_text(
               GAME_WIDTH/2,
               3*GAME_HEIGHT/8,
               font="consolas 40 bold",
               fill = TEXT_COLOR,
               text = score_text,
          )
          score_value = str(score)
          self.canvas.create_text(
               GAME_WIDTH/2,
               1*GAME_HEIGHT/2,
               font="consolas 50 bold",
               fill = TEXT_COLOR,
               text = score_value,
          )
          play_text = "Click to play again \n"
          self.canvas.create_text(
               GAME_WIDTH/2,
               15*GAME_HEIGHT/16,
               font="consolas 20 bold",
               fill = "gray",
               text = play_text,
          )

     # MALCOM
     def place_food(self):
          unoccupied_cells = set(self.board) - set(self.snake) - set(self.old_food_cell) - set(self.old_poison_cell) - set(self.previous_wall_cells)
          self.food_cell = random.choice(list(unoccupied_cells))
          x = self.food_cell[0] * SPACE_SIZE
          y = self.food_cell[1] * SPACE_SIZE
          self.food_obj = self.canvas.create_oval(
               x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=GREEN_COLOR, outline=DARK_GREEN_COLOR, width=5, tag="food"
          )

     # MALCOM
     def place_poison(self):
          unoccupied_cells = set(self.board) - set(self.snake) - set(self.old_food_cell) - set(self.old_poison_cell) - set(self.previous_wall_cells)
          self.poison_cell = random.choice(list(unoccupied_cells))
          x = self.poison_cell[0] * SPACE_SIZE
          y = self.poison_cell[1] * SPACE_SIZE
          self.poison_obj = self.canvas.create_rectangle(
               x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=YELLOW_COLOR, outline=ORANGE_COLOR, width=5, tag="poison"
          )

     ## JADEN
     def place_wall(self):
          unoccupied_cells = set(self.board) - set(self.snake) - set(self.old_food_cell) - set(self.old_poison_cell) - set(self.previous_wall_cells)
          self.wall_cell = random.choice(list(unoccupied_cells))
          x = self.wall_cell[0] * SPACE_SIZE
          y = self.wall_cell[1] * SPACE_SIZE
          self.wall_obj = self.canvas.create_rectangle(
               x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=BLACK_COLOR, outline=BLACK_COLOR, width=5, tag="wall"
          )
          self.previous_wall_cells.append(self.wall_cell)
     
     # RAYNARD
     def display_snake(self, mode=""):
          ## prevent snake from growing without eating, pop every step
          if self.snake_objects != []:
               self.canvas.delete(self.snake_objects.pop(0))

          ## initial state of snake
          if mode == "init":
               for i, cell in enumerate(self.snake):
                    x = cell[0] * SPACE_SIZE
                    y = cell[1] * SPACE_SIZE
                    self.snake_objects.append(
                         self.canvas.create_rectangle(
                              x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, outline=SNAKE_OUTLINE_COLOR, width=5, tag="body"
                         )
                    )
          else:
               ## new head
               head = self.snake[-1]
               x = head[0] * SPACE_SIZE
               y = head[1] * SPACE_SIZE

               ## append new head to snake
               self.snake_objects.append(
                         self.canvas.create_rectangle(
                              x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, outline=SNAKE_OUTLINE_COLOR, width=5, tag="head"
                         )
                    )
               if head == self.old_food_cell:
                    ## insert new cell at tail
                    self.snake.insert(0, self.old_food_cell)
                    self.old_food_cell = []
                    tail = self.snake[0]
                    x = tail[0] * SPACE_SIZE
                    y = tail[1] * SPACE_SIZE
                    self.snake_objects.append(
                         self.canvas.create_rectangle(
                              x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, outline=SNAKE_OUTLINE_COLOR, width=5, tag="new tail"
                         )
                    )
               elif head == self.old_poison_cell:
                    ## delete tail
                    self.canvas.delete(self.snake_objects.pop(0))

          self.window.update()

     # -------------------------------------------------
     # Game Logic Function
     # -------------------------------------------------
     
     # RAYNARD
     def update_snake(self, key):

          tail = self.snake[0]
          head = self.snake[-1]

          ## prevent snake from growing without eating anything
          if tail != self.old_food_cell:
               self.snake.pop(0)

          ## reduce length of snake if it eats poison
          if head == self.old_poison_cell:
               if len(self.snake) == 0: self.crashed = True
               else: self.snake.pop(0)
          
          ## append new head depending on direction of movement
          if key == "Up":
               self.snake.append((head[0], head[1] - 1))
          elif key == "Down":
               self.snake.append((head[0], head[1] + 1))
          elif key == "Left":
               self.snake.append((head[0] - 1, head[1]))
          elif key == "Right":
               self.snake.append((head[0] + 1, head[1]))
          

          head = self.snake[-1]
          if (
               ## exceed right side of border
               head[0] > COLS - 1
               ## exceed left side of border
               or head[0] < 0
               ## exceed top side of border
               or head[1] > ROWS - 1
               ## exceed bottom side of border
               or head[1] < 0
               ## head hits walls
               or head in set(self.previous_wall_cells)
               ## if len not equal means snake body part overlaps
               or len(set(self.snake)) != len(self.snake)
               ## 0 body parts left
               or len(self.snake) <= 0
          ):
               # hit border/ own body/ or no more body
               self.crashed = True

          elif head == self.food_cell:
               # eat food
               self.old_food_cell = self.food_cell
               self.canvas.delete(self.food_obj)
               self.place_food()
               self.place_wall()
               self.display_snake()

          elif head == self.poison_cell:
               # eat poison
               self.old_poison_cell = self.poison_cell
               self.canvas.delete(self.poison_obj)
               self.place_poison()
               self.display_snake()
          else:
               self.heading = key
               self.display_snake()

     # -------------------------------------------------
     # Input Functions
     # -------------------------------------------------

     # JADEN
     def check_if_key_valid(self, key):
        valid_keys = ["Up", "Down", "Left", "Right"]
        ## check if valid key in dict
        if key in valid_keys and self.forbidden_actions[self.heading] != key:
            return True
        else:
            return False
     
     # JADEN
     def mouse_input(self, event):
          self.play_again()

     # JADEN
     def key_input(self, event):
          if not self.crashed:
               key_pressed = event.keysym

               if self.check_if_key_valid(key_pressed):
                    ## only start game if user is ready and presses valid key
                    self.begin = True
                    ## updates last key only when valid
                    self.last_key = key_pressed


game = MakanTime()
game.mainloop()
