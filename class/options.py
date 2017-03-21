import pygame;
import util;

class options():
    # constructeur
    def __init__(self):
        #initialisations et affectations d'attributs :
        self.xRes = 600;
        self.yRes = 800;
        self.windowType = pygame.RESIZABLE;

    def changeResolution(self, new_xRes, new_yRes):
        self.xRes = new_xRes;
        self.yRes = new_yRes;

    def changeWindowType(self, newType):
        self.windowType = newType;
