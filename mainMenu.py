import pygame, sys
from button import *

class MainMenu:



    def __init__(self, sr):
        self.tickables = []
        self.drawables = []
        self.sr = sr
        self.create_buttons()



    def changeScene(self,text):
        self.sr.current_scene = 0

    def exitFun(self,text):
        pygame.quit()
        self.sr.sys.exit()

    def addButton(self,buttonAdd):
        self.tickables.append(buttonAdd)
        self.drawables.append(buttonAdd)
    def create_buttons(self):
        playButton = Button("Play", pygame.Rect(self.sr.WIDTH/2-200, self.sr.HEIGHT/2-100, 400, 100), (100, 150, 20), self.changeScene)
        exitButton = Button("Exit", pygame.Rect(self.sr.WIDTH/2-200, self.sr.HEIGHT/2+100, 400, 100), (230, 14, 14), self.exitFun)
        self.addButton(playButton)
        self.addButton(exitButton)



        