import pygame, sys
from pygame.locals import *
from minigame import *
from random import *
from math import *
from button import *

class MinigameWork(Minigame):
	def __init__(self, player, surface, color):
		Minigame.__init__(self, player, surface, color)
		self.games = [CoinGame(self), CustomerGame(self), DeliveryGame(self)]

class CoinGame:
	def __init__(self, mg):
		self.mg = mg
		self.gameTitle = "Coins!"
		self.subtitle = "you click them"

		self.coinColor = pygame.Color(255,255,0)
		self.coinTextColor = self.coinColor // pygame.Color(3,3,3,1)
		
		self.amount = 4
		self.coinValue = 3
		self.coins = []

		self.mouse_down = False
		self.gain = [0,0,0,0]
		self.end = False

	def setup(self):
		self.end = False
		self.gain = [0,0,0,0]
		self.coins = []
		for i in range(self.amount):
			r = 16
			x = randint(r, self.mg.width-r)
			y = randint(r, self.mg.height-r)
			xs = randint(-5,5)
			ys = randint(-5,5)
			self.coins.append({"x":x,"y":y,"r":r,"xs":xs,"ys":ys})


	def tick(self):
		clicked = False

		for coin in self.coins:
			if (not self.mouse_down and pygame.mouse.get_pressed()[0]):
				clicked = True
				pos = self.mg.get_mouse()

				dx = pos[0] - coin["x"]
				dy = pos[1] - coin["y"]

				if (fabs(dx) <= coin["r"] and fabs(dy) <= coin["r"]):
					self.coins.remove(coin)
					self.gain[0] += self.coinValue
			
			coin["x"] = coin["x"] + coin["xs"]
			coin["y"] = coin["y"] + coin["ys"]

			if (coin["x"] < coin["r"] or coin["x"] > self.mg.width - coin["r"]):
				coin["xs"] = -coin["xs"]

			if (coin["y"]  < coin["r"] or coin["y"]  > self.mg.height - coin["r"]):
				coin["ys"] = -coin["ys"]

		if (clicked):
			self.mouse_down = True

		if (self.mouse_down and not pygame.mouse.get_pressed()[0]):
			self.mouse_down = False


		if (len(self.coins) == 0):
			self.end = True

	def draw(self, surface, font):
		self.dollarSign = font.render("$", True, self.coinTextColor)
		self.dollarSignRect = self.dollarSign.get_rect()
		for coin in self.coins:
			pygame.draw.circle(surface, self.coinColor, (coin["x"], coin["y"]), coin["r"])
			self.dollarSignRect.center = (coin["x"], coin["y"] + 1)
			surface.blit(self.dollarSign, self.dollarSignRect)



