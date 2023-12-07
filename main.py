#Code for Ngee Ann City game, a city building strategy game

import random
exitMainMenu = False

buildingList = {'R': "Residential", 'I': "Industry", 'C': "Commercial", 'O': "Park", '*': "Road"}
State = {
    "Turn" : 1,
    "Points" : 0,
    "Coins": 16
}
pointsRules = {
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
    r1 = random.choice(list(buildingList))
    r2 = random.choice(list(buildingList))
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
    if State['Turn'] > 400:
        return True
    print('')
    print('----------------------- Ngee Ann City-----------------------')
    print('[1] Build a Building')
    print('[2] See Current Score')
    print('[3] Save Game')
    print('[4] Exit to Main Menu')

    while True:
        choice = getOptions("Your Choice: ", 1, 4)
        if choice is not False:
            break
        print ("Invalid choice. Please choose again")
    
    match choice:
        case 1:
            bList = getRandomBuildings()
            print(f'Building 1: {buildingList[bList[0]]}, Building 2: {buildingList[bList[1]]}')
            while True:
                ok = gameBuild("Your Choice: ","Build where? ",bList)
                if not ok:
                    break
        case 2:
            print(State['Points'])
        case 3:
            print("Save gameeeeee")
        case 4:
            return True
    return False
def gameBuild(b,c,l):
    building = input(b)
    if building in buildingList and building in l:
        print("Invalid building")
        return True
    
    coords = input(c)
    x = coords[0]
    if not x.isalpha():
        print("X must be an alphabet")
        return True
    x = ord(x.lower()) - 96
    y = coords[1]
    if not y.isnumeric():
        print("Y must be a number")
        return True
    y = int(y)
    if (x <= 20 and y <= 20):
        if State['Turn'] is 1:
            field[x - 1][y - 1] = building
        State['Turn'] += 1    
    else:
        print("Invalid coordinates")
        return True

    return False
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
        print ("Invalid choice. Please choose again")

    match choice:
        case 1: 
            while True:
                draw_field()
                gameFinish = gameTurn()
                if gameFinish:
                    break
        case 2:
            "Load new game"
        case 3:
            "Display high score"
        case 4:
            exitMainMenu = True


print("Goodbye!")