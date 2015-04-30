import pygame
from gi.repository import Gtk

from gamestate import *
from .patterns.patterns import Patterns

class MainMenu(GameState):
    def __init__(self, main, clock, screen):
        GameState.__init__(self, main, clock, screen)
        self.font = pygame.font.SysFont("monospace", 25)
        pass

    # Update movement, track events
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    # Switch state to sequence game
                    pass
                elif event.key == pygame.K_2:
                    # Switch state to fractions game
                    pass
                elif event.key == pygame.K_3:
                    # Switch state to patterns game
                    self.main.set_gamestate(Patterns(self.main, self.clock, self.screen))
                    pass
                elif event.key == pygame.K_4:
                    # Switch state to angles game
                    pass
        
        self.clock.tick(30)
        pass

    # Draw this state
    def draw(self):
        self.screen.blit(self.font.render("Press a Key:", 1, (10,10,10)), (25,280))
        self.screen.blit(self.font.render("1: Run Sequence Game", 1, (10,10,10)), (50,320))
        self.screen.blit(self.font.render("2: Run Fractions Game", 1, (10,10,10)), (50,340))
        self.screen.blit(self.font.render("3: Run Patterns Game", 1, (10,10,10)), (50,360))
        self.screen.blit(self.font.render("4: Run Angles Game", 1, (10,10,10)), (50,380))
        pass
        
