import pygame;
import util;

class Menu():
    #constructeur
    def __init__(self, options, path):
        #Initialisations du paths du JSON et sauvegarde des options pour modification futur
        self.__path = path;
        self.__options = options;
        self.__components = [];
        self.__load_components(path);

    #Class methods TODO
    def __load_components(self,path):
        components = util.loadJsonFile(self.get_path());
        print(components);
    #def reloadComponents():
    #def __onClickAction()
    #def __modifyOptions

    #Getters
    def get_path(self):
        return self.__path;
    def get_options(self):
        return self.__options;
    def get_components(self):
        return self.__components;
    def get_component(self, index):
        return self.__components[i];
    #Setters
    def set_path(self, newPath):
        if(newPath != ""):
            self.__path = newPath;
