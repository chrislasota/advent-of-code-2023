# Advent of Code 2023
# Day 4
# Parts 1 and 2

def main():
    # We look over the cards, and count how many matches each card has, storing
    # it as an array of integers.  Then we process those numbers to calculate
    # the answers to Part 1 and Part 2 of the problem.

    match_list = []
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

            # identify how many matches
            match_count = 0
            for num in winning_list:
                if num in played_list:
                    match_count += 1
            match_list.append(match_count)

    # Done reading input file

    # Create the answer for Part 1 using match data
    total_points = 0
    for i in range(len(match_list)):
        if match_list[i] > 0:
            total_points = total_points + 2**(match_list[i] - 1)
    print(f"Part 1 : Total points = {total_points}")


    # Create the answer for Part 2
    # Introduce an auxiliary accumulator list ( card_counts[] )
    # If we pre-load this accumulator list with "1"s, the algorithm is short and sweet
    card_counts = []
    for i in range(len(match_list)):
        card_counts.append(1)
    for i in range(len(match_list)):
        for k in range(match_list[i]):
            card_counts[i+k+1] += card_counts[i]

    total_cards = 0
    for cards in card_counts:
        total_cards += cards

    print(f"Part 2 : Total scratchcards = {total_cards}")

    return


if __name__ == "__main__":
    main()
