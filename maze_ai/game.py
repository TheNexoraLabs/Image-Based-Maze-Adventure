from menu import Menu
from image_processor import ImageProcessor
from grid_converter import GridConverter
from maze_game import MazeGame
from sound_manager import SoundManager

class Game:

    def __init__(self, screen):

        self.screen = screen

        self.sound_manager = SoundManager()

        self.sound_manager.play_menu_music()

        self.menu = Menu(
            screen,
            self.sound_manager
        )

        self.selected_maze = None

    def run_maze(self, maze_path):

        print("RUNNING MAZE:", maze_path)

        processor = ImageProcessor(
            maze_path
        )

        binary = processor.process()

        converter = GridConverter(
            binary
        )

        grid = converter.image_to_grid(
            cell_size=8,
            wall_threshold=0.25
        )

        self.sound_manager.play_game_music()

        game = MazeGame(
            grid,
            self.sound_manager
        )

        game.run()

        self.sound_manager.play_menu_music()