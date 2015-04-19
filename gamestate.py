
'''
    Any and all states of the game
    eg main menu, sequence game, fraction game, etc.
'''

class GameState:
    def __init__(self):
        self.paused = False

    # Do things on pause and resume
    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # Update movement, track events
    def update(self, events):
        pass

    # Draw this state
    def draw(self,screen):
        pass