import pygame, sys
from pygame.locals import *

class Minigame:
	def __init__(self, color):
		self.color = color

	def draw(self, surface, font):
		pygame.draw.rect(surface, self.color, surface.get_rect(), 4)