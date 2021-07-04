import os
import re

"""
Welcome to Mars!

It's taken quite some time but we've finally got enough rovers on the planet for public use!
Curious to explore the planet? Well, run the application and begin the adventure.

Some Constraints before we get started:
- The world is a grid with size m * n
- The program asks for inputs, which then moves the rovers and shows their final state/location
- The rovers have a position (x,y) and an orientation (N,E,S,W)
- Rovers can move forward one space (F), rotate left by 90 degrees (L), rotate right (R)
- Be careful, we only have a limited view of the rovers. If the rover gets off the grid, 
    it's marked as lost (we'll bill you, no worries).
- x -> x + 1 (you're heading East), y -> y + 1 (North), negatives are opposite
- (0, 0) represents SW

Program Structure:
1. User inputs grid size (ex. 4 8)
2. User inputs initial state, and then commands for the rover. Ex: (2,3,E) LFRFF
    a. x=2, y=3, facing East. Move Left, Forward, Right, Forward x2
3. The output shows the updated state of the rover:
"""

os.system('clear')

print("""
**************************************************
***         Welcome to Mars, Recruit!          ***
***    Be sure to visit the gift shop after.   ***
**************************************************

It's taken quite some time but we've finally got 
enough rovers on the planet for public use! Curious 
to explore the planet? Well, enter your name to 
start your adventure.
""")

quit_signals = ('q', 'Q', "quit", "exit")
# name = input("What is your Name?\nSergeant ")

# grid_size = input("Please enter the grid size (ex: 4 8):\n")
# robots = []
# while len(robots) != 3:
#     robots.append(input("Please enter the rover details (ex: (2, 3, E) LFRFF):\n"))

grid_size = "4 8"
# rover_desc = "(2, 3, E) LFRFF"
rover_desc = "(0, 2, N) FFLFRFF"

rover_steps = rover_desc.split(") ")[1]  # LFRFF
rover_coords = rover_desc[rover_desc.find("(") + 1:rover_desc.find(")")].split(', ')
rover_direction = rover_coords[-1]  # E
rover_coords = rover_coords[:2]  # [2,3]

rotate_left = {
    "E": "N",
    "N": "W",
    "W": "S",
    "S": "E"
}

rotate_right = {
    "E": "S",
    "N": "E",
    "W": "N",
    "S": "W"
}


def will_rover_leave_grid(grid, coords, direction):
    if direction == 'E':
        return int(coords[0]) + 1 > int(grid[0])
    elif direction == "W":
        return int(coords[0]) - 1 < 0
    elif direction == "N":
        return int(coords[1]) + 1 > int(grid[1])
    else:
        return int(coords[1]) - 1 < 0


def update_coords(coords, direction):
    if direction == "E":
        coords = [int(coords[0]) + 1, int(coords[1])]

    elif direction == "W":
        coords = [int(coords[0]) - 1, int(coords[1])]

    elif direction == "N":
        coords = [int(coords[0]), int(coords[1]) + 1]

    elif direction == "S":
        coords = [int(coords[0]), int(coords[1]) - 1]

    return coords


# grid=[4, 8] ,steps=FFLFRF, direction=E, coords=["0", "1"]
def move_rover(grid, steps, direction, coords):
    grid = grid.split(" ")
    is_lost = False
    for step in steps:
        if step == "L":
            direction = rotate_left[direction]
        if step == "R":
            direction = rotate_right[direction]
        if step == "F":
            if will_rover_leave_grid(grid, coords, direction):
                is_lost = True
                break
            coords = update_coords(coords, direction)
    result = f"{coords[0]}, {coords[1]} {direction}" + (" (Lost)" if is_lost else "")
    print(result)
    return result


move_rover(grid_size, "FFFRFFFF", "N", ["0", "0"])

# for step in rover_steps:
#     if step == "L":
#         rover_direction = rotate_left[rover_direction]
#     if step == "R":
#         rover_direction = rotate_right[rover_direction]
#     if step == "F":
#         if will_rover_leave_grid(grid, rover_coords, rover_direction):
#             break
#         rover_coords = update_coords(rover_coords, rover_direction)
#
# print(f"{rover_coords[0]}, {rover_coords[1]} {rover_direction}")
