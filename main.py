#Code for Ngee Ann City game, a city building strategy game

import random
exitMainMenu = False

# list of buildings + respective points
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
    print()
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
    print()
    print(f"Turn: {State['Turn']}" f"  Points: {State['Points']}" f"  Coins: {State['Coins']}") # display turns

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

def gameTurn():
    # game menu
    if State['Turn'] > 400:
        return True
    print('')
    print('----------------------- Ngee Ann City-----------------------')
    print('[1] Build a Building')
    print('[2] See Current Score')
    print('[3] Save Game')
    print('[4] Exit to Main Menu')

    while True:
        # validation to checek that user has entered a valid choice
        choice = getOptions("Your Choice: ", 1, 4)
        if choice is not False:
            break
        print ("Invalid choice. Please choose again")
    
    match choice:
        case 1: # build building
            bList = getRandomBuildings()
            print(f'Building 1: {buildingList[bList[0]]}, Building 2: {buildingList[bList[1]]}')
            while True:
                ok = gameBuild("Your Choice: ","Build where? ",bList)
                if not ok:
                    break
        case 2:
            print(f"Points: {State['Points']}")
        case 3: # save game
            print("Save gameeeeee")
        case 4: # exit to main menu
            return True
    return False

def calculate_points(building_name, adjacent_buildings): #calculate points
    rules = pointsRules.get(building_name, {})
    points = 0
    for adj_building, adj_count in adjacent_buildings.items():
        # check for points based on rule
        points += rules.get(adj_building, 0) * adj_count
    return points

def calculate_coins(building_name, adjacent_buildings):
    coins = 0
    if building_name == 'I':  # 'I' represents 'Industry'
        coins = adjacent_buildings.get('R', 0)  # 'R' represents 'Residential'
    elif building_name == 'C':  # 'C' represents 'Commercial'
        coins = adjacent_buildings.get('R', 0)
    return coins

def is_connected(x, y): # fuction to check if the selected location is connected to an existing building
    for i in range(max(0, x - 1), min(x + 2, 20)):
        for j in range(max(0, y - 1), min(y + 2, 20)):
            if field[i][j] is not None:
                return True
    return False

def gameBuild(b, c, l):
    building_number = input(b)

    # validation to check if the entered building number is valid
    if building_number not in {'1', '2'}:
        print("Invalid building number")
        return True

    building_name = l[int(building_number) - 1]  # get the building name from the list

    coords = input(c)  # user input for building location
    x = coords[0]
    if not x.isalpha():  # validation to ensure that a valid row is inputted
        print("First character must be a letter")
        return True
    x = ord(x.lower()) - 96  # converting alphabet to numerical value
    y = coords[1]
    if not y.isnumeric():
        print("Second character must be a number")  # validation to ensure that a valid column is inputted
        return True
    y = int(y)

    # check if the cell is already occupied
    if field[x - 1][y - 1] is not None:
        print("Area is already occupied. Please choose a different location")
        return True

    # check if coordinates are within range
    if not (1 <= x <= 20 and 1 <= y <= 20):
        print("Invalid coordinates.  Please choose a different location")
        return True

    # check if it's the first placement
    if State['Turn'] == 1:
        adjacent_buildings = {}  # first building can be placed at any location
    else:
        # check if the selected location is connected to an existing building
        connected = is_connected(x - 1, y - 1)
        if not connected:
            print("You can only build on squares connected to existing buildings.")
            return True

        # calculate the number of adjacent buildings
        adjacent_buildings = {'R': 0, 'C': 0, 'O': 0, 'I': 0, '*': 0}
        for i in range(max(0, x - 1), min(x + 2, 20)):
            for j in range(max(0, y - 1), min(y + 2, 20)):
                if field[i][j] is not None:
                    adjacent_building_type = field[i][j][0]
                    if adjacent_building_type in adjacent_buildings:
                        adjacent_buildings[adjacent_building_type] += 1

    points = calculate_points(building_name, adjacent_buildings)
    coins_generated = calculate_coins(building_name, adjacent_buildings)

    print("Building name:", building_name)
    print("Adjacent buildings:", adjacent_buildings)
    print("Points:", points)
    print("Coins generated:", coins_generated)

    # update the field with the building name
    field[x - 1][y - 1] = building_name
    State['Turn'] += 1
    State['Points'] += points
    State['Coins'] -= 1  # each construction costs 1 coin
    State['Coins'] += coins_generated

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
            while True:
                draw_field()
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