import pygame, sys
from pygame.locals import *

class Healthbar:
	def __init__(self, rect, color, title, value):
		self.rect = rect
		self.color = color
		self.title = title

		self.value = value[0]
		self.max = value[1]

		# Linear Interpolation Stuff
		self.currLerpTime = 0
		self.lerpTime = 30
		self.lerpValue = self.value
		self.lerpAmount = 0

	def doLerp(self):
		if (self.currLerpTime != self.lerpTime):
			change = self.lerpAmount * (1 / self.lerpTime)
			self.lerpValue += change

			self.currLerpTime += 1


	def change(self, amount):
		self.currLerpTime = 0
		self.lerpValue = self.value
		self.value += amount
		
		if (self.value > self.max):
			self.value = self.max
		elif (self.value < 0):
			self.value = 0

		self.lerpAmount = self.value - self.lerpValue

	def draw(self, surface, font):
		self.doLerp()

		filledRect = pygame.Rect(self.rect)
		filledRect.width = int(self.rect.width * (self.lerpValue / self.max))

		emptyRect = pygame.Rect(self.rect)
		emptyRect.width = self.rect.width - filledRect.width
		emptyRect.left = filledRect.right

		buttonText = font.render(self.title, True, (255,255,255))
		buttonTextRect = buttonText.get_rect()
		buttonTextRect.bottomleft = self.rect.topleft
		surface.blit(buttonText, buttonTextRect)

		pygame.draw.rect(surface, self.color, filledRect, 0)
		pygame.draw.rect(surface, (0,0,0), emptyRect, 0)
		pygame.draw.rect(surface, (255,255,255), self.rect, 2)