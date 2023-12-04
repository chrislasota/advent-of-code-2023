# Advent of Code 2023
# Day 4
# Problem 1

def main():
    total_points = 0
    with open("input_day_04.txt", 'r') as input_file:
        for line in input_file:
            line_parts = line.split(":")
            numbers = line_parts[1].split('|')

            # create the list[] of winning numbers
            winning_number_string = numbers[0].lstrip()
            winning_number_string = winning_number_string.rstrip()
            winning_numbers = winning_number_string.split(' ')
            winning_list = []
            for item in winning_numbers:
                if item != '':
                    winning_list.append(int(item))

            # create the list[] of played numbers
            played_number_string = numbers[1].lstrip()
            played_number_string = played_number_string.rstrip()
            played_numbers = played_number_string.split(' ')
            played_list = []
            for item in played_numbers:
                if item != '':
                    played_list.append(int(item))

            # create card point scores based on number of matches
            card_points = 0
            exponent = 0
            for num in winning_list:
                if num in played_list:
                    exponent += 1
            if exponent > 0:
                card_points = 2**(exponent-1)
            total_points += card_points

    return total_points


if __name__ == "__main__":
    print(f"Total points : {main()}")
