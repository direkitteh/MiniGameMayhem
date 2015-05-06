import pygame
import math
import random
from gi.repository import Gtk

from gamestate import *

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
    def parallel_lines(self):
        pass
    
    #Draw to screen at pos
    def draw_shape(self,screen,x,y, rad=10):
        #print "DOOP"
        #print self.points
        for i in range(len(self.points)-1):
            point = self.points[i]
            npoint = self.points[i+1]
            pygame.draw.line(screen, 0x000, (x+point['x']*rad, y+point['y']*rad), (x+npoint['x']*rad, y+npoint['y']*rad))
            
        point = self.points[len(self.points)-1]
        npoint = self.points[0]
        pygame.draw.line(screen, 0x000, (x+point['x']*rad, y+point['y']*rad), (x+npoint['x']*rad, y+npoint['y']*rad))
