# coding: utf-8

import os, pygame

import geral

class Tile:
	def __init__(self, id, pos, size):
		self.sprite = pygame.image.load(os.path.join('imagens', 'tiles', id + '.png'))
		self.sprite = pygame.transform.scale(self.sprite, [int(geral.px * i) for i in self.sprite.get_rect()][2:]).convert_alpha()
		self.pos = pos
		self.size = size
		ladrilhorect = self.sprite.get_rect()
		self.spritemesmo = pygame.Surface((self.size[0] * ladrilhorect[2], self.size[1] * ladrilhorect[3])).convert_alpha()
		self.spritemesmo.fill((0,0,0,0))
		for i in range(size[0]):
			for j in range(size[1]):
				self.spritemesmo.blit(self.sprite, (i * ladrilhorect[2], j * ladrilhorect[3]))

	@staticmethod
	def XML(node):
		id = node.getAttribute('id')
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		try:
			w = int(node.getAttribute('w'))
		except ValueError:
			w = 1
		try:
			h = int(node.getAttribute('h'))
		except ValueError:
			h = 1
		tile = Tile(id, (x, y), (w, h))
		return tile

	def get_rect(self):
		return [i / geral.px for i in self.spritemesmo.get_rect()]

	def render(self, screen):
		pos = (self.pos[0] * geral.px,
		       (geral.lheight - self.pos[1] - self.get_rect()[3]) * geral.px)
		screen.blit(self.spritemesmo, pos)

	def input(self, events):
		pass

	def update(self):
		pass

