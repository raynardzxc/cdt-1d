# Makan-Time

This repository contains the code for the python implmentation the Makan Time game. This game was created for the 1D compoenent of the Computational Thinking for Design course at the Singapore University of Technology and Design.

## About Makan-Time:
This game is a spin off from the traditional Snake-And-Apple game aimed at encouraging young children to eat their vegetables while discouraging them from snacking on unhealthy food.

The game begins with a snake that grows in length when eating vegetables (green circles) while losing length when eating potato chips (yellow blocks). 

The game ends when either the snake hits the borders of the game, eats itself or has its length be reduced to zero.

Additionally, just like how it becomes increasingly harder to maintain a healthy diet, the game also becomes harder as the snake consumes more vegetables. Walls will be spawned everytime the snake eats a vegetable and it will be game over once the snake collides with a wall.

This game is suitable for all ages as people from older age groups can enjoy it as well should they want to train their reflexes.

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


## Members
Chai Yu Cheng, Raynard (1003436)

Chong Wen Xuan Darryl (1005890)

Lim Ho Tong Malcom (1005953)

Jaden Tay Jingyan (1005992)

Haritha Shraeya Rajasekar (1006278)

## Credits

Our team referenced code from the following youtube tutorial to understand more about how the game logic should work: https://www.youtube.com/watch?v=bfRwxS5d0SI

We also referenced code from the following repository: https://github.com/aqeelanwar/Snake-And-Apple.git.

Based on the structure of his code, we came up with pseudocodes for our own functions and wrote our own code.




