# Advent of Code 2023
# Day 1 (Dec 1st)
# Problem 1

import string

def main():
    sum = 0
    input_file = open("input_day_01.txt", 'r')
    lines = input_file.readlines()
    for line in lines:
        digit_string = []
        for character in line:
            if character in string.digits :
                digit_string.append(character)
        result = int(digit_string[0])*10 + int(digit_string[-1])
        sum = sum + result

    return sum


if __name__ == "__main__":
    print(f"The sum is : {main()}")
