import pygame

from settings import *

from menu import Menu

from game import Game

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

game = Game(screen)

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        game.menu.handle_event(event)

    game.menu.draw()

    if (

        game.menu.start_requested

        and

        game.menu.selected_maze

    ):

        game.run_maze(
            game.menu.selected_maze
        )

        screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        game.menu.screen = screen
        game.screen = screen

        game.menu.start_requested = False
        game.menu.selected_maze = None

    pygame.display.flip()

pygame.quit()