import pygame;
import util;

class Element():
    #Aim to be the basic element to display in the Game
    def __init__(self,path,label="component"):
        self.__path = path;
        self.__label = label;
        self.__img = util.load_image(self.__path);
        self.__dim = self.__img.get_rect();
        self.__behavior = None;

    #Methods
    def scale_image(self, newWidth, newHeight):
        pygame.transform.scale(self.img,(newWidth, newHeight));
    def reload_img(self):
        self.__img = util.load_image(self.path);
        self.__dim = self._img.get_rect();
    def perform_behavior(self):
        #don't know if it will work
        if(self.behavior != None):
            self.behavior(self);

    #Getters
    def get_img(self):
        return self.__img;
    def get_dim(self):
        return self.__img.get_rect();
    def get_label(self):
        return self.__label;

    #Setters
    def set_img(self, img):
        self.__img = img;
        self.__dim = self._img.get_rect();
    def set_label(self, newLabel):
        self.__label = newLabel;
    def set_behavior(self, function):
        self.__behavior = function;
