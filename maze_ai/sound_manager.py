import pygame


class SoundManager:

    def __init__(self):

        pygame.mixer.init()

        self.click_sound = pygame.mixer.Sound(
            "assets/sounds/click.wav"
        )

        self.walk_sound = pygame.mixer.Sound(
            "assets/sounds/walk.wav"
        )

        self.cheer_sound = pygame.mixer.Sound(
            "assets/sounds/cheer.wav"
        )

        self.walk_sound.set_volume(0.4)
        self.click_sound.set_volume(0.7)
        self.cheer_sound.set_volume(0.8)

    def play_click(self):

        self.click_sound.play()

    def play_walk(self):

        self.walk_sound.play()

    def play_cheer(self):

        self.cheer_sound.play()

    def play_menu_music(self):

        pygame.mixer.music.load(
            "assets/music/menu_music.mp3"
        )

        pygame.mixer.music.set_volume(0.5)

        pygame.mixer.music.play(-1)

    def play_game_music(self):

        pygame.mixer.music.load(
            "assets/music/game_music.mp3"
        )

        pygame.mixer.music.set_volume(0.5)

        pygame.mixer.music.play(-1)

    def stop_music(self):

        pygame.mixer.music.stop()