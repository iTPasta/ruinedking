from map_setup import vertical_tile_number, tile_size, wid
import pygame
from tiles import AnimatedTile, StaticTile
from support import import_folder
from random import choice, randint
from pathing import path

class Sky:
	def __init__(self,horizon):
		self.top = pygame.image.load(path+'/graphics/decoration/sky/sky_top.png').convert()
		self.bottom = pygame.image.load(path+'/graphics/decoration/sky/sky_bottom.png').convert()
		self.middle = pygame.image.load(path+'/graphics/decoration/sky/sky_middle.png').convert()
		self.horizon = horizon

		# stretch 
		self.top = pygame.transform.scale(self.top,(wid,tile_size))
		self.bottom = pygame.transform.scale(self.bottom,(wid,tile_size))
		self.middle = pygame.transform.scale(self.middle,(wid,tile_size))

	def draw(self,surface):
		for row in range(vertical_tile_number):
			y = row * tile_size
			if row < self.horizon:
				surface.blit(self.top,(0,y))
			elif row == self.horizon:
				surface.blit(self.middle,(0,y))
			else:
				surface.blit(self.bottom,(0,y))


class Water:
	def __init__(self,top,level_width):
		water_start = -wid
		water_tile_width = 192
		tile_x_amount = int((level_width + wid * 2) / water_tile_width)
		self.water_sprites = pygame.sprite.Group()

		for tile in range(tile_x_amount):
			x = tile * water_tile_width + water_start
			y = top
			sprite = AnimatedTile(192,x,y,path+'/graphics/decoration/water')
			self.water_sprites.add(sprite)

	def draw(self,surface,shift):
		self.water_sprites.update(shift)
		self.water_sprites.draw(surface)

class Clouds:
	def __init__(self,horizon,level_width,cloud_number):
		cloud_surf_list = import_folder(path+'/graphics/decoration/clouds')
		min_x = -wid
		max_x = level_width + wid
		min_y = 0
		max_y = horizon
		self.cloud_sprites = pygame.sprite.Group()

		for cloud in range(cloud_number):
			cloud = choice(cloud_surf_list)
			x = randint(min_x,max_x)
			y = randint(min_y,max_y)
			sprite = StaticTile(0,x,y,cloud)
			self.cloud_sprites.add(sprite)

	def draw(self,surface,shift):
		self.cloud_sprites.update(shift)
		self.cloud_sprites.draw(surface)

class SBMouvant:
	def __init__(self, top, level_width):
		start =  -wid
		tile_width = 192
		tile_amount = int((level_width + wid) / tile_width)
		self.sprite = pygame.sprite.Group()

		for tile in range(tile_amount):
			x = tile*tile_width + start
			y = top
			sprite = AnimatedTile(192, x, y, './graphics/decoration/sables mouvants')
			self.sprite.add(sprite)

	def update(self, surface, x_shift):
		self.sprite.update(x_shift)
		self.sprite.draw(surface)