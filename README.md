# Makan-Time

This repository contains the code for the python implmentation the Makan Time game. This game was created for the 1D component of the Computational Thinking for Design course at the Singapore University of Technology and Design.

## About Makan-Time:
This game is a spin off from the traditional Snake-And-Apple game aimed at encouraging young children to eat their vegetables while discouraging them from snacking on unhealthy food.

The game begins with a snake that grows in length when eating vegetables (green circles) while losing length when eating potato chips (yellow blocks). 

The game ends when either the snake hits the borders of the game, eats itself, or has its length be reduced to zero.

Additionally, just like how it becomes increasingly harder to maintain a healthy diet, the game also becomes harder as the snake consumes more vegetables. Walls will be spawned everytime the snake eats a vegetable and it will be game over once the snake collides with a wall.

Children in particular love to play games, thus inculcating good eating habits via game is an effective way to do so. Furthermore, young children in particular are especially impressionable, thus making it easier to sow the idea of eating one's veggies to grow big and strong.

This game is also suitable for people of any age group as it can be an enjoyable way to train their reflexes.

## Installing Makan-Time:

```
git clone https://github.com/raynard/cdt-1d.git
```

## Running Makan-Time:
```
cd cdt-1d
python main.py
```

<p align="center">
<img src="/src/preview.gif">
</p>

## Controls

1. The game begins with a snake of length 3 and will only start when the user presses a valid key.
2. Keyboard Up, Down, Left, and Right are used to control the snake.
3. The result of the game is displayed at the end of the game.
4. Click anywhere on the result screen to play again.

## Documentation

This game utilises the random library and tkinter library.

The game is build on a single class named `MakanTime()` with all the game functions kept within the class.

The functions within the game are split into 4 categories.
1. Initialisation Functions
2. Display Functions
3. Logic Function
4. Input Functions

---
---

### Initialisation Functions

`def __init__()`

description

---

`def initialise_board()`

description

---

`def initialise_snake()`

description

---

`def play_again()`

description

---

`def mainloop()`

description

---
---

### Display Functions

`def display_gameover()`

description

---

`def place_food()`

description

---

`def place_poison()`

description

---

`def place_wall()`

This function displays a wall randomly on the canvas as the game progresses. The function takes into account the list of unoccupied cells and randomly chooses one of the cells to spawn the wall. The location of the new wall spawned will then be removed from the list of unoccupied cells.

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
---

### Logic Function

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
---

### Input Functions

`def check_if_key_valid()`

This function ensures that the snake will change to move in a possible direction (either perpendicularly left or right from its current heading direction), when the correct button is pressed to change the direction of the snake.

A list of valid keys is created to check against when the player presses a key on the keyboard. If the player presses a key that is an element of the list valid_keys, and that it is also not a forbidden_action, the snake will turn in that keyed in direction. If not the snake will continue its direction of motion.

---

`def mouse_input()`

When the player clicks the left-mouse button, the game will restart from the beginning, via calling the function play_again() which deletes the current game canvas and reinitialize a new game canvas with the snake, food and poison.

---

`def key_input()`

This function gives the player the ability to move the snake around. To start the game, the user must press either the down or right arrow key. Up key is not possible as it is a forbidden action our code has took into account to ensure the snake would not immediately eat itself. The left arrow key is not advised to be pressed to start the game as it will cause the snake to crash into the wall, thus ending the game.



---


## Members
Chai Yu Cheng, Raynard (1003436)

Chong Wen Xuan Darryl (1005890)

Lim Ho Tong Malcom (1005953)

Jaden Tay Jingyan (1005992)

Haritha Shraeya Rajasekar (1006278)

## Credits

Our team referenced code from the following [youtube tutorial](https://www.youtube.com/watch?v=bfRwxS5d0SI) to understand more about how the game logic should work.

We also referenced code from the following [repository](https://github.com/aqeelanwar/Snake-And-Apple.git).

Based on the structure of his code, we came up with pseudocodes for our own functions and wrote our own code.




