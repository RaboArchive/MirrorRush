import pygame;
import util;

class Options():
    # constructeur
    def __init__(self, path):
        #initialisations et affectations d'attributs :
        self.path = path;
        self.windowType = pygame.RESIZABLE;
        self.x = 600;
        self.y = 800;
        self.load_options();

    #Load and save options
    def load_options(self):
        options = util.loadJsonFile(self.path);
        #Add line per params
        self.x = options["x"];
        self.y = options["y"];
        self.windowType = options["wType"];

    def save_options(self):
        options = {
            'x' : self.x,
            'y' : self.y,
            'wType' : self.windowType,
        };
        util.save_options(self.path, options);

    #Getters
    def get_resolution(self):
        return (self.x,self.y);
    def get_x(self):
        return self.x;
    def get_y(self):
        return self.y;
    def get_window_type(self):
        return self.windowType;

    #Setters
    def set_resolution(self, new_xRes, new_yRes):
        self.x = new_xRes;
        self.y = new_yRes;
    def set_x(self, newX):
        self.x = newX;
    def set_y(self, newY):
        self.y = newY;
    def set_window_type(self, newType):
        self.windowType = newType;
