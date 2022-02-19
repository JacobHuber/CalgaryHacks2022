import pygame, sys
from pygame.locals import *

class Button:
	def __init__(self, text, rect, color, callback=print):
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

	def draw(self, surface, font):
		pygame.draw.rect(surface, self.color, self.rect, 0)

		buttonText = font.render(self.text, True, (255,255,255))
		buttonTextRect = buttonText.get_rect()
		buttonTextRect.center = self.rect.center
		surface.blit(buttonText, buttonTextRect)

		borderColor = self.borderColor
		if (self.hovered):
			borderColor = self.borderHoverColor
		pygame.draw.rect(surface, borderColor, self.rect, 2)


