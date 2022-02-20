import pygame, sys
from pygame.locals import *
from random import *
from math import *

class Particle:
	def __init__(self, sr):
		self.sr = sr
		self.color = (255,255,255)
		
		margin = 20
		side = choice((True, False))
		x = 0
		y = 0
		if (side):
			x = choice((-margin, self.sr.WIDTH + margin))
			y = randint(0, self.sr.HEIGHT)
		else:
			x = randint(0, self.sr.WIDTH)
			y = choice((-margin, self.sr.HEIGHT + margin))
		self.x = x
		self.y = y
		self.r = randint(1,8)
		self.xs = randint(-10, 10)
		self.ys = randint(-10, 10)

		self.offset1 = (randint(-4,4), randint(-4,4))
		self.offset2 = (randint(-4,4), randint(-4,4))

	def shouldRemove(self):
		if (self.x < -100 or self.x > self.sr.WIDTH + 100):
			return True

		if (self.y < -100 or self.y > self.sr.HEIGHT + 100):
			return True

		return False

	def tick(self):
		self.x += self.xs
		self.y += self.ys

	def draw(self, surface):
		pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)
		pygame.draw.circle(surface, self.color, (self.x + self.offset1[0], self.y + self.offset1[1]), self.r)
		pygame.draw.circle(surface, self.color, (self.x + self.offset2[0], self.y + self.offset2[1]), self.r)
