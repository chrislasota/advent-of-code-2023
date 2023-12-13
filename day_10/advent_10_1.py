# Advent of Code 2023
# Day 10
# Part 1

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
    with open("input_day_10.txt", 'r') as input_file:
        for line in input_file:
            line = line.rstrip()   # remove newline
            pipe_map.append(line)
    # Done reading input file

    # Find 'S' starting position
    found_S = False
    for row in range(len(pipe_map)):
        if found_S == True:
            break
        line = pipe_map[row]
        for column in range(len(line)):
            if line[column] == 'S':
                s_row, s_column = row, column
                found_S = True
                break

    # THIS NEXT PART IS UGLY UGLY UGLY!!!
    # Figure out which kind of pipe 'S' is
    up, down, left, right = False, False, False, False
    if s_row != 0 and s_column !=0:
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

    # Now loop along the path until you get back to the starting point
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

    return total_steps // 2   # total_steps WILL NECESSARILY BE an even number


if __name__ == "__main__":
    print(f"The number of steps to the furthest location is : {main()}")
