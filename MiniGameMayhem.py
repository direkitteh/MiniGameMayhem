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
    fractionsTitle = pygame.image.load("fractionimages/fractionstitle.png")
    titleButtons = ["startButton", "howToPlay"]
    #startButton
    startButtonScalerOrig = .5
    startButtonScaler = startButtonScalerOrig
    startButtonOrig = pygame.image.load("fractionimages/startbutton.png")
    startButton = startButtonOrig
    #self.scaleStartButtonNow()
    #TODO: delete this line below this, the uber long one
    #startButton = pygame.transform.scale(startButtonOrig, (int(round(startButtonOrig.get_width()*startButtonScalerOrig)), int(round(startButtonOrig.get_height()*startButtonScalerOrig))))
    
    #howToPlayButton
    howToPlayButtonScalerOrig = .5
    howToPlayButtonScaler = howToPlayButtonScalerOrig
    howToPlayButtonOrig = pygame.image.load("fractionimages/howToPlayButton.png")
    howToPlayButton = howToPlayButtonOrig
    #self.scaleHowToPlayButtonNow()
    #TODO: delete the line below this, the uber long one
    #howToPlayButton = pygame.transform.scale(howToPlayButtonOrig, (int(round(howToPlayButtonOrig.get_width()*howToPlayButtonScalerOrig)), int(round(howToPlayButtonOrig.get_height()*howToPlayButtonScalerOrig))))
    selectedObjectId = 0
    #if the selected buttonIncreasing Or Not
    buttonIncreasingOrNot = True
    #difficulty screen
    difficultyButtons = ["easy", "medium", "hard", "back"]
    easyButtonScalerOrig = .65
    easyButtonScaler = easyButtonScalerOrig
    easyButtonOrig = pygame.image.load("fractionimages/easy.png")
    easyButton = easyButtonOrig
    mediumButtonScalerOrig = .65
    mediumButtonScaler = mediumButtonScalerOrig
    mediumButtonOrig = pygame.image.load("fractionimages/medium.png")
    mediumButton = mediumButtonOrig
    hardButtonScalerOrig = .65
    hardButtonScaler = hardButtonScalerOrig
    hardButtonOrig = pygame.image.load("fractionimages/hard.png")
    hardButton = hardButtonOrig
    backButtonScalerOrig = .5
    backButtonScaler = backButtonScalerOrig
    backButtonOrig = pygame.image.load("fractionimages/back.png")
    backButton = backButtonOrig

    #howToPlay screen
    howToPlayButtons = ["back"]
    #screens: title, howToPlay, difficulty, playing
    menuScreens = ["title", "howToPlay", "difficulty"]
    currentScreen = "title"
    prevScreen = "title"
    currentMenuSize = len(titleButtons)
    debugErrorOnePrinted = False
    startPrintY = 160 #TEMPORARY TO PRINT FRACTIONS AS TEXT IN GAME
    fractionsToDraw = []

    theScreen = None

    debugPrintLoc = 100

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
        self.scaleAllButtonsNow()

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
        self.theScreen = screen

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

            #self.currentScreen = "title" #for now

            #print("THESCREEN IS!!!!!!!!    " + str(type(self.theScreen)))

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
            elif(self.currentScreen == "difficulty"):
                self.animateObject()
                screen.blit(self.easyButton,\
                    (int(round(screen.get_width()/2 - self.easyButton.get_width()/2)),\
                        int(round(screen.get_height()/5 - self.easyButton.get_height()/2))
                    )\
                )
                screen.blit(self.mediumButton,\
                    (int(round(screen.get_width()/2 - self.mediumButton.get_width()/2)),\
                        int(round(screen.get_height()/4 + 100 - self.mediumButton.get_height()/2))
                    )\
                )
                screen.blit(self.hardButton,\
                    (int(round(screen.get_width()/2 - self.hardButton.get_width()/2)),\
                        int(round(screen.get_height()/3 + 200 - self.hardButton.get_height()/2))
                    )\
                )
                screen.blit(self.backButton,\
                    (int(round(screen.get_width()/2 - self.backButton.get_width()/2)),\
                        int(round(screen.get_height()/1.2 - self.backButton.get_height()/2))
                    )\
                )
            elif(self.currentScreen == "howToPlay"):
                self.animateObject()
                screen.blit(self.backButton,\
                    (int(round(screen.get_width()/2 - self.backButton.get_width()/2)),\
                        int(round(screen.get_height()/1.2 - self.backButton.get_height()/2))
                    )\
                )
            elif self.currentScreen == "easy" or \
                self.currentScreen == "medium" or \
                    self.currentScreen == "hard":
                if self.currentScreen == "easy":
                    level = 1
                elif self.currentScreen == "medium":
                    level = 2
                elif self.currentScreen == "hard":
                    level = 3
                else:
                    print("error, currentScreen not providing level properly")
                #make the fraction
                #level = 1 #for now
                self.startPrintY = 160 #TODO: for now
                while(self.tempNumPrinted < self.tempNumFracToPrint):
                    print("level is: " + str(level))
                    theFraction = self.makeFraction(level)
                    self.fractionsToDraw.append(theFraction)
                    #self.drawFraction(theFraction, screen)
                    #level = 2
                    #theFraction = self.makeFraction(level)
                    #self.drawFraction(theFraction)
                    #level = 3
                    #theFraction = self.makeFraction(level)
                    #self.drawFraction(theFraction)
                    self.tempNumPrinted += 1
                    #level = 1
                for aFrac in self.fractionsToDraw:
                    self.drawFraction(aFrac, screen)
            #print("screenwidth IS : " + str(screen.get_width()))
            #print("screenheighti is : " + str(screen.get_height()))
            #img = pygame.transform.scale(img,(40,50)) #doesnt work
            #print(type(img.get_width))
            #print("width = " + str(img.get_width()))
            #print("height = " + str(img.get_height()))
            #print(type(img))

            #debug tools
            debugOrNot = True
            tryCatchOrNot = True
            self.debugPrintLoc = 100
            if debugOrNot:
                self.doTheDebugThing(tryCatchOrNot)

            # Flip Display (Update the full display Surface to the screen)
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)

    def doTheDebugThing(e, tryCatchOrNot):
        if (tryCatchOrNot):
            try:
                e.actuallyDoTheDebugThing()
            except:
                if(not e.debugErrorOnePrinted):
                    print("ERROR LOLOLOL GIT GUD")
                e.debugErrorOnePrinted = True
        else:
            e.actuallyDoTheDebugThing()

    def actuallyDoTheDebugThing(e):
        #print("actuallydoingthedebug thing woooot")
        e.debugPrint("selectedObjectId" ,e.selectedObjectId)
        e.debugPrint("currentScreen" , e.currentScreen)
        e.debugPrint("the selected button" ,e.getCurrentButtons()[e.selectedObjectId])
        e.debugPrint("buttonIncreasingOrNot",e.buttonIncreasingOrNot)
        e.debugPrint("easyButtonScaler",e.easyButtonScaler)
