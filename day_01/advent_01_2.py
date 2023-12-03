# Advent of Code 2023
# Day 1 (Dec 1st)
# Problem 2

import string

def main():
    sum = 0

    # NOTE: the input file might have cases such as "oneight", "sevenine", "eightwo", etc,
    # and each of these cases requires converting the text into TWO digits.  Therefore we
    # have to 'be clever' when we replace text with digits.  We do this with a dictionary.

    digit_dict = {"one": 'o1e', "two": 't2o', "three": 't3e', "four": '4',
                  "five": '5e', "six": '6', "seven": '7n', "eight": 'e8t', "nine": 'n9e'}

    input_file = open("input_day_01.txt", 'r')
    lines = input_file.readlines()
    for line in lines:
        # convert all spelled digits to actual digit characters
        for digit_name in digit_dict.keys():
            if digit_name in line:
                line = line.replace(digit_name, digit_dict[digit_name])

        # get rid of all non-digits and create a 2-digit integer from the result
        digit_string = []
        for character in line:
            if character in string.digits :
                digit_string.append(character)
        result = int(digit_string[0])*10 + int(digit_string[-1])
        sum = sum + result

    input_file.close()
    return sum


if __name__ == "__main__":
    print(f"The sum is : {main()}")
