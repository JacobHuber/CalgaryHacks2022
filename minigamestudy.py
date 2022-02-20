import pygame, sys
from pygame.locals import *
from minigame import *
from random import *
from math import *
from button import *

class MinigameStudy(Minigame):
	def __init__(self, player, surface, color):
		Minigame.__init__(self, player, surface, color)
		self.games = [MathGame(self), GeographyGame(self)]

def mul(a,b):
	return a * b

def add(a,b):
	return a + b

def sub(a,b):
	return a - b

class MathGame:
	def __init__(self, mg):
		self.mg = mg		
		self.questionValue = 10

		self.gain = 0
		self.end = False

		self.question = ""
		self.answer = 0
		self.answers = []
		self.buttons = []

	def setup(self):
		self.end = False
		self.gain = 0
		self.answers = []
		self.buttons = []

		a = randint(1,9)
		b = randint(1,9)
		op = choice([(mul, "x"), (add, "+"), (sub, "-")])
		self.answer = op[0](a,b)
		self.question = "{0} {2} {1} =".format(a,b,op[1])
		self.answers.append(self.answer)
		self.answers.append(randint(2,81))
		self.answers.append(randint(2,81))
		shuffle(self.answers)

		for i in range(len(self.answers)):
			buttonHeight = 40
			buttonWidth = 100
			colWidth = self.mg.width // 3
			x = (colWidth // 2) - (buttonWidth // 2) + (i * colWidth)
			y = self.mg.height - 80
			button = Button(str(self.answers[i]), (x, y, buttonWidth, buttonHeight), (0,0,0), self.check_answer)
			self.buttons.append(button)

	def check_answer(self, text):
		if (text == str(self.answer)):
			self.gain = self.questionValue
		else:
			self.gain = -self.questionValue
		
		self.end = True

	def tick(self):
		for button in self.buttons:
			button.tick(self.mg.get_mouse())

	def draw(self, surface, font):
		self.answerText = font.render(self.question, True, (255,255,255))
		self.answerTextRect = self.answerText.get_rect()
		self.answerTextRect.center = (self.mg.width // 2, self.mg.height // 3)
		surface.blit(self.answerText, self.answerTextRect)

		for button in self.buttons:
			button.draw(surface, font)

class GeographyGame:
	def __init__(self, mg):
		self.mg = mg
		
		self.questionValue = 3

		self.mouse_down = False
		self.gain = 0
		self.end = False

		self.image = pygame.image.load("pictures/newzealand.png", "png")
		self.imageRect = self.image.get_rect()
		self.imageRect.center = (self.mg.width // 2, self.mg.height // 2)
		self.question = "What country is this?"
		self.answer = "New Zealand"
		self.countries = ["Armenia", "Egypt", "Finland", "France", "Iceland", "India", "Japan", "Madagascar", "Lithuania", "Nigeria", "North Korea", "Norway", "Russia", "Saudi Arabia", "	South Africa", "South Korea", "Sweden", "Spain", "Sri Lanka", "	Thailand", "Turkey", "United Kingdom", "Vietnam"]
		self.answers = []
		self.buttons = []

	def setup(self):
		self.gain = 0
		self.end = False
		self.answers = []
		self.buttons = []

		self.answers.append(self.answer)
		self.answers.append(choice(self.countries))
		self.answers.append(choice(self.countries))
		shuffle(self.answers)

		for i in range(len(self.answers)):
			buttonHeight = 40
			buttonWidth = 200
			colWidth = self.mg.width // 3
			x = (colWidth // 2) - (buttonWidth // 2) + (i * colWidth)
			y = self.mg.height - 80
			button = Button(str(self.answers[i]), (x, y, buttonWidth, buttonHeight), (0,0,0), self.check_answer)
			self.buttons.append(button)

	def check_answer(self, text):
		if (text == str(self.answer)):
			self.gain = self.questionValue
		else:
			self.gain = -self.questionValue
		
		self.end = True

	def tick(self):
		for button in self.buttons:
			button.tick(self.mg.get_mouse())

	def draw(self, surface, font):
		self.answerText = font.render(self.question, True, (255,255,255))
		self.answerTextRect = self.answerText.get_rect()
		self.answerTextRect.center = (self.mg.width // 2, self.mg.height // 4)
		surface.blit(self.answerText, self.answerTextRect)

		surface.blit(self.image, self.imageRect)

		for button in self.buttons:
			button.draw(surface, font)