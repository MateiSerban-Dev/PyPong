# PyPong
Just a normal Pong game made in PyGame, nothing out of the ordinary...

# Instalation
To play the game , you can simply just go to the itch.io page and download : 

https://mateideveloper.itch.io/pypong

Or, you can make an executable using pyinstaller.

First install PyGame:
```bash
pip install pygame
```
Now install pyinstaller:
```bash
pip install pyinstaller
```
Then cd in the directory of where the game source code is saved and run : 
```bash
pyinstaller --clean --onefile --windowed --icon=icon.ico main.py
```
