import pygame;
import util;

class menu():
    #constructeur
    def __init__(self, options, path):
        #Initialisations du paths du JSON et sauvegarde des options pour modification futur
        self.__path = path;
        self.__options = options;
        self.__components = [];
        self.__loadComponents(path);

    #Class methods TODO
    def __loadComponents(path):
        components = util.loadJsonFile(self.getPath()):
        print(components);
    #def reloadComponents():
    #def __onClickAction()
    #def __modifyOptions

    #Getters
    def getPath(self):
        return self.__path;
    def getOptions(self):
        return self.__options;
    def getComponents(self):
        return self.__components;
    def getComponent(self, index):
        return self.__components[i];
    #Setters
    def setPath(self, newPath):
        if(newPath != ""):
            self.__path = newPath;
