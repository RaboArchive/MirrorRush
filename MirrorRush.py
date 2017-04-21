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
import menu;

#Global variable
options = options.options(".\data\options.json");
actionToDo = 0;

#init pygame
pygame.init();

#Creating the window
window  = pygame.display.set_mode((options.getY(),options.getX()), options.getWindowType());
count = 0;

#TODO find a more elegant way to do this
while 1:
    if actionToDo == 0:
        print("Launch Menu");
        actionToDo = menu.launch(options);
    elif actionToDo == 1:
        print("Launch Game");
    elif actionToDo == -1:
        print("exit");
        sys.exit();
    else:
        #In case of error
        actionToDo = 0;
