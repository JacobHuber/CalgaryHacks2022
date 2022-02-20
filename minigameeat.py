import pygame, sys
from pygame.locals import *
from minigame import *
from random import *
from math import *

class MinigameEat(Minigame):
	def __init__(self, player, surface, color):
		Minigame.__init__(self, player, surface, color)
		self.games = [ShoppingGame(self)]




class ShoppingGame:
	def __init__(self, mg):
		self.mg = mg
		self.gain = 0
		self.end = False

		self.shoppingCartX = self.mg.width // 2
		self.imgShoppingCart = pygame.image.load("pictures/cart.png", "png")
		self.shoppingCartRect = self.imgShoppingCart.get_rect()
		self.shoppingCartRect.bottom = self.mg.height

		self.currSpeed = 0
		self.cartAccel = 0.2
		self.cartSpeed = 10


		self.itemValue = 5


		self.imgRamen = pygame.image.load("pictures/ramen.png", "png")
		self.ramenRect = self.imgRamen.get_rect()
		self.ramenSpeed = 5

		self.ramen = []

	def setup(self):
		self.currSpeed = 0
		self.gain = 0
		self.end = False
		self.shoppingCartX = self.mg.width // 2
		self.ramenSpeed = 5

		self.ramen = []
		self.spawn_ramen()


	def spawn_ramen(self):
		x = randint(self.ramenRect.width, self.mg.width - self.ramenRect.width)
		y = -10

		self.ramen.append({"x": x, "y": y})

	def movement(self):
		left = pygame.key.get_pressed()[K_a]
		right = pygame.key.get_pressed()[K_d]

		if (left):
			self.currSpeed -= self.cartAccel
			if (self.currSpeed < -self.cartSpeed):
				self.currSpeed = -self.cartSpeed
		if (right):
			self.currSpeed += self.cartAccel
			if (self.currSpeed > self.cartSpeed):
				self.currSpeed = self.cartSpeed


		self.currSpeed *= 0.99

		self.shoppingCartX += self.currSpeed

		if (self.shoppingCartX > self.mg.width):
			self.shoppingCartX = self.mg.width
			self.currSpeed = -self.currSpeed / 1.5
		elif (self.shoppingCartX < 0):
			self.shoppingCartX = 0
			self.currSpeed = -self.currSpeed / 1.5

		self.shoppingCartRect.centerx = self.shoppingCartX

	def tick(self):
		self.movement()

		for ramen in self.ramen:
			ramen["y"] += self.ramenSpeed

			if (ramen["y"] > self.mg.height):
				self.ramen.remove(ramen)
				self.gain -= self.itemValue
				self.end = True

			if (self.shoppingCartRect.collidepoint((ramen["x"],ramen["y"]))):
				self.ramen.remove(ramen)
				self.gain += self.itemValue
				self.ramenSpeed += 1
				self.spawn_ramen()

	def draw(self, surface, font):
		for ramen in self.ramen:
			x = ramen["x"]
			y = ramen["y"]

			self.ramenRect.center = (x,y)
			surface.blit(self.imgRamen, self.ramenRect)

		surface.blit(self.imgShoppingCart, self.shoppingCartRect)