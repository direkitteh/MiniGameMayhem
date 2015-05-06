import pygame
from gi.repository import Gtk
from .patternshape import *

from gamestate import *

class Patterns(GameState):
    
    SQUARE = PatternShape("Square", [
        {'x':-1,'y':-1},
        {'x':1, 'y':-1},
        {'x':1, 'y':1},
        {'x':-1,'y':1}
    ], 4, 4, 2)
    RECTANGLE = PatternShape("Rectangle", [
        {'x':-1.5,'y':-1},
        {'x':1.5, 'y':-1},
        {'x':1.5, 'y':1},
        {'x':-1.5,'y':1}
    ], 4, 4, 2)
    RHOMBUS = PatternShape("Rhombus", [
        {'x': -1.5, 'y':-1},
        {'x':0.5, 'y':-1},
        {'x':1.5, 'y':1},
        {'x':-0.5, 'y':1}
    ], 4, 0, 2)

    EQ_TRIANGLE = PatternShape("Equilateral Triangle", [
        {'x':0, 'y':-2},
        {'x':2, 'y':1.5},
        {'x':-2, 'y':1.5}
    ], 3,0,0)
    
    AC_TRIANGLE = PatternShape("Acute Triangle", [
        {'x':-0.5, 'y':-2},
        {'x':2, 'y':2},
        {'x':-1.5, 'y':1.5}
    ], 3,0,0)
    
    OB_TRIANGLE = PatternShape("Obtuse Triangle", [
        {'x':0.5, 'y':-2},
        {'x':-2, 'y':2},
        {'x':0.5, 'y':0.5}
    ], 3,0,0)
    
    RT_TRIANGLE = PatternShape("Right Triangle", [
        {'x':1.5, 'y':-2},
        {'x':1.5, 'y':2},
        {'x':-1.5, 'y':2}
    ], 3,0,0)
    
    SHAPES = [ SQUARE, RECTANGLE, RHOMBUS ] 
    
    def __init__(self, main, clock, screen):
        GameState.__init__(self, main, clock, screen)
        self.font = pygame.font.SysFont("monospace", 25)
        self.make_level();
        pass

    # Called to make this round's puzzle
    def make_level(self):
        #self.testPoint = generate_shape(3,0,0)
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
        #self.testPoint.draw_shape(self.screen, 200, 200);
        Patterns.RT_TRIANGLE.draw_shape(self.screen, 200, 200);
        Patterns.OB_TRIANGLE.draw_shape(self.screen, 300, 200);
        Patterns.AC_TRIANGLE.draw_shape(self.screen, 300, 300);
        Patterns.EQ_TRIANGLE.draw_shape(self.screen, 200, 300);
        pass
        
"""

Possible levels:
    Which shape doesnt belong?
        -3 right tirangles vs a not right triangle (not a right triangle)
        -2 right triangles, a square vs a pentagon (no right angles)
        -Square, 2 Rectangles, vs Rhombus (no right angles)
        -Rhombus, Rectangle, Hexagon vs triangle (no parallels)
        -3 acute triangles vs an obtuse or right 
        -3 obtuse triangles vs an acute or right
    (and why)
        

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
    
    return PatternShape(points, edges, rightAngles, parallels)"""