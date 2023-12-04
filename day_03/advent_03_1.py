# Advent of Code 2023
# Day 3
# Problem 1

def main():
    game_sum = 0
    digit_characters = "0123456789"
    raw_schematic = []
    with open("input_day_03.txt", 'r') as input_file:
        for line in input_file:
            line = line.rstrip()        # remove trailing whitespace
            raw_schematic.append(line)

    # THIS IS THE UGLIEST ALGORITHM I'VE EVER HACKED TOGETHER IN A FEW HOURS

    # now create individual character map with added '.' perimeter
    char_grid = []
    new_width = len(raw_schematic[0]) + 2

    # create top perimeter
    char_row = []
    for i in range(new_width):
        char_row.append('.')
    char_grid.append(char_row)

    for row in raw_schematic:
        char_row = []
        char_row.append('.')
        for character in row:
            char_row.append(character)
        char_row.append('.')
        char_grid.append(char_row)

    # create bottom perimiter
    char_row = []
    for i in range(new_width):
        char_row.append('.')
    char_grid.append(char_row)

    # at this point, each character read is stored at char_grid[row][column]
    # but there exists a buffer of '.' characters as a perimeter

    new_length = len(char_grid)
    mask_grid = []
    for i in range(new_length):
        mask_row = []
        for j in range(new_width):
            mask_row.append('.');
        mask_grid.append(mask_row)

    # we next create a grid around each symbol that looks like
    # MMM
    # M.M  where '.' is where the symbol used to be
    # MMM
    for row in range(new_length):
        for column in range(new_width):
            character = char_grid[row][column]
            if character == '.' or character in digit_characters:
                continue
            else:
                mask_grid[row-1][column-1] = 'M'
                mask_grid[row-1][column] = 'M'
                mask_grid[row-1][column+1] = 'M'
                mask_grid[row][column-1] = 'M'
                mask_grid[row][column] = '.'
                mask_grid[row][column+1] = 'M'
                mask_grid[row+1][column-1] = 'M'
                mask_grid[row+1][column] = 'M'
                mask_grid[row+1][column+1] = 'M'

    # get rid of 'M' where there is no corresponding digit
    for row in range(new_length):
        for column in range(new_width):
            if mask_grid[row][column] == 'M' and char_grid[row][column] not in digit_characters:
                mask_grid[row][column] = '.'

    # discover all digits connected to a mask overlap
    for row in range(new_length):
        for column in range(new_width):
            if char_grid[row][column] in digit_characters:
               if mask_grid[row][column-1] == 'M':
                   mask_grid[row][column] = 'M'
        for column in range(new_width-1, 0, -1):
            if char_grid[row][column] in digit_characters:
               if mask_grid[row][column+1] == 'M':
                   mask_grid[row][column] = 'M'

    for row in range(new_length):
        for column in range(new_width):
            if char_grid[row][column] in digit_characters:
               if mask_grid[row][column-1] == 'M':
                   mask_grid[row][column] = 'M'
        for column in range(new_width-1, 0, -1):
            if char_grid[row][column] in digit_characters:
               if mask_grid[row][column+1] == 'M':
                   mask_grid[row][column] = 'M'


    # replace all remaining 'M' chars with digits
    for row in range(new_length):
        for column in range(new_width):
            if mask_grid[row][column] == 'M':
                mask_grid[row][column] = char_grid[row][column]

    # create the new schematic as a list of strings, with each row becoming a string again

    print("Here are the all of the part numbers:")

    for row in range(1,new_length-1):
        new_line = ""
        for column in range(1, new_width-1):
            new_line = new_line + mask_grid[row][column]
        blanks_and_nums = new_line.split('.')
        blank_count = blanks_and_nums.count('')
        for k in range(blank_count):
            blanks_and_nums.remove('')
        print(blanks_and_nums)

        for k in range(len(blanks_and_nums)):
            game_sum += int(blanks_and_nums[k])


    return game_sum


if __name__ == "__main__":
    print(f"The sum is : {main()}")
