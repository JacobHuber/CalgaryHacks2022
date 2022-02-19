import pygame, sys
from pygame.locals import *

class Game:

	def __init__(self):
		self.name = "CalgaryHacks 2022"
		self.WIDTH = 400
		self.HEIGHT = 400

		self.pygame_setup()
		self.main_loop()

	def pygame_setup(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = pygame.time.Clock()
		
		pygame.display.set_caption(self.name)


	def main_loop(self):
		while True:
			self.display_surface.fill((0,0,0))

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
