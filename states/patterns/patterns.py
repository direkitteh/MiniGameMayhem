import pygame
from gi.repository import Gtk
from states.patterns.patternshape import *

from gamestate import *

class Patterns(GameState):
    def __init__(self, clock, screen):
        GameState.__init__(self,clock, screen)
        self.font = pygame.font.SysFont("monospace", 25)
        make_level();
        pass

    # Called to make this round's puzzle
    def make_level(self):
        self.testPoint = generateShape(3,0,0)
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
        self.testPoint.draw_shape(self.screen, 200, 200);
        pass
        
