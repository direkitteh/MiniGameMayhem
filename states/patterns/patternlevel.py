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
        
        self.shapeSelected = -1;
        self.reasonSelected = -1;
        pass
    
    def set_question(self, question):
        self.question = question
    def add_shape(self, shape):
        self.shapes.append(shape)
    def add_reason(self, reason):
        self.reasons.append(reason)
    
    
    def draw(self, screen):
        font = pygame.font.SysFont(None, 32)
        selectedFont = pygame.font.SysFont(None, 32)
        selectedFont.set_underline(True)
        
        mousePos = pygame.mouse.get_pos()
        
        width = screen.get_width();
        height = screen.get_height();
        
        whyText = font.render("and why?", True, [0,0,0])
        screen.blit(whyText, [width/2 - font.size("and why?")[0]/2, height/2 + 70]);
        
        qText = font.render(self.question, True, [0,0,0])
        screen.blit(qText, [width/2 - font.size(self.question)[0]/2, height/2 - 100]);
        
        
        shapeSpacing = 120
        shapePosX = width/2 - 120.0*(len(self.shapes)-1)/2.0;
        shapePosY = height/2;
        for i in range(len(self.shapes)):
            posX = shapePosX + i*shapeSpacing
            rect = [posX-shapeSpacing/2+10, shapePosY-shapeSpacing/2+10, shapeSpacing-20,shapeSpacing-20]
            
            shapeColor = [0,0,0]
            bgColor = [200,200,200]
            
            if(self.shapeSelected == i):
                shapeColor = [255,255,0]
            if(mouse_in_rect(mousePos, rect)):
                bgColor = [0,240,240]
                if(pygame.mouse.get_pressed()[0] == True):
                    self.shapeSelected = i
            
            pygame.draw.rect(screen, bgColor, rect) # background
            self.shapes[i].draw_shape(screen, shapeColor, posX, shapePosY, 30) # TODO change color and width by selection
        
        
        for i in range(len(self.reasons)) :
            size = font.size(self.reasons[i]);
            yPos = height/2 + 120 + i*(size[1]+15)
            rect = [0, yPos-3, width, size[1]+6]
            
            textColor = [0,0,0]
            bgColor = [200,200,200]
            
            if(self.reasonSelected == i):
                textColor = [255,255,0]
            if(mouse_in_rect(mousePos, rect)):
                bgColor = [0,240,240]
                if(pygame.mouse.get_pressed()[0] == True):
                    self.reasonSelected = i
            res = font.render(self.reasons[i], True, textColor); # TODO change color by selection
            pygame.draw.rect(screen, bgColor, rect) # background
            screen.blit(res, [width/2 - size[0]/2, yPos])
        
        pygame.draw.line(screen, (0,0,0), (width/2,0), (width/2,height)) 
        pygame.draw.line(screen, (0,0,0), (0,height/2), (width,height/2))
        pass

def mouse_in_rect(mousePos, rect):
    return (mousePos[0] >= rect[0] and mousePos[1] >= rect[1] and mousePos[0] < (rect[0]+rect[2]) and mousePos[1] < (rect[1]+rect[3]))