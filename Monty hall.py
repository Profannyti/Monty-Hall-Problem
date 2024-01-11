import random

door_ascii = """
 __________           __________           __________
|  __  __  |         |  __  __  |         |  __  __  |                                  
| |  ||  | |         | |  ||  | |         | |  ||  | |
| |  ||  | |         | |  ||  | |         | |  ||  | |
| |__||__| |         | |__||__| |         | |__||__| |
|  __  __()|         |  __  __()|         |  __  __()|
| |  ||  | |         | |  ||  | |         | |  ||  | |
| |  ||  | |         | |  ||  | |         | |  ||  | |
| |  ||  | |         | |  ||  | |         | |  ||  | |                                                                             
| |__||__| |         | |__||__| |         | |__||__| |
|__________|         |__________|         |__________|
     A                     B                    C
"""
opened_door = """
 __________           
|  __  __  |                                        
| |  ||  | |         
| |  ||  | |         
| |__||__| |         
|  __  __()|         
| |  ||  | |         
| |  ||  | |         
| |  ||  | |                                                                                     
| |__||__| |         
|__________|  

"""

duck = """
⠀⠀⠀⠀⠀⢀⡴⠋⠉⠛⠒⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠏⠀⠀⣶⡄⠀⠀⣛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⡤⠋⠠⠉⠡⢤⢀⠀
⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⢉⣝⠲⠤⣄⣀⣀⠌
⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀
⢀⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀
⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀
"""

car = """


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣶⣿⠿⠿⠿⢿⣶⣶⣤⣀⣀⣀⣠⣤⣤⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠈⢿⡏⠉⢻⣿⣿⣿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⣴⣶⡄⠀⠀⢰⣿⠀⠀⠀⠘⣷⡀⠀⢹⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣇⣀⣤⣤⣤⣾⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⡆
⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠀⣰⠋⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣁⣀⣠⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣰⣷⣦⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⣿⣿⣿⣿⣿⣿⣿⠁⠈⠙⢿⣿⣿⣿⣿⠀⣿⠀
⣿⣿⣿⣿⣿⣷⡀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠘⣿⣿⣿⣿⠀⣿⠀
⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⣀⣀⣀⣀⣀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣿⣿⣿⣿⣀⣿⠀
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⣼⣿⠛⠛⠛⠛⠃⠀
⠀⠈⠙⠻⢿⣿⣿⣿⠿⠟⠛⠛⠛⠛⠛⠉⠉⠉⠉⠉⠀⠈⠻⣿⣿⣿⣷⣶⣶⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""

# ASCII to show opened door
door_with_duck = opened_door.replace("|  __  __()|", f"{duck}")

# door_with_car = opened_door.replace("|  __  __()|", f"{car}")



# Define rewards and doors
reward = [duck, duck, car]

door = {
    'A': '',
    'B': '',
    'C': ''
}

# Randomly assign rewards to doors
random.shuffle(reward)

for key in door:
    door[key] = reward.pop()


# Get user's initial choice
print(door_ascii)
initial_choice = input("Welcome to the monty hall problem by Profannyti, behind these doors, there are 2 ducks and a luxary car, choose a door of your choice (A, B, C): ").upper()

# Open a door with a duck that wasn't the initial choice
for item in door:
    if item == initial_choice:
        continue
    elif door[item] == duck:
        print(f"\nI am now going to open the door '{item}'")
        print(door_with_duck)
        break

# Ask the player if they want to switch
ask_to_switch = input("Would you like to switch to the other door or keep the door of your selection? (keep/switch): ")

# Display the final result based on the player's decision
if ask_to_switch == 'keep':
    print(door[initial_choice])

else:
    # Remove the opened door and display the remaining door
    del door[item], door[initial_choice]
    for final_key in door:
        print(door[final_key])























