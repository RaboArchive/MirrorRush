import pygame;
import util;

class options():
    # constructeur
    def __init__(self, path):
        #initialisations et affectations d'attributs :
        self.path = path;
        self.windowType = pygame.RESIZABLE;
        self.x = 600;
        self.y = 800;
        self.loadOptions();

    #Load and save options
    def loadOptions(self):
        options = util.loadJsonFile(self.path);
        #Add line per params
        self.x = options["x"];
        self.y = options["y"];
        self.windowType = options["wType"];

    def saveOptions(self):
        options = {
            'x' : self.x,
            'y' : self.y,
            'wType' : self.windowType,
        };
        util.saveOptions(self.path, options);

    #Getters
    def getResolution(self):
        return (self.x,self.y);
    def getX(self):
        return self.x;
    def getY(self):
        return self.y;
    def getWindowType(self):
        return self.windowType;

    #Setters
    def setResolution(self, new_xRes, new_yRes):
        self.x = new_xRes;
        self.y = new_yRes;
    def setX(self, newX):
        self.x = newX;
    def setY(self, newY):
        self.y = newY;
    def setWindowType(self, newType):
        self.windowType = newType;
