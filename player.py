import pygame, sys
from pygame.locals import *
from healthbar import *

class Player:
	def __init__(self, game):
		self.game = game

		self.create_bars()

		# How much to decay each time
		self.decayAmount = 1

		# How many frames until decay
		self.decayTime = 0
		self.decayMax = 1 * self.game.sr.FPS

	def create_buttons(self):
		self.buttons = []

	def create_bars(self):
		self.start_x = 20
		self.start_y = 60
		self.height = 60

		barNames = ["Money", "Food", "Grades", "Happiness"]
		barColors = [(100,255,100), (220,180,0), (0,255,255), (255,255,0)]
		barValues = [(60, 100), (100, 100), (50, 100), (50, 100)]

		self.bars = []
		for i in range(len(barNames)):
			newBar = Healthbar(pygame.Rect(self.start_x, self.start_y + self.height * i, 200, 20), barColors[i], barNames[i], barValues[i])
			self.bars.append(newBar)

	def decayBars(self):
		for bar in self.bars:
			bar.decrement(self.decayAmount)

	def buyFood(self):
		pass

	def tick(self):
		self.decayTime += 1
		if (self.decayTime >= self.decayMax):
			self.decayTime = 0
			self.decayBars()

	def draw(self, surface, font):
		for bar in self.bars:
			bar.draw(surface,font)