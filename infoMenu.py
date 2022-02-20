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


    def create_buttons(self):
        playButton = Button("Back", pygame.Rect(self.sr.WIDTH-100, self.sr.HEIGHT-100, 400, 100), (100, 150, 20), self.changeMain)
    
        self.addButton(playButton)

        fontTitle = pygame.font.Font("font.ttf",108)
        title = Text(self.sr,fontTitle,"Homework Please",(255,255,255),playButton.rect.x-17,playButton.rect.y-200,100,100)
        self.drawables.append(title)