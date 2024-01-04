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
coinsRules = {
    "Industry": {
        "Residential": 1  
    },
    "Commercial": {
        "Residential": 1 
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
    print("\n"f"Turn: {State['Turn']}" f"  Points: {State['Points']}" f"  Coins: {State['Coins']}") # display turns

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

def calculateCoins():
    c = 0
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
                # Ensure the building type and adjacent building type are in coinsRules
                if building_type in coinsRules and adj_building_type in coinsRules[building_type]:
                    c += coinsRules[building_type][adj_building_type]
    return c
            
def save_game(): 
    file=open('SaveNgeeAnnCity.txt','w') 
    file.write(str(State['Turn'])) #save turn 
    file.write('\n') 
    file.write(str(State['Points'])) #save points
    file.write('\n') 
    file.write(str(State['Coins'])) #save coins  
    file.write('\n') 
    for i in range(len(field)): 
        for n in range(len(field[i])): #save stuff in field that is not none as well as its coordinate 
            if field[i][n] != None: 
                file.write(str(field[i][n][0])) 
                file.write(';') 
                file.write(str(i)) 
                file.write(';') 
                file.write(str(n)) 
                file.write('\n')         
    file.close()
    print("Game saved.")

def load_game():
    load_list = []
    file = open('SaveNgeeAnnCity.txt', 'r') #read save file
    for i in file:
        i = i.strip()
        load_list.append(i)

    file.close()
    for n in range(3, len(load_list)):
        load_list[n] = load_list[n].split(';')
        field[int(load_list[n][1])][int(load_list[n][2])]=[str(load_list[n][0])]

    State['Turn'] = int(load_list[0])
    State['Points'] = int(load_list[1])
    State['Coins'] = int(load_list[2])
    print("Loading game...")
    return

def save_score():
    file=open('SaveScoreNgeeAnnCity.txt','w') #writing new highscore to notepad
    for i in range(1, 12):
        # Write the string "test;" followed by the incremented number and a newline character
        file.write(f'test;{i}\n')

    inputName = input("Please input a name to save game score: ")
    print(f'Game name: {inputName}')
    print(f'Score: {State["Points"]}')
    load_list = []
    file=open('SaveScoreNgeeAnnCity.txt','r') #read file
    for i in file:
        i = i.strip()
        load_list.append(i)
    file.close()
    load_list.append([str(inputName), str(State["Points"])]) #add new score to list

    load_list.sort(key=lambda x: x[1], reverse = True) #sort by second element, points, instead of by game name
    if len(load_list) > 10:
        load_list = load_list[:10]  #removes all other elements in list except for first 10(aka top 10)
    
    file=open('SaveScoreNgeeAnnCity.txt','w') #writing new highscore to notepad
    file.write("") #clears entire notepad
    for n in range(0,len(load_list)):
        file.write(str(load_list[n]))
        file.write(';') 
        file.write(str(load_list[n]))
        file.write('\n') 

    file.close()
    print('Game name and score saved.')



def gameTurn():
    # game menu
    if State['Turn'] > 400:
        return True
    
    calculatePoints()

    print('')
    print('----------------------- Ngee Ann City-----------------------')
    draw_field()
    bList = getRandomBuildings()
    print(f'[1] Build a {buildingList[bList[0]]}')
    print(f'[2] Build a {buildingList[bList[1]]}')
    print('\n[3] Save Game')
    print('[4] Exit to Main Menu')
    
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
            
        elif choice == 3:
            # save game
            save_game()
            return True
        elif choice == 4:
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
    if not x.isalpha():  # validation to ensure that a valid row is inputted
        print("First character must be a letter")
        return True
    x = ord(x.lower()) - 96  # converting alphabet to numerical value
    y = coords[1]
    if not y.isnumeric():
        print("Second character must be a number")  # validation to ensure that a valid column is inputted
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
        State['Coins'] -= 1
        State['Coins'] += calculateCoins()

    else:
        print("Invalid coordinates")
        return True

#Main program
while exitMainMenu == False:
    print('')
    print('------------------Welcome to Ngee Ann City------------------')
    print('[1] Start New Game')
    print('[2] Load Saved Game')
    print('[3] Display High Scores')
    print('[4] Exit Game')

    save_score()

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
                    "save_score"
                    break
        case 2: # load a previously created game
            load_game()
            while True:
                gameFinish = gameTurn()
                if gameFinish:
                    "save_score"
                    break
        case 3: # display all high scores

            "Display high score"
        case 4: # exit the game into main menu
            exitMainMenu = True

print("Goodbye!")