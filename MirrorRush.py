# RaboSchmup
# Made by Raboliot

 #-*- coding:Utf-8 -*-

#importation des biblios
import pygame;
from pygame.locals import *;
import sys;
import os;

#On definit le path
sys.path.append(os.path.realpath('.\module'));
sys.path.append(os.path.realpath('.\class'));
#os.path.join(os.path.dirname(__file__), '.\module');

print(sys.path);

import util;

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

while 1:
    print("coucou");
