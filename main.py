from tkinter import *
import random

# -------------------------------------------------
# Global Constants
# -------------------------------------------------

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50

ROWS = int(GAME_HEIGHT/SPACE_SIZE)
COLS = int(GAME_WIDTH/SPACE_SIZE)

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

class MakanTime:
     # -------------------------------------------------
     # Init Functions
     # -------------------------------------------------
     def __init__(self):
          self.window = Tk()
          self.window.title("Makan Time")

          # ## get game dimensions
          # window_width = self.window.winfo_width()
          # window_height = self.window.winfo_height()

          # ## get screen dimension
          # screen_width = self.window.winfo_screenwidth()
          # screen_height = self.window.winfo_screenheight()

          # ## get coordinate of where game screen should be
          # x = int((screen_width/2) - (window_width/2))
          # y = int((screen_height/2) - (window_height/2))

          # ## set game window
          # self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

          self.window.resizable(False, False)

          self.canvas = Canvas(self.window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
          self.canvas.pack()
          
          
          
          ## Binding User Input
          self.window.bind("<Key>", self.key_input)
          self.window.bind("<Button-1>", self.mouse_input)
          self.play_again()
          self.begin = False
     
     def initialize_board(self):
          self.board = []
          self.poison_obj = []
          self.food_obj = []
          self.old_poison_cell = []
          self.old_food_cell = []

          for i in range(ROWS):
               for j in range(COLS):
                    self.board.append((i, j))

          for i in range(ROWS):
               self.canvas.create_line(
                    i * GAME_WIDTH / ROWS, 0, i * GAME_WIDTH / ROWS, GAME_WIDTH,
                    )

          for i in range(COLS):
               self.canvas.create_line(
                    0, i * GAME_HEIGHT / COLS, GAME_HEIGHT, i * GAME_HEIGHT / COLS,
                    )
     
     def initialise_snake(self):
          self.snake = []
          self.crashed = False
          self.heading = "Right"
          self.last_key = self.heading
          self.forbidden_actions = {}
          self.forbidden_actions["Right"] = "Left"
          self.forbidden_actions["Left"] = "Right"
          self.forbidden_actions["Up"] = "Down"
          self.forbidden_actions["Down"] = "Up"
          self.snake_objects = []
          for i in range(BODY_PARTS):
               self.snake.append((i, 0))

     def play_again(self):
          self.canvas.delete("all")
          self.initialize_board()
          self.initialise_snake()
          self.place_food()
          self.place_poison()
          self.display_snake(mode="full")

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

     def place_food(self):
          unoccupied_cells = set(self.board) - set(self.snake) - set(self.old_poison_cell)
          self.food_cell = random.choice(list(unoccupied_cells))
          x = self.food_cell[0] * SPACE_SIZE
          y = self.food_cell[1] * SPACE_SIZE
          self.food_obj = self.canvas.create_oval(
               x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=GREEN_COLOR, outline=DARK_GREEN_COLOR, width=5, tag="food"
          )

     def place_poison(self):
          unoccupied_cells = set(self.board) - set(self.snake) - set(self.old_food_cell)
          self.poison_cell = random.choice(list(unoccupied_cells))
          x = self.poison_cell[0] * SPACE_SIZE
          y = self.poison_cell[1] * SPACE_SIZE
          self.poison_obj = self.canvas.create_rectangle(
               x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=YELLOW_COLOR, outline=ORANGE_COLOR, width=5, tag="poison"
          )

     def display_snake(self, mode=""):
          if self.snake_objects != []:
               self.canvas.delete(self.snake_objects.pop(0))
          if mode == "full":
               for i, cell in enumerate(self.snake):
                    x = cell[0] * SPACE_SIZE
                    y = cell[1] * SPACE_SIZE
                    self.snake_objects.append(
                         self.canvas.create_rectangle(
                              x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, outline=SNAKE_OUTLINE_COLOR, width=5, tag="body"
                         )
                    )
          else:
               cell = self.snake[-1]
               x = cell[0] * SPACE_SIZE
               y = cell[1] * SPACE_SIZE
               self.snake_objects.append(
                         self.canvas.create_rectangle(
                              x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, outline=SNAKE_OUTLINE_COLOR, width=5, tag="head"
                         )
                    )
               if self.snake[0] == self.old_food_cell:
                    self.snake.insert(0, self.old_food_cell)
                    self.old_food_cell = []
                    tail = self.snake[0]
                    x = tail[0] * SPACE_SIZE
                    y = tail[1] * SPACE_SIZE
                    self.snake_objects.append(
                         self.canvas.create_rectangle(
                              x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, outline=SNAKE_OUTLINE_COLOR, width=5, tag="head"
                         )
                    )
               elif self.snake[0] == self.old_poison_cell:
                    self.canvas.delete(self.snake_objects.pop(0))

               self.window.update()

     # -------------------------------------------------
     # Game Logic Functions
     # -------------------------------------------------
     
     def update_snake(self, key):
          tail = self.snake[0]
          head = self.snake[-1]
          if tail != self.old_food_cell:
               self.snake.pop(0)
          if tail == self.old_poison_cell:
               if len(self.snake) == 0:
                    self.crashed = True
               else: self.snake.pop(0)
               
          if key == "Left":
               self.snake.append((head[0] - 1, head[1]))
          elif key == "Right":
               self.snake.append((head[0] + 1, head[1]))
          elif key == "Up":
               self.snake.append((head[0], head[1] - 1))
          elif key == "Down":
               self.snake.append((head[0], head[1] + 1))

          head = self.snake[-1]
          if (
               head[0] > COLS - 1
               or head[0] < 0
               or head[1] > ROWS - 1
               or head[1] < 0
               or len(set(self.snake)) != len(self.snake)
               or len(self.snake) < 0
          ):
               # hit border/ own body/ or no more body
               self.crashed = True
          elif self.food_cell == head:
               # eat food
               self.old_food_cell = self.food_cell
               self.canvas.delete(self.food_obj)
               self.place_food()
               self.display_snake()
          elif self.poison_cell == head:
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

     def check_if_key_valid(self, key):
        valid_keys = ["Up", "Down", "Left", "Right"]
        if key in valid_keys and self.forbidden_actions[self.heading] != key:
            return True
        else:
            return False
     
     def mouse_input(self, event):
          self.play_again()

     def key_input(self, event):
          if not self.crashed:
               key_pressed = event.keysym

               # Check if the pressed key is a valid key
               if self.check_if_key_valid(key_pressed):
                    # print(key_pressed)
                    self.begin = True
                    self.last_key = key_pressed


main_instance = MakanTime()
main_instance.mainloop()
