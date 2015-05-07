import pygame
import math
import random
from gi.repository import Gtk

from gamestate import *

# Class used to store data about a shape
# so that it may be compared to others
class PatternLevel:
    
    def __init__(self):
        self.question = "";
        self.shapes = [];
        self.shapeAnswer = -1;
        self.reasons = [];
        self.reasonAnswer = -1;
        pass
    
    def set_question(self, question):
        self.question = question
    def add_shape(self, shape):
        self.shapes.append(shape)
    def add_reason(self, reason):
        self.reasons.append(reason)
    
    
    def draw(self, screen):
        font = pygame.font.SysFont(None, 32)
        
        width = screen.get_width();
        height = screen.get_height();
        
        qText = font.render(self.question, True, [0,0,0])
        
        screen.blit(qText, [width/2 - font.size(self.question)[0]/2, height/2 - 100]);
        
        
        shapePosX = width/2 - 120.0*(len(self.shapes)-1)/2.0;
        shapePosY = height/2;
        for i in range(len(self.shapes)):
            self.shapes[i].draw_shape(screen, [0,0,0], shapePosX + i*120, shapePosY, 30) # TODO change color and width by selection
        
        
        for i in range(len(self.reasons)) :
            res = font.render(self.reasons[i], True, [0,0,0]); # TODO change color by selection
            size = font.size(self.reasons[i]);
            screen.blit(res, [width/2 - size[0]/2, height/2 + 100 + i*(size[1]+15)])
        
        pygame.draw.line(screen, (0,0,0), (width/2,0), (width/2,height)) 
        pygame.draw.line(screen, (0,0,0), (0,height/2), (width,height/2))
        pass
