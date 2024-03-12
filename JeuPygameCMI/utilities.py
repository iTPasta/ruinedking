import pygame
import os

#recherche de fichiers grace à la fonction listdir qui renvoie une liste des fichiers
def graphic_folders(path):
    imgs = []
    for image in os.listdir(path):
        new_path = path + '/' + image
        imgs.append(pygame.image.load(new_path))
    return imgs