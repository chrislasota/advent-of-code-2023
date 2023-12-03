# Advent of Code 2023
# Day 2
# Problem 2

def main():
    game_sum = 0
    input_file = open("input_day_02.txt", 'r')
    lines = input_file.readlines()

    for line in lines:
        line = line.rstrip()    # remove trailing whitespace characters, including newline

        # Let's use an example of a line from our input file as we walk through the code:
        #
        # line = 'Game 98: 3 red; 1 green, 10 red; 2 blue, 8 red; 1 green, 11 red, 2 blue'

        line_pieces = line.split(":")
        # line_pieces = ['Game 98', ' 3 red; 1 green, 10 red; 2 blue, 8 red; 1 green, 11 red, 2 blue']

        game_data = line_pieces[1].split(";")
        # game_data = [' 3 red', ' 1 green, 10 red', ' 2 blue, 8 red', ' 1 green, 11 red, 2 blue']

        # Next, we process game data into an ordered array of [R,G,B] counts for each draw from
        # the bag, and determine the maximal number of cubes seen of each color

        fail_flag = False
        maximums = [0, 0, 0]

        for bag_draw in game_data:
            # example : bag_draw = ' 2 blue, 8 red'

            processed_data = [0, 0, 0]         # intialize [R,G,B] cube counts

            cube_set = bag_draw.split(",")
            # cube_set = [' 2 blue', ' 8 red']

            for cube_color in cube_set:
                # example : cube_color = ' 2 blue'
                cube_color = cube_color.lstrip()
                # cube_color = '2 blue'
                data = cube_color.split(" ")
                # data = ['2', 'blue']
                if data[1] == "red":
                    processed_data[0] = int(data[0])
                if data[1] == "green":
                    processed_data[1] = int(data[0])
                if data[1] == "blue":
                    processed_data[2] = int(data[0])
            # when done iterating over this exmaple, processed_data = [8, 0, 2]

            for i in range(3):
                if processed_data[i] > maximums[i]:
                    maximums[i] = processed_data[i]

        # in our exapmple : maximums = [11, 1, 2]

        power = maximums[0] * maximums[1] * maximums[2]
        game_sum = game_sum + power

    input_file.close()
    return game_sum


if __name__ == "__main__":
    print(f"The sum is : {main()}")
