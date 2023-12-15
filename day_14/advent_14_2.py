# Advent of Code 2023
# Day 14
# Part 2

import copy

def tilt_the_dish(dish, direction):
    dish_rows = len(dish)
    dish_columns = len(dish[0])

    if direction in {"north", "south"}:
        # tilt" one column at a time
        for column in range(dish_columns):
            # create a string from the column chars so we can use string methods.
            vertical_str = ''
            for row in range(dish_rows):
                vertical_str += dish[row][column]
            if direction == "north":
                tilted_string = tilt_rocks(vertical_str, "start")
            if direction == "south":
                tilted_string = tilt_rocks(vertical_str, "finish")
            for row in range(dish_rows):
                dish[row][column] = tilted_string[row]

    if direction in {"west", "east"}:
        # tilt on row at a time
        for row in range(dish_rows):
            # create a string from the row chars so we can use string methods.
            horizontal_str = ''
            for column in range(dish_columns):
                horizontal_str += dish[row][column]
            if direction == "west":
                tilted_string = tilt_rocks(horizontal_str, "start")
            if direction == "east":
                tilted_string = tilt_rocks(horizontal_str, "finish")
            for column in range(dish_columns):
                dish[row][column] = tilted_string[column]
    return


def tilt_rocks(rock_str, direction="start") -> str:
    # The input is a string created from a row or column of the dish_grid
    # The "rocks" are shifted towards the start of the string when direction="start"
    # and are shifted towards the end of the string when direction="finish"
    # The "tilted" string is returned

    substring_list = rock_str.split('#')
    # Elements of substring_list are either '', 'O', '.', or a string of
    # chars in set {'0', '.'}.  We "tilt" each of the substrings of
    # length 2 or greater and then and assemble the entire "tilted" string.
    for index in range(len(substring_list)):
        substring = substring_list[index]
        substring_length = len(substring)
        if substring_length < 2:
            continue
        number_of_rocks = substring.count('O')
        new_string_rocks = 'O' * number_of_rocks
        new_string_gaps = '.' * (substring_length - number_of_rocks)
        if direction == "finish":
            substring_list[index] = new_string_gaps + new_string_rocks
        else:
            substring_list[index] = new_string_rocks + new_string_gaps

        # assemble tilted string
        new_str = ''
        for piece in substring_list:
            if piece != '':
                new_str += piece
            new_str += '#'
        temp_length = len(new_str)
        new_str = new_str[:temp_length]  # dump extra '#'
    return new_str


def find_total_load(dish):
    load_sum = 0
    total_rows = len(dish)
    for current_row in range(total_rows):
        rock_count = 0
        for char in dish[current_row]:
            if char == 'O':
                load_sum += total_rows - current_row
    return load_sum


def main() -> int:
    dish_grid = []
    with open("input_day_14.txt") as input_file:
        for line in input_file:
            line = line.rstrip()   # remove newline
            row = []
            for char in line:
                row.append(char)
            dish_grid.append(row)
    dish_rows = len(dish_grid)
    dish_columns = len(dish_grid[0])

    # Do a bunch of initial cycles to shake out transients and reach
    # a periodic siutation.
    num_cycles = 1000
    print(f"Running {num_cycles} initial cycles to reach a periodic configuration.  Please wait...")
    for cycle in range(num_cycles):
        for direction in ["north", "west", "south", "east"]:
            tilt_the_dish(dish_grid, direction)

    # Now do UP TO 1000 more cycles and look for a repeat of the
    # configuration we now have after the initial cycles
    jostled_dish_grid = copy.deepcopy(dish_grid)
    print("Now looking for a repeated configuration...")
    for cycle in range(1000):
        for direction in ["north", "west", "south", "east"]:
            tilt_the_dish(dish_grid, direction)
        if dish_grid == jostled_dish_grid:
            print(f"Found one in {cycle} cycles.")
            break
    return find_total_load(dish_grid)


if __name__ == "__main__":
    print(f"The total load on the north support beams is : {main()}")
