import pygame, sys
from pygame.locals import *
from button import *
from player import *

class Game:
	def __init__(self, sr):
		self.sr = sr

		self.tickables = []
		self.drawables = []
		
		self.create_buttons()
		self.create_player()

	def create_buttons(self):
		testButton = Button("Test", pygame.Rect(200, 200, 200, 100), (100, 150, 20), print)

		self.tickables.append(testButton)
		self.drawables.append(testButton)

	def create_player(self):
		self.player = Player(self)
		self.drawables.append(self.player)