# <h1 p align = "center"> **Makan-Time**

This repository contains the code for the python implmentation for Makan-Time. This game was created for the 1D component of the Computational Thinking for Design course at the Singapore University of Technology and Design.

## <ins>_**About Makan-Time**_</ins>
This game is a spin off from the traditional Snake-And-Apple game aimed at encouraging young children to eat their vegetables while discouraging them from snacking on unhealthy foods.

The game begins with a snake that grows in length when eating vegetables (green circles) while losing length when eating potato chips (yellow blocks). 

The game ends when either the snake hits the borders of the game, eats itself, or has its length be reduced to zero.

Additionally, just like how it becomes increasingly harder to maintain a healthy diet, the game also becomes harder as the snake consumes more vegetables. Walls will be spawned randomly everytime the snake eats a vegetable and it will be game over once the snake collides with a wall.

Children in particular love to play games so inculcating good eating habits through video games can be an effective way to do so. Furthermore, young children in particular are especially impressionable, thus making it easier to inculcate the habit of eating one's veggies to grow big and strong.

This game is also suitable for people of any age group as it can be an enjoyable way to train their reflexes.

## <ins>_**Installing Makan-Time**_</ins>

```
git clone https://github.com/raynard/cdt-1d.git
```

## <ins>_**Running Makan-Time**_</ins>
---
```
cd cdt-1d
python main.py
```

<p align="center">
<img src="/src/preview.gif">
</p>

## <ins>_**Controls**_</ins>

1. The game begins with a snake of length 3 and will only start when the user presses a valid key (all the arrow keys.)
2. Keyboard Up, Down, Left, and Right are used to control the snake.
3. The final result is displayed at the end of the game.
4. Click anywhere on the result screen to play again.

## <ins>_**Documentation**_<ins>

This game utilises the "random" and "tkinter" library.

The game is build on a single class named `MakanTime()` with all the game functions kept within the class.

The functions within the game are split into 4 categories.
1. Initialisation Functions
2. Display Functions
3. Logic Function
4. Input Functions

---

### **Initialisation Functions**

---

`def __init__()`

This method serves as the constructor of the game.

Firstly, we would create a `self.window` as the tkinter object, and we give it a title `"Makan-Time"` and make sure it remains at its original size. 

After that, we would create a canvas using the `Canvas()` method, giving it colour and constructing its size based on the game height and width defined in the global constants. We then pack it as a whole using `.pack()`, making sure to specify its geometry before running the game. 

We then bind the player's key and mouse input to `self.window`, and set the game to its original state first; running the game for the first time using the `play_again()` function, and also making sure that it starts only when the player is ready by setting `self.begin` as False.

---

`def initialise_board()`

This function creates the board for the game to be played.

We firstly initialize the board `self.board` to be an empty list.

We then initialize the display and coordinates of the 3 main objects: `food`, `poison` and `wall`, as also empty lists to be used later during the game.

We then proceeded to create the coordinates and grids of the board, using `.append()` and `.create_line()` methods and the game height, game width, the rows and columns of the grid.

---

`def initialise_snake()`

This function serves to create a snake object for the game

To start of, the function sets `self.snake` into an empty list

The snake's initial conditions will be set as follows:

1. The snake will first not collide with anything
2. The snake will be facing downwards
3. The snake will move based on the last pressed key

Next, the function will also check the validity of the movement of the snake, by creating an empty dictionary `self.forbidden_actions`, while setting the invalid actions beforehand.

Then, we create an empty list for the coordinates of the snake to be used later, and append `self.snake` with the number of body parts.

---

`def play_again()`

This function initializes a new board and snake using `initialize_board()` and `initialize_snake()` function. 

Food and poison gets placed on the board randomly using `place_food()` and `place_poison()` function. 

The initial state of the snake is displayed on the board using the `display_snake()` function.

---

`def mainloop()`

This function ensures that the game goes on as long as the snake doesnt collide with itself or the walls. When a collision occurs, game over is displayed using the `display_gameover()` function.

---

### **Display Functions**

---

`def display_gameover()`

The game over screen is designed using `create_text()`, with font, fill, and text parameters under this function.

---

`def place_food()`

This function does the following:

1. Create a list of unoccupied spaces in the grid by removing coordinates of the snake, poison and walls.

