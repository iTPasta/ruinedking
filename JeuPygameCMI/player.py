import pygame
from particles import Particles
from attack import Attack
from utilities import graphic_folders
from pathing import path
import sys
from map_setup import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, surface):
        super().__init__()

        #Attribut Ingame
        self.base_health = 30
        self.pv = self.base_health
        self.Ingame = True

        #animation et graphismes du personnage
        self.display = surface
        self.state = 'idle'
        self.import_graphics()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]       
        self.rect = self.image.get_rect(topleft = position)

        
        #déplacements du personnage
        self.direction = pygame.math.Vector2(0,0)
        self.velocity = 6
        self.get_gravity = 0.8
        self.jump = -16

        #états du personnage
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.attack = False
        self.attack_cooldown = 0
        
        #ajout des particules de poussière
        self.particles = Particles(self.display)

        #ajout de la trainée d'attaque
        self.attack_zone = Attack(self.display)

    #fonction d'importation des textures
    def import_graphics(self):
        pathPlayer = path+'/graphics/character/'
        
        self.animations = {'idle' : [], 'jump' : [], 'run' : [], 'fall' : [], 'attack' : []}

        for animation in self.animations.keys():
            self.animations[animation] = graphic_folders(pathPlayer+animation) #voir utilities.py
    
    #animation du personnage
    def animate(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        animation = self.animations[self.state] #récupération de l'état (run, idle, jump, fall)
        self.frame_index += self.animation_speed #augmentation de la frame d'animation
        if self.frame_index >= len(animation):
            self.frame_index = 0

        #reinisialisation des états d'attaque (pour que l'animation ne se répete pas)
        if animation[int(self.frame_index)] == self.animations['attack'][-1]:
            self.attack = False

        image = animation[int(self.frame_index)] #modification de l'image à chaque tick
        
        #vérification de la direction (si le personnage va vers la gauche, flip l'image)
        if self.facing_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)
        
        #hitboxes pour les collisions
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        else:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
    
    #movement (gauche, droite, haut, bas)
    def movement(self):
        #détection de la touche pressée
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            self.do_jump()
        if keys[pygame.K_e] and self.on_ground:
            if self.attack_cooldown == 0:
                self.attack = True
                self.attack_cooldown = 15

    #récupération de l'état du personnage en fonction de ses déplacement, s'il va vers le haut, alors il saute.
    def get_state(self):
        if self.attack:
            self.state = 'attack'
        else:
            if self.direction.y < 0:
                self.state = 'jump'
            elif self.direction.y > 1:
                self.state = 'fall'
            else:
                if self.direction.x != 0:
                    self.state = 'run'
                else:
                    self.state = 'idle'
    
    #application de la gravité
    def gravity(self):
        self.direction.y += self.get_gravity
        self.rect.y += self.direction.y
    
    #fonction de saut UNIQUEMENT si le joueur est sur le sol
    def do_jump(self):
        if self.on_ground:
            self.direction.y = self.jump

    #ajout des particules via la classe Particles (voir particles.py)
    def add_dust(self):
        ajustement = pygame.math.Vector2(7,10)
        if self.state == 'run' and self.on_ground:
            self.particles.run_particles()
            if self.facing_right:
                pos = self.rect.bottomleft - ajustement
                self.display.blit(self.particles.image, pos)
            else:
                pos = self.rect.bottomright - ajustement
                self.display.blit(pygame.transform.flip(self.particles.image, True, False), pos)

    def add_attack(self):
        ajustement1 = pygame.math.Vector2(0,-20)
        ajustement2 = pygame.math.Vector2(120,-20)
        if self.attack:
            if self.facing_right:
                pos = self.rect.topright - ajustement1
                self.attack_zone.attaquedroite(pos)
                self.display.blit(self.attack_zone.image, pos)
            else:
                pos = self.rect.topright - ajustement2
                self.attack_zone.attaquegauche(pos)
                self.display.blit(self.attack_zone.image, pos)
        else:
            self.attack_zone.rect = self.attack_zone.image.get_rect(topleft = (0, 0))

    def check(self,enemy_sprites,moi,arrivé,coin_sprites,compteurPiece):
        for enemy in  enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,moi,False): #Si il est en colision avec le player
                moi.sprite.pv-=0.5

        for fin in  arrivé.sprites():
            if pygame.sprite.spritecollide(fin,moi,False): #Si il est en colision avec le player
                self.Ingame = False

        self.compteurPiece=compteurPiece
        for piece in coin_sprites.sprites():
            if pygame.sprite.spritecollide(piece,moi,False):
                piece.kill()
                self.compteurPiece+=piece.value
                if self.compteurPiece >9:
                    self.pv+=10
                    self.compteurPiece =0



        if self.rect.y > vertical_tile_number*tile_size:
            self.pv=0
        elif self.rect.x<0 or self.rect.x> wid:
            self.pv=0

    def update(self,enemy_sprites,moi,arrivé,coin_sprites,compteurPiece):
        
        self.check(enemy_sprites,moi,arrivé,coin_sprites,compteurPiece)
        self.movement()
        self.get_state()
        self.animate()
        self.add_dust()
        self.add_attack()