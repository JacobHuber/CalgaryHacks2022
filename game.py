import pygame, sys
from pygame.locals import *
from button import *
from player import *

class Game:

	def __init__(self):
		self.name = "CalgaryHacks 2022"
		self.WIDTH = 1280
		self.HEIGHT = 720
		self.FPS = 60
		self.tickables = []
		self.drawables = []

		self.pygame_setup()
		self.create_buttons()
		self.create_player()
		self.main_loop()

	def pygame_setup(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font("font.ttf", 32)
		
		pygame.display.set_caption(self.name)

	def create_buttons(self):
		testButton = Button("Test", pygame.Rect(200, 200, 200, 100), (100, 150, 20), print)

		self.tickables.append(testButton)
		self.drawables.append(testButton)

	def create_player(self):
		self.player = Player()

		self.drawables.append(self.player)

	def main_loop(self):
		while True:
			self.display_surface.fill((0,0,0))

			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

			for item in self.tickables:
				item.tick()

			for item in self.drawables:
				item.draw(self.display_surface, self.font)

			pygame.display.update()
			self.clock.tick(self.FPS)
