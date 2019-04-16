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

# ***************
# ** GAME CODE **
# ***************

# will set up some sample classes to help with managable code
# if you know inheritance then it would come in very useful but if not, dont worry there are work arounds

class MoveableObject:
    def __init__(self):
        self.data = []

    def move(self):
        raise NotImplementedError

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

# MAIN GAME LOOP
def game_loop():
    done = False
    while not done:
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_ESCAPE] or keyState[pygame.K_q]:
            done = True
        pygame.event.pump()
            
    pygame.quit()
        # notice that there is currently no way to exit this loop... how can we do that?
        # ^ done
if __name__ == "__main__":
    game_loop()

