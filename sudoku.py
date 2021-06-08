from tkinter import *
import sys, pygame as pg


# pg.init()
# screen_size = 750, 750
# screen = pg.display.set_mode(screen_size)
# font = pg.font.SysFont(None, 80)
matrix = [[0,0,0,2,6,0,7,0,1],[6,8,0,0,7,0,0,9,0],[1,9,0,0,0,4,5,0,0],[8,2,0,1,0,0,0,4,0],[0,0,4,6,0,2,9,0,0],[0,5,0,0,0,3,0,2,8],[0,0,9,3,0,0,0,7,4],[0,4,0,0,5,0,0,3,6],[7,0,3,0,1,8,0,0,0]]



def drawBackground():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80) < 720:
        if i % 3 > 0:
            line_width = 5
        else:
            line_width = 10
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * 80) + 15, 15), pg.Vector2((i * 80) + 15, 735), line_width) #vertical lines
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, (i * 80) + 15), pg.Vector2(735, (i * 80) + 15 ), line_width) #horizontal lines


        i += 1

def drawBoard():

    row = 0

    while(row < 9):
        col = 0
        while(col <9):
            output = matrix[row][col]
            n_text = font.render(str(output), True, pg.Color('black'))
            screen.blit(n_text, pg.Vector2((col * 80) + 45, (row * 80) + 45))
            col += 1

        row +=1



def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    drawBackground()
    drawBoard()
    pg.display.flip()


#while(1):
#    game_loop()



# grabs all 0 coordinates
def find0(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                # x, y coordinates respectively
                return (i, j)
    return False

# checks for rowCheck, columnCheck, and boxCheck
def check(matrix, num, pos) -> bool:

# rowCheck
    for i in range(9):
        if (matrix[pos[0]][i] == num and pos[1] != i):
            return False
# columnCheck
    for i in range(9):
        if(matrix[i][pos[1]] == num and pos[0] != i):
            return False
# boxCheck
    xbox = pos[1] // 3
    ybox = pos[0] // 3

    for i in range(ybox * 3,  ybox * 3 + 3):
            for j in range(xbox * 3,  xbox * 3 + 3):
                if (matrix[i][j] == num and (i, j) != pos):
                    return False

    return True
# uses recursion until no boxes are equal to 0
def run(matrix):
    find = find0(matrix)
    if find == False: # if cannot find anymore 0's
        return True
    row, column = find

    for i in range(1, 10):
        if (check(matrix, i, (row, column)) == True):
            matrix[row][column] = i

            if run(matrix) == True:
                return True # which means it is finished

            matrix[row][column] = 0

    return False

def menu():
    print("Welcome!")
    print("1. Sudoku\n2. Tic Tac Toe\n3. Rock Paper Scissor")
    choice = input("Which Game Would You Like to Play: ")

    if(choice == 1):
        main()
    elif(choic == 2):
        tic_tac_toe()
    else:
        rpp()

    pa = input(str("Play again? (y/n)"))
    if(choice == 'y'):
        menu()

def tic_tac_toe():
    printTTT()

def rpp():
    pass

def printTTT():
    for i in range(2):
        print("   |   |   |")
        print("---------------")


def main():
    #                                         |||||
    # to change/ input the matrix change this vvvvv
    #matrix = [[0,0,0,2,6,0,7,0,1],[6,8,0,0,7,0,0,9,0],[1,9,0,0,0,4,5,0,0],[8,2,0,1,0,0,0,4,0],[0,0,4,6,0,2,9,0,0],[0,5,0,0,0,3,0,2,8],[0,0,9,3,0,0,0,7,4],[0,4,0,0,5,0,0,3,6],[7,0,3,0,1,8,0,0,0]]
    print("First Matrix: ")
    printBoard(matrix)

    run(matrix)
    print("\nSecond Matrix: ")
    printBoard(matrix)

# func that prints the board with lines
def printBoard(newMatrix):
    for i in range(len(newMatrix)):
        if(i % 3 == 0):
            print("--------------------")
        for j in range(9):
            if j % 3 == 0:
                 print("|", end = "")
            if(j == 8):
                print(newMatrix[i][j])
            else:
                print(str(newMatrix[i][j]) + " ", end = "")


if __name__ == "__main__":
    menu()
