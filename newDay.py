import pygame, sys
from button import *
from pygame.locals import *
from text import *

class NewDay:


    def __init__(self, sr):
        self.tickables = []
        self.drawables = []
        self.sr = sr
        self.time = 0
        self.create_buttons()

    def changeMain(self,text):
        self.sr.current_scene = 0

    

    def addButton(self,buttonAdd):
        self.tickables.append(buttonAdd)
        self.drawables.append(buttonAdd)


    def nextDay(self):
        self.tickables = []
        self.drawables = []
        self.sr.scenes[0].player.day+=1
        self.sr.scenes[0].player.decayAmount *= (1 + (1 / 100))
        self.sr.scenes[0].player.time = 0
        self.create_buttons()

    def create_buttons(self):
        conButton = Button("Next Day", pygame.Rect(self.sr.WIDTH/2-200, self.sr.HEIGHT/2+100, 400, 100), (100, 150, 20), self.changeMain)
        self.addButton(conButton)

        

        fontTitle = pygame.font.Font("font.ttf",108)
        title = Text(self.sr,fontTitle,"Day "+ str(self.sr.scenes[0].player.day),(255,255,255),self.sr.WIDTH/2,self.sr.HEIGHT/2-50,100,100)
        self.drawables.append(title)
        
