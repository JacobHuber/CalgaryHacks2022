import pygame, sys
from button import *
from pygame.locals import *
from text import *

class InfoMenu:


    def __init__(self, sr):
        self.tickables = []
        self.drawables = []
        self.sr = sr
        self.create_buttons()

    def changeMain(self,text):
        self.sr.current_scene = 1

    def addButton(self,buttonAdd):
        self.tickables.append(buttonAdd)
        self.drawables.append(buttonAdd)


    def create_buttons(self):
        backButton = Button("Back", pygame.Rect(self.sr.WIDTH//2-200, self.sr.HEIGHT-150, 400, 100), (100, 150, 20), self.changeMain)
    
        self.addButton(backButton)

        fontTitle = pygame.font.Font("font.ttf",108)
        title = Text(self.sr,fontTitle,"How to play",(255,255,255),self.sr.WIDTH/2,self.sr.HEIGHT/2-200,100,100)
        self.drawables.append(title)

        fontbody = pygame.font.Font("font.ttf",58)
        body = Text(self.sr,fontbody,"Keep all you meter bars up by performing tasks.",(255,255,255),self.sr.WIDTH/2,self.sr.HEIGHT/2-100,100,100)
        self.drawables.append(body)

        body2 = Text(self.sr,fontbody,"If a meter runs out it's Game Over",(255,255,255),self.sr.WIDTH/2,self.sr.HEIGHT/2,100,100)
        self.drawables.append(body2)

        body2 = Text(self.sr,fontbody,"Last as long as you can!",(255,255,255),self.sr.WIDTH/2,self.sr.HEIGHT/2+100,100,100)
        self.drawables.append(body2)