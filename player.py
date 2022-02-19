import pygame, sys
from pygame.locals import *
from healthbar import *

class Player:
	def __init__(self):
		self.money = Healthbar(pygame.Rect(20, 100, 800, 40), (100,255,100), "Money", (60, 100))
		self.food = 0
		self.grades = 0
		self.happiness = 0

	def draw(self, surface, font):
		self.money.draw(surface, font)