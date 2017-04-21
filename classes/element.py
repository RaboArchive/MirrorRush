import pygame;
import util;

class element():
    #Aim to be the basic element to display in the Game
    def __init__(self,path,label="component"):
        self.__path = path;
        self.__label = label;
        self.__img = util.load_image(self.__path);
        self.__dim = self.__img.get_rect();
        self.__behavior = None;

    #Methods
    def scaleImage(self, newWidth, newHeight):
        pygame.transform.scale(self.img,(newWidth, newHeight));
    def reloadImg(self):
        self.__img = util.load_image(self.path);
        self.__dim = self._img.get_rect();
    def performBehavior(self):
        #don't know if it will work
        if(self.behavior != None):
            self.behavior(self);

    #Getters
    def getImg(self):
        return self.__img;
    def getDim(self):
        return self.__img.get_rect();
    def getLabel(self):
        return self.__label;

    #Setters
    def setImg(self, img):
        self.__img = img;
        self.__dim = self._img.get_rect();
    def setLabel(self, newLabel):
        self.__label = newLabel;
    def setBehavior(self, function):
        self.__behavior = function;
