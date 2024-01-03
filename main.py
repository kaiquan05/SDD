#Code for Ngee Ann City game, a city building strategy game

import random
exitMainMenu = False

# list of buildings + respective points
buildingList = {
    'R': "Residential", 
    'I': "Industry", 
    'C': "Commercial", 
    'O': "Park", 
    '*': "Road"
}
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
#
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
            if field[row][col] == None: # checking if the cell is occupied
                print('    ', end = '')
            else:
                print('{:4s}'.format(field[row][col][0]), end = '')
        print('|')
        print(" +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+")

# get building function to get two random buildings for the user to select
def getRandomBuildings():
    r1 = random.choice(list(buildingList))
    r2 = random.choice(list(buildingList))
    return [r1,r2]

# validation function to check if user has entered a valid choice 
def getOptions(i, lower, upper):
    choice = input(i)
    if not choice.isdigit():
        return False
    choice = int(choice)
    if lower <= choice <= upper:
        return choice
    return False

def calculatePoints():
    p = State['Points']
    for row in range(len(field)):
        for col in range(len(field[row])):
            building_code = field[row][col]
            if building_code is None:
                continue
            building_type = buildingList[building_code]
            adj_buildings_codes = checkOrthogonal(row, col)

            for adj_building_code in adj_buildings_codes:
                if adj_building_code is None:
                    continue

                adj_building_type = buildingList[adj_building_code]
                # Ensure the building type and adjacent building type are in pointsRules
                if building_type in pointsRules and adj_building_type in pointsRules[building_type]:
                    p += pointsRules[building_type][adj_building_type]

    State['Points'] = p


            

def gameTurn():
    # game menu
    if State['Turn'] > 400:
        return True
    
    displayPoints = False  # Flag to control redrawing the game state

    print('')
    print('----------------------- Ngee Ann City-----------------------')
    draw_field()
    bList = getRandomBuildings()
    print(f'Turn: {State["Turn"]}')
    print(f'[1] Build a {buildingList[bList[0]]}')
    print(f'[2] Build a {buildingList[bList[1]]}')
    print('[3] See Current Score')
    print('\n[4] Save Game')
    print('[5] Exit to Main Menu')
    if displayPoints:
        calculatePoints()
        print(f'Current Points: {State["Points"]}')\
    
    while True:
        # validation to checek that user has entered a valid choice
        choice = getOptions("Your Choice: ", 1, 5)
        if choice is not False:
            break
        print ("Invalid choice. Please choose again")
    if choice is not False:
        if choice == 1 or choice == 2:
            # build building
            building_choice = bList[0] if choice == 1 else bList[1]
            while True:
                ok = gameBuild(bList, "Build where? ", building_choice)
                if not ok:
                    break
            displayPoints = False  
        elif choice == 3:
            # see current score
            calculatePoints()
            print(f"Current Points : {State['Points']}")
            displayPoints = True  
        elif choice == 4:
            # save game
            print("Save gameeeeee")
            redraw = False
        elif choice == 5:
            return True
    else:
        print("Invalid choice. Please choose again")
        redraw = False 

    return False


def checkOrthogonal(x, y):
    adj = []
    if x > 0 and field[x - 1][y] is not None:
        adj.append(field[x - 1][y])
    if x < len(field) - 1 and field[x + 1][y] is not None:
        adj.append(field[x + 1][y])
    if y > 0 and field[x][y - 1] is not None:
        adj.append(field[x][y - 1])
    if y < len(field[x]) - 1 and field[x][y + 1] is not None:
        adj.append(field[x][y + 1])
    return adj

# build building function
def gameBuild(b,c,l):
    coords = input(c) # user input for building location
    x = coords[0]
    if not x.isalpha(): # validation to ensure that a valid row is inputted
        print("X must be an alphabet")
        return True
    x = ord(x.lower()) - 96 # converting alphabet to numerical value
    y = coords[1]
    if not y.isnumeric():
        print("Y must be a number") # validation to ensure that a valid column is inputted
        return True
    y = int(y)
    # update the field with the building name
    if (x <= 20 and y <= 20 and x >= 1 and y >= 1):
        if State['Turn'] == 1:
            field[x - 1][y - 1] = l
        elif State['Turn'] > 1:
            if field[x - 1][y - 1] is None:
                ok = checkOrthogonal(x - 1, y - 1)  
                if len(ok) != 0:
                    field[x - 1][y - 1] = l
                else: 
                    print("Cell is not orthogonal to existing buildings")
                    return True
            else:
                print("Cell is occupied")
                return True
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
        # validation to checek that user has entered a valid choice
        choice = getOptions("Your Choice: ", 1, 4)
        if choice is not False:
            break
        print ("Invalid choice. Please choose again")

    match choice: # associate choice to respective game features
        case 1:  # start new game
            for row in range(len(field)):
                for item in range(len(field[row])):
                    if field[row][item] is not None:
                        field[row][item] = None
            State['Turn'] = 1
            State['Points'] = 0
            while True:
                gameFinish = gameTurn()
                if gameFinish:
                    break
        case 2: # load a previously created game
            "Load new game"
        case 3: # display all high scores
            "Display high score"
        case 4: # exit the game into main menu
            exitMainMenu = True

print("Goodbye!")