# Advent of Code 2023
# Day 10
# Part 2

def main() -> int:
    total_steps = 0
    # tuples below are displacements (delta_row, delta_column)
    move_dict = { 'J': [( 0, -1), (-1, 0)],
                  '-': [( 0, -1), ( 0, 1)],
                  '7': [( 0, -1), ( 1, 0)],
                  'L': [(-1,  0), ( 0, 1)],
                  '|': [(-1,  0), ( 1, 0)],
                  'F': [( 0,  1), ( 1, 0)] }

    pipe_map = []
    path_only_map = []

    with open("input_day_10.txt", 'r') as input_file:
        for line in input_file:
            line = line.rstrip()   # remove newline
            pipe_map.append(line)
    # Done reading input file

    map_height = len(pipe_map)
    map_width = len(pipe_map[0])

    # Find 'S' starting position
    found_S = False
    for row in range(map_height):
        line = pipe_map[row]
        path_only_map.append('.' * map_width)
        if found_S == True:
            continue
        for column in range(map_width):
            if line[column] == 'S':
                s_row, s_column = row, column
                found_S = True
                break

    # THIS NEXT PART IS UGLY UGLY UGLY!!!
    # Figure out which kind of pipe 'S' is
    up, down, left, right = False, False, False, False
    if s_row != 0 and s_column !=0 and s_row < map_height and s_column < map_height :
        pipe_char = pipe_map[s_row - 1][s_column]
        if pipe_char == '7' or pipe_char == '|' or pipe_char == 'F':
            up = True
        pipe_char = pipe_map[s_row][s_column - 1]
        if pipe_char == '-' or pipe_char == 'L' or pipe_char == 'F':
            left = True
        pipe_char = pipe_map[s_row][s_column + 1]
        if pipe_char == 'J' or pipe_char == '-' or pipe_char == '7':
            right = True
        pipe_char = pipe_map[s_row + 1][s_column]
        if pipe_char == 'J' or pipe_char == '|' or pipe_char == 'L':
            down = True
    else:
        print("S is on the boundary -- deal with this by writing more code")
        exit(1)

    if up and left:
        current_char = 'J'
    if up and down:
        current_char = '|'
    if up and right:
        current_char = 'L'
    if left and right:
        current_char = '-'
    if left and down:
        current_char = '7'
    if right and down:
        current_char = 'F'

    s_equivalent = current_char

    # Now loop along the path until you get back to the starting point,
    # creating a new path_only_map that turns all non-loop pipe into '.'
    previous_location = (s_row, s_column)
    row = s_row
    column = s_column
    while True:
        displacement_1 = move_dict[current_char][0]
        displacement_2 = move_dict[current_char][1]
        new_row = row + displacement_1[0]
        new_column = column + displacement_1[1]
        if (new_row, new_column) == previous_location:
            new_row = row + displacement_2[0]
            new_column = column + displacement_2[1]
        total_steps += 1
        if new_row == s_row and new_column == s_column:
            break
        current_char = pipe_map[new_row][new_column]
        previous_location = (row, column)
        row, column = new_row, new_column
        temp_row = path_only_map[row]
        temp_row = temp_row[:column] + current_char + temp_row[column+1:]
        path_only_map[row] = temp_row

    temp_row = path_only_map[s_row]
    temp_row = temp_row[:s_column] + s_equivalent + temp_row[column+1:]
    path_only_map[s_row] = temp_row

    # Now scan across the rows of the path_only_map[], and pay
    # attention to crossing the path
    inner_tiles = 0

    for row in range(map_height):
        side_status = -1  # -1 means out and +1 means in
        path_status = "off"
        for column in range(map_width):
            char = path_only_map[row][column]
            if char == '.' and side_status == 1:
                inner_tiles += 1
                continue

            if char == '|':
                side_status = -(side_status)

            if path_status == "off" and char in {'L', 'F'}:
                path_status = char
                continue

            if path_status == 'L':
                if char == 'J':
                    path_status = "off"
                if char == '7':
                    side_status = -(side_status)
                    path_status = "off"
                continue
            if path_status == 'F':
                if char == '7':
                    path_status = "off"
                if char == 'J':
                    side_status = -(side_status)
                    path_status = "off"
                continue

    return inner_tiles


if __name__ == "__main__":
    print(f"The total number of tiles enclosed by the loop is : {main()}")
