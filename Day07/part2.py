from collections import Counter
from functools import cmp_to_key, partial
from Common.utils import read_lines_from_file


def rank_hand(hand):
    card_count = Counter(hand)
    count_of_counts = Counter(card_count.values())
    highest_count = max(count_of_counts)

    print(f"Ranking hand: {hand}, Card count: {card_count}, Count of counts: {count_of_counts}, Highest count: {highest_count}")

    if highest_count >= 4:
        return highest_count + 2
    elif highest_count == 3:
        return 4 + (2 in count_of_counts)
    elif highest_count == 2:
        return 2 + (count_of_counts[2] == 2)
    else:
        return 1


def replace_joker(hand):
    if 'J' not in hand:
        return hand
    if hand == 'JJJJJ':
        return 'AAAAA'

    non_joker_counts = Counter(hand.replace('J', ''))
    replacement_candidates = [(c, tie_rank_order.index(c), non_joker_counts[c]) for c in hand if c != 'J']

    def compare_candidates(candidate1, candidate2):
        return (candidate1[2] - candidate2[2]) or (candidate2[1] - candidate1[1])

    sorted_candidates = sorted(replacement_candidates, key=cmp_to_key(compare_candidates))

    print(f"Replacing joker in hand: {hand}, Replacement candidate: {sorted_candidates[-1][0]}")

    return hand.replace('J', sorted_candidates[-1][0])


def compare_hands_with_joker(hand1_data, hand2_data, consider_jokers=False):
    hand1, hand2 = hand1_data[0], hand2_data[0]

    print(f"\nComparing hands: {hand1} vs {hand2}, Considering jokers: {consider_jokers}")

    hand1_rank = rank_hand(replace_joker(hand1) if consider_jokers else hand1)
    hand2_rank = rank_hand(replace_joker(hand2) if consider_jokers else hand2)

    if hand1_rank == hand2_rank:
        for card1, card2 in zip(hand1, hand2):
            if card1 != card2:
                return tie_rank_order.index(card2) - tie_rank_order.index(card1)
        raise ValueError('No two hands should be the same for this problem.')
    else:
        return hand1_rank - hand2_rank

tie_rank_order = 'AKQT98765432J'

# Read and sort hands
hands = read_lines_from_file('input.txt', delimiter=' ')
hands.sort(key=cmp_to_key(partial(compare_hands_with_joker, consider_jokers=True)))

# Calculate total winnings with debugging
total_winnings_with_joker = 0
for rank, (hand, bid) in enumerate(hands, 1):
    hand_winnings = rank * int(bid)
    total_winnings_with_joker += hand_winnings
    print(f"Hand: {hand}, Rank: {rank}, Bid: {bid}, Hand Winnings: {hand_winnings}")

print("Total winnings with joker:", total_winnings_with_joker)
