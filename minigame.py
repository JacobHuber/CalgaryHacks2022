import pygame, sys
from pygame.locals import *

class Minigame:
	def __init__(self, player, surface, color):
		self.player = player
		self.surface = surface
		self.color = color

		dims = surface.get_rect()
		self.width = dims.width
		self.height = dims.height

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
		pass

	def draw(self, font):
		self.surface.fill((20,20,20))
		pygame.draw.rect(self.surface, self.color, (0,0,self.width,self.height), 4)