# Import libraries that we'll use
import pygame, sys 

# Import some useful constants
from pygame.locals import *

# Constants representing colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Constnats representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

# A dictionary linking resources to colors
colors = {
            DIRT    : BROWN,
            GRASS   : GREEN,
            WATER   : BLUE,
            COAL    : BLACK
        }

# Aa list representing our tilemap
tilemap = [
            [GRASS, COAL, DIRT],
            [WATER, WATER, GRASS],
            [COAL, GRASS, WATER],
            [DIRT, GRASS, COAL],
            [GRASS, WATER, DIRT]
        ]

# Useful game dimensions
TILESIZE = 40
MAPWIDTH = 3
MAPHEIGHT = 5

# Set up display
pygame.init() 
# Create a new drawing surface, width=?, height=?
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

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

    # Loop through each row
    for row in range(MAPHEIGHT):
        # loop through each column in a row
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

    # update the display
    pygame.display.update()
