from selectors import SelectorKey
import pygame
from utilities import graphic_folders
from pathing import path

class Particles(pygame.sprite.Sprite):
    def __init__(self, surface):

        #basics
        self.display = surface
        self.import_particles()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['run'][self.frame_index]

    #importation des textures dans un dictionnaire
    def import_particles(self):
        pathDust = path+'/graphics/character/dust_particles/'
        self.animations = {'jump' : [], 'land' : [], 'run' : []}

        for animation in self.animations.keys():
            self.animations[animation] = graphic_folders(pathDust+animation)
    
    #fonction des particules de course utilisée dans player.py
    def run_particles(self):
        animation = self.animations['run']

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]

    #ces deux fonctions sont là au cas ou on a le temps de les faire (ce qui je pense sera le cas mais ça n'est pas urgent)
    def jump_particles(self):
        animation = self.animations['jump']
    
    def land_particles(self):
        animation = self.animations['jump']