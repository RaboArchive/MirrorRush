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
sys.path.append(os.path.realpath('.\classes'));

#Importation des modules customs
import util;
import options;

#Global variable
options = options.options(".\data\options.json");

#init pygame
pygame.init();


#Creating the window
widowResolution = pygame.display.Info();
height = widowResolution.current_h;
width = widowResolution.current_w;
window  = pygame.display.set_mode((widowResolution.current_w,widowResolution.current_h), FULLSCREEN);

img = util.load_image('.\data\img\BG.jpg');
window.blit(img,(0,0));
pygame.display.flip();
