import pygame
import math
import random
from gi.repository import Gtk

from gamestate import *

# Class used to store data about a shape
# so that it may be compared to others
class PatternLevel:
    
    def __init__(self):
        self.question = ""
        self.shapes = []
        self.shapeAnswer = -1
        self.reasons = []
        self.reasonAnswer = -1
        
        self.shapeSelected = -1
        self.reasonSelected = -1
        self.checkHighlighted = False
        pass
    
    def set_question(self, question):
        self.question = question
    def add_shape(self, shape):
        self.shapes.append(shape)
    def add_reason(self, reason):
        self.reasons.append(reason)
    
    def update(self):
        if(self.checkHighlighted and pygame.mouse.get_pressed()[0]):
            #boop = ""
            pass
    
    def draw(self, screen):
        font = pygame.font.SysFont(None, 32)
        selectedFont = pygame.font.SysFont(None, 32)
        selectedFont.set_underline(True)
        
        mousePos = pygame.mouse.get_pos()
        
        width = screen.get_width()
        height = screen.get_height()
        centerY = height/4;
        
        
        # Static text
        whyText = font.render("and why?", True, [0,0,0])
        screen.blit(whyText, [width/2 - font.size("and why?")[0]/2, centerY + 120]);
        
        qText = font.render(self.question, True, [0,0,0])
        screen.blit(qText, [width/2 - font.size(self.question)[0]/2, centerY - 100]);
        
        
        # Selected shape box
        selectedShapeBoxWidth = 250
        pygame.draw.rect(screen, [0,0,0], [width/2-selectedShapeBoxWidth/2,centerY + 70,selectedShapeBoxWidth,font.size("M")[1]+6], 2)
        
        # Shape drawing
        shapeSpacing = 120
        shapePosX = width/2 - 120.0*(len(self.shapes)-1)/2.0;
        shapePosY = centerY;
        
        printedName = "" # Name of shape selected to draw in box
        for i in range(len(self.shapes)):
            posX = shapePosX + i*shapeSpacing
            rect = [posX-shapeSpacing/2+10, shapePosY-shapeSpacing/2+10, shapeSpacing-20,shapeSpacing-20]
            
            shapeColor = [0,0,0]
            bgColor = [200,200,200]
            
            highlighted = mouse_in_rect(mousePos, rect)
            selected = self.shapeSelected
            
            if(self.shapeSelected == i):
                shapeColor = [255,255,0]
                if(printedName == ""): printedName = self.shapes[i].name
            if(mouse_in_rect(mousePos, rect)):
                bgColor = [0,240,240]
                printedName = self.shapes[i].name # Being highlighted overrides being selected
                if(pygame.mouse.get_pressed()[0]):
                    self.shapeSelected = i
            
            pygame.draw.rect(screen, bgColor, rect) # background
            self.shapes[i].draw_shape(screen, shapeColor, posX, shapePosY, 30)
        
        # Draw name in box of selected shape
        name = font.render(printedName, True, [0,0,0])
        nameSize = font.size(printedName)
        screen.blit(name, [width/2 - nameSize[0]/2, centerY+73])
        
        # Reasons drawing
        for i in range(len(self.reasons)) :
            size = font.size(self.reasons[i]);
            yPos = centerY + 170 + i*(size[1]+15)
            rect = [0, yPos-3, width, size[1]+6]
            
            textColor = [0,0,0]
            bgColor = [200,200,200]
            
            if(self.reasonSelected == i):
                textColor = [255,255,0]
            if(mouse_in_rect(mousePos, rect)):
                bgColor = [0,240,240]
                if(pygame.mouse.get_pressed()[0]):
                    self.reasonSelected = i
            res = font.render(self.reasons[i], True, textColor)
            pygame.draw.rect(screen, bgColor, rect) # background
            screen.blit(res, [width/2 - size[0]/2, yPos])
        
        pygame.draw.line(screen, (0,0,0), (width/2,0), (width/2,height)) # centering lines
        pygame.draw.line(screen, (0,0,0), (0,centerY), (width,centerY))

        # submit button
        checkText = "Check Answer"
        checkBlit = font.render(checkText, True, [0,0,0])
        checkTextDim = font.size(checkText)
        checkRect = [width/2-checkTextDim[0]/2-10, centerY + 170 + len(self.reasons)*(checkTextDim[1]+15) + 15, checkTextDim[0]+20, checkTextDim[1]+20]
        
        checkBGColor = [200,200,200]
        if(mouse_in_rect(mousePos,checkRect)):
            checkBGColor = [0,240,240]
            self.checkHighlighted = True
        else:
            self.checkHighlighted = False
        pygame.draw.rect(screen, checkBGColor, checkRect)
        screen.blit(checkBlit, [width/2 - checkTextDim[0]/2, checkRect[1]+10]) 

        pass

def mouse_in_rect(mousePos, rect):
    return (mousePos[0] >= rect[0] and mousePos[1] >= rect[1] and mousePos[0] < (rect[0]+rect[2]) and mousePos[1] < (rect[1]+rect[3]))
