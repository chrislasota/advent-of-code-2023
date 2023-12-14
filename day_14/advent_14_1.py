# Advent of Code 2023
# Day 14
# Part 1

def tilt_the_dish(dish):
    dish_rows = len(dish)
    dish_columns = len(dish[0])
    # "tilt" one column at a time
    for column in range(dish_columns):
        # create a string from the column chars so we can use string methods.
        vertical_str = ''
        for row in range(dish_rows):
            vertical_str += dish[row][column]
        split_str_list = vertical_str.split('#')
        # Elements of this list are either '', 'O', '.', or a string of chars
        # from set {'0', '.'}.  We "tilt" all of the substrings of length 2
        # or greater and then and assemble the entire "tilted" string.
        for index in range(len(split_str_list)):
            substring = split_str_list[index]
            substring_length = len(substring)
            if substring_length < 2:
                continue
            number_of_rocks = substring.count('O')
            new_string_rocks = 'O' * number_of_rocks
            new_string_gaps = '.' * (substring_length - number_of_rocks)
            split_str_list[index] = new_string_rocks + new_string_gaps
        new_vertical_str = ''
        for piece in split_str_list:
            if piece != '':
                new_vertical_str += piece
            new_vertical_str += '#'
            new_vertical_str = new_vertical_str[:dish_rows]  # toss extra '#'
        for index in range(dish_rows):
            dish[index][column] = new_vertical_str[index]
    return


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
    tilt_the_dish(dish_grid)
    return find_total_load(dish_grid)


if __name__ == "__main__":
    print(f"The number of steps to the furthest location is : {main()}")
