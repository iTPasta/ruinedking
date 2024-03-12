from pygame import image
import pygame_menu
from pathing import path
from map_setup import wid, hei
from progress import reset_progress

class Menu():
    def __init__(self, window):
        self.window = window
        self.menu = pygame_menu.Menu('Menu', wid, hei)
    
    def reset(self):
        reset_progress()
        self.close()
    
    def create_components(self):
        self.menu.add.button('Reprendre', self.close)
        self.menu.add.button('Quitter le jeu', pygame_menu.events.EXIT)
        self.menu.add.button('Recommencer', self.reset)
        
    
    def create_theme(self):
        background_image = pygame_menu.BaseImage(
            image_path = path + "/graphics/background_image_blur.jpg",
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
            )

        theme = pygame_menu.themes.Theme(background_color=background_image,
            title_background_color=(102, 145, 16),
            title_font_shadow=True)

        return theme

    def open(self):
        self.menu = pygame_menu.Menu('Menu', wid, hei, theme=self.create_theme())
        self.create_components()

        self.menu.enable()
        self.menu.mainloop(self.window)
    
    def close(self):
        self.menu.disable()