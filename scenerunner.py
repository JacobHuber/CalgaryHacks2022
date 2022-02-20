from enum import unique
import pygame, sys
from pygame.locals import *
from game import *
from infoMenu import InfoMenu
from mainMenu import *
from gameOver import *

global unique_Click
unique_Click = False

class SceneRunner:
	def __init__(self):
		self.name = "CalgaryHacks 2022"
		self.WIDTH = 1280
		self.HEIGHT = 720
		self.FPS = 60

		self.current_scene = 1

		self.songName = "spookysong.ogg"
		self.pygame_setup()
		self.scenes = [Game(self),MainMenu(self),InfoMenu(self)]
		self.scenes.append(GameOver(self))
		self.main_loop()

	def pygame_setup(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font("font.ttf", 32)
		pygame.mixer.music.load(self.songName, "ogg")
		pygame.mixer.music.play(loops=1, fade_ms=1000)

		
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
			for item in self.scenes[0].player.bars:
				if item.value == 0:
					self.scenes[3].updateScore()
					self.current_scene = 3
			pygame.display.update()
			self.clock.tick(self.FPS)
