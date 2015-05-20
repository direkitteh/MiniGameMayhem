import pygame

from gi.repository import Gtk
from gamestate import *
from .patterns.patterns import Patterns
from states.sequences import SequenceGame

class MainMenu(GameState):
    def __init__(self, clock, screen):
        GameState.__init__(self, clock, screen)
        self.font = pygame.font.SysFont(None, 25)
        pass

    # Run the menu
    def start(self):
        self.running = True
        global NOT_XO
        global CANVAS
        while self.running:
            while Gtk.events_pending():
                Gtk.main_iteration()
            if( NOT_XO == True ):
              events == CANVAS.translator
            else:
              events = pygame.event.get()
            self.update(events)
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

    # Update movement, track events
    def update(self, events):
        # for event in events:
        global NOT_XO
        if(NOT_XO):
          for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP0:
                    # Switch state to sequence game
                    game = SequenceGame(self.screen, self.clock)
                    game.start()
                elif event.key == pygame.K_2:
                    # Switch state to fractions game
                    pass
                elif event.key == pygame.K_3:
                    # Switch state to patterns game
                    game = Patterns(self.clock, self.screen)
                    game.start()
                    pass
                elif event.key == pygame.K_4:
                    # Switch state to angles game
                    pass
        else:
          pressed = event._get_pressed()
          if checkPressed(pressed, pygame.K_1):
              # Switch state to sequence game
              game = SequenceGame(self.screen, self.clock)
              game.start()
          elif checkPressed(pressed, pygame.K_2):
              # Switch state to fractions game
              pass
          elif checkPressed(pressed, pygame.K_3):
              # Switch state to patterns game
              game = Patterns(self.clock, self.screen)
              game.start()
              pass
          elif checkPressed(pressed, pygame.K_4):
              # Switch state to angles game
              pass
    
    # Draw this state
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.font.render("Press a Key:", 1, (10,10,10)), (25,280))
        self.screen.blit(self.font.render("1: Run Sequence Game", 1, (10,10,10)), (50,320))
        self.screen.blit(self.font.render("2: Run Fractions Game", 1, (10,10,10)), (50,340))
        self.screen.blit(self.font.render("3: Run Patterns Game", 1, (10,10,10)), (50,360))
        self.screen.blit(self.font.render("4: Run Angles Game", 1, (10,10,10)), (50,380))

    
def checkPressed(pressed, key):
  return key in pressed and pressed[key]