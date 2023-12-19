# Advent of Code 2023
# Day 11
# Part 2

def main() -> int:

    cosmic_addition_factor = 999999 # how many EXTRA rows/column are added for every empty row/column 

    # create input galaxy map as a list[] of strings of '.' and '#' characters
    galaxy_map = []
    with open("input_day_11.txt") as input_file:
        for line in input_file:
            line = line.rstrip()   # remove newline
            galaxy_map.append(line)

    map_height = len(galaxy_map)
    map_width  = len(galaxy_map[0])

    # indentify which rows and columns have no galaxies using histograms
    galaxy_row_histogram = []
    galaxy_column_histogram = [0] * map_width
    for row in range(map_height):
        line = galaxy_map[row]
        galaxy_row_count = 0
        for index in range(map_width):
            if line[index] == '#':
                galaxy_row_count += 1
                galaxy_column_histogram[index] += 1
        galaxy_row_histogram.append(galaxy_row_count)

    # create a list of (row, column) tuples for the location of each galaxy
    # performing the expansion as we do so
    galaxy_locations = []
    row_expansion = 0
    for row in range(map_height):
        column_expansion = 0
        for column in range(map_width):
            if galaxy_map[row][column] == '#':
                location = (row + row_expansion, column + column_expansion)
                galaxy_locations.append(location)
            if galaxy_column_histogram[column] == 0:
                column_expansion += cosmic_addition_factor
        if galaxy_row_histogram[row] == 0:
            row_expansion += cosmic_addition_factor

    # add up (Manhattan) distances between pairs of galaxies
    sum_of_lengths = 0
    number_of_galaxies = len(galaxy_locations)
    for first in range(number_of_galaxies):
        for second in range(first + 1, number_of_galaxies):
            row_distance = abs(galaxy_locations[first][0] - galaxy_locations[second][0])
            column_distance = abs(galaxy_locations[first][1] - galaxy_locations[second][1])
            sum_of_lengths += (row_distance + column_distance)

    return sum_of_lengths


if __name__ == "__main__":
    print(f"The sum of pairwise lengths between galaxies is : {main()}")
