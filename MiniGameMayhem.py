#!/usr/bin/python
import pygame

from states.mainmenu import *
from gamestate import *

class MiniGameMayhem:
    def __init__(self):
        self.paused = False
        global NOT_XO
        NOT_XO = False
        global NOT_XO
        NOT_XO = False

    def initNonXO(self):
        global NOT_XO
        NOT_XO = True
        pygame.init()
        pygame.font.init()
        swidth = pygame.display.Info().current_w
        sheigh = pygame.display.Info().current_h           
        size = (1200, 900)
        if( float(swidth)/float(sheigh) == 4/3 ):
            size = (swidth, sheight)
        pygame.display.set_mode(size) #, pygame.RESIZABLE)
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()
        #if (self.screen == None):
            #print "SCREEN IS still NULL"
            #exit()
        #self.gamestate = MainMenu(self.clock, self.screen)
            
    def write_file(self, file_path):
        pass
    def read_file(self, file_path):
        pass

    def set_gamestate(self, gamestate):
        self.gamestate = gamestate
    
    def set_paused(self, paused):
        self.paused = paused
        #self.gamestate.set_paused(paused)

    # The main game loop.
    def run(self):
        pygame.font.init() 

        global NOT_XO
        if( NOT_XO == False ): # canvas seems to start pygame
            self.screen = pygame.display.get_surface()
            self.clock = pygame.time.Clock()
            print "boop " + str(self.clock)
        self.gamestate = MainMenu(self.clock, self.screen)
        self.gamestate.start()


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    # pygame.init()
    # pygame.font.init()
    # swidth = pygame.display.Info().current_w
    # sheight = pygame.display.Info().current_h
    # pygame.display.set_mode((swidth,sheight))
    # pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    # pygame.display.set_caption('MiniGameMayhem')
    # For know if running on xo or not
    # global NOT_XO
    #NOT_XO = True
    game = MiniGameMayhem()
    game.initNonXO()
    game.run()

if __name__ == '__main__':
    main()
