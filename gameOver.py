import pygame, sys
from button import *
from pygame.locals import *
from text import *

class GameOver:


    def __init__(self, sr):
        self.tickables = []
        self.drawables = []
        self.sr = sr
        self.time = 0
        self.create_buttons()

    def changeMain(self,text):
        self.sr.current_scene = 1

    def exitFun(self,text):
        pygame.quit()
        sys.exit()

    def addButton(self,buttonAdd):
        self.tickables.append(buttonAdd)
        self.drawables.append(buttonAdd)


    def updateScore(self):
        time = self.sr.scenes[0].player.time
        seconds = (time // self.sr.FPS) % 60
        minutes = (time // (self.sr.FPS * 60)) % 60

        text = f'{minutes:02}' + ":" + f'{seconds:02}'

        fontbody = pygame.font.Font("font.ttf",58)
        body = Text(self.sr,fontbody,"Score: "+text,(255,255,255),self.sr.WIDTH/2,self.sr.HEIGHT/2-100,100,100)
        self.drawables.append(body)

    def create_buttons(self):
        playButton = Button("Play Again", pygame.Rect(self.sr.WIDTH/2-200, self.sr.HEIGHT/2+100, 400, 100), (100, 150, 20), self.changeMain)
        exitButton = Button("Exit", pygame.Rect(self.sr.WIDTH/2-200, self.sr.HEIGHT/2+200, 400, 100), (230, 14, 14), self.exitFun)
        self.addButton(playButton)
        self.addButton(exitButton)
        

        fontTitle = pygame.font.Font("font.ttf",108)
        title = Text(self.sr,fontTitle,"GAME OVER",(255,0,0),self.sr.WIDTH/2,self.sr.HEIGHT/2-200,100,100)
        self.drawables.append(title)