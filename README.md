# Snake Game

Welcome to the Snake Game! This classic arcade-style game is implemented in Python using the Turtle library. The game offers hours of fun as you navigate a snake around the screen, collecting food to grow longer while avoiding collisions with the walls and yourself.

## Game Components

The Snake Game consists of several modules, each responsible for different aspects of the game:

- `main.py`: The main driver for the game. It sets up the game window, initializes game components, and manages the game loop.

- `scoreboard.py`: Manages and displays the player's score and highest score during gameplay. It also saves the highest score to the 'gamedata.txt' file.

- `snake.py`: Defines the behavior and control of the snake as it moves around the game area, grows, and detects collisions.

- `border.py`: Draws the boundary around the game area, preventing the snake from moving outside.

- `food.py`: Manages the creation and positioning of food items that the snake needs to consume to grow.

- `gamedata.txt`: A text file that stores the highest score achieved in the game.

## How to Play

1. Run `main.py` to start the game.

2. Control the snake's direction using the arrow keys (Up, Down, Left, Right).

3. The snake will continuously move in the direction it's facing.

4. Your goal is to collect as much food as possible without colliding with the walls or the snake's own body.

5. Each time you eat food, the snake grows longer, and your score increases.

6. The game ends when the snake collides with the walls or itself.

7. Your highest score is saved in 'gamedata.txt' and displayed during the game.

## Requirements

- Python 3.x
- Turtle graphics library (usually included with Python)

## Installation

1. Clone the repository to your local machine.

2. Run `main.py` to start the game.

Enjoy the game and have fun collecting those tasty dots!
