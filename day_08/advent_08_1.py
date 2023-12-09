# Advent of Code 2023
# Day 8
# Part 1

import re

def main() -> int:
    # This code emulates a finite state automata to recognize whether or not the string
    # of 'L' and 'R' characters at the top of the input file is in a particular grammar
    number_of_steps = 0
    transition_function = {}
    with open("input_day_08.txt", 'r') as input_file:
        instructions = input_file.readline().rstrip()
        input_file.readline()  # skip the blank line
        state_filter = re.compile('[A-Z]+')
        for line in input_file:
            states = state_filter.findall(line)
            transition_function[states[0]] = [states[1], states[2]]
        current_state = "AAA"
        halting_flag = False
        while not halting_flag:
            for instruction in instructions:
                if instruction == 'L':
                    current_state = transition_function[current_state][0]
                else:
                    current_state = transition_function[current_state][1]
                number_of_steps += 1
                if current_state == "ZZZ":
                    halting_flag = True
                    break
    return number_of_steps


if __name__ == "__main__":
    print(f"The number of steps required to reach 'ZZZ' is : {main()}")
