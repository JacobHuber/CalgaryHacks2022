import pygame, sys
from pygame.locals import *
from button import *
from player import *

class Game:
	def __init__(self, sr):
		self.sr = sr

		self.tickables = []
		self.drawables = []

		self.create_player()

	def create_player(self):
		self.tickables = []
		self.drawables = []
		
		self.player = Player(self)

		self.tickables.append(self.player)
		self.drawables.append(self.player)