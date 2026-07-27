# Fluttering Bird
Flappy bird knockoff implementation in Pygame(-ce).

# Demo
[Demo.mp4](https://github.com/user-attachments/assets/385a26eb-f9df-4c82-a555-7fd2beb04659)

# Features
- Score counter counts amount of columns passed
- Pixel-perfect collision detection between player and columns
- Custom pixel art made by me
- Title and game over screens

# Installation
## Releases (LINUX ONLY)
Head over to [the releases page](https://github.com/nautrw/fluttering-bird/releases/latest) and download the attached file for Linux. Run the file and the game should start.
## Building From Scratch
**Minimum Python Version Required: Python 3.9**
1. Clone the GitHub repository onto your system
1. Open a shell inside the folder of the cloned repository
3. Copy and run the following commands:
- On Linux:

```shell
python -m venv .venv
.venv/scripts/activate
python -m pip install pyinstaller -r requirements.txt
pyinstaller --onefile --windowed --add-data "assets/*:assets" --exclude-module numpy --exclude-module pandas --exclude-module scipy --exclude-module matplotlib --name="Fluttering Bird" run.py
```

- On Windows (Powershell):
```powershell
pip install pyinstaller -r requirements.txt
pyinstaller --onefile --windowed --add-data "assets\*;assets" --exclude-module numpy --exclude-module pandas --exclude-module scipy --exclude-module matplotlib --name="Fluttering Bird" run.py
```

4. The executable should be in the `dist` folder:
- On Linux: `./dist/Asteroid\ Shooter`
- On Windows: `& '.\dist\Asteroid Shooter.exe'`

# Libraries Used
- `pygame-ce` for graphics, user input, etc. (The main library of the project)
- `pyinstaller` for compiling the project
- `pygame_gui` for buttons, text, and other GUI elements
