import pygame
from player import Player
from maze_utils import MazeUtils
from pathfinder import AStarPathfinder

class MazeGame:

    def __init__(
        self,
        grid,
        sound_manager
    ):
        
        self.sound_manager = sound_manager
        self.grid = grid

        self.rows = len(grid)
        self.cols = len(grid[0])

        self.cell_size = min(
            600 // self.cols,
            600 // self.rows
        )

        if self.cell_size < 1:
            self.cell_size = 1

        self.camera_size = 25

        self.cell_size = 30

        self.width = (
            self.camera_size *
            self.cell_size
        )

        self.height = (
            self.camera_size *
            self.cell_size
        )

        start_x, start_y = (
            MazeUtils.find_start(
                self.grid
            )
        )

        self.player = Player(
            start_x,
            start_y
        )

        self.exit_x, self.exit_y = (
            MazeUtils.find_best_exit(

                self.grid,

                self.player.x,

                self.player.y
            )
        )

        self.pathfinder = AStarPathfinder(
            self.grid
        )

        self.path = self.pathfinder.find_path(
            (
                self.player.x,
                self.player.y
            ),
            (
                self.exit_x,
                self.exit_y
            )
        )

        self.move_delay = 80
        self.last_move = 0
        self.game_won = False

        self.start_time = pygame.time.get_ticks()

        self.finish_time = None

        self.show_path = False
        self.auto_solve = False
        self.path_index = 0
        self.screenshot_saved = False

    def update_path(self):

        self.path = self.pathfinder.find_path(

            (
                self.player.x,
                self.player.y
            ),

            (
                self.exit_x,
                self.exit_y
            )
        )

        self.path_index = 0

    def draw_grid(self, screen):

        camera_size = 25

        half = camera_size // 2

        start_x = self.player.x - half
        start_y = self.player.y - half

        for screen_y in range(camera_size):

            for screen_x in range(camera_size):

                grid_x = start_x + screen_x
                grid_y = start_y + screen_y

                if (
                    0 <= grid_x < self.cols
                    and
                    0 <= grid_y < self.rows
                ):

                    if self.grid[grid_y][grid_x] == 1:

                        color = (
                            255,
                            255,
                            255
                        )

                    else:

                        color = (
                            0,
                            0,
                            0
                        )

                else:

                    color = (
                        50,
                        50,
                        50
                    )

                pygame.draw.rect(

                    screen,

                    color,

                    (
                        screen_x *
                        self.cell_size,

                        screen_y *
                        self.cell_size,

                        self.cell_size,

                        self.cell_size
                    )
                )

    def draw_player(self, screen):

        center = (
            self.camera_size // 2
        )

        pygame.draw.rect(

            screen,

            (255, 0, 0),

            (
                center *
                self.cell_size,

                center *
                self.cell_size,

                self.cell_size,

                self.cell_size
            )
        )

    def draw_exit(self, screen):

        half = (
            self.camera_size // 2
        )

        screen_x = (
            self.exit_x
            -
            self.player.x
            +
            half
        )

        screen_y = (
            self.exit_y
            -
            self.player.y
            +
            half
        )

        if (
            0 <= screen_x < self.camera_size
            and
            0 <= screen_y < self.camera_size
        ):

            pygame.draw.rect(

                screen,

                (0, 255, 0),

                (
                    screen_x *
                    self.cell_size,

                    screen_y *
                    self.cell_size,

                    self.cell_size,

                    self.cell_size
                )
            )

    def draw_path(self, screen):

        if not self.show_path:
            return

        half = (
            self.camera_size // 2
        )

        for x, y in self.path:

            screen_x = (
                x
                -
                self.player.x
                +
                half
            )

            screen_y = (
                y
                -
                self.player.y
                +
                half
            )

            if (
                0 <= screen_x < self.camera_size
                and
                0 <= screen_y < self.camera_size
            ):

                pygame.draw.rect(

                    screen,

                    (0, 100, 255),

                    (
                        screen_x *
                        self.cell_size,

                        screen_y *
                        self.cell_size,

                        self.cell_size,

                        self.cell_size
                    )
                )

    def run(self):

        pygame.init()

        font = pygame.font.SysFont(
            None,
            80
        )

        small_font = pygame.font.SysFont(
            None,
            35
        )

        screen = pygame.display.set_mode(
            (
                self.width,
                self.height
            )
        )

        pygame.display.set_caption(
            "Maze Game"
        )

        clock = pygame.time.Clock()

        running = True

        while running:

            clock.tick(30)
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_p:

                        self.update_path()

                        self.show_path = (
                            not self.show_path
                        )

                    elif event.key == pygame.K_o:

                        self.update_path()

                        self.auto_solve = (
                            not self.auto_solve
                        )

                        self.path_index = 0

            current_time = pygame.time.get_ticks()

            if current_time - self.last_move > self.move_delay:
                moved = False
                if keys[pygame.K_UP]:

                    moved = self.player.move(
                        0,
                        -1,
                        self.grid
                    )

                    self.last_move = current_time

                elif keys[pygame.K_DOWN]:

                    moved = self.player.move(
                        0,
                        1,
                        self.grid
                    )

                    self.last_move = current_time

                elif keys[pygame.K_LEFT]:

                    moved = self.player.move(
                        -1,
                        0,
                        self.grid
                    )

                    self.last_move = current_time

                elif keys[pygame.K_RIGHT]:

                    moved = self.player.move(
                        1,
                        0,
                        self.grid
                    )

                    self.last_move = current_time

                if moved:
                        self.sound_manager.play_walk()

            if (
                self.player.x == self.exit_x
                and
                self.player.y == self.exit_y
            ):

                if not self.game_won:

                    self.game_won = True

                    self.finish_time = (
                        pygame.time.get_ticks()
                    )

                    self.sound_manager.play_cheer()

            screen.fill(
                (0, 0, 0)
            )

            if self.auto_solve:

                if self.path_index < len(self.path):

                    x, y = self.path[
                        self.path_index
                    ]

                    old_x = self.player.x
                    old_y = self.player.y

                    self.player.x = x
                    self.player.y = y

                    if (
                        old_x != x
                        or
                        old_y != y
                    ):
                        self.sound_manager.play_walk()

                    self.path_index += 1

            self.draw_grid(screen)

            self.draw_path(screen)

            self.draw_exit(screen)

            self.draw_player(screen)

            elapsed = (
                pygame.time.get_ticks()
                -
                self.start_time
            ) // 1000

            timer_text = small_font.render(

                f"Time: {elapsed}s",

                True,

                (255, 255, 255)
            )

            screen.blit(
                timer_text,
                (10, 10)
            )

            if self.game_won:

                text = font.render(
                    "YOU WIN!",
                    True,
                    (255,255,0)
                )

                rect = text.get_rect(
                    center=(
                        self.width // 2,
                        self.height // 2
                    )
                )

                screen.blit(
                    text,
                    rect
                )

                seconds = (

                    self.finish_time
                    -
                    self.start_time

                ) // 1000

                time_text = small_font.render(

                    f"Solved in {seconds}s",

                    True,

                    (255,255,0)
                )

                screen.blit(

                    time_text,

                    (
                        self.width // 2 - 80,
                        self.height // 2 + 70
                    )
                )

            if self.game_won and not self.screenshot_saved:

                pygame.image.save(

                    screen,

                    "assets/output/solved_maze.png"
                )

                self.screenshot_saved = True

            pygame.display.flip()

        pygame.display.quit()