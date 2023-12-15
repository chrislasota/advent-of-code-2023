# Advent of Code 2023
# Day 15
# Part 1

def compute_hash(input_str):
    current = 0
    for ch in input_str:
        current = ((current + ord(ch)) * 17) % 256
    return current


def main() -> int:
    hash_sum = 0
    with open("input_day_15.txt") as input_file:
        for line in input_file:
           line = line.rstrip()   # remove newline
           step_str = line.split(',')
           for step in step_str:
               hash_sum += compute_hash(step)
    return hash_sum


if __name__ == "__main__":
    print(f"The sum of the hash results is : {main()}")
