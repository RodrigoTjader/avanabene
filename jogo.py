#! /usr/bin/env python
# coding: utf-8

import os, sys, pygame, random, datetime
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Aventuras de Ananias e Benevides') 

def gerafundo():
	pasto = pygame.image.load("images/t_grama.png")
	pasto = pygame.transform.scale(pasto, [4 * i for i in pasto.get_rect()][2:]).convert_alpha()
	pastorect = pasto.get_rect()
	fro = pygame.image.load("images/t_gramaflor.png")
	fro = pygame.transform.scale(fro, [4 * i for i in fro.get_rect()][2:]).convert_alpha()
	fundo = pygame.Surface(size)

	for i in range(0, size[0], pastorect[2]):
		for j in range(0, size[1], pastorect[3]):
			if random.random() > 0.92:
				fundo.blit(fro, (i, j))
			else:
				fundo.blit(pasto, (i, j))
	return fundo

fundo = gerafundo()

import actor
ananias = actor.Actor('ananias', (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN))
benevides = actor.Actor('benevides', (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s))

tela = [0, 0]
txt = pygame.font.Font('unifont-5.1.20080820.pcf', 16).render(repr(tela), False, (255, 255, 255))
txt = pygame.transform.scale(txt, [4 * i for i in txt.get_rect()][2:])

pygame.mixer.music.load(os.path.join('music', 'lojinha song.mp3'))
pygame.mixer.music.play(-1)

tempo = pygame.time.Clock()

while True:
	events = pygame.event.get()
	ananias.input(events)
	benevides.input(events)
	for event in events:
		if event.type == pygame.QUIT \
		   or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			sys.exit()

	ananias.update()
	benevides.update()

	def mudatela(actor, outro):
		if actor.pos[0] + actor.sprites[0].get_rect()[2] <= 0:
			actor.pos[0] += size[0]
			outro.pos[0] = actor.pos[0] - actor.sprites[0].get_rect()[2]
			outro.pos[1] = actor.pos[1]
			tela[0] -= 1
		elif actor.pos[0] >= size[0]:
			actor.pos[0] -= size[0]
			outro.pos[0] = actor.pos[0] + actor.sprites[0].get_rect()[2]
			outro.pos[1] = actor.pos[1]
			tela[0] += 1
		elif actor.pos[1] + actor.sprites[0].get_rect()[3] <= 0:
			actor.pos[1] += size[1]
			outro.pos[0] = actor.pos[0]
			outro.pos[1] = actor.pos[1] - actor.sprites[0].get_rect()[3]
			tela[1] -= 1
		elif actor.pos[1] >= size[1]:
			actor.pos[1] -= size[1]
			outro.pos[0] = actor.pos[0]
			outro.pos[1] = actor.pos[1] + actor.sprites[0].get_rect()[3]
			tela[1] += 1
		else:
			return
		global fundo, txt
		fundo = gerafundo()
		txt = pygame.font.Font('unifont-5.1.20080820.pcf', 16).render(repr(tela), False, (255, 255, 255))
		txt = pygame.transform.scale(txt, [4 * i for i in txt.get_rect()][2:])
		print tela

	mudatela(ananias, benevides)
	mudatela(benevides, ananias)

	screen.blit(fundo, (0, 0))
	screen.blit(txt, [4 * i for i in (size[0] / 8 - txt.get_rect()[2] / 8, size[1] / 8 - txt.get_rect()[3] / 8)])
	ananias.render(screen)
	benevides.render(screen)
	pygame.display.flip()

	tempo.tick(60)
#	print tempo.get_fps(), 'QPS'

