# Advent of Code 2023
# Day 6
# Part 2

import re

def main() -> int:
    ways_product = 1
    with open("input_day_06.txt", 'r') as input_file:
        # read in race times and record distances as arrays of stringified numbers
        data_filter = re.compile('\d+')
        race_times = data_filter.findall(input_file.readline())
        record_distances = data_filter.findall(input_file.readline())
        big_time = ''
        big_record = ''
        big_time = int(big_time.join(race_times))
        big_record = int(big_record.join(record_distances))

        ways_to_win = 0
        for t in range(big_time + 1):
            distance = t*(big_time - t)
            if distance > big_record:
                ways_to_win += 1
        ways_product *= ways_to_win

    return ways_product


if __name__ == "__main__":
    print(f"The number of ways to beat the record is : {main()}")
