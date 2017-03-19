# Import libraries that we'll use
import pygame, sys 
import random

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
DIAMOND = 7

# A dictionary linking resources to textures
resource_dir = './resources/'
textures = {
            DIRT    : pygame.image.load(resource_dir+'dirt.png'),
            GRASS   : pygame.image.load(resource_dir+'grass.png'),
            WATER   : pygame.image.load(resource_dir+'water.png'),
            COAL    : pygame.image.load(resource_dir+'coal.png'),
            COTTON  : pygame.image.load(resource_dir+'cotton.png'),
            ROCK    : pygame.image.load(resource_dir+'rock.png'),
            LAVA    : pygame.image.load(resource_dir+'lava.png'),
            DIAMOND : pygame.image.load(resource_dir+'diamond.png')
        }

# Inventory
inventory = {
            DIRT    : 0,
            GRASS   : 0,
            WATER   : 0,
            COAL    : 0,
            COTTON  : 0,
            ROCK    : 0,
            LAVA    : 0,
            DIAMOND : 0 
        }

# Useful game dimensions
TILESIZE = 40
MAPWIDTH = 35
MAPHEIGHT = 20

# Aa list representing our tilemap
tilemap = [ [ DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

# Set up display
pygame.init() 

# Add a font for our inventory
INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

# Create a new drawing surface, width=?, height=?
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE+60))
# Change the ratio of different resources
for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        # pick a random number between 0 and 20
        randomNumber = random.randint(0,30)
        # if a zero, then the tile is a coal
        if randomNumber == 0:
            tile = DIAMOND
        elif randomNumber == 1 or randomNumber == 2:
            tile = COTTON
        elif randomNumber == 3 or randomNumber == 4:
            tile = LAVA
        elif randomNumber == 5 or randomNumber == 6:
            tile = ROCK
        elif randomNumber == 7:
            tile = COAL
        elif randomNumber >= 8 and randomNumber <= 13:
            tile = WATER
        elif randomNumber >= 14 and randomNumber <= 20:
            tile = GRASS
        else:
            tile = DIRT
        # set the position in the map 
        tilemap[rw][cl] = tile

# Give the window a caption
pygame.display.set_caption("james's 2D World")

#the position of the player
playerPos = [3,3]
# Add player to the map
PLAYER = pygame.image.load('resources/player.png').convert_alpha()

# loop (repeat) forever
while True:
    # get all the user events
    for event in pygame.event.get():
        # If the user wants to quit
        if event.type==QUIT:
            # end the game and close the window
            pygame.quit()
            sys.exit()
        # If a key is pressed
        elif event.type==KEYDOWN:
            # if the right arrow is pressed
            if (event.key==K_RIGHT) and playerPos[0] < MAPWIDTH-1:
                playerPos[0] += 1
            elif (event.key==K_LEFT) and playerPos[0] > 0:
                playerPos[0] -= 1
            elif (event.key==K_UP) and playerPos[1] > 0:
                playerPos[1] -= 1
            elif (event.key==K_DOWN) and playerPos[1] < MAPHEIGHT-1:
                playerPos[1] += 1

            if event.key==K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT

    # Loop through each row
    for row in range(MAPHEIGHT):
        # loop through each column in a row
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

    # Display the player
    DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))

    # Inventory display
    placePosition = 10
    for item in inventory:
        # Draw the item image
        DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT*TILESIZE+15))
        placePosition += 30
        # Add text show the amount of item in inventory
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT*TILESIZE+15))
        placePosition += 50
    
    # update the display
    pygame.display.update()
