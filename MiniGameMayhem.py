#!/usr/bin/python
import pygame

from states.mainmenu import *
from gamestate import *

class MiniGameMayhem:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()

        self.gamestate = MainMenu(self.clock, self.screen)

        self.paused = False

    def set_gamestate(self, gamestate):
        self.gamestate = gamestate
    
    def set_paused(self, paused):
        self.paused = paused
        #self.gamestate.set_paused(paused)

    # The main game loop.
    def run(self):
        self.gamestate.start()


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = MiniGameMayhem()
    game.run()

if __name__ == '__main__':
    main()
