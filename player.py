import pygame, sys
from pygame.locals import *
from healthbar import *
from button import *

class Player:
	def __init__(self, game):
		self.game = game

		self.create_bars()
		self.create_buttons()

		# How much to decay each time
		self.decayAmount = 1

		# How many frames until decay
		self.decayTime = 0
		self.decayMax = 1 * self.game.sr.FPS

	def create_buttons(self):
		buttonNames = ["Work", "Eat", "Study", "Play"]
		buttonColors = [(100,255,100), (220,180,0), (0,255,255), (255,200,0)]
		buttonCallback = [print, print, print, print]

		mid_y = self.game.sr.HEIGHT // 2

		buttonHeight = 60
		buttonWidth = 200
		totalHeight = buttonHeight * len(buttonNames)

		start_x = self.game.sr.WIDTH - buttonWidth - 20
		start_y = mid_y - totalHeight // 2

		self.buttons = []
		for i in range(len(buttonNames)):
			newButton = Button(buttonNames[i], pygame.Rect(start_x, start_y + buttonHeight * i, buttonWidth, buttonHeight), buttonColors[i], buttonCallback[i])
			self.buttons.append(newButton)

	def create_bars(self):
		barNames = ["Money", "Food", "Grades", "Happiness"]
		barColors = [(100,255,100), (220,180,0), (0,255,255), (255,255,0)]
		barValues = [(60, 100), (100, 100), (50, 100), (50, 100)]

		mid_y = self.game.sr.HEIGHT // 2

		barHeight = 60
		barWidth = 200
		totalHeight = barHeight * len(barNames)

		start_x = 20
		start_y = mid_y - totalHeight // 2

		self.bars = []
		for i in range(len(barNames)):
			newBar = Healthbar(pygame.Rect(start_x, start_y + barHeight * i, barWidth, 20), barColors[i], barNames[i], barValues[i])
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

		for button in self.buttons:
			button.tick()

	def draw(self, surface, font):
		for bar in self.bars:
			bar.draw(surface, font)

		for button in self.buttons:
			button.draw(surface, font)