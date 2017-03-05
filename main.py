# Import libraries that we'll use
import pygame, sys 

# Import some useful constants
from pygame.locals import *

# Initialize the pygame module
pygame.init()

# Create a new drawing surface, width=?, height=?
DISPLAYSURF = pygame.display.set_mode((300,300))
# Give the window a caption
pygame.display.set_caption("james's 2D World")

# loop (repeat) forever
while True:
    # get all the user events
    for event in pygame.event.get():
        # If the user wants to quit
        if event.type==QUIT:
            # end the game and close the window
            pygame.quit()
            sys.exit()
    pygame.draw.rect(DISPLAYSURF, (143,212,101), (231,111,232,82))
    pygame.draw.rect(DISPLAYSURF, (243,0,0), (0,0,20,20))
    pygame.draw.rect(DISPLAYSURF, (231,245,45), (99,67,67,100))
    pygame.draw.rect(DISPLAYSURF, (243,129,255), (22,56,90,70))
    # update the display
    pygame.display.update()
