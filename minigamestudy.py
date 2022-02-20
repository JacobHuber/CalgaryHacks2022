import pygame, sys
from pygame.locals import *
from minigame import *
from random import *
from math import *
from button import *

class MinigameStudy(Minigame):
	def __init__(self, player, surface, color):
		Minigame.__init__(self, player, surface, color)
		self.games = [MathGame(self), HardMath(self), GeographyGame(self),TypingGame(self)]

def mul(a,b):
	return a * b

def add(a,b):
	return a + b

def sub(a,b):
	return a - b

class MathGame:
	def __init__(self, mg):
		self.mg = mg
		self.gameTitle = "Everyone Loves Math"
		self.subtitle = "no they don't"
		self.questionValue = 10

		self.gain = [0,0,0,0]
		self.end = False

		self.question = ""
		self.answer = 0
		self.answers = []
		self.buttons = []

	def setup(self):
		self.end = False
		self.gain = [0,0,0,0]
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
			self.gain[2] = self.questionValue
		else:
			self.gain[2] = -self.questionValue
		
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

class HardMath:
	def __init__(self, mg):
		self.gameTitle = "AlgeBruh"
		self.subtitle = "Now it's a little harder!"
		self.questionValue = 20
		self.mg = mg
		self.gain = [0,0,0,0]
		self.end = False

		self.question = ""
		self.answer = 0
		self.answers = []
		self.buttons = []

	def setup(self):
		self.end = False
		self.gain = [0,0,0,0]
		self.answers = []
		self.buttons = []

		a = randint(1,7) # coefficient
		b = randint(1,7) # term
		c = randint(1,7) # rhs

		operators = [(add, "+"), (sub, "-")]
		op = choice(operators)
		other = operators[(operators.index(op) + 1) % len(operators)]
		c = op[0]((c * a), b)

		self.answer = int(other[0](c ,b) / a)
		self.question = "{0}a {1} {2} = {3}".format(a,op[1],b,c)
		self.answers.append(self.answer)
		self.answers.append(randint(1,10))
		self.answers.append(randint(1,10))
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
			self.gain[2] = self.questionValue
		else:
			self.gain[2] = -self.questionValue
		
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
		self.gameTitle = "New Zealand"
		self.subtitle = "which country could it be?"
		self.mg = mg
		
		self.questionValue = 3

		self.mouse_down = False
		self.gain = [0,0,0,0]
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
		self.gain = [0,0,0,0]
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
			self.gain[2] = self.questionValue
		else:
			self.gain[2] = -self.questionValue
		
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



class TypingGame:
	def __init__(self,mg):
		self.gameTitle = "Typing Test!!"
		self.subtitle = "type the word correctly"
		self.mg = mg
		self.gain = [0,0,0,0]
		self.end = False
		self.text = ""
		self.dum_text = list("")
		self.current_letter = ''
		self.current_index = 0
		self.possibleText = [list("Type this for a B"),list("Type this for an A"),list("Where is New Zealand"),list("The mitochondria is the power house of the cell"),list("I LOVE BEAN BURRITOS"),list("Where is my chicken statue"),list("UCalgary Dating Sim when")]

		self.cursor_blink = True
		self.cursor_speed = 0.5 * self.mg.player.game.sr.FPS

	def setup(self):
		
		self.text = choice(self.possibleText)
		self.dum_text = list("")
		self.end = False
		self.gain[2] = len(self.text)//2
		self.current_letter = ''
		self.current_index = 0

		self.current_letter = self.text[0]

	def nextLetter(self):
		self.dum_text.append(self.current_letter)
		if(self.current_index+1 == (len(self.text))):
			self.end = True
			return
		self.current_index+=1
		self.current_letter = self.text[self.current_index]

	def tick(self):
		for events in self.mg.player.pressedKeys:
			if (events.key >= K_a and events.key <= K_z or events.key == K_SPACE):
				if events.unicode == self.current_letter:
					self.nextLetter()

		if (self.mg.player.time % self.cursor_speed == 0):
			self.cursor_blink = not self.cursor_blink

	def draw(self,surface,font):
		self.answerText = font.render("".join(self.text), True, (255,255,255))
		self.answerTextRect = self.answerText.get_rect()
		self.answerTextRect.center = (self.mg.width // 2, self.mg.height // 4)
		surface.blit(self.answerText, self.answerTextRect)

		self.dum_Text = font.render(">" + "".join(self.dum_text), True, (0,255,0))
		self.dum_TextRect = self.dum_Text.get_rect()
		self.dum_TextRect.midleft = (self.answerTextRect.left, self.mg.height // 4+200)
		surface.blit(self.dum_Text, self.dum_TextRect)

		sx = self.dum_TextRect.right
		sy = self.dum_TextRect.bottom - 5
		if (self.cursor_blink):
			pygame.draw.line(surface, (0,255,0), (sx, sy), (sx + 10, sy))