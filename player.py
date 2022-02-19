import pygame, sys
from pygame.locals import *
from healthbar import *
from button import *
from minigamework import *

class Player:
	def __init__(self, game):
		self.game = game

		self.time = 0

		self.buttonWidth = 200
		self.buttonHeight = 60
		self.margin = 20 + self.buttonWidth

		
		self.create_buttons()
		self.create_bars()
		self.create_minigames()

		# How much to decay each time
		self.decayAmount = 1

		# How many frames until decay
		self.decayTime = 0
		self.decayMax = 1 * self.game.sr.FPS

	def create_buttons(self):
		self.buttonNames = ["Work", "Eat", "Study", "Play"]
		self.buttonColors = [(100,255,100), (255,50,50), (0,255,255), (220,180,0)]
		self.buttonCallback = [print, print, print, print]

		mid_y = self.game.sr.HEIGHT // 2


		totalHeight = self.buttonHeight * len(self.buttonNames)

		start_x = self.game.sr.WIDTH - self.buttonWidth - 20
		start_y = mid_y - totalHeight // 2

		self.buttons = []
		for i in range(len(self.buttonNames)):
			newButton = Button(self.buttonNames[i], pygame.Rect(start_x, start_y + self.buttonHeight * i, self.buttonWidth, self.buttonHeight), self.buttonColors[i], self.buttonCallback[i])
			self.buttons.append(newButton)

	def create_bars(self):
		self.barNames = ["Money", "Food", "Grades", "Happiness"]
		self.barValues = [(60, 100), (100, 100), (50, 100), (50, 100)]

		mid_y = self.game.sr.HEIGHT // 2

		totalHeight = self.buttonHeight * len(self.barNames)

		start_x = 20
		start_y = mid_y - totalHeight // 2

		self.bars = []
		for i in range(len(self.barNames)):
			newBar = Healthbar(pygame.Rect(start_x, start_y + self.buttonHeight * i, self.buttonWidth, 20), self.buttonColors[i], self.barNames[i], self.barValues[i])
			self.bars.append(newBar)

	def create_minigames(self):
		sideLength = min(self.game.sr.HEIGHT, self.game.sr.WIDTH - self.margin * 2)
		self.gameSurfaceRect = pygame.Rect( (self.game.sr.WIDTH // 2) - sideLength // 2, 0, sideLength, sideLength )
		self.gameSurface = pygame.Surface((sideLength, sideLength))
		self.gameSurface.fill((20,20,20))


		self.currentMinigame = 1
		self.minigames = []
		self.minigames.append(MinigameWork(self.buttonColors[0]))
		self.minigames.append(Minigame(self.buttonColors[1]))
		self.minigames.append(Minigame(self.buttonColors[2]))
		self.minigames.append(Minigame(self.buttonColors[3]))

	def decayBars(self):
		for bar in self.bars:
			bar.decrement(self.decayAmount)

	def buyFood(self):
		pass

	def tick(self):
		self.time += 1
		if (self.time % self.decayMax == 0):
			self.decayBars()

		for button in self.buttons:
			button.tick()

			if (pygame.mouse.get_pressed()[0]):
				button.off = True
			else:
				button.off = False

	def update_clock(self, surface, font):
		seconds = (self.time // self.game.sr.FPS) % 60
		minutes = (self.time // (self.game.sr.FPS * 60)) % 60

		text = f'{minutes:02}' + ":" + f'{seconds:02}'

		clockText = font.render(text, True, (255,255,255))
		clockTextRect = clockText.get_rect()
		clockTextRect.bottomright = (self.game.sr.WIDTH - 20, self.game.sr.HEIGHT - 20)
		surface.blit(clockText, clockTextRect)

	def draw(self, surface, font):
		self.update_clock(surface, font)

		for bar in self.bars:
			bar.draw(surface, font)

		for button in self.buttons:
			button.draw(surface, font)

		
		self.minigames[self.currentMinigame].draw(self.gameSurface, font)
		
		surface.blit(self.gameSurface, self.gameSurfaceRect)