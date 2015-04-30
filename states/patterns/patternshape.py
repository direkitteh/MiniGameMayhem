import pygame
from gi.repository import Gtk

from gamestate import *

class PatternShape:
    def __init__(self):
        self.edges = 1;
        pass
        
    #Get number of right angles
    def right_angles(self):
        pass
    
    #Get number of parallel line pairs
    def parallel_lines(self):
        pass
    
    #Draw to screen at pos
    def draw_shape(self,screen,x,y):
        pass
