# 🧩 Image-Based Maze Adventure

A Python game that turns any maze image into a playable puzzle — with A* pathfinding, auto-solve, and a camera that follows your player.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red?logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🎮 What It Does

You supply a PNG image of a maze. The game:
1. Processes the image using OpenCV (grayscale → blur → threshold → invert)
2. Converts it into a binary grid (walls = 1, paths = 0)
3. Drops you into the maze with a top-down camera view
4. Lets you navigate manually — or press a key to watch it auto-solve using **A\***

---

## ✨ Features

- 📷 **Image-to-grid conversion** — any black & white maze PNG works
- 🧠 **A\* pathfinding** — finds the optimal route from start to exit
- 🤖 **Auto-solve mode** — press `O` to watch the AI solve it
- 👁️ **Path hint mode** — press `P` to reveal the solution path
- 📷 **Camera system** — 25×25 viewport follows the player
- ⏱️ **Timer** — tracks how long you take to solve
- 🔊 **Sound effects & background music** — menu and in-game tracks
- 💾 **Auto-screenshot** — saves a `solved_maze.png` when you win

---

## 📁 Project Structure

```
maze_ai/
├── assets/
│   ├── input/          # Your maze PNG files go here
│   │   ├── maze1.png
│   │   ├── maze2.png
│   │   └── maze3.png
│   ├── music/          # Background music
│   │   ├── menu_music.mp3
│   │   └── game_music.mp3
│   ├── output/         # Auto-saved screenshots
│   │   └── solved_maze.png
│   └── sounds/         # Sound effects
│       ├── click.wav
│       ├── walk.wav
│       └── cheer.wav
├── main.py             # Entry point
├── game.py             # Game orchestrator
├── menu.py             # Main menu UI
├── maze_game.py        # Core game loop & rendering
├── player.py           # Player movement logic
├── image_processor.py  # OpenCV image pipeline
├── grid_converter.py   # Image → binary grid
├── maze_utils.py       # BFS start/exit finder
├── pathfinder.py       # A* algorithm
├── sound_manager.py    # Audio management
├── settings.py         # Global constants
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/TheNexoraLabs/Image-Based-Maze-Adventure.git
cd Image-Based-Maze-Adventure
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your maze images
Drop any black & white maze PNG files into `assets/input/`. The game will list them automatically in the menu.

> **Tip:** Mazes should have thick enough walls relative to image size. The grid converter uses an 8×8 pixel cell size by default.

### 4. Run the game
```bash
python main.py
```

---

## 🕹️ Controls

| Key | Action |
|-----|--------|
| `Arrow Keys` | Move the player |
| `P` | Toggle path hint (shows solution in blue) |
| `O` | Toggle auto-solve (AI takes over) |
| `ESC` / Close window | Exit to menu |

---

## ⚙️ How It Works

### Image Processing Pipeline (`image_processor.py`)
```
PNG → Grayscale → Gaussian Blur → Adaptive Threshold → Invert → Binary Image
```

### Grid Conversion (`grid_converter.py`)
The binary image is divided into 8×8 pixel cells. If more than 25% of a cell's pixels are white, it's marked as a wall (`1`). Otherwise it's a path (`0`).

### Pathfinding (`pathfinder.py` + `maze_utils.py`)
- **Start:** First open cell (`0`) found scanning top-left to bottom-right
- **Exit:** The open cell farthest from start, found via BFS
- **Route:** A\* with Manhattan distance heuristic finds the optimal path

---

## 🖼️ Adding Your Own Mazes

1. Create or download a black & white maze image (PNG format)
2. Make sure walls are white and paths are black (or mostly so)
3. Place it in `assets/input/`
4. Launch the game — it will appear in the maze selection menu

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `pygame` | Game rendering, input, audio |
| `opencv-python` | Image processing pipeline |
| `numpy` | Pixel array operations |
| `pillow` | Image utility support |

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Maze solving algorithm based on classic A\* with Manhattan heuristic
- Image processing pipeline built with OpenCV's adaptive thresholding
