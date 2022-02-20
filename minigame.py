import pygame, sys
from pygame.locals import *
from random import *
from math import *

class Minigame:
	def __init__(self, player, surface, color):
		self.player = player
		self.surface = surface
		self.color = color

		dims = surface.get_rect()
		self.width = dims.width
		self.height = dims.height

		self.current_game = 0
		self.end = True
		self.games = []

		self.titleTime = 0
		self.titleMax = 0.8 * self.player.game.sr.FPS

		self.BIGFONT = pygame.font.Font("font.ttf", 64)


		self.shouldDraw = False

	def new_game(self):
		self.end = False
		self.showTitle = True
		self.shouldDraw = False
		self.titleTime = 0
		self.current_game = randrange(0, len(self.games))
		self.games[self.current_game].setup()

	def get_mouse(self):
		mouse = pygame.mouse.get_pos()
		left = self.player.gameSurfaceRect.left
		x = mouse[0] - left
		x = min(x, self.width)

		top = self.player.gameSurfaceRect.top
		y = mouse[1] - top
		y = min(y, self.height)

		return (x,y)

	def tick(self):
		if (not self.end):
			if (self.showTitle):
				self.titleTime += 1
				if (self.titleTime >= self.titleMax):
					self.showTitle = False
			else:
				game = self.games[self.current_game]
				game.tick()
				self.shouldDraw = True

				if (game.end):
					self.player.end_minigame(game.gain)
					self.end = True

	def draw_title_screen(self, font):
		game = self.games[self.current_game]
		self.title = self.BIGFONT.render(game.gameTitle, True, (255,255,255))
		self.titleRect = self.title.get_rect()
		self.titleRect.center = (self.width // 2, self.height // 2)
		self.surface.blit(self.title, self.titleRect)

		self.subtitle = font.render(game.subtitle, True, (255,255,255))
		self.subtitleRect = self.subtitle.get_rect()
		self.subtitleRect.center = (self.width // 2, self.height // 2 + 40)
		self.surface.blit(self.subtitle, self.subtitleRect)


	def draw(self, font):
		self.surface.fill((20,20,20))

		if (not self.end):
			if (self.showTitle):
				self.draw_title_screen(font)
			elif (self.shouldDraw):
				self.games[self.current_game].draw(self.surface, font)
		
		pygame.draw.rect(self.surface, self.color, (0,0,self.width,self.height), 4)