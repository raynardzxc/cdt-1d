from tkinter import *
import random

# -------------------------------------------------
# Global Constants
# -------------------------------------------------

## Setting the size of the board

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50

## Getting rows and columns from the board size for objects (eg. snake)

ROWS = int(GAME_HEIGHT/SPACE_SIZE)
COLS = int(GAME_WIDTH/SPACE_SIZE)

## Initializing the characteristics of the game

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
    def __init__(self):        ## Create window settings
          
        ## Tkinter object from library
        self.window = Tk()
          
        ## Title of window
        self.window.title("Makan-Time")
          
        ## Fix the window so the size does not change
        self.window.resizable(False, False)

        ## Instantiate the canvas and packing it
        self.canvas = Canvas(self.window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.canvas.pack()
          
        ## Binding user key and mouse input
        self.window.bind("<Key>", self.key_input)
        self.window.bind("<Button-1>", self.mouse_input)
          
        ## function to reset the game
        self.play_again()
          
        ## Start the game only when the user has input a key
        self.begin = False
     
    # DARRYL
    def initialize_board(self):        ## Creating the board for the game
         
        ## Instantiating an empty board as an empty list
        self.board = []

        ## Object list used to generate display
        self.poison_obj = []
        self.food_obj = []
        self.wall_obj = []

        ## Cell list used to identify coordinate of object
        self.old_poison_cell = []
        self.old_food_cell = []
        self.previous_wall_cells = []

        ## Create board based on rows and columns stated previously
        for i in range(ROWS):
            for j in range(COLS):
                self.board.append((i, j))

        ## Drawing lines to create grids for both rows and columns
        for i in range(ROWS):
            self.canvas.create_line(
                i * GAME_WIDTH / ROWS, 
                0, 
                i * GAME_WIDTH / ROWS, 
                GAME_WIDTH,
                )
        for i in range(COLS):
            self.canvas.create_line(
                0, 
                i * GAME_HEIGHT / COLS,
                GAME_HEIGHT, 
                i * GAME_HEIGHT / COLS,
                )
     
    # DARRYL
    def initialise_snake(self):        ## Creating the snake object
        
        ## Initializing the snake as an empty list for its coordinates on the board
        self.snake = []
        
        ## Making the initial conditions of the snake
        self.crashed = False
        self.heading = "Down"
        self.last_key = self.heading

        ## Creating dictionary of forbidden actions
        ##  to prevent snake from eating itself
        self.forbidden_actions = {}
        self.forbidden_actions["Up"] = "Down"
        self.forbidden_actions["Down"] = "Up"
        self.forbidden_actions["Right"] = "Left"
        self.forbidden_actions["Left"] = "Right"
        
        ## Creating list for the display of the snake on the canvas
        self.snake_objects = []
        
        ## Creating the snake with its body parts
        for i in range(BODY_PARTS):
            self.snake.append((0, i))

    # HARITHA
    def play_again(self):       ## Prompt the player to play again
        
        ## Resets the board by deleting the canvas
        self.canvas.delete("all")
        
        ## Creates another new board
        self.initialize_board()
        
        ## Creates another new snake
        self.initialise_snake()
        
        ## Randomizes the places of the food and poison for the new board
        self.place_food()
        self.place_poison()
        
        ## Displaying the initial state of the snake on the new board
        self.display_snake(mode="init")

    # HARITHA
    def mainloop(self):         ## Main game
        
        ## Let the game run when it starts by starting a while loop
        while True:
            
            ## Continue to update the board while the game is running
            self.window.update()
            
            ## Player prompts the game to start
            if self.begin:
                
                ## If the snake doesn't collide with anything, the snake continues to update on the board
                if not self.crashed:
                    self.window.after(SPEED, self.update_snake(self.last_key))
                
                ## Else, the game forcefully stops, and the screen will show "game over"
                else:
                    self.begin = False
                    self.display_gameover()
     
    # -------------------------------------------------
    # Display Functions
    # -------------------------------------------------
     
    # HARITHA
    def display_gameover(self):         ## Game Over Screen
        
        ## Deducing the final score of the game, and creating the text to show the final score
        score = len(self.snake)
        score_text = "Score:\n"
        
        ## Resetting the canvas to display the final score, and to prompt the player to play again
        self.canvas.delete("all")
        
        ## Creation of the final score label
        self.canvas.create_text(
            GAME_WIDTH/2,
            3*GAME_HEIGHT/8,
            font="consolas 40 bold",
            fill = TEXT_COLOR,
            text = score_text,
            )
        
        ## Creation of the final score value
        score_value = str(score)
        self.canvas.create_text(
            GAME_WIDTH/2,
            1*GAME_HEIGHT/2,
            font="consolas 50 bold",
            fill = TEXT_COLOR,
            text = score_value,
            )
        
        ## Creation of the prompt to ask the player to play again
        play_text = "Click to play again \n"
        self.canvas.create_text(
            GAME_WIDTH/2,
            15*GAME_HEIGHT/16,
            font="consolas 20 bold",
            fill = "gray",
            text = play_text,
            )

    # MALCOM
    def place_food(self):       ## Placements of the food throughout the game
        
        ## Checking the "occupancy" of the grid so the food will not spawn on the same tile as the other objects
        unoccupied_cells = set(self.board) - set(self.snake) - set(self.old_food_cell) - set(self.old_poison_cell) - set(self.previous_wall_cells)
        
        ## Randomize the spawn of the food object
        self.food_cell = random.choice(list(unoccupied_cells))
        
        ## Creating the shape of the food, and making sure it fits the grid of the board
        x = self.food_cell[0] * SPACE_SIZE
        y = self.food_cell[1] * SPACE_SIZE
        self.food_obj = self.canvas.create_oval(
            x, 
            y, 
            x+SPACE_SIZE, 
            y+SPACE_SIZE, 
            fill=GREEN_COLOR, 
            outline=DARK_GREEN_COLOR, 
            width=5, 
            tag="food"
            )

    # MALCOM
    def place_poison(self):
        
        ## Checking the "occupancy" of the grid so the poison will not spawn on the same tile as the other objects
        unoccupied_cells = set(self.board) - set(self.snake) - set(self.old_food_cell) - set(self.old_poison_cell) - set(self.previous_wall_cells)
        
        ## Randomize the spawn of the poison object
        self.poison_cell = random.choice(list(unoccupied_cells))
        
        ## Creating the shape of the poison, and making sure it fits the grid of the board
        x = self.poison_cell[0] * SPACE_SIZE
        y = self.poison_cell[1] * SPACE_SIZE
        self.poison_obj = self.canvas.create_rectangle(
            x, 
            y, 
            x+SPACE_SIZE, 
            y+SPACE_SIZE, 
            fill=YELLOW_COLOR, 
            outline=ORANGE_COLOR, 
            width=5, 
            tag="poison"
            )

    # JADEN
    def place_wall(self):
        
        ## Checking the "occupancy" of the grid so the wall will not spawn on the same tile as the other objects
        unoccupied_cells = set(self.board) - set(self.snake) - set(self.old_food_cell) - set(self.old_poison_cell) - set(self.previous_wall_cells)
        
        ## Ramdomize the spawn of the wall object
        self.wall_cell = random.choice(list(unoccupied_cells))
        
        ## Creating the shape of the wall, and making sure it fits the grid of the board
        x = self.wall_cell[0] * SPACE_SIZE
        y = self.wall_cell[1] * SPACE_SIZE
        self.wall_obj = self.canvas.create_rectangle(
            x, 
            y, 
            x+SPACE_SIZE, 
            y+SPACE_SIZE, 
            fill=BLACK_COLOR, 
            outline=BLACK_COLOR, 
            width=5, 
            tag="wall"
            )
        
        ## Making the walls stay on the board without disappearing
        self.previous_wall_cells.append(self.wall_cell)
     
    # RAYNARD
    def display_snake(self, mode=""):
        
        ## Using the .pop() function to make the snake "move" without extending on the board
        if self.snake_objects != []:
            self.canvas.delete(self.snake_objects.pop(0))

        ## Creating the initial state of the snake
        ## If the snake is at its initial state, create the snake at the top-right corner of the board
        if mode == "init":
            
            for i, cell in enumerate(self.snake):
                x = cell[0] * SPACE_SIZE
                y = cell[1] * SPACE_SIZE
                self.snake_objects.append(
                    self.canvas.create_rectangle(
                        x, 
                        y, 
                        x+SPACE_SIZE, 
                        y+SPACE_SIZE, 
                        fill=SNAKE_COLOR, 
                        outline=SNAKE_OUTLINE_COLOR, 
                        width=5, 
                        tag="body"
                        )
                    )
        
        ## Else, the snake will "move" by appending a "new head" in front of the snake body
        else:
            
            ## Creation of the new head
            head = self.snake[-1]
            x = head[0] * SPACE_SIZE
            y = head[1] * SPACE_SIZE

            ## Appending the new head to the snake
            self.snake_objects.append(
                self.canvas.create_rectangle(
                    x, 
                    y, 
                    x+SPACE_SIZE, 
                    y+SPACE_SIZE, 
                    fill=SNAKE_COLOR, 
                    outline=SNAKE_OUTLINE_COLOR, 
                    width=5, 
                    tag="head"
                    )
                )
            
            ## If the cell occupied by the snake is also occupied by the food, add the body size of the snake
            if head == self.old_food_cell:
                
                ## Appending the new tail when the snake has "eaten" the food
                self.snake.insert(0, self.old_food_cell)
                self.old_food_cell = []
                tail = self.snake[0]
                x = tail[0] * SPACE_SIZE
                y = tail[1] * SPACE_SIZE
                self.snake_objects.append(
                    self.canvas.create_rectangle(
                        x, 
                        y, 
                        x+SPACE_SIZE, 
                        y+SPACE_SIZE, 
                        fill=SNAKE_COLOR, 
                        outline=SNAKE_OUTLINE_COLOR, 
                        width=5, 
                        tag="new tail"
                        )
                    )
                
            ## If the cell occupied by the snake is also occupied by the poison, reduce the body size of the snake
            elif head == self.old_poison_cell:
                
                ## Deleting the tail using the .pop() function
                self.canvas.delete(self.snake_objects.pop(0))
        
        ## Keep updating the snake as the snake "moves"
        self.window.update()

    # -------------------------------------------------
    # Game Logic Function
    # -------------------------------------------------
    
    # RAYNARD
    def update_snake(self, key):

        tail = self.snake[0]
        head = self.snake[-1]

        ## Preventing the snake from growing without eating food
        if head != self.old_food_cell:
            self.snake.pop(0)

        ## Reducing the length of the snake if it eats poison
        if head == self.old_poison_cell:
            
            ## If the length of the snake is 0, then the game is lost
            if len(self.snake) == 0: 
                self.crashed = True
                
            ## Else, the length of the snake will be reduced by 1
            else: 
                self.snake.pop(0)
          
        ## Appending the head depending on the direction the snake is heading
        if key == "Up":
            self.snake.append((head[0], head[1] - 1))
        elif key == "Down":
            self.snake.append((head[0], head[1] + 1))
        elif key == "Left":
            self.snake.append((head[0] - 1, head[1]))
        elif key == "Right":
            self.snake.append((head[0] + 1, head[1]))
        
        head = self.snake[-1]
        
        ## If the snake exceeds the board or collides with itself, the game is also lost
        if (
            ## Right side of border
            head[0] > COLS - 1
            
            ## Left side of border
            or head[0] < 0
            
            ## Top side of border
            or head[1] > ROWS - 1
            
            ## Bottom side of border
            or head[1] < 0
            
            ## Head of snake hits the walls
            or head in set(self.previous_wall_cells)
            
            ## If the snake body overlaps with itself
            or len(set(self.snake)) != len(self.snake)
            
            ## 0 Body Parts
            or len(self.snake) <= 0
          ):
            self.crashed = True
        
        ## Process of eating food
        elif head == self.food_cell:
            
            ## Snake in the midst of eating food
            self.old_food_cell = self.food_cell
            
            ## Removing the food object from the board
            self.canvas.delete(self.food_obj)
            self.place_food()

            if random.choice([0,1])==1:
                    self.place_wall()
            else:
                pass

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
        if (
                key in valid_keys 
                and self.forbidden_actions[self.heading] != key
            ):
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
            # print(key_pressed)

            if self.check_if_key_valid(key_pressed):
                
                ## only start game if user is ready and presses valid key
                self.begin = True
                ## updates last key only when valid
                self.last_key = key_pressed


game = MakanTime()
game.mainloop()
