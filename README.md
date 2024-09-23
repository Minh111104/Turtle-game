# Turtle-crossing-game 🐢 

This is a Python-based game inspired by the classic arcade game "Frogger". The player controls a turtle that needs to cross the road and avoid oncoming cars. The objective is to reach the top of the screen without colliding with any cars. As the player progresses, the game increases in difficulty by speeding up the cars.

**Features**

- **Player Movement**: The player (turtle) moves upward by pressing the "Up" arrow key.
- **Cars**: Cars move horizontally across the screen. As the game progresses, the speed of the cars increases.
- **Scoring**: The player earns points by successfully crossing the screen. The current level is displayed at the top of the screen.
- **Game Over**: If the turtle collides with a car, the game ends, and a "Game Over" message is displayed.

**Files**

- _'player.py'_: Handles player movement and logic.
- _'car_manager.py'_: Manages car creation, movement, and level progression.
- _'scoreboard.py'_: Displays the current level and shows the "Game Over" message.

**Game Mechanics**

- **Player Movement**: The player can only move up by pressing the "Up" arrow key. Reaching the top of the screen advances the player to the next level.
- **Car Movement**: Cars are generated randomly on the screen and move from right to left. With each level, the cars' speed increases.
- **Collision Detection**: If the turtle gets too close to a car (within 20 units), the game ends.
- **Level Progression**: Successfully reaching the top of the screen resets the turtle's position and increases the game difficulty by speeding up the cars. The level counter also increases.
