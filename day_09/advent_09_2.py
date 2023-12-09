# Advent of Code 2023
# Day 9
# Part 2

import re

def main() -> int:
    total_sum = 0
    data_set = []
    with open("input_day_09.txt", 'r') as input_file:
        data_filter = re.compile('-{0,1}\d+')
        for line in input_file:
            sensor_values = data_filter.findall(line)
            data_history = []
            for value in sensor_values:
                data_history.append(int(value))
            data_set.append(data_history)
    # Done reading input file

    for sequence in data_set:
        first_values = []
        first_values.append(sequence[0])
        temp_sequence = sequence
        new_sequence = []
        all_zeros = False
        while not all_zeros:
            for index in range(1,len(temp_sequence)):
                new_sequence.append(temp_sequence[index] - temp_sequence[index-1])
            first_values.append(new_sequence[0])
            nonzero = False
            for value in new_sequence:
                if value != 0:
                    nonzero = True
                    break
            if nonzero == True:
                temp_sequence = new_sequence
                new_sequence = []
            else:
                all_zeros = True

        new_value = 0
        for x in first_values[-1::-1]:
            new_value = x - new_value
        total_sum += new_value

    return total_sum


if __name__ == "__main__":
    print(f"The total sum of predicted values is : {main()}")
