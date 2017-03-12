# Import libraries that we'll use
import pygame, sys 

# Import some useful constants
from pygame.locals import *

# Constants representing colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

# Constnats representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
COTTON = 4
ROCK = 5
LAVA = 6

# A dictionary linking resources to textures
resource_dir = './resources/'
textures = {
            DIRT    : pygame.image.load(resource_dir+'dirt.png'),
            GRASS   : pygame.image.load(resource_dir+'grass.png'),
            WATER   : pygame.image.load(resource_dir+'water.png'),
            COAL    : pygame.image.load(resource_dir+'coal.png'),
            COTTON  : pygame.image.load(resource_dir+'cotton.png'),
            ROCK    : pygame.image.load(resource_dir+'rock.png'),
            LAVA    : pygame.image.load(resource_dir+'lava.png')
        }

# Aa list representing our tilemap
tilemap = [
            [GRASS, COAL, DIRT, COTTON, COAL],
            [WATER, COTTON, GRASS ,DIRT, WATER],
            [COTTON, GRASS, WATER, GRASS, COTTON],
            [DIRT, GRASS, COAL, WATER, ROCK],
            [GRASS, WATER, LAVA, GRASS, DIRT]
        ]

# Useful game dimensions
TILESIZE = 40
MAPWIDTH = 5
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
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

    # update the display
    pygame.display.update()
