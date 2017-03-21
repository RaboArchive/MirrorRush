# MirrorRush
# Made by Salle14 Lab

 #-*- coding:Utf-8 -*-

#importation des biblios
import pygame;
from pygame.locals import *;
import sys;
import os;

#On definit le path
sys.path.append(os.path.realpath('.\module'));
sys.path.append(os.path.realpath('.\class'));

#Importation des modules customs
import util;
import loading;

#Global variable
#Maybe set a global dict for all global variable
optionsPath = ".\data\options.json";

#init pygame
pygame.init();
options = loading.loadJsonFile(optionsPath);
#result = loading.saveOptions(optionsPath,options);

#Creating the window
widowResolution = pygame.display.Info();
height = widowResolution.current_h;
width = widowResolution.current_w;
window  = pygame.display.set_mode((widowResolution.current_w,widowResolution.current_h), FULLSCREEN);

img = util.load_image('.\data\img\BG.jpg');
window.blit(img,(0,0));
pygame.display.flip();
