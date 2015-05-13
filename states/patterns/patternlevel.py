import pygame
import math
import random
from gi.repository import Gtk

from gamestate import *

# Class used to store data about a shape
# so that it may be compared to others
class PatternLevel:
    
    def __init__(self, patState):
        self.patState = patState
        self.question = ""
        self.shapes = []
        self.shapeAnswer = -1
        self.reasons = []
        self.reasonAnswer = -1
        
        self.reset()
        pass
    
    def reset(self):
        self.done = False
        self.addScore = 0
        self.checkHighlighted = False
        self.contHighlighted = False
        self.answerSubmitted = False
        self.shapeSelected = -1
        self.reasonSelected = -1
    
    def set_question(self, question):
        self.question = question
    def add_shape(self, shape):
        self.shapes.append(shape)
    def add_reason(self, reason):
        self.reasons.append(reason)
    
    def update(self):
        if(self.shapeSelected != -1 and self.reasonSelected != -1 and self.checkHighlighted and pygame.mouse.get_pressed()[0] and not self.answerSubmitted):
            self.answerSubmitted = True
            if(self.reasonSelected == self.reasonAnswer): self.addScore += 50
            if(self.shapeSelected == self.shapeAnswer): self.addScore += 50
        if(self.contHighlighted and pygame.mouse.get_pressed()[0]):
          self.done = True
    
    def draw(self, screen):
        if(not self.answerSubmitted):
            self.draw_level(screen)
        else:
            self.draw_submit(screen)
    
    def draw_submit(self,screen):
        labelfont = pygame.font.SysFont(None, 36)
        font = pygame.font.SysFont(None, 32)
        width = screen.get_width()
        height = screen.get_height()
        centerY = height/3
        color = [120,120,120]
        mousePos = pygame.mouse.get_pos()
        
        # draw background
        pygame.draw.rect(screen, [200,200,200], [width/2-300, centerY-200,600,350])
        draw_cen_text("Correct Answer:", screen, labelfont, [0,0,0], [width/2, centerY -170])
        
        # draw correct shape
        shape = self.shapes[self.shapeAnswer]
        shape.draw_shape(screen, color , width/2, centerY-90, 30)
        draw_cen_text(shape.name, screen, font, color, [width/2, centerY-40])
        
        # draw correct answer
        draw_cen_text("Reason:", screen, labelfont, [0,0,0], [width/2, centerY - 0])
        draw_cen_text(self.reasons[self.reasonAnswer], screen, font, color, [width/2, centerY + 40])
        
        # draw red or green based on submission and awarded points
        
        
        # draw added score
        draw_cen_text("+" + str(self.addScore), screen, labelfont, [128,128,0], [width/2, centerY + 100])
        # draw total score
        draw_cen_text("Total: " + str(self.addScore + self.patState.score), screen, labelfont, [128,128,0], [width/2, centerY + 120])
        
        # draw next level button
        contText = "Continue"
        contBlit = font.render(contText, True, [0,0,0])
        contTextDim = font.size(contText)
        contRect = [width/2-contTextDim[0]/2-10, centerY + 50 + len(self.reasons)*(contTextDim[1]+15) + 15, contTextDim[0]+20, contTextDim[1]+20]
        
        contBGColor = [200,200,200]
        if(mouse_in_rect(mousePos,contRect)):
            contBGColor = [0,240,240]
            self.contHighlighted = True
        else:
            self.contHighlighted = False
        pygame.draw.rect(screen, contBGColor, contRect)
        screen.blit(contBlit, [width/2 - contTextDim[0]/2, contRect[1]+10]) 
        
        pass
    
    def draw_level(self, screen):
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
        checkTextDim = font.size(checkText)
        checkRect = [width/2-checkTextDim[0]/2-10, centerY + 170 + len(self.reasons)*(checkTextDim[1]+15) + 15, checkTextDim[0]+20, checkTextDim[1]+20]
        
        checkBGColor = [200,200,200]
        checkTextColor = [0,0,0]
        if(self.shapeSelected == -1 or self.reasonSelected == -1):
            checkBGColor = [80,80,80]
            checkTextColor = [200,200,200]
        elif(mouse_in_rect(mousePos,checkRect)):
            checkBGColor = [0,240,240]
            self.checkHighlighted = True
        else:
            self.checkHighlighted = False
        checkBlit = font.render(checkText, True, checkTextColor)
        pygame.draw.rect(screen, checkBGColor, checkRect)
        screen.blit(checkBlit, [width/2 - checkTextDim[0]/2, checkRect[1]+10]) 

        pass
    
def draw_cen_text(text, screen, font, color, pos):
    dim = font.size(text)
    ren = font.render(text, True, color)
    screen.blit(ren, [pos[0] - dim[0]/2, pos[1] - dim[1]/2])

def mouse_in_rect(mousePos, rect):
    return (mousePos[0] >= rect[0] and mousePos[1] >= rect[1] and mousePos[0] < (rect[0]+rect[2]) and mousePos[1] < (rect[1]+rect[3]))
