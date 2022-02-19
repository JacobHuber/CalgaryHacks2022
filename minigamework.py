import pygame, sys
from pygame.locals import *

class MinigameWork:
	def __init__(self, color):
		self.color = color
		# load images
		pass

	def draw(self, surface, font):
		pygame.draw.rect(surface, self.color, surface.get_rect(), 4)