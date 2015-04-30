import pygame
from gi.repository import Gtk
from .patternshape import *

from gamestate import *

class Patterns(GameState):
    def __init__(self, main, clock, screen):
        GameState.__init__(self, main, clock, screen)
        self.font = pygame.font.SysFont("monospace", 25)
        self.make_level();
        pass

    # Called to make this round's puzzle
    def make_level(self):
        self.testPoint = generate_shape(3,0,0)
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
        


# Returns a shape with the given parameters
# edges: Number of edges for this shape
# rightAngles: Number of right angles for this shape
# parallels: Number of parallel pairs for this shape
def generate_shape(edges, rightAngles, parallels):
    if(edges < 3): return # impossible
    if(parallels*2 > edges): return # too many parallel pairs
    maxAng = 180 * (edges-2)
    if(90*rightAngles > maxAng): return # too many right angles    
    
    points = []
    # TODO
    # Rotate the object randomly
    # set angles randomly
    rad = 150
    rIter = (maxAng/edges)*3.14/180
    for i in range(edges):
        dist = random.randint(rad-40, rad+40)
        x = math.cos(i*rIter)*dist
        y = math.sin(i*rIter)*dist
        
        points.append({ 'x':x, 'y':y })
    
    return PatternShape(points, edges, rightAngles, parallels)