2. Chose a random index in the list of unoccupied spaces and assign it to the food cell.

3. Extract the X and Y coordinate from the randomized index from the unoccupied spaces list.

4. Create an oval shape using canvas with green colour to represent the vegetables in the game with a dark green outline at the X and Y coordinate.

---

`def place_poison()`

This function does the following

1. Create a list of unoccupied spaces in the grid by removing coordinates of the snake, food and walls.

2. Chose a random index in the list of unoccupied spaces and assign it to the poison cell.

3. Extract the X and Y coordinate from the randomized index from the unoccupied spaces list.

4. Create an rectangle shape using canvas with yellow colour to represent the potato chips in the game with a orange outline at the X and Y coordinate.

---

`def place_wall()`

This function displays a wall randomly on the canvas everytime the snake consumes the food. 

The function takes into account the list of unoccupied cells `unoccupied_cells` and randomly chooses one of the cells to spawn the wall. 

The location of the new wall spawned will then be removed from the list of unoccupied cells.

---

`def display_snake()`

This function displays the snake on the canvas based on different situations.
1. Initilisation
2. Eat Food
3. Eat Poison
4. None of the above

For 1, the function generates squares to the snake object based on the length of the initial snake list.

For 2, the function will insert a new item at the tail of the snake list as well as generate a new square for the snake object.

For 3, The function will delete the tail from the snake object.

For 4, the function will remove the tail and add a new head in the direction of movement of the snake. This is to ensure that the snake does not keep growing if it is not eating anything.

---

### **Logic Function**

---

`def update_snake()` 

This function is the main logic for the game that is run at every step/frame of the game. The function takes a variable `key` from the user input and this decides the direction the snake will travel at the next step.

Within the function, there are also checks for the different situations the snake may encounter which are:
1. Eating food
2. Eating poison
3. Hitting a wall
4. Hitting the border
5. Eating itself
6. None of the above

For 1, the food object will be deleted and a new one will be spawned along with a new wall while the snake grows in length.

For 2, the poison object will be deleted and a new one will be spawned while the snake is reduced in length. If the length of the snake is = 0, it will be game over.

For 3, 4 and 5, it results in game over.

For 6, the snake will just continue to the next step/frame.

---

### **Input Functions**

---

`def check_if_key_valid()`

This function ensures that the snake will move in a possible direction (either perpendicularly left or right from its current heading direction), when the correct button is pressed to change the direction of the snake.

A list of valid keys is created to check against when the player presses a key on the keyboard. If the player presses a key that is an element of the list `valid_keys`, and that it is also not a `forbidden_action`, the snake will turn in that keyed in direction. If not the snake will continue its direction of motion.

---

`def mouse_input()`

When the player clicks the left-mouse button, the game will reinitialise itself by calling the function `play_again()` which clears the current game canvas and with a new game canvas, snake, food and poison.

---

`def key_input()`

This function gives the player the ability to move the snake around. To start the game, the user must press either the down or right arrow key. Up key is not possible as it is a forbidden action our code has took into account to ensure the snake would not immediately eat itself. The left arrow key is not advised to be pressed to start the game as it will cause the snake to crash into the wall, thus ending the game. The player will be able to move the snake as long as it has not crashed into anything.

`event.keysym` converts the button pressed by the user into a string, which is then passed into `check_if_key_valid`.

Tkinter keysym recognition: 

```
https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.html
```

The function `check_if_key_valid` ensures the snake only begins moving when the correct key is pressed (right, left, down), when `check_if_key_valid` returns True, it causes the snake to turn in the specified direction via assigning `last_key` to the new direction, hence turning the snake to head in that direction.

---


## <ins>**Members**</ins>
Chai Yu Cheng, Raynard (1003436)

Chong Wen Xuan Darryl (1005890)

Lim Ho Tong Malcom (1005953)

Jaden Tay Jingyan (1005992)

Haritha Shraeya Rajasekar (1006278)

## <ins>**Credits**</ins>

Our team referenced code from the following [youtube tutorial](https://www.youtube.com/watch?v=bfRwxS5d0SI) to understand more about how the game logic should work.

We also referenced code from the following [repository](https://github.com/aqeelanwar/Snake-And-Apple.git).

Based on the structure of his code, we came up with pseudocodes for our own functions and wrote our own code.




