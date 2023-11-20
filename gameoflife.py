import sys
import pygame

clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
boardArr = []
windowHeight = 400
windowWidth = 400
blockSize = 20


#Draws grid in pygame graphics
def drawGrid():
    for x in range(0, windowWidth, blockSize):
        for y in range(0, windowHeight, blockSize):  
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
            


#Draws white block in pygame graphics
def drawBlockWhite(row, col):
            cords = convert(row, col)
            rect = pygame.Rect(cords[0], cords[1], blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 10)
            boardArr[row][col] = 1


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
    colW = windowWidth // 20
    rowH = windowHeight // 20
    
    for i in range(colW):
        boardArr.append([])
        for j in range(rowH):
            boardArr[i].append(0)


#Count number of neigbours of a cell
def countNeighbours(array, i, j):
    
    count = 0

    if (array[i][j] == 1):
        count +=1

    if (array[i-1][j-1] == 1):
        count +=1

    if (array[i-1][j] == 1):
        count +=1

    if (array[i-1][j+1] == 1):
        count +=1

    if (array[i][j-1] == 1):
        count +=1

    if (array[i][j+1] == 1):
        count +=1

    if (array[i+1][j-1] == 1):
        count +=1

    if (array[i+1][j] == 1):
        count +=1

    if (array[i+1][j+1] == 1):
        count +=1

    print(count)

    return count



def Update(array, i, j):

    count = countNeighbours(array, i, j)

    #apply rules
    if (array[i][j] == 1 and count <2):
        array[i][j] == 0
        drawBlockBlack(i, j)
        
    if (array[i][j] == 1 and count == 2 or count == 3):
        array[i][j] == 1
        drawBlockWhite(i, j)

    if (array[i][j] == 1 and count > 3):
        array[i][j] == 0
        drawBlockBlack(i, j)
        
    if (array[i][j] == 0 and count == 3):
        array[i][j] == 1
        drawBlockWhite(i, j)




#Main loop for refreshing board status        
def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((windowWidth, windowHeight))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    initBoardArr()
    drawBlockWhite(2,2)
    drawBlockWhite(2,3)
    drawBlockWhite(2,4)
    drawBlockWhite(1,3)
    drawBlockWhite(1,4)
    drawBlockWhite(3,2)

    while True:
        drawGrid()
        Update(boardArr, 2, 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(1)
main()