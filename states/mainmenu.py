import pygame
from gi.repository import Gtk

from gamestate import *

class MainMenu(GameState):
    def __init__(self):
        self.x = 0
        self.y = 0
        pass

    # Update movement, track events
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x -= 10
                elif event.key == pygame.K_RIGHT:
                    self.x += 10
                elif event.key == pygame.K_UP:
                    self.y -= 10
                elif event.key == pygame.K_DOWN:
                    self.y += 10
        pass

    # Draw this state
    def draw(self,screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)
        pass
        
