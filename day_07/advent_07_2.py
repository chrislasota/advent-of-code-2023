# Advent of Code 2023
# Day 7
# Part 2

import re

def get_strongest_wildcard_hand(hand_str, wildcard) -> str:
    # Takes in a 5-char string and a single wild card character and returns
    # the strongest of all possible 5-card hands that can be made.  The
    # strongest possible hands result when all instances of the wild card
    # occurring in the input string are set to the same character and that
    # character is in the hand.

    face_chars = "23456789TJQKA"
    if wildcard not in hand_str:
        return hand_str
    # find and remove wild card character from face_chars string
    wild_index = face_chars.find(wildcard)
    face_chars = face_chars[:wild_index] + face_chars[(wild_index + 1):]
    # find best TYPE of hand using wild card
    best_hand_score = 0
    for char in face_chars:
        temp_hand_str = hand_str.replace(wildcard, char)
        score = hand_type_score(temp_hand_str)
        if score >= best_hand_score:
            best_hand = temp_hand_str
            best_hand_score = score
    return best_hand


def hand_type_score(hand_str) -> int:
    # This method returns a score for any of the allowed TYPES of hands
    # that can be formed from the characters in the 5-character input
    # string. The scores which will assigned to hand TYPES are as follows:
    #
    #  5 of a kind : 6000000
    #  4 of a kind : 5000000
    #  Full house  : 4000000
    #  3 of a kind : 3000000
    #  2 pair      : 2000000
    #  1 pair      : 1000000
    #  Nothing     : 0
    #
    # This method does NOT assign different scores based on what cards form
    # a given type.  It only assigns a score for the type.  This means that
    # hands 'A484A' and 'KK233' will get the same score of 2000000
    #
    # The values are very large for a reason.  We may want to add an additional
    # amount elsewhere that WILL uniquely identify a hand by the card order.
    #
    # Every 'legal' hand is a 5-character string from the set {23456789TJKQA}
    # Associated to each of these characters is a integer value from 2 to 14.
    #
    # A 15-element list will act as a histogram to count how many of each
    # face card exists in a hand.  The integer values associated to each of
    # the characters will be used as indicies for this histogram.  This is
    # why we use a 15 element histogram instead of 13.
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
    # Yes, there's always a zero at list locations [0] and [1].  Convenience.
    #
    # Once the histogram is made, we can determine the "type" of hand our
    # string represents, and assign it a score.
    #
    # Our example above would get a score of 1000000, because it's 1 pair.

    face_value_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8':  8,
                 '7':  7, '6':  6, '5':  5, '4':  4, '3':  3, '2': 2}

    histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index in range(5):
        face_value = face_value_dict[hand_str[index]]
        histogram[face_value] += 1

    sorted_histogram = sorted(histogram, reverse=True)  # NOTE the reverse!!!
    biggest = sorted_histogram[0]
    big     = sorted_histogram[1]

    # This ugly "if waterfall" is used for speed purposes
    if biggest == 1:              # nothing
        return 0
    if biggest == 2 and big == 1: # one pair
        return 1000000
    if biggest == 2 and big == 2: # two pair
        return 2000000
    if biggest == 3 and big == 1: # 3 of a kind
        return 3000000
    if biggest == 3 and big == 2: # full house
        return 4000000
    if biggest == 4:              # 4 of a kind
        return 5000000
    if biggest == 5:              # 5 of a kind
        return 6000000
# end of method


def ordered_cards_score(hand_str, face_value_dict) -> int:
    # Example:
    #     face_value_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8':  8,
    #                        '7':  7, '6':  6, '5':  5, '4':  4, '3':  3, '2': 2}
    #     hand_str = "7A39K"
    #
    #     score = 7*50625 + 14*3375 + 3*225 + 9*15+13 = 402448
    powers_of_fifteen = [50625, 3375, 225, 15, 1]
    score = 0
    for index in range(5):
        face_value = face_value_dict[hand_str[index]]
        score += face_value * powers_of_fifteen[index]
    return score


def main() -> int:
    face_value_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8':  8,
                 '7':  7, '6':  6, '5':  5, '4':  4, '3':  3, '2': 2}
    wildcard = 'J'
    face_value_dict[wildcard] = 1
    total_winnings = 0
    score_list = []
    bid_list = []
    with open("input_day_07.txt", 'r') as input_file:
        data_filter = re.compile('[A,K,Q,J,T,0-9]+')
        for line in input_file:
            hand = data_filter.findall(line)
            hand[1] = int(hand[1])
            hand_bid = hand[1]
            hand_str = hand[0]
            ordered_score = ordered_cards_score(hand_str, face_value_dict)
            best_hand_str = get_strongest_wildcard_hand(hand_str, wildcard)
            best_type_score = hand_type_score(best_hand_str)
            total_score = best_type_score + ordered_score
            score_list.append(total_score)
            bid_list.append(hand_bid)

    # use zip() to make things easier
    zipped = list(zip(score_list, bid_list))
    zipped.sort()
    for rank in range(len(zipped)):
        total_winnings += (rank + 1) * zipped[rank][1]
    return total_winnings


if __name__ == "__main__":
    print(f"The total_winnings are : {main()}")
