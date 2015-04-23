#!/usr/bin/python
import pygame
from gi.repository import Gtk

from states.mainmenu import *
from gamestate import *

class MiniGameMayhem:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()

        self.gamestate = MainMenu(self.clock, self.screen)

        self.paused = False

    def set_paused(self, paused):
        self.paused = paused
        self.gamestate.set_paused(paused)

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        self.gamestate.write_file(self, file_path)
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        self.gamestate.read_file(self, file_path)
        pass

    # The main game loop.
    def run(self):
        self.running = True


        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)

            # Update states
            self.gamestate.update(events)

            # Clear Display
            self.screen.fill((255, 255, 255))  # 255 for white

            # Draw States
            self.gamestate.draw()

            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            #self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = MiniGameMayhem()
    game.run()

if __name__ == '__main__':
    main()
