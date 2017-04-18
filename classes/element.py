import pygame;
import util;

class element():
    #Basic element to display in the Game
    def __init__(self,path,options,label="component"):
        self.path = path;
        self.label = label;
        self.options = options;
        #loadScaledImage
