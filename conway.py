import pygame
import numpy as np
import time


width, height = 1000, 1000

#Game area creation
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('pyGOL')

#Setup background color
bg = 25, 25, 25
screen.fill(bg)

ncx, ncy = 50, 50

dimCW = width / ncx
dimCH = height / ncy
#Cell state description: 1 alive, 0 dead
gameState = np.zeros((ncx, ncy))

pauseExect = False
#Game loop
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    

    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        mouseClick = pygame.mouse.get_pressed()
        print(mouseClick)
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]
    time.sleep(0.1)

    for y in range(0, ncx):
        for x in range(0, ncy):
            if not pauseExect:
                numN = gameState[(x - 1) % ncx, (y - 1) % ncy] + \
                    gameState[(x)     % ncx, (y - 1) % ncy] + \
                    gameState[(x + 1) % ncx, (y - 1) % ncy] + \
                    gameState[(x - 1) % ncx, (y)     % ncy] + \
                    gameState[(x + 1) % ncx, (y)     % ncy] + \
                    gameState[(x - 1) % ncx, (y + 1) % ncy] + \
                    gameState[(x)     % ncx, (y + 1) % ncy] + \
                    gameState[(x + 1) % ncx, (y + 1) % ncy]
                #Rule 1: if number of neighbours equals 3, then cell goes alive
                if gameState[x, y] == 0 and numN == 3:
                    newGameState[x, y] = 1
                
                #Rule 2: Cell dies if less than 2 neighbours or more than 3 neighbours
                elif gameState[x, y] == 1 and (numN < 2 or numN > 3):
                    newGameState[x, y] = 0

            #Poly dimensions definition
            poly = [((x)   * dimCW, y     * dimCH),
                    ((x+1) * dimCW, y     * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    gameState = np.copy(newGameState)
    pygame.display.flip()
    
