
import random
import sys
import pygame

clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
windowHeight = 400
windowWidth = 400
blockSize = 20


#Draws grid in pygame graphics
def drawGrid():
    for x in range(0, windowWidth, blockSize):
        for y in range(0, windowHeight, blockSize):  
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


#Print grid based on value of the different cells
def print_grid(rows, cols, grid):
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                drawBlockBlack(rows, cols)
            if grid[row][col] == 1:
                drawBlockWhite(rows, cols)
   

#Draws white block in pygame graphics
def drawBlockWhite(row, col):
            cords = convert(row, col)
            rect = pygame.Rect(cords[0], cords[1], blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 10)



#Draws black block in pygame graphics
def drawBlockBlack(row, col):
            cords = convert(row, col)
            rect = pygame.Rect(cords[0], cords[1], blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 10)


#Converts normal index places to pygame coordinate places
def convert(row, col):
    newRow = (row * 20)
    newCol = (col * 20)
    return [newRow, newCol]


#Creates boardarray to keep track of cell status
def initBoardArr():
    boardArray = []
    for row in range(20):
            rows = []
            for col in range(20):
                if random.randint(0, 7) == 0:
                    rows += [1]
                else:
                    rows += [0]
            boardArray += [rows]
    return boardArray


#Count number of neigbours of a cell
def countNeighbours(array, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                count += array[((row + i) % 20)][((col + j) % 20)]
    print(count)
    return count


#Updates the current grid based on the value of the different cells, calls the countNeighbour function and applies the gameoflife rules
def Update(boardArr, numRows, numCols):
    for row in range(numRows):
        for col in range(numCols):

            count = countNeighbours(boardArr, row, col)

            if count < 2 or count > 3:
                boardArr[row][col] = 0
                drawBlockBlack(row,col)

            elif count == 3 and boardArr[row][col] == 0:
                boardArr[row][col] = 1
                drawBlockWhite(row,col)


#Main loop for refreshing board status        
def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((windowWidth, windowHeight))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    # Create the initial random Game of Life grids
    grid = initBoardArr()
 
    while True:
        print_grid(20,20, grid)
        Update(grid, 20, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(1)
main()