import pygame, sys
from pygame.locals import *
from game import *

class SceneRunner:
	def __init__(self):
		self.name = "CalgaryHacks 2022"
		self.WIDTH = 1280
		self.HEIGHT = 720
		self.FPS = 60

		self.current_scene = 0
		self.scenes = [Game(self)]

		self.pygame_setup()
		self.main_loop()

	def pygame_setup(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font("font.ttf", 32)
		
		pygame.display.set_caption(self.name)

	def main_loop(self):
		while True:
			scene = self.scenes[self.current_scene]

			self.display_surface.fill((0,0,0))

			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

			for item in scene.tickables:
				item.tick()

			for item in scene.drawables:
				item.draw(self.display_surface, self.font)

			pygame.display.update()
			self.clock.tick(self.FPS)
