# coding: utf-8

import os, pygame, xml

import geral

class Object:
	def __init__(self, id, pos, colisao, frames, size):
		self.pos = pos
		self.colisao = colisao
		self.frames = 0
		spritesheet = pygame.image.load(os.path.join('imagens', 'objetos', id + '.png'))
		spritesheet = pygame.transform.scale(spritesheet, [int(geral.px * i) for i in spritesheet.get_rect()][2:]).convert_alpha()
		if frames == 1:
			self.sprites = [spritesheet]
			return
		self.sprites = []
		for x in range(frames):
			rect = [(size[0] + 1) * x, 0, size[0], size[1]]
			rect = [geral.px * i for i in rect]
			self.sprites.append(spritesheet.subsurface(rect))

	@staticmethod
	def XML(node):
		id = node.getAttribute('id')
		x = int(node.getAttribute('x'))
		y = int(node.getAttribute('y'))
		try:
			frames = int(node.getAttribute('frames'))
		except:
			frames = 1
		if frames == 1:
			w = h = 0
		else:
			w = int(node.getAttribute('w'))
			h = int(node.getAttribute('h'))
		try:
			colisao = [[int(i) for i in node.getAttribute('colisao').split(',')]]
		except:
			colisao = []
		for elemento in node.childNodes:
			if elemento.nodeType != xml.dom.Node.ELEMENT_NODE:
				continue
			elif elemento.tagName == 'colisao':
				colisao.append([int(i) for i in elemento.getAttribute('colisao').split(',')])
			else:
				raise Exception
		object = Object(id, (x, y), colisao, frames, (w, h))
		return object

	def get_rect(self):
		return [i / geral.px for i in self.sprites[0].get_rect()]

	def render(self, screen):
		v = 12
		nframe = ((self.frames + v-1) / v) % len(self.sprites)
		pos = (self.pos[0] * geral.px,
		       (geral.lheight - self.pos[1] - self.get_rect()[3]) * geral.px)
		screen.blit(self.sprites[nframe], pos)
		self.frames += 1

	def input(self, events):
		pass

	def update(self):
		pass

