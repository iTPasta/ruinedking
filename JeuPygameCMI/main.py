import sys
import pygame
from progress import *
from niveau import Niveau
from map_setup import *
from game_data import *
from menu import *
from PIL import Image, ImageFilter

def loop(window):
    for monde in mondes:
        for lvl in monde :
            if not(progress_ON) or get_progress() == lvl["name"] or get_progress() == "RESET":
                if get_progress() == "RESET":
                    clear_progress()
                
                window.fill((0,0,1))
                loading_image = pygame.image.load(path + "/graphics/loading.png")
                loading_rect = loading_image.get_rect()
                window.blit(loading_image, (int(wid/2 - loading_rect.w/2), int(hei/2 - loading_rect.h/2)))
            
                pygame.display.flip()

                level = Niveau(lvl, window)

                while level.running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                            pygame.image.save(window, path + "/graphics/background_image.jpg")
                            Image.open(path +
                            "/graphics/background_image.jpg").filter(ImageFilter.BoxBlur(6)).save(path +
                            "/graphics/background_image_blur.jpg")
                            menu.open()
                            if get_progress() == "RESET":
                                loop(window)
                                break

                    #window.fill('black')
                    level.launch()
                
                    pygame.display.update()
                    clock.tick(60)
                    
                if progress_ON:
                    save_progress(lvl)

#setup de la fenêtre
pygame.init()
window = pygame.display.set_mode((wid, hei))
menu = Menu(window)


#création d'une horloge interne pour afficher un certain nombre d'image par secondes
clock = pygame.time.Clock() 

#lancement du jeu
running = True

loop(window)

clear_progress()