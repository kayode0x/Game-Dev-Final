# CSCI-43700: 3D Game Graphics Final

PS: This is a continuation of my previous assignment on Game Engine.

### What's new?

## Game Design Document:
The player controls a car and tries to keep it from running into balls that move across the screen. The car, balls, a life bar, and a progress bar make up the main scene. The arrow keys are used to control the car, which can move in any of four directions. The balls move across the screen from left to right at different speeds. The car's health goes down by 5% when it hits a ball, as shown by the health bar. The progress bar shows how far the car has moved across the screen. When the progress bar fills up to 100%, the level goes up, the progress bar starts over, and the balls move faster. The game stops when the car's health drops to 0% or when the player moves on to level 4.

## Software Engineering Plan:
The development team is divided into three main roles: Game Designers, who focus on the game's mechanics and user experience; Programmers, who write and manage the game's code; and Testers, who make sure the game works as expected and help find bugs. The project schedule had several important points: Initial idea and design, coding of basic game play, testing and bug fixing, coding of extra features, and final testing and release.

## State Transition Diagram:
This would have to be shown with a picture, but in words: The game starts in the "Start" state. When the person starts the game, it moves to the "Play" state. In the "Play" state, it can change to either "Game Over" if the player's health drops to 0 or "Level Up" if the progress bar fills up and the player's level is lower than 3. The 'Level Up' state goes back to the 'Play' state right away, but the game gets harder. When the player's life reaches 0 or after level 3, the game stays in the "Game Over" state.

## User Instructions: 
Make sure Python and Pygame are installed on your machine before you run the game. The game needs at least Python 3.8 and at least Pygame 2.0.0. Use the arrow keys on your computer to move the car around. To keep your health, you need to stay away from the moving balls. The progress bar at the bottom of the screen shows how far you've come. The game is over when your health goes down to 0% or when you finish all three levels.

NB: Here's the old documentation.

## Game Overview:
This simple 2D game is based on the idea of "drive a car, hit a ball." You control a car sprite that you move around the screen and hit balls with. Players experience basic game dynamics through simple movement and collision detection.

## Technology Choices:
The game utilizes Python, a versatile, high-level programming language, along with Pygame, a widely-used set of Python modules designed specifically for video game creation. This combination provides ease of development and the capability to handle sprite management, collision detection, boundary detection, and rendering.

## How to Play:
The player controls the car sprite with the arrow keys. The goal is to connect with the ball sprites. Every time the car hits a ball, a message appears on the screen. This could be used to keep track of points or other game elements.

## Installation and Gameplay Instructions:
Python and Pygame must be on the machine for the game to work. Then, the code for the game and the pictures of the car and ball need to be saved in a.py file. If you run this file in a system that can handle Python, the game will start. Use the arrow keys to move around.

## Lessons Learned:
The process of making this game taught me about the basic parts of game creation, such as game loops, sprite management, collision detection, and boundary detection. It showed how important these things are for making a game that is easy to play and responds well. It also showed how these basic ideas are used to make more complicated games.
