import pygame

from settings import *


class Button:

    def __init__(self, x, y, width, height, text):

        self.rect = pygame.Rect(x, y, width, height)

        self.text = text

        self.color = LIGHT_BLUE

        self.hover_color = GREEN

    def draw(self, screen, font):

        mouse_pos = pygame.mouse.get_pos()

        color = self.color

        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=10
        )

        text_surface = font.render(
            self.text,
            True,
            BLACK
        )

        text_rect = text_surface.get_rect(
            center=self.rect.center
        )

        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                return self.rect.collidepoint(event.pos)

        return False


class Menu:

    def __init__(
        self,
        screen,
        sound_manager
    ):
        
        self.sound_manager = sound_manager
        self.screen = screen

        self.title_font = pygame.font.SysFont(
            FONT_NAME,
            60
        )

        self.button_font = pygame.font.SysFont(
            FONT_NAME,
            35
        )

        self.buttons = [
            Button(
                350,
                250,
                300,
                60,
                "Select Maze"
            ),

            Button(
                350,
                350,
                300,
                60,
                "Exit"
            )
        ]

        self.maze_buttons = []

        self.show_maze_selection = False

        self.selected_maze = None

        self.start_requested = False

    def draw(self):

        self.screen.fill(GRAY)

        if self.show_maze_selection:

            title = self.title_font.render(

                "Select Maze",

                True,

                WHITE

            )

            self.screen.blit(
                title,
                (
                    WIDTH // 2 - 150,
                    70
                )
            )

            for button in self.maze_buttons:

                button.draw(

                    self.screen,

                    self.button_font

                )

            return

        title = self.title_font.render(
            "Maze Adventure",
            True,
            WHITE
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 100)
        )

        self.screen.blit(title, title_rect)

        for button in self.buttons:
            button.draw(
                self.screen,
                self.button_font
            )

    def handle_event(self, event):
        if self.show_maze_selection:

            for button in self.maze_buttons:

                if button.is_clicked(event):

                    self.sound_manager.play_click()

                    self.selected_maze = (
                        "assets/input/" +
                        button.text
                    )

                    self.show_maze_selection = False

                    self.start_requested = True

                    print(
                        "SELECTED:",
                        self.selected_maze
                    )

            return

        if self.buttons[0].is_clicked(event):

            self.sound_manager.play_click()

            self.show_maze_selection = True

            self.load_mazes()

        if self.buttons[1].is_clicked(event):

            self.sound_manager.play_click()

            pygame.quit()

            exit()


    def load_mazes(self):

        import os

        self.maze_buttons = []

        files = []

        for file in os.listdir(
            "assets/input"
        ):

            if file.lower().endswith(".png"):

                files.append(file)

        files.sort()

        y = 180

        for file in files:

            button = Button(

                250,

                y,

                500,

                50,

                file

            )

            self.maze_buttons.append(
                button
            )

            y += 70

        print(files)


            