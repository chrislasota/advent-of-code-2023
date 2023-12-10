# Advent of Code 2023
# Day 7
# Part 1

import re

def determine_hand_type_score(hand_str) -> int:
    # This method returns a UNIQUE score for any legal hand, based on which
    # "type" of hand it is, classified the same way ordinary poker hands are
    # classified: 5 of a kind, 4 of a kind, full house, 3 of a kind, 2 pair,
    # 1 pair, and "nothing".  The INITIAL scores are assigned as follows:
    #
    #  5 of a kind : 6000000
    #  4 of a kind : 5000000
    #  Full house  : 4000000
    #  3 of a kind : 3000000
    #  2 pair      : 2000000
    #  1 pair      : 1000000
    #  Nothing     : 0
    #
    # The INITIAL score is modified by adding a unique integer created by treating
    # each character in hand_str as if it were a base-15 representation.
    #
    # Every 'legal' hand is a 5-character string from the set {23456789TJKQA}
    # Associated to each of these characters is a integer value from 2 to 14.
    # This integer value will be used as the index in a histogram list
    # which tallies how many of each kind of card exists in the hand.
    #
    # A 15-element list will act as a histogram to count how many of each
    # face card exists in a hand.  We use 15 elements instead of 13 as a
    # mental convenience -- nothing more.
    #
    # EXAMPLE:  Suppose we are given a string '4QT3T'.  The histogram list
    #           Will have the following form:
    #           [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0]
    #           We can see that list locations [3] and [4] each have a value
    #           of 1, which tells us there is a single '3' and '4' in the hand.
    #           List location [10] has a 2, telling us the hand contains 2 'T'
    #           characters.  Finally list location [12] contains a 1, so the
    #           hand has a single 'Q' character.  All locations containing
    #           a 0 tell us there are no characters of that kind in the hand.
    #
    # Note that there's always a zero at list locations [0] and [1].  Again
    # this is just done for the mental convenience of assigined the usual
    # numeric face values for cards to their respective histogram indices.
    #
    # Once the histogram is made, we can determine the "type" of hand our
    # string represents, and assign it the score described above.
    #
    # Our example above would get an INITIAL score of 1000000, because it is
    # 1 pair.  Then we would add 245305 which is the integer value of the hand
    # interpreted as a base-15 number (4*50625 + 12*3375 + 10*225 + 3*15 + 10)
    # This method would susequently return a value of 1245305 for hand '4QT3T'

    face_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8':  8,
                 '7':  7, '6':  6, '5':  5, '4':  4, '3':  3, '2': 2}

    histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    powers_of_fifteen = [1, 15, 225, 3375, 50625]
    high_card_value = 0
    for index in range(5):
        face_value = face_dict[hand_str[index]]
        histogram[face_value] += 1
        high_card_value += face_value * powers_of_fifteen[4 - index]

    sorted_histogram = sorted(histogram, reverse=True)  # NOTE the reverse!!!
    biggest = sorted_histogram[0]
    big     = sorted_histogram[1]

    # This ugly "if cascade" is used for speed purposes
    if biggest == 1:              # nothing
        return high_card_value
    if biggest == 2 and big == 1: # one pair
        return 1000000 + high_card_value
    if biggest == 2 and big == 2: # two pair
        return 2000000 + high_card_value
    if biggest == 3 and big == 1: # 3 of a kind
        return 3000000 + high_card_value
    if biggest == 3 and big == 2: # full house
        return 4000000 + high_card_value
    if biggest == 4:              # 4 of a kind
        return 5000000 + high_card_value
    if biggest == 5:              # 5 of a kind
        return 6000000 + high_card_value
# end of method


def main() -> int:
    total_winnings = 0
    score_list = []
    bid_list = []
    with open("input_day_07.txt", 'r') as input_file:
        data_filter = re.compile('[A,K,Q,J,T,0-9]+')
        for line in input_file:
            hand = data_filter.findall(line)
            hand[1] = int(hand[1])
            score_list.append(determine_hand_type_score(hand[0]))
            bid_list.append(hand[1])
    # done reading input

    # use zip() to make things easier
    zipped = list(zip(score_list, bid_list))
    zipped.sort()
    for rank in range(len(zipped)):
        total_winnings += (rank + 1) * zipped[rank][1]
    return total_winnings


if __name__ == "__main__":
    print(f"The total_winnings are : {main()}")
