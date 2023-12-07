# Advent of Code 2023
# Day 6
# Part 1

import re

def main() -> int:
    ways_product = 1
    with open("input_day_06.txt", 'r') as input_file:
        # read in race times and record distances as arrays of stringified numbers
        data_filter = re.compile('\d+')
        race_times = data_filter.findall(input_file.readline())
        record_distances = data_filter.findall(input_file.readline())

    for race in range(len(race_times)):
        max_time = int(race_times[race])
        ways_to_win = 0
        for t in range(max_time + 1):
            distance = t*(max_time - t)
            if distance > int(record_distances[race]):
                ways_to_win += 1
        ways_product *= ways_to_win

    return ways_product


if __name__ == "__main__":
    print(f"The product of the number of ways to beat each record is : {main()}")
