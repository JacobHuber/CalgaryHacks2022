import pygame, sys
from pygame.locals import *
from minigame import *
from random import *
from math import *
from button import *

class MinigamePlay(Minigame):
	def __init__(self, player, surface, color):
		Minigame.__init__(self, player, surface, color)
		self.games = [AlcoholismGame(self), SoccerGame(self), SprintGame(self)]



class AlcoholismGame:
	def __init__(self, mg):
		self.gameTitle = "Alcoholism!"
		self.subtitle = "drink responsibly"
		self.mg = mg
		self.end = False
		self.gain = [0,0,0,0]

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
		self.gain = [0,0,0,0]

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
		self.gain[3] += self.drinkValue * self.drinkCount
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

class SoccerGame:
	def __init__(self, mg):
		self.gameTitle = "Burrito Bounce"
		self.subtitle = "click the burrito!"
		self.mg = mg
		self.gain = [0,0,0,0]
		self.end = False

		self.image = pygame.image.load("pictures/burrito.png", "png")
		self.imageRect = self.image.get_rect()

		self.burrito = {"x": self.mg.width // 2, "y": 0, "xs": 0, "ys": 0}
		self.gravity = 0.5
		self.gravityCap = 20

		self.mouse_down = False

		self.bounceCount = 0
		self.winCount = 10

		self.gainAmount = 5

	def setup(self):
		self.gain = [0,0,0,0]
		self.end = False
		self.bounceCount = 0

		xs = randint(-10, 10)
		ys = 0
		self.burrito = {"x": self.mg.width // 2, "y": 100, "xs": xs, "ys": ys}

	def tick(self):
		clicked = False

		if (not self.mouse_down and pygame.mouse.get_pressed()[0]):
			clicked = True
			halfWidth = self.imageRect.width // 2
			halfHeight = self.imageRect.height // 2
			pos = self.mg.get_mouse()

			dx = pos[0] - self.burrito["x"]
			dy = pos[1] - self.burrito["y"]

			if (fabs(dx) <= halfWidth and fabs(dy) <= halfHeight):
				self.burrito["ys"] = -15
				self.bounceCount += 1

				if (self.bounceCount >= self.winCount):
					self.gain[3] = self.bounceCount * self.gainAmount
					self.end = True

		if (clicked):
			self.mouse_down = True

		if (self.mouse_down and not pygame.mouse.get_pressed()[0]):
			self.mouse_down = False

		self.burrito["ys"] += self.gravity
		if (self.burrito["ys"] >= self.gravityCap):
			self.burrito["ys"] = self.gravityCap

		self.burrito["x"] = self.burrito["x"] + self.burrito["xs"]
		self.burrito["y"] = self.burrito["y"] + self.burrito["ys"]

		if (self.burrito["x"] < self.imageRect.width // 2 or self.burrito["x"] > self.mg.width - self.imageRect.width // 2):
			self.burrito["xs"] = -self.burrito["xs"]

		if (self.burrito["y"] > self.mg.height):
			self.gain[3] = self.bounceCount * self.gainAmount
			self.end = True

		self.imageRect.center = (self.burrito["x"], self.burrito["y"])

		

	def draw(self, surface, font):
		surface.blit(self.image, self.imageRect)


class SprintGame:
	def __init__(self, mg):
		self.gameTitle = "Sprint"
		self.subtitle = "mash SPACE a LOT"

		self.mg = mg
		self.end = False
		self.gain = [0,0,0,0]

		self.spaceAmount = 0
		self.spaceValue = 1.5

		self.carX = -100
		self.frames = []
		self.frameCount = 10
		self.currentFrame = 0
		for i in range(self.frameCount):
			self.frames.append(pygame.image.load("pictures/run/run" + str(i + 1) + ".png", "png"))
		self.imageRect = self.frames[0].get_rect()
		self.imageRect.bottomleft = (self.carX, self.mg.height)
		self.image = self.frames[self.currentFrame]

		self.timer = 2 * self.mg.player.game.sr.FPS
		self.currTime = 0

		self.mashTime = True

		self.texts = ["uhhhh..", "OKAY!", "ZOOOM"]
		self.text = self.texts[0]

	def setup(self):
		self.end = False
		self.mashTime = True
		self.gain = [0,0,0,0]

		self.spaceAmount = 0
		self.currTime = 0
		self.carX = -100

	def tick(self):
		if (self.mashTime):
			if (self.currTime >= self.timer):
				self.mashTime = False
			else:
				self.currTime += 1

				for event in self.mg.player.pressedKeys:
					if (event.key == K_SPACE):
						self.spaceAmount += 1
		else:
			speed = 1.5 * (self.spaceAmount + 1)
			if (speed < 10):
				self.text = self.texts[0]
			elif (speed < 20):
				self.text = self.texts[1]
			else:
				self.text = self.texts[2]

			self.carX += speed
			self.imageRect.x = self.carX

			if (self.mg.player.time % 4 == 0):
				self.currentFrame = (self.currentFrame + 1) % self.frameCount
			self.image = self.frames[self.currentFrame]

			if (self.carX > self.mg.width):
				self.gain = [0,0,0, int(self.spaceAmount * self.spaceValue)]
				self.end = True

	def draw(self, surface, font):
		if (self.mashTime):
			self.mashText = self.mg.BIGFONT.render(str(self.spaceAmount), True, (255,255,255))
			self.mashTextRect = self.mashText.get_rect()
			self.mashTextRect.center = (self.mg.width // 2, self.mg.height // 3)
			surface.blit(self.mashText, self.mashTextRect)
			
			self.mashText = font.render("press SPACE", True, (255,255,255))
			self.mashTextRect = self.mashText.get_rect()
			self.mashTextRect.center = (self.mg.width // 2, self.mg.height // 3 + 80)
			surface.blit(self.mashText, self.mashTextRect)
			
		else:
			self.mashText = self.mg.BIGFONT.render(self.text, True, (255,255,255))
			self.mashTextRect = self.mashText.get_rect()
			self.mashTextRect.center = (self.mg.width // 2, self.mg.height // 3)
			surface.blit(self.mashText, self.mashTextRect)
			surface.blit(self.image, self.imageRect)