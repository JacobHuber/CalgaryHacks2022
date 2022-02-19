import pygame, sys
from pygame.locals import *

class Button:
	def __init__(self, text, rect, color, callback=print):
		self.borderColor = (0,0,0)
		self.borderHoverColor = (255,255,255)

		self.color = pygame.Color(color)
		self.fontColor = pygame.Color(255,255,255)
		self.text = text
		self.rect = rect
		self.callback = callback

		self.hovered = False
		self.clicked = False

		self.off = False
		scale = 10
		scaleCol = pygame.Color(scale,scale,scale,1)
		self.offColor = self.color // scaleCol
		self.offFontColor = self.fontColor // scaleCol

	def tick(self):
		if (not self.off):
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
		else:
			self.hovered = False

	def draw(self, surface, font):
		bgColor = self.color
		fontColor = self.fontColor
		if (self.off):
			bgColor = self.offColor
			fontColor = self.offFontColor

		pygame.draw.rect(surface, bgColor, self.rect)

		buttonText = font.render(self.text, True, fontColor)
		buttonTextRect = buttonText.get_rect()
		buttonTextRect.center = self.rect.center
		surface.blit(buttonText, buttonTextRect)

		borderColor = self.borderColor
		if (self.hovered):
			borderColor = self.borderHoverColor
		pygame.draw.rect(surface, borderColor, self.rect, 2)


