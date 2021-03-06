from enum import unique
import pygame, sys
from pygame.locals import *
from game import *
from infoMenu import InfoMenu
from mainMenu import *
from gameOver import *
from newDay import *
from particle import *

global unique_Click

class SceneRunner:
	def __init__(self):
		global unique_Click
		unique_Click = False
		self.name = "Homework Please"
		self.WIDTH = 1280
		self.HEIGHT = 720
		self.FPS = 60
		self.particles = []
		self.create_particles()

		self.current_scene = 1

		self.songName = "spookysong"
		self.songEndings = ["ogg", "mp3"]
		self.pygame_setup()
		self.scenes = [Game(self),MainMenu(self),InfoMenu(self)]
		self.scenes.append(GameOver(self))
		self.scenes.append(NewDay(self))
		self.main_loop()


	def create_particles(self):
		for i in range(20):
			self.particles.append(Particle(self))

	def pygame_setup(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font("font.ttf", 32)
		try:
			ending = self.songEndings[0]
			pygame.mixer.music.load("{0}.{1}".format(self.songName, ending), self.songEndings[0])
		except:
			ending = self.songEndings[1]
			pygame.mixer.music.load("{0}.{1}".format(self.songName, ending), self.songEndings[1])
		pygame.mixer.music.play(loops=-1, fade_ms=1000)
		pygame.mixer.music.set_volume(0.2)

		
		pygame.display.set_caption(self.name)

	def main_loop(self):
		while True:
			scene = self.scenes[self.current_scene]

			self.display_surface.fill((0,0,0))

			for particle in self.particles:
				particle.tick()
				particle.draw(self.display_surface)

				if (particle.shouldRemove()):
					self.particles.remove(particle)
					self.particles.append(Particle(self))

			keysThatAreDown = []
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					keysThatAreDown.append(event)

			self.scenes[0].player.pressedKeys = keysThatAreDown

			for item in scene.tickables:
				item.tick()

			for item in scene.drawables:
				item.draw(self.display_surface, self.font)
			
			if (self.current_scene == 0):
				for item in self.scenes[0].player.bars:
					if item.value == 0:
						self.scenes[3].updateScore()
						self.scenes[0].create_player()
						self.current_scene = 3

			

			pygame.display.update()
			self.clock.tick(self.FPS)
