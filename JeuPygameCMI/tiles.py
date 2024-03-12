import pygame
from support import *
from random import randint
from pathing import path


class Tile(pygame.sprite.Sprite):
    def __init__(self,size,x,y):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self,shift):
        self.rect.x+=shift #Deplace les sprites si besoint (scroll)

class StaticTile(Tile):     
    '''
    ICI Nous utilisons le principe d'heritage pour créer un Tile (et donc avoir accés a toute ses fonctions ) puis pouvoir le modifier
    c'est une sorte de Tile special . Par exemple une fois le Tile crée nous remplaçons self.image par notre surface
    '''
    def __init__(self, size, x, y,surface):
        super().__init__(size, x, y)
        self.image = surface

class CrateTile(StaticTile):
    '''
    ICI Nous utilisons aussi le principe d'heritage pour créer un StaticTile (et donc avoir accés a toute ses fonctions ) puis pouvoir le modifier
    et créer de nouvelle fonction speciale a ce type 
    '''
    def __init__(self, size, x, y):
        super().__init__(size, x, y,pygame.image.load(path+'/graphics/terrain/crate.png').convert_alpha())
        offset_y = y+size
        self.rect = self.image.get_rect(bottomleft = (x,offset_y))#Comme le sprite de la caisse fais seulement (48x48) pixel et que par default les surface sont placé en haut a gauche du rec notre caisse n'est pas collé au sol car elle ne touche pas le bas de la surface donc on la decale un peu vers le bas

class AnimatedTile(Tile):
    def __init__(self, size, x, y,path):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.frames_index = 0
        self.image = self.frames[self.frames_index]

    def animate(self):
        self.frames_index += 0.15 #On ajoute 0.15 toute les frames 
        if self.frames_index >= len(self.frames):#Si on a utilisé toute les images on recommence a 0
            self.frames_index = 0# Retour a 0 ducoup
        self.image =  self.frames[int(self.frames_index)] #choisis l'image qu'on vas afficher
    
    def update(self, shift):
        self.animate()
        self.rect.x+=shift #Deplace les sprites si besoint (scroll)

class Coin(AnimatedTile):
    def __init__(self, size, x, y, path,value):
        super().__init__(size, x, y, path)
        self.value = value
        center_x = x + int(size/2) #La coord au millieu de la surface pour les x 
        center_y = y + int(size/2) #La coord au millieu de la surface pour les y
        self.rect = self.image.get_rect(center = (center_x,center_y)) #Recentre la piece par rapport a la surface / au rect

class Palm(AnimatedTile):
    def __init__(self, size, x, y, path,offset):
        super().__init__(size, x, y, path)
        offset_y = y-offset #Meme principe que pour les caisses 
        self.rect.topleft = (x,offset_y)

class Enemy(AnimatedTile):
	def __init__(self,size,x,y,path333):
		super().__init__(size,x,y,path+path333)
		self.rect.y += size - self.image.get_size()[1] #Comme pour les autres lenemie est un peu trop haut et flotte on le baisse donc un peu
		self.speed = randint(3,5) #Choisis une vitesse aleatoire entre 3 et 5

	def move(self):
		self.rect.x += self.speed #Deplace l'enemie de sa vitesse case

	def reverse_image(self):
		if self.speed > 0:
			self.image = pygame.transform.flip(self.image,True,False) #Si il court vers la droite on dait la symetrique de l'image par rapport a laxe des ordonné (on le tourne vers la droite quoi)

	def reverse(self):
		self.speed *= -1 #Inverse la direction

	def update(self,shift):
		self.rect.x += shift
		self.animate()
		self.move()
		self.reverse_image()

class Enemy2(AnimatedTile):
	def __init__(self, position, size,path333):
		super().__init__(size, position[0], position[1], path333)
		self.rect.y += size - self.image.get_size()[1]
		self.velocity = 4

	def move(self):
		self.rect.x += self.velocity
		if self.velocity < 0:
			self.image = pygame.transform.flip(self.image, True, False)

	def reverse(self):
		self.velocity *= -1

	def update(self, x_shift):
		self.rect.x += x_shift
		self.animate()
		self.move()

