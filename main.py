#Code for Ngee Ann City game, a city building strategy game

import random
exitMainMenu = False

buildingList = {'R': "Residential", 'I': "Industry", 'C': "Commercial", 'O': "Park", '*': "Road"}
defaultCoin = 16
Turn = 1
scoring_rules = {
    "Residential": {
        "Industry": 1,
        "Residential": 1,
        "Commercial": 1,
        "Park": 2,
        "Road": 0
    },
    "Industry": {
        "Industry": 1,
        "Residential": 1  
    },
    "Commercial": {
        "Commercial": 1,
        "Residential": 1 
    },
    "Park": {
        "Park": 1
    },
    "Road": {
        "Road": 1
    }
}    
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

def getRandomBuildings():
    r1 = random(list(buildingList))
    r2 = random(list(buildingList))
    return [r1,r2]

def getOptions(i, lower, upper):
    choice = input(i)
    if not choice.isdigit():
        return False
    choice = int(choice)
    if lower <= choice <= upper:
        return choice
    return False

def gameTurn():
    if Turn > len[field] * len[field][0]:
        return True
    
#Main program
while exitMainMenu == False:
    print('')
    print('------------------Welcome to Ngee Ann City------------------')
    print('[1] Start New Game')
    print('[2] Load Saved Game')
    print('[3] Display High Scores')
    print('[4] Exit Game')

    while True:
        choice = getOptions("Your Choice: ", 1, 4)
        if choice is not False:
            break
        print('')
        print('------------------Welcome to Ngee Ann City------------------')
        print('[1] Start New Game')
        print('[2] Load Saved Game')
        print('[3] Display High Scores')
        print('[4] Exit Game')
        print ("Invalid choice. Please choose again")

    match choice:
        case 1: 
            draw_field()
            
        case 2:
            "Load new game"
        case 3:
            "Display high score"
        case 4:
            exitMainMenu = True


print("Goodbye!")