import pygame
from utilities import graphic_folders
from pathing import path

class Attack(pygame.sprite.Sprite):
    def __init__(self, surface):
        #basics
        self.display = surface
        self.import_attack()
        self.image = self.animations[0]
        self.rect = self.image.get_rect()

        #importation des textures
    def import_attack(self):
        pathAttack = path+'/graphics/attack/'
        self.animations = graphic_folders(pathAttack)

        #animation de l'attaque
    def attaquedroite(self, position):
        self.image = self.animations[0]
        self.rect = self.image.get_rect(topleft = position)

    def attaquegauche(self, position):
        self.image = pygame.transform.flip(self.animations[0], True, False)
        self.rect = self.image.get_rect(topright = position)