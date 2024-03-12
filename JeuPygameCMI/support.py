from csv import reader
from map_setup import tile_size
from os import walk
import pygame
from pathing import path

def import_folder(path):
	surface_list = []

	for _,__,image_files in walk(path):
		for image in image_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list

def import_csv_layout(path): #Créer un layout qui contient toute les coordonné ou ont étais placé nos element (lors de la creation avec le logiciel Tiled) (list des lignes) et l'ID de la tuile sur cette coord (meme fonctionnement que la map)
	terrain_map = []
	with open(path) as map:
		level = reader(map,delimiter = ',')
		for row in level:
			terrain_map.append(list(row))
		return terrain_map

imported_cut_graphics = {} 

def import_cut_graphics(path):
	if imported_cut_graphics.__contains__(path):
		return imported_cut_graphics[path]
	
	else:
		surface = pygame.image.load(path).convert_alpha()
		tile_num_x = int(surface.get_size()[0] / tile_size)
		tile_num_y = int(surface.get_size()[1] / tile_size)

		cut_tiles = []
		#fonctionnement similaire a create_tile_group() pour les boucles 
		for row in range(tile_num_y):
			for col in range(tile_num_x):
				x = col * tile_size
				y = row * tile_size
				new_surf = pygame.Surface((tile_size,tile_size),flags = pygame.SRCALPHA)
				new_surf.blit(surface,(0,0),pygame.Rect(x,y,tile_size,tile_size)) 
				cut_tiles.append(new_surf)

		imported_cut_graphics[path] = cut_tiles
		return cut_tiles

