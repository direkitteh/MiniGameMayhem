
'''
    Any and all states of the game
    eg main menu, sequence game, fraction game, etc.
'''

class GameState:
    def __init__(self, clock, screen):
        self.clock = clock
        self.screen = screen
        self.paused = False

    # Do things on pause and resume
    def set_paused(self, paused):
        self.paused = paused

    # Hand over control to the mini game
    def start(self):
        pass