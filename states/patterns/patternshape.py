import pygame
import math
import random
from gi.repository import Gtk

from gamestate import *

# Class used to store data about a shape
# so that it may be compared to others
class PatternShape:
    
    def __init__(self, name, points, edges, rightAngels, parallels):
        self.name = name;
        self.edges = edges;
        self.points = points;
        self.rightAngels = rightAngels;
        self.parallels = parallels;
        
        # Normalizing points
        if "Rhombus" not in name: #I'm angry and tired
          for point in self.points:
              mag = math.sqrt(point['x']*point['x'] + point['y']*point['y'])
              point['x'] /= mag
              point['y'] /= mag
        
        pass
        
    # Get number of right angles
    def right_angles(self):
        pass
    
    # Get number of parallel line pairs
    def parallel_lines(self):
        pass
    
    #Draw to screen at pos
    def draw_shape(self,screen,color,x,y, rad=10, width=0):
        #print "DOOP"
        #print self.points
        scaledPoints = []
        for i in range(len(self.points)):
            point = self.points[i]
            scaledPoints.append([point['x']*rad+x, point['y']*rad+y])
        pygame.draw.polygon(screen,color, scaledPoints, width)
