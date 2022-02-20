import pygame, sys
from pygame.locals import *
from minigame import *
from random import *
from math import *
from button import *

class MinigamePlay(Minigame):
	def __init__(self, player, surface, color):
		Minigame.__init__(self, player, surface, color)
		self.games = [AlcoholismGame(self)]



class AlcoholismGame:
	def __init__(self, mg):
		self.mg = mg
		self.end = False
		self.gain = 0

		self.drinkImages = []
		self.drinkImages.append(pygame.image.load("pictures/empty.png","png"))
		self.drinkImages.append(pygame.image.load("pictures/filled1.png","png"))
		self.drinkImages.append(pygame.image.load("pictures/filled2.png","png"))
		self.drinkImages.append(pygame.image.load("pictures/filled3.png","png"))
		self.drinkImages.append(pygame.image.load("pictures/filled4.png","png"))
		self.drinkRect = self.drinkImages[0].get_rect()

		self.drinkCount = 0
		self.drinkMax = len(self.drinkImages) - 1

		self.drinkValue = 4
		self.drunkValue = 3 * self.mg.player.game.sr.FPS

		self.buttons = []
		self.drinks = []

		self.isSliding = True

	def setup(self):
		self.end = False
		self.gain = 0

		self.buttons = []
		self.drinks = []
		self.drinkCount = 0

		drinkRect = (40, self.mg.height - 80, 200, 40)
		drinkBtn = Button("Drink", drinkRect, (0,0,0), self.drink)
		self.buttons.append(drinkBtn)

		exitRect = (self.mg.width - 40 - 200, self.mg.height - 80, 200, 40)
		exitBtn = Button("Stop", exitRect, (0,0,0), self.stop)
		self.buttons.append(exitBtn)

		self.add_drink()

	def add_drink(self):
		self.drinkCount += 1
		self.isSliding = True

		x = self.mg.width + 50
		y = self.mg.height // 2
		image = self.drinkImages[self.drinkCount]

		self.drinks.append({"x":x,"y":y,"img":image})

	def drink(self, text):
		self.gain += self.drinkValue * self.drinkCount
		self.mg.player.drunkeness += self.drunkValue * self.drinkCount
		self.drinks[len(self.drinks) - 1]["img"] = self.drinkImages[0]

		if (self.drinkCount < self.drinkValue):
			self.add_drink()
		else:
			self.end = True

	def stop(self, text):
		self.end = True

	def tick(self):
		if (not self.isSliding):
			for button in self.buttons:
				button.tick(self.mg.get_mouse())
		else:
			i = len(self.drinks) - 1

			gotoX = 100 + (i * (self.drinkRect.width + 40))

			dx = gotoX - self.drinks[i]["x"]

			if (fabs(dx) <= 5):
				self.drinks[i]["x"] = gotoX
				self.isSliding = False
			else:
				speed = min(-1, (dx / (0.5 * self.mg.player.game.sr.FPS)))
				self.drinks[i]["x"] += speed

	def draw(self, surface, font):
		if (not self.isSliding):
			for button in self.buttons:
				button.draw(surface, font)

		for drink in self.drinks:
			self.drinkRect.midbottom = (drink["x"], drink["y"])
			surface.blit(drink["img"], self.drinkRect)