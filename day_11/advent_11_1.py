# Advent of Code 2023
# Day 11
# Part 1

def main() -> int:
    sum_of_lengths = 0
    galaxy_map = []

    # read first line of file ONLY to get width
    with open("input_day_11.txt", 'r') as input_file:
        line = input_file.readline().rstrip()
        original_width = len(line)

    galaxy_histogram = [0] * original_width

    original_height = 0
    # re-open file to process data
    with open("input_day_11.txt", 'r') as input_file:
        for line in input_file:
            line = line.rstrip()   # remove newline
            galaxy_map.append(line)
            original_height += 1
            for index in range(original_width):
                if line[index] == '#':
                    galaxy_histogram[index] += 1
            # duplicate any empty lines
            if '#' not in line:
                galaxy_map.append(line)

    # Perform horiz. expansion using galaxy_histogram[] to find empty columns
    new_height = len(galaxy_map)
    for row in range(new_height):
        temp_line = galaxy_map[row]
        # go backwards to avoid string length growth as we insert
        for index in range(original_width - 1, -1, -1):
            if galaxy_histogram[index] == 0:
                temp_line = temp_line[:index] + '.' + temp_line [index:]
        galaxy_map[row] = temp_line

    new_width = len(galaxy_map[0])
    # now create a list of all the galaxy locations, expressed as (row, column] tuples
    galaxy_locations = []
    for row in range(new_height):
        for column in range(new_width):
            if galaxy_map[row][column] == '#':
                galaxy_locations.append((row, column))

    # add up (Manhattan) distances between pairs of galaxies
    number_of_galaxies = len(galaxy_locations)
    for first in range(number_of_galaxies):
        for second in range(first + 1, number_of_galaxies):
            row_distance = abs(galaxy_locations[first][0] - galaxy_locations[second][0])
            column_distance = abs(galaxy_locations[first][1] - galaxy_locations[second][1])
            sum_of_lengths += (row_distance + column_distance)

    return sum_of_lengths


if __name__ == "__main__":
    print(f"The sum of pairwise lengths between galaxies is : {main()}")
