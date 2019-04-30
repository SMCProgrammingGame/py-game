# main.py
# By: {{Names}}
# Created: April 3rd, 2019
# Simple program made with the Santa Monica College Programming Club to get familiar with concepts in python
# Game is a simple over the shoulder "hack and slash" with maze like gameplay
# built primarily in python

import pygame
import pygame.locals
import sys

# Game needs Python 3 and higher in order to be ran without errors
if sys.version_info[0] < 3:
    raise Exception("Ran with Python 2. Needed Python 3.")

# *********** CONSTANTS ***********
HEIGHT = 600
WIDTH = 800
size = (WIDTH, HEIGHT)

# init game
pygame.init()

# setting window size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Platform Game")

# setting up clock for refresh rate
clock = pygame.time.Clock()

#Directional Jump per move
dx = 50
dy = 50

#Colors
WHITE = (255, 255, 255)
BLACK=(0,0,0)

#Test Toon
toon = pygame.image.load("toon.png")
toon = pygame.transform.scale(toon, (50,50))

# ***************
# ** GAME CODE **
# ***************

# will set up some sample classes to help with managable code
# if you know inheritance then it would come in very useful but if not, dont worry there are work arounds

class MoveableObject:
    def __init__(self, image, width, height, inX, inY):
        self.image = image
        self.width = width
        self.height = height
        self.pos = image.get_rect().move(inX,inY)
        
    def move(self, direction):
        if direction == "left":
            self.pos = self.pos.move(-dx, 0)
            if self.pos.left<dx:
                self.pos.right = dx-self.pos.left
        if direction == "right":
            self.pos = self.pos.move(dx, 0)
            if self.pos.right<dx:
                self.pos.left = dx-self.pos.right
        
    

class Character(MoveableObject):
    def __init__(self):
        pass

    def move(self):
        pass

class Enemy(MoveableObject):
    def __init__(self):
        pass

    def move(self):
        pass


obj = MoveableObject(toon,50,50,300,300)
        
# MAIN GAME LOOP
def game_loop():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    done = True
                if event.key == pygame.K_LEFT:
                    obj.move("left")
                if event.key == pygame.K_RIGHT:
                    obj.move("right")

        pygame.display.flip()
        screen.blit(obj.image, obj.pos)
        clock.tick(30)
        pygame.display.update()
        
        
    
        # notice that there is currently no way to exit this loop... how can we do that?
        # ^ done
if __name__ == "__main__":
    game_loop()
    pygame.quit()
    #quit()
