import pygame;
import util;

class menu():
    #constructeur
    def __init__(self, options, path):
        #Initialisations du paths du JSON et sauvegarde des options pour modification futur
        self._path = path;
        self._options = options;
        self._components = [];
        self._loadComponents(path);

    #Class methods TODO
    #def loadComponents(path):
    #def reloadComponents():
    #def onClickAction()
    #def modifyOptions

    #Getters
    def getPath(self):
        return self._path;
    def getOptions(self):
        return self._options;
    def getComponents(self):
        return self._components;
    def getComponent(self, index):
        return self._components[i];
    #Setters
    def setPath(self, newPath):
        if(newPath != ""):
            self._path = newPath;
