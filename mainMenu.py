import pygame, sys
from button import *
from pygame.locals import *
from text import *

class MainMenu:



    def __init__(self, sr):
        self.tickables = []
        self.drawables = []
        self.sr = sr
        self.create_buttons()
        



    def changePlay(self,text):
        self.sr.current_scene = 0
    def changeInfo(self,text):
        self.sr.current_scene = 2


    def exitFun(self,text):
        pygame.quit()
        sys.exit()

    def addButton(self,buttonAdd):
        self.tickables.append(buttonAdd)
        self.drawables.append(buttonAdd)


    def create_buttons(self):
        playButton = Button("Play", pygame.Rect(self.sr.WIDTH/2-200, self.sr.HEIGHT/2-100, 400, 100), (100, 150, 20), self.changePlay)
        exitButton = Button("Exit", pygame.Rect(self.sr.WIDTH/2-200, self.sr.HEIGHT/2+100, 400, 100), (230, 14, 14), self.exitFun)
        
        infoButton = Button("Info", pygame.Rect(self.sr.WIDTH/2-200,  self.sr.HEIGHT/2, 400, 100), (230, 230, 30), self.changeInfo)
        self.addButton(playButton)
        self.addButton(infoButton)
        self.addButton(exitButton)
        fontTitle = pygame.font.Font("font.ttf",108)
        title = Text(self.sr,fontTitle,"Homework Please",(255,255,255),self.sr.WIDTH/2,self.sr.HEIGHT/2-200,100,100)
        self.drawables.append(title)
        #title = self.font.render("Homework Please", True, (255,255,255))
        #titleRect = title.get_rect()
        #titleRect.x = playButton.rect.x
        #titleRect.y = playButton.rect.y-100
        #titleRect.width = 400
        #titleRect.height = 100
        #self.sr.display_surface.blit(title,titleRect)

        