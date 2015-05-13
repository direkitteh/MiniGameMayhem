import pygame
from gi.repository import Gtk
from .patternshape import *
from .patternlevel import *
from pygame.locals import *
from random import randint

from gamestate import *

class Patterns(GameState):
    
    SQUARE = PatternShape("Square", [
        {'x':-10,'y':-10},
        {'x':10, 'y':-10},
        {'x':10, 'y':10},
        {'x':-10,'y':10}
    ], 4, 4, 2)

    EQ_TRIANGLE = PatternShape("Equilateral Triangle", [
        {'x':0, 'y':-2},
        {'x':2, 'y':1.5},
        {'x':-2, 'y':1.5}
    ], 3,0,0)

    HEXAGON = PatternShape("Equilateral Hexagon", [
        {'x':1.25, 'y':2},
        {'x':2.5, 'y':0},
        {'x':1.25, 'y':-2},
        {'x':-1.25, 'y':-2},
        {'x':-2.5, 'y':0},
        {'x':-1.25, 'y':2},
    ], 6,0,3)
    
    RECTANGLES = [ # mutations of a rectangle
        PatternShape("Rectangle", [
            {'x':-2,'y':-0.5},
            {'x':2, 'y':-0.5},
            {'x':2, 'y':0.5},
            {'x':-2,'y':0.5}
        ], 4, 4, 2),
        PatternShape("Rectangle", [
            {'x':-1.5,'y':-1},
            {'x':1.5, 'y':-1},
            {'x':1.5, 'y':1},
            {'x':-1.5,'y':1}
        ], 4, 4, 2),
        PatternShape("Rectangle", [
            {'x':-1,'y':-1.5},
            {'x':1, 'y':-1.5},
            {'x':1, 'y':1.5},
            {'x':-1,'y':1.5}
        ], 4, 4, 2),
        PatternShape("Rectangle", [
            {'x':-2,'y':-0.5},
            {'x':2, 'y':-0.5},
            {'x':2, 'y':0.5},
            {'x':-2,'y':0.5}
        ], 4, 4, 2),
    ]
    RHOMBUSES = [
        PatternShape("Rhombus", [
            {'x': 0.5, 'y':-1},
            {'x': 1, 'y':1},
            {'x':-0.5, 'y':1},
            {'x':-1, 'y':-1}
        ], 4, 0, 2),
        PatternShape("Rhombus", [
            {'x':-0.5, 'y':-1},
            {'x':-1, 'y':1},
            {'x': 0.5, 'y':1},
            {'x': 1, 'y':-1}
        ], 4, 0, 2),
        PatternShape("Rhombus", [
            {'x':-1, 'y':-0.5},
            {'x': 1, 'y':-1},
            {'x': 1, 'y': 0.5},
            {'x':-1, 'y': 1}
        ], 4, 0, 2),
        PatternShape("Rhombus", [
            {'x':-1, 'y': 0.5},
            {'x': 1, 'y': 1},
            {'x': 1, 'y':-0.5},
            {'x':-1, 'y':-1}
        ], 4, 0, 2)
    ]
    
    AC_TRIANGLES = [
        PatternShape("Acute Triangle", [
            {'x':-0.5, 'y':-2},
            {'x':2, 'y':2},
            {'x':-1.5, 'y':1.5}
        ], 3,0,0),
        PatternShape("Acute Triangle", [
            {'y':-0.5, 'x':-2},
            {'y':2, 'x':2},
            {'y':-1.5, 'x':1.5}
        ], 3,0,0),
        PatternShape("Acute Triangle", [
            {'x':0, 'y':-3},
            {'x':-2, 'y':2},
            {'x':2, 'y':-2}
        ], 3,0,0),
        PatternShape("Acute Triangle", [
            {'x':-1, 'y':-1},
            {'x':3, 'y':-2},
            {'x':0, 'y':2}
        ], 3,0,0)
    ]
    
    OB_TRIANGLES = [
        PatternShape("Obtuse Triangle", [
            {'x':0.5, 'y':-2},
            {'x':-2, 'y':2},
            {'x':0.5, 'y':0.5}
        ], 3,0,0),
        PatternShape("Obtuse Triangle", [
            {'x':2, 'y':1},
            {'x':4, 'y':-2},
            {'x':-3, 'y':0}
        ], 3,0,0),
        PatternShape("Obtuse Triangle", [
            {'x':-1, 'y':2},
            {'x':3, 'y':-3},
            {'x':-1, 'y':-1}
        ], 3,0,0),
        PatternShape("Obtuse Triangle", [
            {'x':0, 'y':1},
            {'x':4, 'y':-1},
            {'x':-3, 'y':-1}
        ], 3,0,0)
    ]
    
    RT_TRIANGLES = [
        PatternShape("Right Triangle", [
            {'x':-2, 'y':3},
            {'x':3, 'y':-1},
            {'x':-2, 'y':-1}
        ], 3,0,0),
        PatternShape("Right Triangle", [
            {'x':-3, 'y':1},
            {'x':2, 'y':1},
            {'x':2, 'y':-1}
        ], 3,0,0),
        PatternShape("Right Triangle", [
            {'x':-3, 'y':1},
            {'x':2, 'y':1},
            {'x':2, 'y':-1}
        ], 3,0,0),
        PatternShape("Right Triangle", [
            {'x':-2, 'y':0},
            {'x':1, 'y':3},
            {'x':0, 'y':-2}
        ], 3,0,0)
    ]
    
    SHAPES = [RECTANGLES, RHOMBUSES, AC_TRIANGLES, OB_TRIANGLES, RT_TRIANGLES, [SQUARE, EQ_TRIANGLE, HEXAGON]]
    
    LEVELS = []
    
    def __init__(self, clock, screen):
        GameState.__init__(self, clock, screen)
        self.font = pygame.font.SysFont("monospace", 25)
        self.score = 0
        self.currentLevel = 0;
        self.build_levels();
        self.level = Patterns.LEVELS[self.currentLevel];
        pass


    # Run the menu
    def start(self):
        self.running = True
        while self.running:
            events = events = pygame.event.get()
            self.update(events)
            self.screen.fill([255,255,255])
            self.draw()
            events = pygame.event.get()

            for event in events:
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.running = False
                    
            pygame.display.flip()
            self.clock.tick(60)
    
    
    def build_levels(self):
        if(len(Patterns.LEVELS) != 0): pass # Already populated
        
        ########  not right vs right  #########
        level = PatternLevel(self)
        level.set_question("Which shape doesn't match?")
        
        
        level.add_shape(Patterns.RT_TRIANGLES[ randint(0,len(Patterns.RT_TRIANGLES)-1) ])
        level.add_shape(Patterns.RT_TRIANGLES[ randint(0,len(Patterns.RT_TRIANGLES)-1) ])
        
        non_rt_tris = [ [Patterns.EQ_TRIANGLE], Patterns.AC_TRIANGLES, Patterns.OB_TRIANGLES ]
        arr = non_rt_tris[ randint(0,len(non_rt_tris)-1) ]
        level.add_shape(arr[ randint(0,len(arr)-1) ])
        
        level.add_shape(Patterns.RT_TRIANGLES[ randint(0,len(Patterns.RT_TRIANGLES)-1) ])
        
        
        level.shapeAnswer = 2
        
        level.add_reason("It is an obtuse triangle")
        level.add_reason("It is not a right triangle")
        level.add_reason("It is an acute triangle")
        level.add_reason("It is not an equilateral triangle")
        
        level.reasonAnswer = 1
        
        Patterns.LEVELS.append(level)
        
        
        ########  2 right vs square vs pentagon  #########
        level = PatternLevel(self)
        level.set_question("Which shape doesn't match?")
        
        level.add_shape(Patterns.HEXAGON)
        level.add_shape(Patterns.RT_TRIANGLES[ randint(0,len(Patterns.RT_TRIANGLES)-1) ])
        level.add_shape(Patterns.RT_TRIANGLES[ randint(0,len(Patterns.RT_TRIANGLES)-1) ])
        level.add_shape(Patterns.SQUARE)
        
        level.shapeAnswer = 0
        
        level.add_reason("It has too many sides")
        level.add_reason("It is a right triangle")
        level.add_reason("It has no acute angles")
        level.add_reason("It has no right angles")
        
        level.reasonAnswer = 3
        
        Patterns.LEVELS.append(level)
        
        
        ########  Square, 2 Rectangles, vs Rhombus (no right angles) #########
        level = PatternLevel(self)
        level.set_question("Which shape doesn't match?")
        
        level.add_shape(Patterns.RECTANGLES[ randint(0,len(Patterns.RECTANGLES)-1) ])
        level.add_shape(Patterns.SQUARE)
        level.add_shape(Patterns.RHOMBUSES[ randint(0,len(Patterns.RHOMBUSES)-1) ])
        level.add_shape(Patterns.RECTANGLES[ randint(0,len(Patterns.RECTANGLES)-1) ])
        
        level.shapeAnswer = 2
        
        level.add_reason("It isn't equilateral")
        level.add_reason("It has no parallel sides")
        level.add_reason("It has no right angles")
        level.add_reason("It has no acute angles")
        
        level.reasonAnswer = 2
        
        Patterns.LEVELS.append(level)
        
        
        ########  Rhombus, Rectangles, Hexagon, vs Triangle (no paralels) #########
        level = PatternLevel(self)
        level.set_question("Which shape doesn't match?")
        
        level.add_shape(Patterns.HEXAGON)
        arr = non_rt_tris[ randint(0,len(non_rt_tris)-1) ]
        level.add_shape(arr[ randint(0,len(arr)-1) ])
        level.add_shape(Patterns.SQUARE)
        level.add_shape(Patterns.RHOMBUSES[ randint(0,len(Patterns.RHOMBUSES)-1) ])
        
        level.shapeAnswer = 1
        
        level.add_reason("It has no right angles")
        level.add_reason("It has no parallel sides")
        level.add_reason("It isn't equilateral")
        level.add_reason("It has no acute angles")
        
        level.reasonAnswer = 1
        
        Patterns.LEVELS.append(level)
        
        pass
    
    # Update movement, track events
    def update(self, events):
        self.level.update()
        self.clock.tick(30)
        
        if(self.level.done):
          self.currentLevel += 1
          if(self.currentLevel >= len(Patterns.LEVELS)):
            self.running = False
            return;
          
          self.score += self.level.addScore;
          self.level.reset()
          self.level = Patterns.LEVELS[self.currentLevel]
        pass

    # Draw this state
    def draw(self):
        #self.testPoint.draw_shape(self.screen, 200, 200);
        """Patterns.RT_TRIANGLES[0].draw_shape(self.screen,[255,0,0], 200, 200,10,5);
        Patterns.RT_TRIANGLES[0].draw_shape(self.screen,[0,0,0], 200, 200,10);
        
        Patterns.OB_TRIANGLES[0].draw_shape(self.screen,[255,0,0], 300, 200,10,5);
        Patterns.OB_TRIANGLES[0].draw_shape(self.screen,[0,0,0], 300, 200,10);
        
        Patterns.HEXAGON.draw_shape(self.screen,[255,0,0], 300, 300,10,5);
        Patterns.HEXAGON.draw_shape(self.screen,[0,0,0], 300, 300, 10);
        
        Patterns.EQ_TRIANGLE.draw_shape(self.screen,[255,0,0], 200, 300, 10,5);
        Patterns.EQ_TRIANGLE.draw_shape(self.screen,[0,0,0], 200, 300, 10);"""
        self.level.draw(self.screen)
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
