# Advent of Code 2023
# Day 2
# Problem 1

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

        game_text = line_pieces[0].split(" ")
        # game_text = ['Game', '98']

        game_number = int(game_text[1])
        # game_number = 98

        game_data = line_pieces[1].split(";")
        # game_data = [' 3 red', ' 1 green, 10 red', ' 2 blue, 8 red', ' 1 green, 11 red, 2 blue']

        # Next, we process game data into an ordered array of [R,G,B] counts for each draw from
        # the bag, and check to see if any of the draws violate the problem criteria

        fail_flag = False

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

            # when done iterating this exmaple, processed_data = [8, 0, 2]

            # check if the condition for the problem is violated
            if processed_data[0] > 12 or processed_data[1] > 13 or processed_data[2] > 14:
                fail_flag = True

        if fail_flag == False:
            game_sum = game_sum + game_number

    return game_sum


if __name__ == "__main__":
    print(f"The sum is : {main()}")
