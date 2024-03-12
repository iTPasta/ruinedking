import pygame
from tiles import *
from map_setup import tile_size, wid,hei
from player import Player
from support import *
from decoration import *
from particles import *
from pathing import path
from game_data import *
import sys

class Niveau():
    def __init__(self, terrain_shape, surface):# !!! le terrain de terrain_shape reference a la forme du lvl alors que le terrain de terrain layout reference a la terre (le sol plateform ect)!!! (A rename)
        self.terrain_shape = terrain_shape
        self.running = True
        self.display = surface

        self.heart = pygame.transform.scale(pygame.image.load(path + "/graphics/heart/heart.png"), (56, 48))
        self.coin = pygame.transform.scale(pygame.image.load(path + "/graphics/coins/gold/0.png"), (56, 56))
        self.compteurPiece = 0

        if terrain_shape == level_0 :

            #détails du niveau
            self.world_shift = 0 #Valeur du scrollage de l'ecran
            self.musique = pygame.mixer.Sound("./levels/lvl0/musique.ogg")
            

            #self.create_tile_group(terrain_shape) -> ancienne comande inutile maintenant

            #Creation du player
            player_layout = import_csv_layout(terrain_shape['player'])
            self.player = pygame.sprite.GroupSingle()
            self.player_attack = pygame.sprite.GroupSingle()
            self.goal = pygame.sprite.GroupSingle() #Le goal est la case d'arrivé
            self.player_setup(player_layout) #Appelle la fonction ci dessous

            
            #Creation du Terrain du niveau
            terrain_layout = import_csv_layout(terrain_shape['terrain']) #Remplace self.create_tile_group (voire support.py);Le terrain layout contient toute les coordonné de la map (list des lignes) et l'ID de la tuile sur cette coord (meme fonctionnement que la map)
            self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

            #Creation De l'herbe sur le niveau (meme fonctionement que pour le terrain)
            grass_layout = import_csv_layout(terrain_shape['grass'])
            self.grass_sprites = self.create_tile_group(grass_layout,'grass')

            #Creation des crates (caisse)
            crates_layout = import_csv_layout(terrain_shape['crates'])
            self.crates_sprites = self.create_tile_group(crates_layout,'crates')

            #Creationt des coins (pieces)
            coin_layout = import_csv_layout(terrain_shape['coins'])
            self.coin_sprites = self.create_tile_group(coin_layout,'coins')

            #Creation arbres
            fg_palm_layout = import_csv_layout(terrain_shape['fg palms'])
            self.fg_palm_sprites = self.create_tile_group(fg_palm_layout,'fg palms')

            #Creation arbres
            bg_palm_layout = import_csv_layout(terrain_shape['bg palms'])
            self.bg_palm_sprites = self.create_tile_group(bg_palm_layout,'bg palms')

            #Creation enemy
            enemy_layout = import_csv_layout(terrain_shape['enemies'])
            self.enemy_sprites = self.create_tile_group(enemy_layout,'enemies')

            #Creation contrainte ( point ou les ennemies ne peuvent pas aller plus loin et tourne (invisible car pas dessiner))
            constraint_layout = import_csv_layout(terrain_shape['constraints'])
            self.constraint_sprites = self.create_tile_group(constraint_layout,'constraint')

            #decoration
            self.sky = Sky(8)
            niveau_width = len(terrain_layout[0])*tile_size
            self.water = Water(hei - 40, niveau_width)
            self.clouds = Clouds(300,wid,15)

            self.is_moving = (False, True)
            self.position = 0 #position en x du terrain



        elif terrain_shape == level_1 or terrain_shape == level_5:

            #détails du niveau
            terrain_layout = import_csv_layout(terrain_shape['terrain'])
            self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain2')
            self.is_moving = (False, True)
            self.position = 0 #position en x du terrain
            self.world_shift = 0

            self.musique = pygame.mixer.Sound("./levels/lvl1/musique.ogg")

            #vegetation
            vegetation_layout = import_csv_layout(terrain_shape['vegetation'])
            self.vegetation_sprites = self.create_tile_group(vegetation_layout, 'vegetation')
            
            #ennemies
            enemy_layout = import_csv_layout(terrain_shape['enemies'])
            self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies2')
            
            #crates
            crates_layout = import_csv_layout(terrain_shape['crates'])
            self.crates_sprites = self.create_tile_group(crates_layout, 'crates')

            #coins
            coins_layout = import_csv_layout(terrain_shape['coins'])
            self.coins_sprites = self.create_tile_group(coins_layout, 'coins')

            #constraints
            constraint_layout = import_csv_layout(terrain_shape['constraints'])
            self.constraint_sprites = self.create_tile_group(constraint_layout, 'constraint')

            #decorations
            self.background = pygame.image.load('./levels/lvl1/backgrounds/Desert.png').convert_alpha()
            self.sbmouvant = SBMouvant(hei - 40, wid*tile_size)

            #propriétés du joueur dans le niveau

            self.goal_layout = import_csv_layout(terrain_shape['player'])
            self.player = pygame.sprite.GroupSingle()
            self.player_attack = pygame.sprite.GroupSingle()
            self.goal = pygame.sprite.GroupSingle()
            self.player_setup(self.goal_layout)
            #self.player_x_position = self.player.rect.centerx
            #self.player_x_direction = self.player.direction.xcrates_layout
        
        elif terrain_shape == level_2:

            #détails du niveau
            self.world_shift = 0 #Valeur du scrollage de l'ecran
            self.musique = pygame.mixer.Sound("./levels/lvl2/musique.ogg")

            #self.create_tile_group(terrain_shape) -> ancienne comande inutile maintenant

            #Creation du player
            player_layout = import_csv_layout(terrain_shape['player'])
            self.player = pygame.sprite.GroupSingle()
            self.player_attack = pygame.sprite.GroupSingle() #Création de la hitbox d'attaque (le sprite qui fait les dégats)
            self.goal = pygame.sprite.GroupSingle() #Le goal est la case d'arrivé
            self.player_setup(player_layout) #Appelle la fonction ci dessous

            
            #Creation du Terrain du niveau
            terrain_layout = import_csv_layout(terrain_shape['terrain']) #Remplace self.create_tile_group (voire support.py);Le terrain layout contient toute les coordonné de la map (list des lignes) et l'ID de la tuile sur cette coord (meme fonctionnement que la map)
            self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

            #Creation De l'herbe sur le niveau (meme fonctionement que pour le terrain)
            grass_layout = import_csv_layout(terrain_shape['grass'])
            self.grass_sprites = self.create_tile_group(grass_layout,'grass')

            #Creation des crates (caisse)
            crates_layout = import_csv_layout(terrain_shape['crates'])
            self.crates_sprites = self.create_tile_group(crates_layout,'crates')

            #Creationt des coins (pieces)
            coin_layout = import_csv_layout(terrain_shape['coins'])
            self.coin_sprites = self.create_tile_group(coin_layout,'coins')

            #Creation arbres
            fg_palm_layout = import_csv_layout(terrain_shape['fg palms'])
            self.fg_palm_sprites = self.create_tile_group(fg_palm_layout,'fg palms')

            #Creation arbres
            bg_palm_layout = import_csv_layout(terrain_shape['bg palms'])
            self.bg_palm_sprites = self.create_tile_group(bg_palm_layout,'bg palms')

            #Creation enemy
            enemy_layout = import_csv_layout(terrain_shape['enemies'])
            self.enemy_sprites = self.create_tile_group(enemy_layout,'enemies')

            #Creation contrainte ( point ou les ennemies ne peuvent pas aller plus loin et tourne (invisible car pas dessiner))
            constraint_layout = import_csv_layout(terrain_shape['constraints'])
            self.constraint_sprites = self.create_tile_group(constraint_layout,'constraint')

            #decoration
            self.sky = Sky(8)
            niveau_width = len(terrain_layout[0])*tile_size
            self.water = Water(hei - 40, niveau_width)
            self.clouds = Clouds(300,wid,15)

            self.is_moving = (False, True)
            self.position = 0 #position en x du terrain

        elif terrain_shape == level_3 or terrain_shape == level_4 or terrain_shape == level_6 :

            #détails du niveau
            self.world_shift = 0 #Valeur du scrollage de l'ecran
            self.musique = pygame.mixer.Sound("./levels/lvl3/musique.ogg")

            #self.create_tile_group(terrain_shape) -> ancienne comande inutile maintenant

            #Creation du player
            player_layout = import_csv_layout(terrain_shape['player'])
            self.player = pygame.sprite.GroupSingle()
            self.player_attack = pygame.sprite.GroupSingle()
            self.goal = pygame.sprite.GroupSingle() #Le goal est la case d'arrivé
            self.player_setup(player_layout) #Appelle la fonction ci dessous

            
            #Creation du Terrain du niveau
            terrain_layout = import_csv_layout(terrain_shape['terrain']) #Remplace self.create_tile_group (voire support.py);Le terrain layout contient toute les coordonné de la map (list des lignes) et l'ID de la tuile sur cette coord (meme fonctionnement que la map)
            self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain3')

            #Creation De l'herbe sur le niveau (meme fonctionement que pour le terrain)
            grass_layout = import_csv_layout(terrain_shape['grass'])
            self.grass_sprites = self.create_tile_group(grass_layout,'grass3')

            #Creation des crates (caisse)
            crates_layout = import_csv_layout(terrain_shape['crates'])
            self.crates_sprites = self.create_tile_group(crates_layout,'crates')

            #Creation arbres
            fg_palm_layout = import_csv_layout(terrain_shape['trees'])
            self.fg_palm_sprites = self.create_tile_group(fg_palm_layout,'trees')

            #Creation bushes
            bg_palm_layout = import_csv_layout(terrain_shape['bushes'])
            self.bg_palm_sprites = self.create_tile_group(bg_palm_layout,'bushes')

            #Creationt des coins (pieces)
            coin_layout = import_csv_layout(terrain_shape['coins'])
            self.coin_sprites = self.create_tile_group(coin_layout,'coins')

            #Creation enemy
            enemy_layout = import_csv_layout(terrain_shape['enemies'])
            self.enemy_sprites = self.create_tile_group(enemy_layout,'enemies')

            #Creation contrainte ( point ou les ennemies ne peuvent pas aller plus loin et tourne (invisible car pas dessiner))
            constraint_layout = import_csv_layout(terrain_shape['constraints'])
            self.constraint_sprites = self.create_tile_group(constraint_layout,'constraint')

            #decoration
            self.sky = Sky(8)
            niveau_width = len(terrain_layout[0])*tile_size
            self.water = Water(hei - 4000, niveau_width)
            self.clouds = Clouds(300,wid,15)

            self.is_moving = (False, True)
            self.position = 0 #position en x du terrain

        self.musique.play(-1, 0, 5000)
        self.musique.set_volume(0.15)


    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index,row in enumerate(layout):#Pour chaque la ligne "row" numero row_index de la map :
            for col_index,val in enumerate(row):#Pour chaque case de la ligne
                if val != '-1': #Si la case a une valeur de '-1' alors il n'y a rien de poser dessus elle ne nous interesse donc pas 
                    x = col_index * tile_size #Coord x de la case 
                    y = row_index * tile_size #Coord y de la case 

                    if type == 'terrain':                  
                        terrain_tile_list = import_cut_graphics(path+'/graphics/terrain/terrain_tiles.png')#Importe les differents tiles du fichier (les separent) et les mets dans une liste
                        tile_surface = terrain_tile_list[int(val)]
                        sprite  = StaticTile(tile_size,x,y,tile_surface)#Creer un StaticTile (voire tiles.py)

                    elif type == 'grass':
                        grass_tile_list = import_cut_graphics(path+'/graphics/decoration/grass/grass.png')
                        tile_surface = grass_tile_list[int(val)]
                        sprite  = StaticTile(tile_size,x,y,tile_surface)#Creer un StaticTile (voire tiles.py)

                    elif type == 'crates':                    
                        sprite  = CrateTile(tile_size,x,y)#Creer un CrateTile (voire tiles.py)

                    elif type == 'coins':
                        if val == '0': #Diferencie les pieces d'or et d'argent en fonction de leur numero dans le layout
                            sprite = Coin(tile_size,x,y,path+'/graphics/coins/gold',4)
                        else : 
                            sprite = Coin(tile_size,x,y,path+'/graphics/coins/silver',1)     
                    
                    elif type == 'fg palms' :
                        if val == '0' : #Diferencie les petit des grands en fonction de leur numero dans le layout
                            sprite = Palm(tile_size,x,y,path+'/graphics/terrain/palm_small',38)
                        else :
                            sprite = Palm(tile_size,x,y,path+'/graphics/terrain/palm_large',64)

                    elif type == 'bg palms' :
                        sprite = Palm(tile_size,x,y,path+'/graphics/terrain/palm_bg',64)

                    elif type == 'enemies':
                        sprite = Enemy(tile_size,x,y,"/graphics/enemy/run")

                    elif type == 'constraint':
                        sprite = Tile(tile_size,x,y)

                    elif  type == 'terrain2':
                        terrain_tile_list = import_cut_graphics('./levels/lvl1/tilesets/desert/assets/desert_terrain.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile( tile_size,x,y,tile_surface)   

                    elif type == 'vegetation':
                        vegetation_tile_list = import_cut_graphics('./levels/lvl1/tilesets/desert/vegetation/vegetation.png')
                        tile_surface = vegetation_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)

                    elif type == "enemies2":
                        sprite = Enemy2((x,y),tile_size,'./graphics/enemies/animation')
                    
                    elif type == 'trees':                  
                        terrain_tile_list = import_cut_graphics(path+'/graphics/terrain/trees.png')#Importe les differents tiles du fichier (les separent) et les mets dans une liste
                        tile_surface = terrain_tile_list[int(val)]
                        sprite  = StaticTile(tile_size,x,y,tile_surface)#Creer un StaticTile (voire tiles.py)

                    elif type == 'bushes':                  
                        terrain_tile_list = import_cut_graphics(path+'/graphics/terrain/bushes.png')#Importe les differents tiles du fichier (les separent) et les mets dans une liste
                        tile_surface = terrain_tile_list[int(val)]
                        sprite  = StaticTile(tile_size,x,y,tile_surface)#Creer un StaticTile (voire tiles.py)

                    elif type == 'terrain3':                  
                        terrain_tile_list = import_cut_graphics(path+'/graphics/terrain/terrain_tiles_lvl3.png')#Importe les differents tiles du fichier (les separent) et les mets dans une liste
                        tile_surface = terrain_tile_list[int(val)]
                        sprite  = StaticTile(tile_size,x,y,tile_surface)#Creer un StaticTile (voire tiles.py)

                    elif type == 'grass3':                  
                        terrain_tile_list = import_cut_graphics(path+'/graphics/terrain/grass_lvl3.png')#Importe les differents tiles du fichier (les separent) et les mets dans une liste
                        if int(val) > 4:
                            return sprite_group # Deux lignes dégueu mais il y a un problème que j'arrive pas à résoudre pour le level_4 
                        tile_surface = terrain_tile_list[int(val)]
                        sprite  = StaticTile(tile_size,x,y,tile_surface)#Creer un StaticTile (voire tiles.py)
                    sprite_group.add(sprite)#L'ajoute a son groupe

        return(sprite_group)



    
    #application du scroll de l'écran (uniquement droite/gauche)
    def scroll(self):
            player = self.player.sprite
            player_x = player.rect.centerx
            direction_x = player.direction.x

            if player_x < wid / 2.5 and direction_x < 0:
                self.world_shift = 8
                player.velocity = 0
            elif player_x > wid - (wid / 2.5) and direction_x > 0:
                self.world_shift = -8
                player.velocity = 0
            else:
                self.world_shift = 0
                player.velocity = 8
        

    #collisions horizontales
    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.velocity
        sprites_avec_collision = self.terrain_sprites.sprites() + self.crates_sprites.sprites()
        if self.terrain_shape == level_0 or self.terrain_shape == level_2:
            sprites_avec_collision += self.fg_palm_sprites.sprites()
        #pygame peut savoir que deux entités rentrent en collision, je lui dit juste que si c'est le cas, il doit stopper le joueur.
        for sprite in sprites_avec_collision :
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        
        #désactivation des collisions si le joueurs ne bouge plus ou va dans la direction opposée
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        elif player.on_right and (player.rect.right < self.current_x or player.direction.x <= 0):
            player.on_right = False

    #meme systeme ici (approximativement)
    def vertical_collision(self):
        player = self.player.sprite
        player.gravity()
        sprites_avec_collision = self.terrain_sprites.sprites() + self.crates_sprites.sprites()
        if self.terrain_shape == level_0 or self.terrain_shape == level_2:
            sprites_avec_collision += self.fg_palm_sprites.sprites()


        for sprite in sprites_avec_collision:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                    player.on_ground = False
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.on_ceiling = False
        
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def player_setup(self,layout):
        """
        Cette fonction est une sorte de create_tile_group() unique au player et a son goal du faite qu'ils sont dans un
        SingleGroup ici on setup les coordoné de l'arrivé et du depart
        """
        for row_index,row in enumerate(layout):#Pour chaque la ligne "row" numero row_index de la map :
            for col_index,val in enumerate(row):#Pour chaque case de la ligne
                x = col_index * tile_size #Coord x de la case 
                y = row_index * tile_size #Coord y de la case 
                if val == '0': #Si la case a une valeur de '-1' alors il n'y a rien de poser dessus elle ne nous interesse donc pas 
                    sprite = Player((x,y),self.display)
                    self.player.add(sprite)
                if val == '1':
                    hat_surface = pygame.image.load(path+'/graphics/character/hat.png')
                    sprite = StaticTile(tile_size,x,y,hat_surface)
                    self.goal.add(sprite)

    def enemy_demis_tours(self):
        for enemy in  self.enemy_sprites.sprites():#Pour tout les enemy créer :
            if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False): #Si il est en colision avec un point contrainte
                enemy.reverse() #On le retourne (voire tiles.py class Enemy)
            elif enemy.rect.colliderect(self.player.sprite.attack_zone.rect):
                self.enemy_sprites.remove(enemy)

    def update_heart(self):
        heart_count = int(self.player.sprite.pv / 10)
        for i in range(1, heart_count + 1):
            self.display.blit(self.heart, (self.display.get_size()[0] - (56 + 22) * i, 20))

    def update_coins(self):
        font = pygame.font.Font(path + '/graphics/ARCADECLASSIC.TTF', 60)
        text = font.render(str(self.compteurPiece), True, (191, 141, 17))
        textRect = text.get_rect()
        textRect.center = (98, 51)
        self.display.blit(text, textRect)
        self.display.blit(self.coin, (20, 20))

    def game_over(self) :
        sys.exit()


    def launch(self):
        #Check si la game continue
        self.running = self.player.sprite.Ingame
        if self.running == False:
            self.musique.stop()

        if self.player.sprite.pv <= 0 :
            self.musique.stop()
            self.game_over()


        if self.terrain_shape == level_0:

            #decoration
            self.sky.draw(self.display)
            self.clouds.draw(self.display,self.world_shift)

            #Palm 2 (on les peints en premier comme ça ils sont en arriere plan)
            self.bg_palm_sprites.update(self.world_shift)
            self.bg_palm_sprites.draw(self.display)
            

            #Platforme / terrain
            self.terrain_sprites.update(self.world_shift)
            self.terrain_sprites.draw(self.display)
            

            #Enemies
            self.enemy_sprites.update(self.world_shift)
            self.constraint_sprites.update(self.world_shift) #Point invisible (donc pas draw )égale a la Fin de l'allé de l'enemi / endroit ou il fait demis-tour 
            self.enemy_demis_tours() #Check si un enemy doit faire demis tours
            self.enemy_sprites.draw(self.display)
            

            #Caisses
            self.crates_sprites.update(self.world_shift)
            self.crates_sprites.draw(self.display)
            

            #Herbe
            self.grass_sprites.update(self.world_shift)
            self.grass_sprites.draw(self.display)
            

            #Piece
            self.coin_sprites.update(self.world_shift)
            self.coin_sprites.draw(self.display)
            

            #Palm
            self.fg_palm_sprites.update(self.world_shift)
            self.fg_palm_sprites.draw(self.display)

            #
            self.player.update(self.enemy_sprites,self.player,self.goal,self.coin_sprites,self.compteurPiece)
            self.compteurPiece = self.player.sprite.compteurPiece
            self.horizontal_collision()
            self.vertical_collision()
            self.scroll()
            self.player.draw(self.display)
            self.goal.update(self.world_shift)
            self.goal.draw(self.display)

            #water
            self.water.draw(self.display,self.world_shift)

        elif self.terrain_shape == level_1 or self.terrain_shape == level_5 :
            #background
            self.display.blit(self.background,(0,0))

            #terrain       
            self.terrain_sprites.update(self.world_shift)
            self.terrain_sprites.draw(self.display)

            #vegetation
            self.vegetation_sprites.update(self.world_shift)
            self.vegetation_sprites.draw(self.display)

            #crates
            self.crates_sprites.update(self.world_shift)
            self.crates_sprites.draw(self.display)

            #coins
            self.coins_sprites.update(self.world_shift)
            self.coins_sprites.draw(self.display)

            #enemies
            self.enemy_sprites.update(self.world_shift)
            self.constraint_sprites.update(self.world_shift)
            self.enemy_demis_tours()
            self.enemy_sprites.draw(self.display)

            #player sprites
            self.player.update(self.enemy_sprites,self.player,self.goal,self.coins_sprites,self.compteurPiece)
            self.compteurPiece = self.player.sprite.compteurPiece
            self.horizontal_collision()
            self.vertical_collision()
            self.scroll()
            self.player.draw(self.display)
            self.goal.update(self.world_shift)
            self.goal.draw(self.display)

            #sables mouvants
            self.sbmouvant.update(self.display, self.position)

        elif self.terrain_shape == level_2:

            #decoration
            self.sky.draw(self.display)
            self.clouds.draw(self.display,self.world_shift)

            #Palm 2 (on les peints en premier comme ça ils sont en arriere plan)
            self.bg_palm_sprites.update(self.world_shift)
            self.bg_palm_sprites.draw(self.display)
            

            #Platforme / terrain
            self.terrain_sprites.update(self.world_shift)
            self.terrain_sprites.draw(self.display)
            

            #Enemies
            self.enemy_sprites.update(self.world_shift)
            self.constraint_sprites.update(self.world_shift) #Point invisible (donc pas draw )égale a la Fin de l'allé de l'enemi / endroit ou il fait demis-tour 
            self.enemy_demis_tours() #Check si un enemy doit faire demis tours
            self.enemy_sprites.draw(self.display)
            

            #Caisses
            self.crates_sprites.update(self.world_shift)
            self.crates_sprites.draw(self.display)
            

            #Herbe
            self.grass_sprites.update(self.world_shift)
            self.grass_sprites.draw(self.display)
            

            #Piece
            self.coin_sprites.update(self.world_shift)
            self.coin_sprites.draw(self.display)
            

            #Palm
            self.fg_palm_sprites.update(self.world_shift)
            self.fg_palm_sprites.draw(self.display)

            #
            self.player.update(self.enemy_sprites,self.player,self.goal,self.coin_sprites,self.compteurPiece)
            self.compteurPiece = self.player.sprite.compteurPiece
            self.horizontal_collision()
            self.vertical_collision()
            self.scroll()
            self.player.draw(self.display)
            self.goal.update(self.world_shift)
            self.goal.draw(self.display)

            #water
            self.water.draw(self.display,self.world_shift)

        elif self.terrain_shape == level_3 or self.terrain_shape == level_4 or self.terrain_shape == level_6 :

            #decoration
            self.sky.draw(self.display)
            self.clouds.draw(self.display,self.world_shift)

            #Palm 2 (on les peints en premier comme ça ils sont en arriere plan)
            self.bg_palm_sprites.update(self.world_shift)
            self.bg_palm_sprites.draw(self.display)
            

            #Platforme / terrain
            self.terrain_sprites.update(self.world_shift)
            self.terrain_sprites.draw(self.display)
            

            #Enemies
            self.enemy_sprites.update(self.world_shift)
            self.constraint_sprites.update(self.world_shift) #Point invisible (donc pas draw )égale a la Fin de l'allé de l'enemi / endroit ou il fait demis-tour 
            self.enemy_demis_tours() #Check si un enemy doit faire demis tours
            self.enemy_sprites.draw(self.display)
            

            #Caisses
            self.crates_sprites.update(self.world_shift)
            self.crates_sprites.draw(self.display)
            

            #Herbe
            self.grass_sprites.update(self.world_shift)
            self.grass_sprites.draw(self.display)
            

            #Palm
            self.fg_palm_sprites.update(self.world_shift)
            self.fg_palm_sprites.draw(self.display)

            #Piece
            self.coin_sprites.update(self.world_shift)
            self.coin_sprites.draw(self.display)

            #
            self.player.update(self.enemy_sprites,self.player,self.goal,self.coin_sprites,self.compteurPiece)
            self.compteurPiece = self.player.sprite.compteurPiece
            self.horizontal_collision()
            self.vertical_collision()
            self.scroll()
            self.player.draw(self.display)
            self.goal.update(self.world_shift)
            self.goal.draw(self.display)

            #water
            self.water.draw(self.display,self.world_shift)


        self.update_heart()
        self.update_coins()