import pygame, sys
from pygame.locals import *
from minigame import *
from random import *
from math import *

class MinigameWork(Minigame):
	def __init__(self, player, surface, color):
		Minigame.__init__(self, player, surface, color)
		self.games = [CoinGame(self)]
		



class CoinGame:
	def __init__(self, mg):
		self.mg = mg
		self.coinColor = (255,255,0)
		
		self.amount = 4
		self.coinValue = 3
		self.end = False

		self.mouse_down = False

		self.gain = 0
		self.coins = []

	def setup(self):
		self.end = False
		self.gain = 0
		self.coins = []
		for i in range(self.amount):
			r = randint(10,15)
			x = randint(r, self.mg.width-r)
			y = randint(r, self.mg.height-r)
			xs = randint(-5,5)
			ys = randint(-5,5)
			self.coins.append({"x":x,"y":y,"r":r,"xs":xs,"ys":ys})


	def tick(self):
		if (not self.mouse_down and pygame.mouse.get_pressed()[0]):
			self.mouse_down = True

		for coin in self.coins:
			if (self.mouse_down):
				pos = self.mg.get_mouse()

				dx = pos[0] - coin["x"]
				dy = pos[1] - coin["y"]

				if (fabs(dx) <= coin["r"] and fabs(dy) <= coin["r"]):
					self.coins.remove(coin)
					self.gain += self.coinValue
			
			coin["x"] = coin["x"] + coin["xs"]
			coin["y"] = coin["y"] + coin["ys"]

			if (coin["x"] < coin["r"] or coin["x"] > self.mg.width - coin["r"]):
				coin["xs"] = -coin["xs"]

			if (coin["y"]  < coin["r"] or coin["y"]  > self.mg.height - coin["r"]):
				coin["ys"] = -coin["ys"]

		if (self.mouse_down and not pygame.mouse.get_pressed()[0]):
			self.mouse_down = False


		if (len(self.coins) == 0):
			self.end = True

	def draw(self, surface):
		for coin in self.coins:
			pygame.draw.circle(surface, self.coinColor, (coin["x"], coin["y"]), coin["r"])

