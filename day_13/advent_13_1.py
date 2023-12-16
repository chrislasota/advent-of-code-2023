# Advent of Code 2023
# Day 13
# Part 1

import character_grid

def find_horizontal_reflection(char_grid) -> int:
    # returns the number of columns to the left of the line of reflection
    height = char_grid.height()
    rows_above_reflection_line = 0
    # loop through rows and find any matching pairs
    for row_index in range(height - 1):
        if char_grid.get_row_str(row_index) == char_grid.get_row_str(row_index + 1):
            row_delta = 1
            # assume this match IS from a mirror until we prove otherwise
            is_a_mirror = True
            checking = True
            while checking:
                above_index = row_index - row_delta
                below_index = row_index + row_delta + 1
                if above_index >= 0 and below_index < height:
                    above_str = char_grid.get_row_str(above_index)
                    below_str = char_grid.get_row_str(below_index)
                    row_delta += 1
                    if above_str != below_str:
                        is_a_mirror = False
                        break
                else:
                    checking = False
            if is_a_mirror == True:
                rows_above_reflection_line += row_index + 1
    return rows_above_reflection_line


def find_vertical_reflection(char_grid) -> int:
    # returns the number of rows above the line of reflection
    width = char_grid.width()
    columns_left_of_reflection_line = 0
    # loop through columns and find any matching pairs
    for column_index in range(width - 1):
        if char_grid.get_column_str(column_index) == char_grid.get_column_str(column_index + 1):
            column_delta = 1
            # assume this match IS from a mirror until we prove otherwise
            is_a_mirror = True
            checking = True
            while checking:
                left_index = column_index - column_delta
                right_index = column_index + column_delta + 1
                if left_index >= 0 and right_index < width:
                    left_str = char_grid.get_column_str(left_index)
                    right_str = char_grid.get_column_str(right_index)
                    column_delta += 1
                    if left_str != right_str:
                        is_a_mirror = False
                        break
                else:
                    checking = False
            if is_a_mirror == True:
                columns_left_of_reflection_line += column_index + 1
    return columns_left_of_reflection_line


def summarize_mirror(char_grid) -> int:
    return find_vertical_reflection(char_grid) + 100 * find_horizontal_reflection(char_grid)


def main() -> int:
    total_summary = 0
    mirror_grid = []
    with open("input_day_13.txt") as input_file:
        for line in input_file:
            line = line.rstrip()   # remove newline
            if line != '':
                row = []
                for char in line:
                    row.append(char)
                mirror_grid.append(row)
            else:
                # done reading data for one mirror, process data
                grid = character_grid.CharacterGrid(mirror_grid)
                total_summary += summarize_mirror(grid)
                mirror_grid = []

    # Process last mirror separately beacause of how we read the file input
    grid = character_grid.CharacterGrid(mirror_grid)
    total_summary += summarize_mirror(grid)
    return total_summary


if __name__ == "__main__":
    print(f"Total summarized notes value : {main()}")
