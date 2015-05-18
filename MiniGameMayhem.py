#!/usr/bin/python
import pygame
import random
from gi.repository import Gtk
from fraction import Fraction
from fractions import gcd


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

    #results screen
    resultsButtons = ["playAgain", "menu"]

    #screens: title, howToPlay, difficulty, playing
    menuScreens = ["title", "howToPlay", "difficulty", "results"]
    currentScreen = "title"
    prevScreen = "title"
    currentMenuSize = len(titleButtons)
    debugErrorOnePrinted = False
    startPrintY = 160 #TEMPORARY TO PRINT FRACTIONS AS TEXT IN GAME
    fractionsToDraw = []

    framerate = 30

    level = None

    theScreen = None

    fractionIsSolved = False
    roundIsInitalized = False

    #in game stuff
    currentScore = 0
    theCurrentFraction = None
    answerScore = None
    currentAnsNumerator = ""
    currentAnsDenominator = ""
    selectedAnsPart = "numerator" #only "numerator" or "denominator"

    #timer stuff
    timerMax = None
    timerCur = None
    gameIsOver = False

    debugPrintLoc = 100
    debugFracOrNot = False

    startButton = pygame.transform.scale(startButtonOrig,\
        (int(round(startButtonOrig.get_width() * startButtonScaler)), \
            int(round(startButtonOrig.get_height() * startButtonScaler))\
        )\
    )

    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        self.paused = False
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

            # Clear Display (fill it with proper color)
            screen.fill((2, 120, 120))

            #handle events
            handled = self.handleEvents()
            if handled == "quit":
                return

            

            #do different things depending on the current screen
            if(self.currentScreen == "title"): #title screen
                #blit the title background
                screen.blit(self.fractionsTitle,(0,0))
                #animate selected button
                self.animateObject()
                #draw the buttons to the screen
                self.drawCurrentButtons()
            elif(self.currentScreen == "difficulty"): #difficulty select screen
                #animate selected button
                self.animateObject()
                #draw the buttons to the screen
                self.drawCurrentButtons()
            elif(self.currentScreen == "howToPlay"): #how to play screen
                #animate selected button
                self.animateObject()
                #draw the buttons to the screen
                self.drawCurrentButtons()
            elif self.currentScreen == "easy" or \
                self.currentScreen == "medium" or \
                    self.currentScreen == "hard":
                if self.currentScreen == "easy":
                    self.level = 1
                elif self.currentScreen == "medium":
                    self.level = 2
                elif self.currentScreen == "hard":
                    self.level = 3
                else:
                    print("error, currentScreen not providing level properly")
                #temporary game display stuff
                self.startPrintY = 160 #TODO: for now
                if (self.debugFracOrNot):
                    while(self.tempNumPrinted < self.tempNumFracToPrint):
                        print("level is: " + str(self.level))
                        theFraction = self.makeFraction()
                        self.fractionsToDraw.append(theFraction)
                        self.tempNumPrinted += 1
                    for aFrac in self.fractionsToDraw:
                        self.drawFraction(aFrac, screen)
                else: #actual game display stuff
                    self.handleGameplay()

            #debug tools. set debugOrNot to True to enable. How to use:
            #set tryCatchOrNot to False if you want debug data able to fail
            #set debugFracOrNot to True to show in game fraction debug info
            debugOrNot = True
            tryCatchOrNot = True
            self.debugPrintLoc = 100
            if debugOrNot:
                self.doTheDebugThing(tryCatchOrNot)
                self.debugFracOrNot = False

            # Flip Display (Update the full display Surface to the screen)
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(self.framerate)

    def handleGameplay(e):
        if(e.gameIsOver):
            e.switchToResultsScreen()
        elif (e.roundIsInitalized == False):
            e.initializeRound()
        elif(e.fractionIsSolved):
            e.fractionWasSolved()
        else:
            e.updateGameState()

    def switchToResultsScreen(e):
        self.currentScreen = "results"

    def initializeRound(e):
        e.newFraction()
        e.gameIsOver = False
        e.fractionIsSolved = False
        e.currentScore = 0
        e.answerScore = e.getMaxAnswerScore()
        e.currentAnsNumerator = ""
        e.currentAnsDenominator = ""
        e.selectedAnsPart = "numerator"
        maxTimeInSec = 60
        e.timerMax = 60 * e.framerate
        e.timerCur = e.timerMax
        #done
        e.roundIsInitalized = True

    def fractionWasSolved(e):
        e.fractionIsSolved = False
        e.currentAnsNumerator = ""
        e.currentAnsDenominator = ""
        e.selectedAnsPart = "numerator"
        e.currentScore += e.answerScore
        e.answerScore = e.getMaxAnswerScore()
        e.newFraction()
        e.updateGameState()

    def updateGameState(e):
        #redraw screen
        e.drawFraction(e.theCurrentFraction, e.theScreen)
        #decay answerScore
        e.answerScore -= .1 * e.level
        if (e.answerScore < (10 * e.level)):
            e.answerScore = 10
        #decay timer by 1 frame
        e.timerCur -= 1
        #check if game is over
        if(e.timerCur <= 0):
            gameIsOver = True
        #redraw more stuff
        myFont = pygame.font.SysFont("monospace", 32)
        answerScoreRender = myFont.render(str(int(round(e.answerScore))), 1, (255,255,0))
        e.theScreen.blit(answerScoreRender, (400,200))
        currentScore = myFont.render("Total Score: " + str(int(round(e.currentScore))), 1, (255,255,0))
        currentTime = myFont.render("Time: " + str(int(round(e.timerCur/e.framerate))), 1, (255,255,0))
        e.theScreen.blit(currentScore, (522, 155))
        e.theScreen.blit(currentTime, (522,105))

    def newFraction(e):
        e.theCurrentFraction = e.makeFraction()

    def getMaxAnswerScore(e):
        maxAnswerScore = 100 + 200 * (e.level - 1)
        return maxAnswerScore

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
        e.debugPrint("e.isMenuScreen()", e.isMenuScreen())
        e.debugPrint("selectedObjectId" ,e.selectedObjectId)
        e.debugPrint("currentScreen" , e.currentScreen)
        e.debugPrint("the selected button" ,e.getCurrentButtons()[e.selectedObjectId])
        e.debugPrint("buttonIncreasingOrNot",e.buttonIncreasingOrNot)
        e.debugPrint("easyButtonScaler",e.easyButtonScaler)

    def debugPrint(e, strTitle, valueToPrint):
        myfont = pygame.font.SysFont("monospace", 15)
        ahaha = myfont.render("" + strTitle + ": " + str(valueToPrint), 1, (255,255,0))
        e.theScreen.blit(ahaha, (100, e.debugPrintLoc))
        e.debugPrintLoc += 20

    #returns a Fraction object that is created based on the level.
    def makeFraction(e):
        #reference for possibleX/Y. See actual value at beginning of class
        #possibleX = [0,1,2,3,5,7,9,11,13,17,19,23]
        #possibleY = [1,2,3,5,7,9,11,13,17,19,23]
        simpX = -1
        simpY = -1
        unSimpX = -1
        unSimpY = -1
        if (e.level == 1):
            theFactor = random.randint(2,5)
            unSimpX = 1 * theFactor
            unSimpY = random.randint(1,5) * theFactor
        elif (e.level == 2):
            theFactor = random.randint(3,7)
            unSimpX = random.randint(1,2) * theFactor
            unSimpY =  e.possibleY[random.randint(2,4)] * theFactor
        elif (e.level == 3):
            theFactor = random.randint(7,12)
            unSimpX =  random.randint(1,7) * theFactor
            unSimpY =  random.randint(2,10) * theFactor
        #create Fraction
        theFraction = Fraction()
        theFraction.theFactor = theFactor
        theFraction.unSimpX = unSimpX
        theFraction.unSimpY = unSimpY
        theFraction.gcd = gcd(theFraction.unSimpX, theFraction.unSimpY)
        theFraction.ansX = theFraction.unSimpX / theFraction.gcd
        theFraction.ansY = theFraction.unSimpY / theFraction.gcd
        return theFraction

    def drawFraction(e, theFraction, theScreen):
        if (e.debugFracOrNot == False):
            myfont = pygame.font.SysFont("monospace", 32)

            numerator = myfont.render(str(theFraction.unSimpX), 1, (255,255,0))
            denominator = myfont.render(str(theFraction.unSimpY), 1, (255,255,0))
            divideSign = myfont.render("/", 1, (255,255,0))
            equalsSign = myfont.render("=", 1, (255,255,0))
            horizontalLines = myfont.render("__", 1, (255,255,0))
            #if level is 1, show the GCD, otherwise show ?
            if(e.level == 1):
                gcd = myfont.render(str(theFraction.gcd), 1, (255,255,0))
            else:
                gcd = myfont.render("?", 1, (255,255,0))

            #show ? if nothing is inputed yet for numerator or denominator
            if(e.currentAnsNumerator == ""):
                ansNumerator = myfont.render("?", 1, (255,255,0))
            else:
                ansNumerator = myfont.render(e.currentAnsNumerator, 1, (255,255,0))
            if(e.currentAnsDenominator == ""):
                ansDenominator = myfont.render("?", 1, (255,255,0))
            else:
                ansDenominator = myfont.render(e.currentAnsDenominator, 1, (255,255,0))

            e.theScreen.blit(numerator, (250, 350))
            e.theScreen.blit(denominator, (250, 450))
            e.theScreen.blit(divideSign, (350, 400))
            e.theScreen.blit(gcd, (450, 350))
            e.theScreen.blit(gcd, (450, 450))
            e.theScreen.blit(equalsSign, (550, 400))
            e.theScreen.blit(ansNumerator, (650, 350))
            e.theScreen.blit(ansDenominator, (650, 450))
            e.theScreen.blit(horizontalLines, (250, 400))
            e.theScreen.blit(horizontalLines, (450, 400))
            e.theScreen.blit(horizontalLines, (650, 400))
        elif (e.debugFracOrNot == True):
            e.debugDrawFraction(theFraction, theScreen)
        else:
            print("ERROR, e.debugOrNot is not true or false")

    def drawCurrentButtons(e):
        theCurrentButtons = e.getCurrentButtons()
        for aButton in theCurrentButtons:
            if (aButton == "startButton"):
                e.theScreen.blit(e.startButton,\
                    (int(round(e.theScreen.get_width()/2 - e.startButton.get_width()/2)),\
                        int(round(e.theScreen.get_height()/2 - e.startButton.get_height()/2)) \
                    )\
                )
            elif (aButton == "howToPlay"):
                e.theScreen.blit(e.howToPlayButton,\
                    (int(round(e.theScreen.get_width()/2 - e.howToPlayButton.get_width()/2)),\
                        int(round(e.theScreen.get_height()/1.6 - e.howToPlayButton.get_height()/2)) \
                    )\
                )
            elif (aButton == "easy"):
                e.theScreen.blit(e.easyButton,\
                    (int(round(e.theScreen.get_width()/2 - e.easyButton.get_width()/2)),\
                        int(round(e.theScreen.get_height()/5 - e.easyButton.get_height()/2))
                    )\
                )
            elif (aButton == "medium"):
                e.theScreen.blit(e.mediumButton,\
                    (int(round(e.theScreen.get_width()/2 - e.mediumButton.get_width()/2)),\
                        int(round(e.theScreen.get_height()/4 + 100 - e.mediumButton.get_height()/2))
                    )\
                )
            elif (aButton == "hard"):
                e.theScreen.blit(e.hardButton,\
                    (int(round(e.theScreen.get_width()/2 - e.hardButton.get_width()/2)),\
                        int(round(e.theScreen.get_height()/3 + 200 - e.hardButton.get_height()/2))
                    )\
                )
            elif (aButton == "back"):
                e.theScreen.blit(e.backButton,\
                    (int(round(e.theScreen.get_width()/2 - e.backButton.get_width()/2)),\
                        int(round(e.theScreen.get_height()/1.2 - e.backButton.get_height()/2))
                    )\
                )

    def debugDrawFraction(e, theFraction, theScreen):
        bla2 = "theFraction.theFactor = " + str(theFraction.theFactor)
        bla3 = "theFraction.unSimpX = " + str(theFraction.unSimpX)
        bla4 = "theFraction.unSimpY = " + str(theFraction.unSimpY)
        bla5 = "theFraction.gcd = " + str(theFraction.gcd)
        bla6 = "theFraction.ansX = " + str(theFraction.ansX)
        bla7 = "theFraction.ansY = " + str(theFraction.ansY)
        myfont = pygame.font.SysFont("monospace", 22)
        lab2 = myfont.render(bla2, 1, (255,255,0))
        lab3 = myfont.render(bla3, 1, (255,255,0))
        lab4 = myfont.render(bla4, 1, (255,255,0))
        lab5 = myfont.render(bla5, 1, (255,255,0))
        lab6 = myfont.render(bla6, 1, (255,255,0))
        lab7 = myfont.render(bla7, 1, (255,255,0))
        theScreen.blit(lab2, (200,e.startPrintY))
        e.startPrintY += 20
        theScreen.blit(lab3, (200,e.startPrintY))
        e.startPrintY += 20
        theScreen.blit(lab4, (200,e.startPrintY))
        e.startPrintY += 20
        theScreen.blit(lab5, (200,e.startPrintY))
        e.startPrintY += 20
        theScreen.blit(lab6, (200,e.startPrintY))
        e.startPrintY += 20
        theScreen.blit(lab7, (200,e.startPrintY))
        e.startPrintY += 20

    def animateObject(e):
        theCurrentButtons = e.getCurrentButtons()
        if(theCurrentButtons[e.selectedObjectId] == "startButton"): #if selected is startButton
            e.animateStartButton()
        elif(theCurrentButtons[e.selectedObjectId] == "howToPlay"): #if selected is How To Play
            e.animateHowToPlayButton()
        elif(theCurrentButtons[e.selectedObjectId] == "easy"):
            e.animateEasyButton()
        elif(theCurrentButtons[e.selectedObjectId] == "medium"):
            e.animateMediumButton()
        elif(theCurrentButtons[e.selectedObjectId] == "hard"):
            e.animateHardButton()
        elif(theCurrentButtons[e.selectedObjectId] == "back"):
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
        if(e.easyButtonScaler >= .85):
            e.buttonIncreasingOrNot = False
        elif(e.easyButtonScaler <= .65):
            e.buttonIncreasingOrNot = True
        if(e.buttonIncreasingOrNot == True):
            e.easyButtonScaler += .005
        elif(e.buttonIncreasingOrNot == False):
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

    def getCurrentButtons(e):
        if e.currentScreen == "title":
            return e.titleButtons
        elif e.currentScreen == "difficulty":
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
        try:
            if e.currentScreen in e.menuScreens:
                return True
            else:
                return False
        except:
            return False

    def handleEvents(e):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode(event.size, pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    e.kDownPressed()
                elif event.key == pygame.K_UP:
                    e.kUpPressed()
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    e.kEnterPressed()
                else:
                    e.handleMoreInGameEvents(event)

    #handles more keys than handleEvents, but only if the game is not on a menu
    def handleMoreInGameEvents(e, event):
        if e.isMenuScreen():
            pass
        else:
            key = event.key
            if key == pygame.K_0 or key == pygame.K_KP0:
                e.ansAddValue("0")
            elif key == pygame.K_1 or key == pygame.K_KP1:
                e.ansAddValue("1")
            elif key == pygame.K_2 or key == pygame.K_KP2:
                e.ansAddValue("2")
            elif key == pygame.K_3 or key == pygame.K_KP3:
                e.ansAddValue("3")
            elif key == pygame.K_4 or key == pygame.K_KP4:
                e.ansAddValue("4")
            elif key == pygame.K_5 or key == pygame.K_KP5:
                e.ansAddValue("5")
            elif key == pygame.K_6 or key == pygame.K_KP6:
                e.ansAddValue("6")
            elif key == pygame.K_7 or key == pygame.K_KP7:
                e.ansAddValue("7")
            elif key == pygame.K_8 or key == pygame.K_KP8:
                e.ansAddValue("8")
            elif key == pygame.K_9 or key == pygame.K_KP9:
                e.ansAddValue("9")
            elif key == pygame.K_BACKSPACE:
                e.ansBackspace()
            elif key == pygame.K_RIGHT or \
                key == pygame.K_LEFT or \
                key == pygame.K_TAB or \
                key == pygame.K_KP_DIVIDE or \
                key == pygame.K_SLASH:
                e.switchSelectedAnsPart()

    #strToAdd: the character to add to the current answer's string
    def ansAddValue(e, strToAdd):
        if(e.selectedAnsPart == "numerator"):
            e.currentAnsNumerator = "" + e.currentAnsNumerator + str(strToAdd)
        elif(e.selectedAnsPart == "denominator"):
            e.currentAnsDenominator = "" + e.currentAnsDenominator + str(strToAdd)
        else:
            print("error: selectedAnsPart not numerator or denominator")

    def ansBackspace(e):
        if(e.selectedAnsPart == "numerator"):
            if len(e.currentAnsNumerator) > 0:
                e.currentAnsNumerator = e.currentAnsNumerator[:-1]
        elif(e.selectedAnsPart == "denominator"):
            if len(e.currentAnsDenominator) > 0:
                e.currentAnsDenominator = e.currentAnsDenominator[:-1]
        else:
            print("error: selectedAnsPart not numerator or denominator")

    def kUpPressed(e):
        if e.isMenuScreen():
            e.resetCurrentMenuItemSize()
            e.buttonIncreasingOrNot = True
            e.selectedObjectId -= 1
            if(e.selectedObjectId < 0):
                e.selectedObjectId = len(e.getCurrentButtons()) - 1
        else:
            e.switchSelectedAnsPart()

    def kDownPressed(e):
        if e.isMenuScreen():
            e.resetCurrentMenuItemSize()
            e.buttonIncreasingOrNot = True
            e.selectedObjectId += 1
            if(e.selectedObjectId >= len(e.getCurrentButtons())):
                e.selectedObjectId = 0
        else:
            e.switchSelectedAnsPart()

    def kEnterPressed(e):
        if e.isMenuScreen():
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
                print("error? menu button not found")
        else:
            e.checkAnswer()

    def switchSelectedAnsPart(e):
        if(e.selectedAnsPart == "numerator"):
            e.selectedAnsPart = "denominator"
        elif e.selectedAnsPart == "denominator":
            e.selectedAnsPart = "numerator"
        else:
            print("error, selectedAnsPart != numerator or denominator")

    def checkAnswer(e):
        try:
            if int(e.currentAnsNumerator) == e.theCurrentFraction.ansX and \
                int(e.currentAnsDenominator) == e.theCurrentFraction.ansY:
                e.drawCheckMark()
                e.fractionIsSolved = True
            else:
                e.drawXMark()
        except:
            e.drawXMark()

    def drawCheckMark(e):
        myfont = pygame.font.SysFont("monospace", 32)
        checkMark = myfont.render("RIGHT", 1, (255,255,0))
        e.theScreen.blit(checkMark, (222, 222))

    def drawXMark(e):
        myfont = pygame.font.SysFont("monospace", 32)
        XMark = myfont.render("WRONGGGGGGGGGGGGGGGGGGGGGG", 1, (255,255,0))
        e.theScreen.blit(XMark, (222, 222))
        e.answerScore -= 10 * e.level

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

# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = MiniGameMayhem()
    game.run()

if __name__ == '__main__':
    main()