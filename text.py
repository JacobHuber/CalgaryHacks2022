import pygame, sys
from button import *
from pygame.locals import *


class Text:

    def __init__(self,sr,font,text,colour,x,y,width,height):
        self.sr = sr
        self.font = font
        self.text = text
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def draw(self,surface,font,):
        title = self.font.render(self.text, True, self.colour)
        titleRect = title.get_rect()
        titleRect.centerx = self.x
        titleRect.centery = self.y
        titleRect.width = self.width
        titleRect.height = self.height
        self.sr.display_surface.blit(title,titleRect)
