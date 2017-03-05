# Import libraries that we'll use
import pygame, sys 

# Import some useful constants
from pygame.locals import *

# Initialize the pygame module
pygame.init()

# Create a new drawing surface, width=?, height=?
DISPLAYSURF = pygame.display.set_mode((1000,300))
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

    # update the display
    pygame.display.update()