class CustomerGame:
	def __init__(self, mg):
		self.mg = mg
		self.gain = [0,0,0,0]
		self.end = False
		self.gameTitle = "Customer Service"
		self.subtitle = "choose wisely"

		self.imgCustomer = pygame.image.load("pictures/customer.png", "png")
		self.customerRect = self.imgCustomer.get_rect()
		self.messages = ["I want a bean burrito!", "Why are there no good bean burrito places at the university?", "beans"]
		self.message = ""

		self.isTalking = False
		self.customerY = self.mg.height + 100
		self.buttons = []

		self.positiveValue = 10
		self.negativeValue = -3

	def setup(self):
		self.customerY = self.mg.height + 100
		self.isTalking = False
		self.buttons = []
		self.gain = [0,0,0,0]
		self.end = False

		self.message = choice(self.messages)

		goodRect = (40, 80, 200, 40)
		goodBtn = Button("Have a nice day!", goodRect, (0,0,0), self.good)
		self.buttons.append(goodBtn)

		badRect = (self.mg.width - 40 - 200, 80, 200, 40)
		badBtn = Button("Fuck you!", badRect, (0,0,0), self.bad)
		self.buttons.append(badBtn)

	def good(self, text):
		self.mg.player.bars[3].change(self.negativeValue)
		self.gain[0] = self.positiveValue
		self.end = True

	def bad(self, text):
		self.mg.player.bars[3].change(self.positiveValue)
		self.gain[0] = self.negativeValue
		self.end = True

	def tick(self):
		if (not self.isTalking):
			self.customerY -= 5
			self.customerRect.bottom = self.customerY

			if (self.customerY < self.mg.height + 10):
				self.isTalking = True
		else:
			for button in self.buttons:
				button.tick(self.mg.get_mouse())


	def draw(self, surface, font):
		surface.blit(self.imgCustomer, self.customerRect)

		if (self.isTalking):
			for button in self.buttons:
				button.draw(surface, font)

			self.answerText = font.render("\"" + self.message + "\"", True, (255,255,255))
			self.answerTextRect = self.answerText.get_rect()
			self.answerTextRect.center = (self.mg.width // 2, self.customerRect.top - 40)
			surface.blit(self.answerText, self.answerTextRect)

class DeliveryGame:
	def __init__(self, mg):
		self.gameTitle = "Uber Eats"
		self.subtitle = "WASD to MOVE"
		self.mg = mg
		self.gain = [0,0,0,0]
		self.end = False

		self.coinColor = pygame.Color(255,255,0)
		self.coinTextColor = self.coinColor // pygame.Color(3,3,3,1)

		self.image = pygame.image.load("pictures/car.png", "png")
		self.imageRect = self.image.get_rect()

		self.carRot = pygame.image.load("pictures/car.png", "png")

		self.car = {}

		self.accel = 0.2
		self.topSpeed = 15

		self.turnSpeed = 3


		self.target = (0,0)
		self.targetRadius = 50

		self.coins = []
		self.collected = 0
		self.coinCount = 4
		self.coinRadius = 16

		self.coinValue = 5

	def setup(self):
		self.end = False
		self.gain = [0,0,0,0]
		self.coins = []
		self.collected = 0

		x = self.mg.width // 2
		y = self.mg.height - 40
		d = 0
		speed = 0

		self.imageRect = self.image.get_rect()
		self.car = {"x":x, "y":y, "dir":d, "speed":speed}
		self.target = (randint(self.targetRadius, self.mg.width - self.targetRadius), randint(self.targetRadius, self.mg.height - self.targetRadius))

		for i in range(self.coinCount):
			x = randint(self.coinRadius, self.mg.width-self.coinRadius)
			y = randint(self.coinRadius, self.mg.height-self.coinRadius)
			
			self.coins.append((x,y))


	def car_movement(self):
		if (pygame.key.get_pressed()[K_w]):
			self.car["speed"] += self.accel
			if (self.car["speed"] >= self.topSpeed):
				self.car["speed"] = self.topSpeed
		elif (pygame.key.get_pressed()[K_s]):
			self.car["speed"] -= self.accel
			if (self.car["speed"] <= -self.topSpeed):
				self.car["speed"] = -self.topSpeed
		else:
			self.car["speed"] *= 0.9
			if (fabs(self.car["speed"]) <= 1):
				self.car["speed"] = 0

		ratio = min(fabs(self.car["speed"]) / 3, 1)
		if (pygame.key.get_pressed()[K_a]):
			self.car["dir"] += self.turnSpeed * ratio
		if (pygame.key.get_pressed()[K_d]):
			self.car["dir"] -= self.turnSpeed * ratio
		self.car["dir"] = self.car["dir"] % 360


		dx = cos(radians(self.car["dir"])) * self.car["speed"]
		dy = sin(radians(self.car["dir"])) * self.car["speed"]

		self.car["x"] += dx
		self.car["y"] -= dy

	def tick(self):
		self.car_movement()

		for coin in self.coins:
			if (self.imageRect.collidepoint(coin)):
				self.coins.remove(coin)
				self.collected += 1

		if (dist((self.car["x"], self.car["y"]), self.target) < self.targetRadius):
			self.gain = [self.collected * self.coinValue,0,0,0]
			self.end = True

	def draw(self, surface, font):
		pygame.draw.circle(surface, (255,0,0), self.target, self.targetRadius, 2)

		self.dollarSign = font.render("$", True, self.coinTextColor)
		self.dollarSignRect = self.dollarSign.get_rect()
		for coin in self.coins:
			pygame.draw.circle(surface, (255,255,0), coin, self.coinRadius)
			self.dollarSignRect.center = (coin[0], coin[1] + 1)
			surface.blit(self.dollarSign, self.dollarSignRect)

		self.carRot = pygame.transform.rotate(self.image, self.car["dir"])
		self.imageRect = self.carRot.get_rect()
		self.imageRect.center = (self.car["x"], self.car["y"])
		surface.blit(self.carRot, self.imageRect)