import pygame
from gi.repository import Gtk

from gamestate import *

class Patterns(GameState):
    def __init__(self, clock, screen):
        GameState.__init__(self,clock, screen)
        self.font = pygame.font.SysFont("monospace", 25)
        make_level();
        pass

    # Called to make this round's puzzle
    def make_level(self):
        pass
    
    # Update movement, track events
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        self.clock.tick(30)
        pass

    # Draw this state
    def draw(self):
        pass
        
