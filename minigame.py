import pygame, sys
from pygame.locals import *
from random import *
from math import *

class Minigame:
	def __init__(self, player, surface, color):
		self.player = player
		self.surface = surface
		self.color = color

		dims = surface.get_rect()
		self.width = dims.width
		self.height = dims.height

		self.current_game = 0
		self.end = True
		self.games = []

	def new_game(self):
		self.end = False
		self.current_game = randrange(0, len(self.games))
		self.games[self.current_game].setup()

	def get_mouse(self):
		mouse = pygame.mouse.get_pos()
		left = self.player.gameSurfaceRect.left
		right = self.player.gameSurfaceRect.right
		x = mouse[0] - left
		x = min(x, right)

		top = self.player.gameSurfaceRect.top
		bottom = self.player.gameSurfaceRect.bottom
		y = mouse[1] - top
		y = min(y, bottom)

		return (x,y)

	def tick(self):
		if (not self.end):
			game = self.games[self.current_game]
			game.tick()

			if (game.end):
				self.player.end_minigame(game.gain)
				self.end = True

	def draw(self, font):
		self.surface.fill((20,20,20))
		pygame.draw.rect(self.surface, self.color, (0,0,self.width,self.height), 4)

		self.games[self.current_game].draw(self.surface, font)