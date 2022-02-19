import pygame
import button

class MainMenu:



    def __init__(self, sr):
        self.tickables = []
        self.drawables = []
        self.sr = sr

    def create_buttons(self):
        testButton = Button("Test", pygame.Rect(200, 200, 200, 100), (100, 150, 20), print)
        self.tickables.append(testButton)
        self.drawables.append(testButton)

    def Menu():
        create_buttons(self)


        