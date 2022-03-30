
from email.mime import base, image
from lib2to3.pytree import convert
from tkinter import font
from turtle import Screen, pos
#from pip import main
import pygame, sys
import os
import sys
#import pygame_menu
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1380, 710))
pygame.display.set_caption("Air Battle")

BG = pygame.image.load("assets/Background.jpg")
BG = pygame.transform.scale(BG, (1380, 710))





def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#Level Screen
def level():
    while True:
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        
        lvlbg = pygame.image.load("assets/levelscreenbg.jpeg").convert()
        lvlbg = pygame.transform.scale(lvlbg, (1380, 710))
        x=0
        SCREEN.blit(lvlbg,(x,0))


        LEVEL_1 = Button(image=None, pos=(640, 130), 
                            text_input="Level 1", font=get_font(75), base_color="Green", hovering_color="BLUE")

        LEVEL_1.changeColor(LEVEL_MOUSE_POS)
        LEVEL_1.update(SCREEN)

        LEVEL_2 = Button(image=None, pos=(640, 260), 
                            text_input="Level 2", font=get_font(75), base_color="Yellow", hovering_color="BLUE")

        LEVEL_2.changeColor(LEVEL_MOUSE_POS)
        LEVEL_2.update(SCREEN) 

        LEVEL_3 = Button(image=None, pos=(640, 360),
                        text_input="Level 3", font=get_font(75), base_color="Red", hovering_color="GREEN")
        
        LEVEL_3.changeColor(LEVEL_MOUSE_POS)
        LEVEL_3.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_1.checkForInput(LEVEL_MOUSE_POS):
                    LEVEL1PLAY()  #this goes to level 1 play screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_2.checkForInput(LEVEL_MOUSE_POS):
                    LEVEL2PLAY() #this goes to level 2 play screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_3.checkForInput(LEVEL_MOUSE_POS):
                    LEVEL3PLAY() #this goes to level 3 play screen
        pygame.display.update()

def LEVEL1PLAY():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        game1 = pygame.image.load("assets/gamelvl1backdrp.png").convert()
        game1 = pygame.transform.scale(game1, (1380, 710))
        x = 0
        SCREEN.blit(game1,(x,0))
    
        PLAY_BACK = Button(image=None, pos=(640, 560), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="BLACK")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    level()
                            
        pygame.display.update()


def LEVEL2PLAY():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("Yellow")

    
        PLAY_BACK = Button(image=None, pos=(640, 560), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="BLACK")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    level()
        pygame.display.update()

def LEVEL3PLAY():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("Purple")

    
        PLAY_BACK = Button(image=None, pos=(640, 560), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="BLACK")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    level()
        pygame.display.update()



#options
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

       
        
        
        PLAY_BUTTON = Button(image= None, pos=(970, 250), 
                            text_input="LEVEL", font=get_font(60), base_color="RED", hovering_color="Green")
        OPTIONS_BUTTON = Button(image= None, pos=(970, 400), 
                            text_input="OPTIONS", font=get_font(60), base_color="#BFEFFF", hovering_color="GREEN")
        QUIT_BUTTON = Button(image= None, pos=(970, 550), 
                            text_input="QUIT", font=get_font(60), base_color="#BFEFFF", hovering_color="GREEN")

        

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()