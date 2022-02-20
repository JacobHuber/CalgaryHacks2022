import pygame, sys
from pygame.locals import *


class Button:
	def __init__(self, text, rect, color, callback=print):
		self.borderColor = (0,0,0)
		self.borderHoverColor = (255,255,255)

		self.color = pygame.Color(color)
		self.fontColor = pygame.Color(255,255,255)
		self.text = text
		self.rect = pygame.Rect(rect)
		self.callback = callback

		self.hovered = False

		self.off = False
		scale = 10
		scaleCol = pygame.Color(scale,scale,scale,1)
		self.offColor = self.color // scaleCol
		self.offFontColor = self.fontColor // scaleCol

	def tick(self, mouse=None):
		global unique_Click
		if (not self.off):
			if (mouse is None):
				mouse = pygame.mouse.get_pos()
			
			if (self.rect.collidepoint(mouse)):
				if (pygame.mouse.get_pressed()[0]):
					if (not unique_Click):
						unique_Click = True
						self.callback(self.text)
				else:
					unique_Click = False
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


