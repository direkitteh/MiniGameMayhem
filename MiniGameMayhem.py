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
    #title screen
    fractionsTitle = pygame.image.load("fractionstitle.png")
    titleButtons = ["startButton", "howToPlay"]
    #startButton
    startButtonScalerOrig = .5
    startButtonScaler = startButtonScalerOrig
    startButtonOrig = pygame.image.load("startbutton.png")
    startButton = startButtonOrig
    #self.scaleStartButtonNow()
    #TODO: delete this line below this, the uber long one
    #startButton = pygame.transform.scale(startButtonOrig, (int(round(startButtonOrig.get_width()*startButtonScalerOrig)), int(round(startButtonOrig.get_height()*startButtonScalerOrig))))
    
    #howToPlayButton
    howToPlayButtonScalerOrig = .5
    howToPlayButtonScaler = howToPlayButtonScalerOrig
    howToPlayButtonOrig = pygame.image.load("howToPlayButton.png")
    howToPlayButton = howToPlayButtonOrig
    #self.scaleHowToPlayButtonNow()
    #TODO: delete the line below this, the uber long one
    #howToPlayButton = pygame.transform.scale(howToPlayButtonOrig, (int(round(howToPlayButtonOrig.get_width()*howToPlayButtonScalerOrig)), int(round(howToPlayButtonOrig.get_height()*howToPlayButtonScalerOrig))))
    selectedObjectId = 0
    #selected button increasingOrNot
    buttonIncreasingOrNot = True
    #difficulty screen
    difficultyButtons = ["easy", "medium", "hard", "back"]
    #howToPlay screen
    howToPlayButtons = ["back"]
    #screens: title, howToPlay, difficulty, playing
    menuScreens = ["title", "howToPlay", "difficulty"]
    currentScreen = "title"
    currentMenuSize = len(titleButtons)

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
        self.scaleStartButtonNow()
        self.scaleHowToPlayButtonNow()

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
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    return
#                elif event.type == pygame.VIDEORESIZE:
#                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
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

            #handle events
            handled = self.handleEvents()
            if handled == "quit":
                return

            # Clear Display
            screen.fill((2, 120, 120))  # 255 for white

            # Draw the ball
            #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

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

            #self.currentScreen = "title" #for now

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
                self.animateObject()

                #display start button
                screen.blit(self.startButton,\
                    (int(round(screen.get_width()/2 - self.startButton.get_width()/2)),\
                        int(round(screen.get_height()/2 - self.startButton.get_height()/2)) \
                    )\
                )
                #display howToPlay button
                screen.blit(self.howToPlayButton,\
                    (int(round(screen.get_width()/2 - self.howToPlayButton.get_width()/2)),\
                        int(round(screen.get_height()/1.6 - self.howToPlayButton.get_height()/2)) \
                    )\
                )
            elif(self.currentScreen == "difficulty"): #TODO: this
                #difficulty background
                #TODO: blit difficulty background
                #TODO: blit 3 difficulty buttons
                pass

            elif(self.currentScreen == "howToPlay"): #TODO: this
                #howtoplay background
                #blit background
                #blit 3 difficulty buttons
                pass

            #print("screenwidth IS : " + str(screen.get_width()))
            #print("screenheighti is : " + str(screen.get_height()))
            #img = pygame.transform.scale(img,(40,50)) #doesnt work
            #print(type(img.get_width))
            #print("width = " + str(img.get_width()))
            #print("height = " + str(img.get_height()))
            #print(type(img))

            #debug tools
            debugOrNot = True
            if debugOrNot:
                self.doTheDebugThing(screen)

            # Flip Display (Update the full display Surface to the screen)
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)

    def doTheDebugThing(e, screen):
        try:
            myfont = pygame.font.SysFont("monospace", 15)
            lab = myfont.render("selectedObjectId: " + str(e.selectedObjectId), 1, (255,255,0))
            screen.blit(lab, (100,100))
            lab2 = myfont.render("currentScreen: " + e.currentScreen, 1, (255,255,0))
            screen.blit(lab2, (100,80))
            lab3 = myfont.render("the selected button: " + \
                e.getCurrentButtons()[e.selectedObjectId], 1, (255,255,0))
            screen.blit(lab3, (100,120))
        except:
            print("ERROR LOLOLOL GIT GUD")
            pass

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

    def animateObject(e):
        #titleButtons
        #currentScreen
        if e.currentScreen == "title":
            if(e.getCurrentButtons()[e.selectedObjectId] == "startButton"): #if selected is startButton
                e.animateStartButton()
            elif(e.getCurrentButtons()[e.selectedObjectId] == "howToPlay"): #if selected is How To Play
                e.animateHowToPlayButton()

    def animateStartButton(e):
        if(e.startButtonScaler >= .75):
            e.buttonIncreasingOrNot = False
        elif(e.startButtonScaler <= .50):
            e.buttonIncreasingOrNot = True
        if(e.buttonIncreasingOrNot):
            e.startButtonScaler += .005
        else:
            e.startButtonScaler -= .005
        e.scaleStartButtonNow()

    def scaleStartButtonNow(e):
        e.startButton = pygame.transform.scale(e.startButtonOrig,\
            (int(round(e.startButtonOrig.get_width() * e.startButtonScaler)), \
                int(round(e.startButtonOrig.get_height() * e.startButtonScaler))\
            )\
        )

    def animateHowToPlayButton(e):
        if(e.howToPlayButtonScaler >= .75):
            e.buttonIncreasingOrNot = False
        elif(e.howToPlayButtonScaler <= .50):
            e.buttonIncreasingOrNot = True
        if(e.buttonIncreasingOrNot):
            e.howToPlayButtonScaler += .005
        else:
            e.howToPlayButtonScaler -= .005
        e.scaleHowToPlayButtonNow()

    def scaleHowToPlayButtonNow(e):
        e.howToPlayButton = pygame.transform.scale(e.howToPlayButtonOrig,\
            (int(round(e.howToPlayButtonOrig.get_width() * e.howToPlayButtonScaler)), \
                int(round(e.howToPlayButtonOrig.get_height() * e.howToPlayButtonScaler))\
            )\
        )

    def handleEvents(e):
        for event in pygame.event.get():
            #print("event: " + str(event))
            #print("event in events")
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode(event.size, pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                #print("pygame.keydown done")
                if event.key == pygame.K_DOWN:
                    e.kDownPressed()
                elif event.key == pygame.K_UP:
                    e.kUpPressed()
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    e.kEnterPressed()

    def kDownPressed(e):
        #print("downpressed")
        if e.isMenuScreen():
            e.resetCurrentMenuItemSize()
            e.increasingOrNot = True
            e.selectedObjectId += 1
            if(e.selectedObjectId >= len(e.getCurrentButtons())):
                e.selectedObjectId = 0

    def getCurrentButtons(e):
        if e.currentScreen == "title":
            return e.titleButtons
        elif e.currentScreen == "difficulty":
            return e.difficultyButtons
        elif e.currentScreen == "howToPlay":
            return e.howToPlayButtons

    def resetCurrentMenuItemSize(e):
        if e.currentScreen == "title":
            if(e.titleButtons[e.selectedObjectId] == "startButton"): #if selected is startButton
                e.startButtonScaler = e.startButtonScalerOrig
                e.scaleStartButtonNow()
            elif(e.titleButtons[e.selectedObjectId] == "howToPlay"): #if selected is How To Play
                e.howToPlayButtonScaler = e.howToPlayButtonScalerOrig
                e.scaleHowToPlayButtonNow()

    def isMenuScreen(e):
        if e.currentScreen in e.menuScreens:
            return True
        else:
            return False

    def kUpPressed(e):
        #print("uppressed")
        if e.isMenuScreen():
            e.resetCurrentMenuItemSize()
            e.increasingOrNot = True
            #print("subtracting 1")
            e.selectedObjectId -= 1
            if(e.selectedObjectId < 0):
                #print("len of title buttons: " + str(len(e.titleButtons)))
                e.selectedObjectId = len(e.getCurrentButtons()) - 1

    def kEnterPressed(e):
        #print("enterpressed")
        if e.currentScreen == "title":
            if e.getCurrentButtons()[e.selectedObjectId] == "howToPlay":
                e.switchToScreen("howToPlay")
            elif e.getCurrentButtons()[e.selectedObjectId] == "startButton":
                e.switchToScreen("difficulty")

    def switchToScreen(e, theScreen):
        e.currentScreen = theScreen
        e.selectedObjectId = 0
        if(theScreen in e.menuScreens):
            if theScreen == "title":
                e.currentMenuSize = len(e.titleButtons)
            elif theScreen == "howToPlay":
                e.currentMenuSize = len(e.howToPlayButtons)
            elif theScreen == "difficulty":
                e.currentMenuSize = len(e.difficultyButtons)
        else:
            e.currentMenuSize = -1

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