#        myfont = pygame.font.SysFont("monospace", 15)
#        lab = myfont.render("selectedObjectId: " + str(e.selectedObjectId), 1, (255,255,0))
#        screen.blit(lab, (100,100))
#        lab2 = myfont.render("currentScreen: " + e.currentScreen, 1, (255,255,0))
#        screen.blit(lab2, (100,80))
#        lab3 = myfont.render("the selected button: " + \
#            e.getCurrentButtons()[e.selectedObjectId], 1, (255,255,0))
#        screen.blit(lab3, (100,120))
#        lab5 = myfont.render("buttonIncreasingOrNot: " + \
#            str(e.buttonIncreasingOrNot), 1, (255,255,0))
#        screen.blit(lab5, (100,160))
#        lab4 = myfont.render("easyButtonScaler: " + \
#            str(e.easyButtonScaler), 1, (255,255,0))
#        screen.blit(lab4, 1, (100,140))

    def debugPrint(e, strTitle, valueToPrint):
        #print("DEBUG PIRITNG!!! W5555555555555555t")
        myfont = pygame.font.SysFont("monospace", 15)
        ahaha = myfont.render("" + strTitle + ": " + str(valueToPrint), 1, (255,255,0))
        #print("###### thescreen" + str(type(e.theScreen)))
        e.theScreen.blit(ahaha, (100, e.debugPrintLoc))
        e.debugPrintLoc += 20

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
    def drawFraction(e, theFraction, theScreen):
        bla1 = "theFraction.simpX = " + str(theFraction.simpX)
        bla2 = "theFraction.simpY = " + str(theFraction.simpY)
        bla3 = "theFraction.unSimpX = " + str(theFraction.unSimpX)
        bla4 = "theFraction.unSimpY = " + str(theFraction.unSimpY)
        myfont = pygame.font.SysFont("monospace", 22)
        lab1 = myfont.render(bla1, 1, (255,255,0))
        lab2 = myfont.render(bla2, 1, (255,255,0))
        lab3 = myfont.render(bla3, 1, (255,255,0))
        lab4 = myfont.render(bla4, 1, (255,255,0))
        theScreen.blit(lab1, (200,e.startPrintY))
        e.startPrintY += 20
        theScreen.blit(lab2, (200,e.startPrintY))
        e.startPrintY += 20
        theScreen.blit(lab3, (200,e.startPrintY))
        e.startPrintY += 20
        theScreen.blit(lab4, (200,e.startPrintY))
        e.startPrintY += 20

    def animateObject(e):
        #titleButtons
        #currentScreen
        #if e.currentScreen == "title":
        #print("hereA")
        theCurrentButtons = e.getCurrentButtons()
        #print("WHATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        #print("printingTHEOIAUSERIVUAWEIORJACWOIEJRCURRENTBUTTONS!!")
        #print(theCurrentButtons)
        if(theCurrentButtons[e.selectedObjectId] == "startButton"): #if selected is startButton
            #print("hereB")
            e.animateStartButton()
        elif(theCurrentButtons[e.selectedObjectId] == "howToPlay"): #if selected is How To Play
            #print("hereC")
            e.animateHowToPlayButton()
        elif(theCurrentButtons[e.selectedObjectId] == "easy"):
            #print("woohooD")
            e.animateEasyButton()
        elif(theCurrentButtons[e.selectedObjectId] == "medium"):
            #print("hereE")
            e.animateMediumButton()
        elif(theCurrentButtons[e.selectedObjectId] == "hard"):
            #print("hereF")
            e.animateHardButton()
        elif(theCurrentButtons[e.selectedObjectId] == "back"):
            #print("hereG")
            e.animateBackButton()

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

    def animateEasyButton(e):
        #print("here1")
        if(e.easyButtonScaler >= .85):
            #print("here2")
            e.buttonIncreasingOrNot = False
        elif(e.easyButtonScaler <= .65):
            #print("here3")
            e.buttonIncreasingOrNot = True
        if(e.buttonIncreasingOrNot == True):
            #print("here4")
            e.easyButtonScaler += .005
        elif(e.buttonIncreasingOrNot == False):
            #print("here5")
            e.easyButtonScaler -= .005
        e.scaleEasyButtonNow()

    def animateMediumButton(e):
        if(e.mediumButtonScaler >= .85):
            e.buttonIncreasingOrNot = False
        elif(e.mediumButtonScaler <= .65):
            e.buttonIncreasingOrNot = True
        if(e.buttonIncreasingOrNot):
            e.mediumButtonScaler += .005
        else:
            e.mediumButtonScaler -= .005
        e.scaleMediumButtonNow()

    def animateHardButton(e):
        if(e.hardButtonScaler >= .85):
            e.buttonIncreasingOrNot = False
        elif(e.hardButtonScaler <= .65):
            e.buttonIncreasingOrNot = True
        if(e.buttonIncreasingOrNot):
            e.hardButtonScaler += .005
        else:
            e.hardButtonScaler -= .005
        e.scaleHardButtonNow()

    def animateBackButton(e):
        if(e.backButtonScaler >= .75):
            e.buttonIncreasingOrNot = False
        elif(e.backButtonScaler <= .50):
            e.buttonIncreasingOrNot = True
        if(e.buttonIncreasingOrNot):
            e.backButtonScaler += .005
        else:
            e.backButtonScaler -= .005
        e.scaleBackButtonNow()

    def scaleAllButtonsNow(e):
        e.scaleStartButtonNow()
        e.scaleHowToPlayButtonNow()
        e.scaleEasyButtonNow()
        e.scaleMediumButtonNow()
        e.scaleHardButtonNow()
        e.scaleBackButtonNow()

    def scaleStartButtonNow(e):
        e.startButton = pygame.transform.scale(e.startButtonOrig,\
            (int(round(e.startButtonOrig.get_width() * e.startButtonScaler)), \
                int(round(e.startButtonOrig.get_height() * e.startButtonScaler))\
            )\
        )

    def scaleHowToPlayButtonNow(e):
        e.howToPlayButton = pygame.transform.scale(e.howToPlayButtonOrig,\
            (int(round(e.howToPlayButtonOrig.get_width() * e.howToPlayButtonScaler)), \
                int(round(e.howToPlayButtonOrig.get_height() * e.howToPlayButtonScaler))\
            )\
        )

    def scaleEasyButtonNow(e):
        e.easyButton = pygame.transform.scale(e.easyButtonOrig,\
            (int(round(e.easyButtonOrig.get_width() * e.easyButtonScaler)), \
                int(round(e.easyButtonOrig.get_height() * e.easyButtonScaler))\
            )\
        )

    def scaleMediumButtonNow(e):
        e.mediumButton = pygame.transform.scale(e.mediumButtonOrig,\
            (int(round(e.mediumButtonOrig.get_width() * e.mediumButtonScaler)), \
                int(round(e.mediumButtonOrig.get_height() * e.mediumButtonScaler))\
            )\
        )

    def scaleHardButtonNow(e):
        e.hardButton = pygame.transform.scale(e.hardButtonOrig,\
            (int(round(e.hardButtonOrig.get_width() * e.hardButtonScaler)), \
                int(round(e.hardButtonOrig.get_height() * e.hardButtonScaler))\
            )\
        )

    def scaleBackButtonNow(e):
        e.backButton = pygame.transform.scale(e.backButtonOrig,\
            (int(round(e.backButtonOrig.get_width() * e.backButtonScaler)), \
                int(round(e.backButtonOrig.get_height() * e.backButtonScaler))\
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
            e.buttonIncreasingOrNot = True
            e.selectedObjectId += 1
            if(e.selectedObjectId >= len(e.getCurrentButtons())):
                e.selectedObjectId = 0

    def getCurrentButtons(e):
        if e.currentScreen == "title":
            return e.titleButtons
        elif e.currentScreen == "difficulty":
            #print("printing diff buttons below")
            #print(e.difficultyButtons)
            return e.difficultyButtons
        elif e.currentScreen == "howToPlay":
            return e.howToPlayButtons

    def resetCurrentMenuItemSize(e):
        curMenuItem = e.getCurrentButtons()[e.selectedObjectId]
        if curMenuItem == "startButton":
            e.startButtonScaler = e.startButtonScalerOrig
            e.scaleStartButtonNow()
        elif curMenuItem == "howToPlay":
            e.howToPlayButtonScaler = e.howToPlayButtonScalerOrig
            e.scaleHowToPlayButtonNow()
        elif curMenuItem == "easy":
            e.easyButtonScaler = e.easyButtonScalerOrig
            e.scaleEasyButtonNow()
        elif curMenuItem == "medium":
            e.mediumButtonScaler = e.mediumButtonScalerOrig
            e.scaleMediumButtonNow()
        elif curMenuItem == "hard":
            e.hardButtonScaler = e.hardButtonScalerOrig
            e.scaleHardButtonNow()
        elif curMenuItem == "back":
            e.backButtonScaler = e.backButtonScalerOrig
            e.scaleBackButtonNow()
        else:
            print("error: curMenuItem not found in resetCurrentMenuItemSize")
        

    def isMenuScreen(e):
        if e.currentScreen in e.menuScreens:
            return True
        else:
            return False

    def kUpPressed(e):
        #print("uppressed")
        if e.isMenuScreen():
            e.resetCurrentMenuItemSize()
            e.buttonIncreasingOrNot = True
            #print("subtracting 1")
            e.selectedObjectId -= 1
            if(e.selectedObjectId < 0):
                #print("len of title buttons: " + str(len(e.titleButtons)))
                e.selectedObjectId = len(e.getCurrentButtons()) - 1

    def kEnterPressed(e):
        #print("enterpressed")
        #if e.currentScreen == "title":
        try:
            if e.getCurrentButtons()[e.selectedObjectId] == "howToPlay":
                e.switchToScreen("howToPlay")
            elif e.getCurrentButtons()[e.selectedObjectId] == "startButton":
                e.switchToScreen("difficulty")
            elif e.getCurrentButtons()[e.selectedObjectId] == "back":
                e.switchToScreen("prev")
            elif e.getCurrentButtons()[e.selectedObjectId] == "easy":
                e.switchToScreen("easy")
            elif e.getCurrentButtons()[e.selectedObjectId] == "medium":
                e.switchToScreen("medium")
            elif e.getCurrentButtons()[e.selectedObjectId] == "hard":
                e.switchToScreen("hard")
        except:
            print("error? enter pressed while playing")

    def switchToScreen(e, theScreen):
        if theScreen == "prev":
            theScreen = e.prevScreen
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