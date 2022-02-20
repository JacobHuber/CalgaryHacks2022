import pygame, sys
from pygame.locals import *
from minigame import *
from random import *
from math import *

class MinigamePlay(Minigame):
	def __init__(self, player, surface, color):
		Minigame.__init__(self, player, surface, color)
		self.games = []