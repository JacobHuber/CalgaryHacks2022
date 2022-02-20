import pygame, sys
from pygame.locals import *
from healthbar import *
from button import *
from minigamework import *
from minigamestudy import *

class Player:
	def __init__(self, game):
		self.game = game

		self.time = 0

		self.buttonWidth = 200
		self.buttonHeight = 60
		self.margin = 20 + self.buttonWidth

		self.buttonColors = [(100,255,100), (255,50,50), (0,255,255), (220,180,0)]

		self.fadeSurface = pygame.Surface((self.game.sr.WIDTH, self.game.sr.HEIGHT))
		self.fadeSurfaceRect = self.fadeSurface.get_rect()
		self.fadeSurface.fill((0,0,0))
		
		self.create_minigames()
		self.create_buttons()
		self.create_bars()

		# How much to decay each time
		self.decayAmount = 1

		# How many frames until decay
		self.decayTime = 0
		self.decayMax = 1 * self.game.sr.FPS

	def create_buttons(self):
		self.buttonNames = ["Work", "Eat", "Study", "Play"]
		self.buttonCallback = self.play_minigame

		mid_y = self.game.sr.HEIGHT // 2


		totalHeight = self.buttonHeight * len(self.buttonNames)

		start_x = self.game.sr.WIDTH - self.buttonWidth - 20
		start_y = mid_y - totalHeight // 2

		self.buttons = []
		for i in range(len(self.buttonNames)):
			newButton = Button(self.buttonNames[i], pygame.Rect(start_x, start_y + self.buttonHeight * i, self.buttonWidth, self.buttonHeight), self.buttonColors[i], self.buttonCallback)
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


		self.currentMinigame = 0
		self.minigames = []
		self.minigames.append(MinigameWork(self, self.gameSurface,self.buttonColors[0]))
		self.minigames.append(Minigame(self, self.gameSurface, self.buttonColors[1]))
		self.minigames.append(MinigameStudy(self, self.gameSurface,self.buttonColors[2]))
		self.minigames.append(Minigame(self, self.gameSurface,self.buttonColors[3]))

	def play_minigame(self, text):
		i = self.buttonNames.index(text)
		self.currentMinigame = i
		self.minigames[i].new_game()

		for button in self.buttons:
			button.off = True

	def end_minigame(self, gain):
		i = self.currentMinigame
		self.bars[i].increment(gain)

		for button in self.buttons:
			button.off = False

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

		self.minigames[self.currentMinigame].tick()

	def update_clock(self, surface, font):
		seconds = (self.time // self.game.sr.FPS) % 60
		minutes = (self.time // (self.game.sr.FPS * 60)) % 60

		text = f'{minutes:02}' + ":" + f'{seconds:02}'

		clockText = font.render(text, True, (255,255,255))
		clockTextRect = clockText.get_rect()
		clockTextRect.bottomright = (self.game.sr.WIDTH - 20, self.game.sr.HEIGHT - 20)
		surface.blit(clockText, clockTextRect)

	def get_faded_level(self):
		values = []
		for bar in self.bars:
			values.append(bar.value)


		level = min(min(values) / 50, 1)
		return 255 - int(level * 255)

	def draw(self, surface, font):
		self.update_clock(surface, font)

		for bar in self.bars:
			bar.draw(surface, font)

		for button in self.buttons:
			button.draw(surface, font)


		self.minigames[self.currentMinigame].draw(font)
		
		surface.blit(self.gameSurface, self.gameSurfaceRect)
		self.fadeSurface.set_alpha(self.get_faded_level())
		surface.blit(self.fadeSurface, self.fadeSurfaceRect)