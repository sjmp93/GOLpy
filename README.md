# pyGOL
Implementation of Conway's Game Of Life in Python, using numpy and pygame

pygame and numpy libraries needed, so you have to execute this command (assuming that you have python3 and pip3 installed on your machine):

``
pip3 install pygame numpy
``

If pygame installation fails, then execute this command:
```
sudo apt-get install python3-pygame
```

To execute the game, use this command, where $path will be the directory where conway.py is stored:
```
python3 $path/conway.py
```
Game Instructions:

Left click in a cell to get that cell alive.
Right click in a cell to get that cell die.
Any key from the keyboard to stop the game. Then you coud setup the game state as you wish before resume the game.
The game area has a torus topology, so up and down, and left and right are connected, respectively.

<img src="https://user-images.githubusercontent.com/13170751/80438051-8a837680-8903-11ea-8850-3ccdab1b7458.png" width="75%"></img> 

Thanks to DotCSV for [the tutorial](https://www.youtube.com/watch?v=qPtKv9fSHZY
).
