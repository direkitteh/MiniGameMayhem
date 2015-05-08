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
    fractionsTitle = pygame.image.load("fractionstitle.png")
    titleButtons = ["startButton", "howToPlay"]
    startButtonOrig = pygame.image.load("startbutton.png")
    startButton = pygame.image.load("startbutton.png")
    #this is default button scale. the bounds are in animate object function
    startButtonScaler = .5
    buttonIncreasingOrNot = True
    currentScreen = "title"
    selectedObjectId = 0

    startButton = pygame.transform.scale(startButtonOrig,\
        (int(round(startButtonOrig.get_width() * startButtonScaler)), \
            int(round(startButtonOrig.get_height() * startButtonScaler))\
        )\
    )

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
#                elif event.type == pygame.KEYDOWN:
#                    if event.key == pygame.K_LEFT:
#                        self.direction = -1
#                    elif event.key == pygame.K_RIGHT:
#                        self.direction = 1

            # Move the ball
#            if not self.paused:
#                self.x += self.vx * self.direction
#                if self.direction == 1 and self.x > screen.get_width() + 100:
#                    self.x = -100
#                elif self.direction == -1 and self.x < -100:
#                    self.x = screen.get_width() + 100
#
#                self.y += self.vy
#                if self.y > screen.get_height() - 100:
#                    self.y = screen.get_height() - 100
#                    self.vy = -self.vy
#
#                self.vy += 5

            # Clear Display
            screen.fill((255, 255, 255))  # 255 for white

            # Draw the ball
            #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

            #handle events
            self.handleEvents()

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

            self.currentScreen = "title" #for now

            #title screen
            if(self.currentScreen == "title"):
                #title background
                screen.blit(self.fractionsTitle,(0,0))
                #startbutton is 366x108, scaled to 183x54, 
                #print("round blah is: " + str(round(self.startButton.get_height())))

                #print("startbuttonwidth: " + str(self.startButton.get_width()))
                #print("startbuttonheight: " + str(self.startButton.get_height()))
                #if(self.selectedObject == "startButton"):
                #animate selected button
                self.animateObject(self.selectedObjectId)

                #display start button
                screen.blit(self.startButton,\
                    (int(round(screen.get_width()/2 - self.startButton.get_width()/2)),\
                        int(round(screen.get_height()/2 - self.startButton.get_height()/2)) \
                    )\
                )
            elif(self.currentScreen == "difficulty"): #TODO: this
                #difficulty background
                #TODO: blit difficulty background
                #TODO: blit 3 difficulty buttons
                pass

            #print("screenwidth IS : " + str(screen.get_width()))
            #print("screenheighti is : " + str(screen.get_height()))
            #img = pygame.transform.scale(img,(40,50)) #doesnt work
            #print(type(img.get_width))
            #print("width = " + str(img.get_width()))
            #print("height = " + str(img.get_height()))
            #print(type(img))

            # Flip Display (Update the full display Surface to the screen)
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)

    #returns a Fraction object that is created based on the level.
    def makeFraction(e, level):
        #reference for possibleX/Y. See actual value at beginning of class
        #possibleX = [0,1,2,3,5,7,9,11,13,17,19,23]
        #possibleY = [1,2,3,5,7,9,11,13,17,19,23]
        #print("level is : " + str(level))
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
        #print("theFraction.simpX = " + str(theFraction.simpX))
        #print("theFraction.simpY = " + str(theFraction.simpY))
        #print("theFraction.unSimpX = " + str(theFraction.unSimpX))
        #print("theFraction.unSimpY = " + str(theFraction.unSimpY))
        pass

    def animateObject(e, selectedObjectId):
        #titleButtons
        #currentScreen
        if e.currentScreen == "title":
            if(selectedObjectId == 0): #if selected is startButton
                e.animateStartButton()
            elif(selectedObjectId == 1): #if selected is How To Play
                pass #TODO: animate how to play button

    def animateStartButton(e):
        #print("e.startbuttonscaler : " + str(e.startButtonScaler))
        if(e.startButtonScaler >= .75):
            #print("here1")
            e.buttonIncreasingOrNot = False
        elif(e.startButtonScaler <= .50):
            #print("here2")
            e.buttonIncreasingOrNot = True
        if(e.buttonIncreasingOrNot):
            #print("here3")
            e.startButtonScaler += .005
        else:
            #print("here4")
            e.startButtonScaler -= .005
        e.startButton = pygame.transform.scale(e.startButtonOrig,\
            (int(round(e.startButtonOrig.get_width() * e.startButtonScaler)), \
                int(round(e.startButtonOrig.get_height() * e.startButtonScaler))\
            )\
        )

    def handleEvents(e):
        for event in pygame.event.get():
            print("event: " + str(event))
            print("event in events")
            if event.type == pygame.KEYDOWN:
                print("pygame.keydown done")
                if event.key == pygame.K_DOWN:
                    kDownPressed(e)
                if event.key == pygame.K_RETURN or event.key == pygame.K_ENTER:
                    kEnterPressed(e)

    def kDownPressed(e):
        print("downpressed")

    def kEnterPressed(e):
        print("enterpressed")

        #old
#        theButtonScaler = 0.1
#        if(selectedObject == "startButton"):
#            if(e.startButtonScaler > .75):
#                e.startButtonScaler -= .01
#            else:
#                e.startButtonScaler += .01
#            theButtonScaler = e.startButtonScaler
#        theButton = pygame.transform.scale(selectedObject,\
#            (int(round(selectedObjectOrig.get_width() * theButtonScaler)), \
#                int(round(selectedObjectOrig.get_height() * theButtonScaler))\
#            )\
#        )

# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = MiniGameMayhem()
    game.run()

if __name__ == '__main__':
    main()