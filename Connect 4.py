grid = [
    ["01", "02", "03", "04", "05", "06", "07"],
    ["08", "09", "10", "11", "12", "13", "14"],
    ["15", "16", "17", "18", "19", "20", "21"],
    ["22", "23", "24", "25", "26", "27", "28"],
    ["29", "30", "31", "32", "33", "34", "35"],
    ["36", "37", "38", "39", "40", "41", "42"],
]

current_piece = "Y"

def print_grid():
    for row in range(6):
        for col in range(7):
            if col != 6:
                print(grid[row][col], end="  ")            
            else:
                print(grid[row][col])
                print()

def is_bad_num_string(choice : str):
    if (choice.isnumeric() and int(choice) >= 1 and int(choice) <= 9):
        return False
    return True
                
def is_bad_choice(choice : str):
    if(choice.__eq__("STOP")):
        return False
    return is_bad_num_string(choice)

def get_row(grid_spot):
    if grid_spot == 1 or grid_spot == 2 or grid_spot == 3:
        return 0
    elif grid_spot == 4 or grid_spot == 5 or grid_spot == 6:
        return 1
    else:
        return 2    

def get_col(grid_spot):
    if grid_spot == 1 or grid_spot == 4 or grid_spot == 7:
        return 0
    elif grid_spot == 2 or grid_spot == 5 or grid_spot == 8:
        return 1
    else:
        return 2
    
def place_piece(grid_spot : int):
    while(True):
        row = get_row(grid_spot)
        col = get_col(grid_spot)
        grid_value = grid[row][col]
        if (not grid_value.__eq__("R") and not grid_value.__eq__("Y")):
            break
        user_choice = ""
        while (is_bad_num_string(user_choice)):
            user_choice = input(
                "Enter a number (1-9) where to put the piece: ")
        grid_spot = int(user_choice)
    grid[row][col] = current_piece 

def check_row():
    for row in range(3):
        if grid[row][0].__eq__(grid[row][1]) and grid[row][1].__eq__(grid[row][2]):
            return True
    return False
 
def check_col():
    for col in range(3):
        if grid[0][col].__eq__(grid[1][col]) and grid[1][col].__eq__(grid[2][col]):
            return True
    return False

def check_left_diag():
    return grid[0][0].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][2])

def check_right_diag():
    return grid[0][2].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][0])

def check_draw():
    for row in range(3):
        for col in range(3):
            if grid[row][col].isnumeric():
                return False  
    return True

def check_game_over():
    if check_row():
        print(current_piece + " wins!")
        return True
    elif check_col():
        print(current_piece + " wins!")
        return True
    elif check_left_diag():
        print(current_piece + " wins!")
        return True
    elif check_right_diag():
        print(current_piece + " wins!")
        return True
    elif check_draw():
        print("The Game Ends in a Draw!")
        return True
    else:
        return False

def game_loop():
    global current_piece
    print("Welcome to TIC TAC TOE")
    user_choice = ""
    while(True):
        print_grid()
        while(is_bad_choice(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (1-9) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        grid_spot = int(user_choice)
        place_piece(grid_spot)
        if(check_game_over()):
            print_grid()
            break
        current_piece = "Y" if current_piece.__eq__("R") else "R"
        user_choice = ""
    print("GAME OVER")
        
game_loop()