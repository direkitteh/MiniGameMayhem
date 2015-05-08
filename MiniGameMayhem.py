#!/usr/bin/python
import pygame
import random
from gi.repository import Gtk
from fraction import Fraction


class MiniGameMayhem:
    #global variables
    possibleX = [0,1,2,3,5,7,9,11,13,17,19,23]
    possibleY = [1,2,3,5,7,9,11,13,17,19,23]
    tempNumFracToPrint = 4
    tempNumPrinted = 0;

    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = False
        self.direction = 1

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1

            # Move the ball
            if not self.paused:
                self.x += self.vx * self.direction
                if self.direction == 1 and self.x > screen.get_width() + 100:
                    self.x = -100
                elif self.direction == -1 and self.x < -100:
                    self.x = screen.get_width() + 100

                self.y += self.vy
                if self.y > screen.get_height() - 100:
                    self.y = screen.get_height() - 100
                    self.vy = -self.vy

                self.vy += 5

            # Clear Display
            screen.fill((255, 255, 255))  # 255 for white

            # Draw the ball
            pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

            #make the fraction
            level = 1 #for now
            while(self.tempNumPrinted < self.tempNumFracToPrint):
                theFraction = self.makeFraction(level)
                self.drawFraction(theFraction)
                level = 2
                theFraction = self.makeFraction(level)
                self.drawFraction(theFraction)
                level = 3
                theFraction = self.makeFraction(level)
                self.drawFraction(theFraction)
                self.tempNumPrinted += 1
                level = 1

            #img=pygame.image.load("whiteboard.jpg")
            #screen.blit(img,(12,12))
            #img = pygame.transform.scale(img,(40,50))
            #print(type(img.get_width))
            #print("width = " + str(img.get_width()))
            #print("height = " + str(img.get_height()))
            #print(type(img))

            # Flip Display (Update the full display Surface to the screen)
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)

    def makeFraction(e, level):
        #reference for possibleX/Y. See actual value at beginning of class
        #possibleX = [0,1,2,3,5,7,9,11,13,17,19,23]
        #possibleY = [1,2,3,5,7,9,11,13,17,19,23]
        print("level is : " + str(level))
        simpX = -1
        simpY = -1
        unSimpX = -1
        unSimpY = -1
        if (level == 1):
            simpX = e.possibleX[random.randint(1,3)]
            simpY = e.possibleY[random.randint(0,2)]
            unSimpX = random.randint(2,3) * simpX
            unSimpY = random.randint(2,3) * simpY
        elif (level == 2):
            simpX = e.possibleX[random.randint(0,6)]
            simpY = e.possibleY[random.randint(0,5)]
            unSimpX = random.randint(2,4) * simpX
            unSimpY =  random.randint(2,4) * simpY
        elif (level == 3):
            simpX = e.possibleX[random.randint(4,7)]
            simpY = e.possibleY[random.randint(4,7)]
            unSimpX = random.randint(2,10) * simpX
            unSimpY =  random.randint(2,10) * simpY
        #create Fraction
        theFraction = Fraction()
        theFraction.simpX = simpX
        theFraction.simpY = simpY
        theFraction.unSimpX = unSimpX
        theFraction.unSimpY = unSimpY
        return theFraction

    #TODO: finish this rather than just print the values
    def drawFraction(e, theFraction):
        print("theFraction.simpX = " + str(theFraction.simpX))
        print("theFraction.simpY = " + str(theFraction.simpY))
        print("theFraction.unSimpX = " + str(theFraction.unSimpX))
        print("theFraction.unSimpY = " + str(theFraction.unSimpY))
        pass

# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = MiniGameMayhem()
    game.run()

if __name__ == '__main__':
    main()