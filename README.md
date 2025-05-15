# 🏓 Python Pong Game

A classic Pong arcade game implementation using Python's Turtle graphics module.

![Pong Game](https://img.shields.io/badge/Game-Pong-brightgreen)
![Python](https://img.shields.io/badge/Language-Python-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📝 Description

This project is a recreation of the classic Pong arcade game using Python's Turtle graphics library. In this two-player game, each player controls a paddle to hit a ball back and forth. If a player misses the ball, the opponent scores a point. The ball gradually speeds up after each successful hit, making the game progressively more challenging.

## ✨ Features

- Two-player gameplay
- Automatic ball movement with increasing speed
- Score tracking
- Collision detection
- Responsive paddle controls

## 🕹️ Controls

- **Right Paddle**:
  - Move Up: Up Arrow
  - Move Down: Down Arrow

- **Left Paddle**:
  - Move Up: 'W' key
  - Move Down: 'S' key

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pong-game.git
cd pong-game
```

2. Make sure you have Python installed. This game was developed using Python 3.

3. No additional dependencies are required as the game uses the built-in Turtle graphics library.

## 🎮 How to Play

Run the main script:
```bash
python main.py
```

- The game will start immediately with the ball moving from the center
- Each player controls their paddle to hit the ball
- If a player misses the ball, the opponent scores a point
- The ball speed increases after each successful hit
- After scoring, the ball resets to the center with the default speed

## 🏗️ Project Structure

- `main.py`: Main game script that initializes the screen, paddles, ball, and scoreboard and runs the game loop
- `paddle.py`: Contains the `Paddle` class that handles paddle creation and movement
- `ball.py`: Contains the `Ball` class that handles ball movement and collision behavior
- `scoreboard.py`: Contains the `Scoreboard` class that tracks and displays the score

## 📋 Development Process

The game was developed following these steps:

1. ✅ Create game screen
2. ✅ Create and implement movement for the first paddle
3. ✅ Create the second paddle
4. ✅ Create the ball and implement its movement
5. ✅ Detect collision with walls and implement bouncing
6. ✅ Detect collision with paddles
7. ✅ Detect when a paddle misses the ball
8. ✅ Implement score tracking

## 🐛 Known Issues

- There is a lag before paddle movement responds to key presses
- Players cannot move both paddles simultaneously (limitation of the Turtle module)

## 🔜 Future Improvements

- Fix input lag with paddle controls
- Implement space bar to start ball movement
- Add a start screen
- Add game over condition and restart option
- Add sound effects
- Implement AI opponent option for single-player mode

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👏 Acknowledgements

- Inspired by the classic Pong arcade game created by Atari in 1972
- Built using Python's Turtle graphics library
