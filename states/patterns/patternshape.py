import pygame
<<<<<<< Updated upstream
=======
import math
import random
>>>>>>> Stashed changes
from gi.repository import Gtk

from gamestate import *

<<<<<<< Updated upstream
class PatternShape:
    def __init__(self):
        self.edges = 1;
        pass
        
    #Get number of right angles
    def right_angles(self):
        pass
    
    #Get number of parallel line pairs
=======

# Class used to store data about a shape
# so that it may be compared to others
class PatternShape:
    def __init__(self, points, edges, rightAngels, parallels):
        self.edges = edges;
        self.points = points;
        self.rightAngels = rightAngels;
        self.parallels = parallels;
        pass
        
    # Get number of right angles
    def right_angles(self):
        pass
    
    # Get number of parallel line pairs
>>>>>>> Stashed changes
    def parallel_lines(self):
        pass
    
    #Draw to screen at pos
    def draw_shape(self,screen,x,y):
<<<<<<< Updated upstream
        pass
=======
        for i in range(self.points.length-2):
            point = self.points[i]
            npoint = self.points[i+1]
            pygame.draw.line(screen, 0x000, (x+point.x, y+point.y), (x+npoint.x, y+npoint.y))

# Returns a shape with the given parameters
# edges: Number of edges for this shape
# rightAngles: Number of right angles for this shape
# parallels: Number of parallel pairs for this shape
def generate_shape(edges, rightAngles, parallels):
    if(edges < 3) pass # impossible
    if(parallels*2 > edges) pass # too many parallel pairs
    maxAng = 180 * (edges-2)
    if(90*rightAngles > maxAng) pass # too many right angles    
    
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
        
        points.append({ x:x, y:y })
    
    return PatternShape(points, edges, rightAngles, parallels)
>>>>>>> Stashed changes
