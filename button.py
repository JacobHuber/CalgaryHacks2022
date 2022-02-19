import pygame, sys
from pygame.locals import *

class Button:
	def __init__(self, text, rect, color, callback):
		self.borderColor = (0,0,0)
		self.borderHoverColor = (255,255,255)

		self.color = color
		self.text = text
		self.rect = rect
		self.callback = callback

		self.hovered = False
		self.clicked = False

	def tick(self):
		mouse = pygame.mouse.get_pos()

		if (self.rect.collidepoint(mouse)):
			if (pygame.mouse.get_pressed()[0]):
				if (not self.clicked):
					self.clicked = True
					self.callback(self.text)
			else:
				self.clicked = False
			self.hovered = True
		else:
			self.hovered = False

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect, 0)

		borderColor = self.borderColor
		if (self.hovered):
			borderColor = self.borderHoverColor
		pygame.draw.rect(surface, borderColor, self.rect, 2)
