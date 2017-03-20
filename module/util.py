import sys;
import pygame;

#To load an image with a given path
def load_image(name):
    image = pygame.image.load(name);
    return image;
