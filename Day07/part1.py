from collections import Counter
from functools import cmp_to_key
from Common.utils import read_lines_from_file


def rank_hand(hand):
    """
    Ranks a hand based on the game rules.

    Args:
    hand (str): A string representing a hand.

    Returns:
    int: The rank of the hand.
    """
    card_counts = Counter(hand)
    unique_counts = Counter(card_counts.values())
    most_common_count = max(unique_counts)

    if most_common_count >= 4:
        return most_common_count + 2
    elif most_common_count == 3:
        return 4 + int(2 in unique_counts)
    elif most_common_count == 2:
        return 2 + int(unique_counts[2] == 2)
    else:
        return 1


def compare_hands(hand1, hand2):
    """
    Compares two hands based on their ranks and individual card strengths.

    Args:
    hand1 (tuple): A tuple containing the hand and its bid.
    hand2 (tuple): A tuple containing the hand and its bid.

    Returns:
    int: Negative if hand1 < hand2, zero if hand1 == hand2, positive if hand1 > hand2.
    """
    rank1 = rank_hand(hand1[0])
    rank2 = rank_hand(hand2[0])

    if rank1 == rank2:
        tie_rank_order = 'AKQJT98765432'
        for card1, card2 in zip(hand1[0], hand2[0]):
            tie_rank1 = tie_rank_order.index(card1)
            tie_rank2 = tie_rank_order.index(card2)
            if tie_rank1 != tie_rank2:
                return tie_rank2 - tie_rank1

    else:
        return rank1 - rank2


# Reading hands from file
hands = read_lines_from_file('input.txt', delimiter=' ')
print("Read hands:", hands)

# Sorting hands based on their ranks
hands.sort(key=cmp_to_key(compare_hands))
print("Sorted hands:", hands)

# Calculating total winnings
total_winnings = 0
for rank, (hand, bid) in enumerate(hands, 1):
    hand_winnings = rank * int(bid)
    total_winnings += hand_winnings
    print(f"Hand: {hand}, Rank: {rank}, Bid: {bid}, Hand Winnings: {hand_winnings}")

print("Total winnings:", total_winnings)