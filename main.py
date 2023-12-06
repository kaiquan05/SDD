#Code for Ngee Ann City game, a city building strategy game

import random
randomNum = random.randint(1,5)
exitMainMenu = False

#----------------------------------------------------------------------
# draw_field()
#
#    Draws the field of play
#    The column numbers only go to 3 since players can only place units
#      in the first 3 columns
#----------------------------------------------------------------------
field = [ [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]



def draw_field():
    row_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
    print("   1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20")
    print(" +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+")
    for row in range(len(field)):
        print(row_names[row], end = '')
        for col in range(len(field[row])):
            print('|', end = '')
            if field[row][col] == None:
                print('    ', end = '')
            else:
                print('{:5s}'.format(field[row][col][0]), end = '')
        print('|')
        print(' ', end = '')
        for col in range(len(field[row])):
            print('|', end = '')
            if field[row][col] == None:
                print('    ', end = '')
            else:
                print('15/15', end = '') # change this to print current HP and max HP
        print('|')
        print(" +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+")


#Main program
while exitMainMenu == False:
    print('')
    print('------------------Welcome to Ngee Ann City------------------')
    print('[1] Start New Game')
    print('[2] Load Saved Game')
    print('[3] Display High Scores')
    print('[4] Exit Game')

    playerMenuInput = int(input('Please input your choice: '))

    if playerMenuInput == 1:
        print('start new game')
        draw_field()
    elif playerMenuInput == 2:
        print('load saved code')
    elif playerMenuInput == 3:
        print('Display highscore')
    elif playerMenuInput == 4:
        exitMainMenu = True
        print('Exiting Ngee Ann City...')

