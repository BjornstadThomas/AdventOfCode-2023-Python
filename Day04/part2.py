from Common.utils import read_lines_from_file


def count_matches(winning_numbers, scratchcard_numbers):
    """Count the number of matches between winning and player numbers."""
    return sum(num in winning_numbers for num in scratchcard_numbers)


def process_scratchcards(cards):
    """Process all scratchcards and return the total count including won cards."""

    total_cards = len(cards)  #Start with the original number of cards
    won_cards = [0] * len(cards)  #Initialize a list to track won cards

    for i in range(len(cards)):
        winning_numbers, scratchcard_numbers = cards[i]
        matches = count_matches(winning_numbers, scratchcard_numbers)

        #Distribute won cards
        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            won_cards[j] += 1

        print(f"Card {i + 1}: Matches = {matches}, Distributing {matches} won cards")

    #Process won cards
    for i in range(len(won_cards)):
        while won_cards[i] > 0:
            winning_numbers, scratchcard_numbers = cards[i]
            matches = count_matches(winning_numbers, scratchcard_numbers)
            won_cards[i] -= 1
            total_cards += 1
            for j in range(i + 1, min(i + 1 + matches, len(cards))):
                won_cards[j] += 1

            print(f"Processing won card from Card {i + 1}: Matches = {matches}, Total Cards = {total_cards}")

    return total_cards


def total_scratchcards(file_path):
    """Calculate the total number of scratchcards including won cards."""

    lines = read_lines_from_file(file_path, delimiter='|')
    cards = []

    for parts in lines:
        #Remove text "Card X:" and process the numbers given
        winning_numbers = set(map(int, parts[0].split(':')[1].split()))
        scratchcard_numbers = list(map(int, parts[1].split()))
        cards.append((winning_numbers, scratchcard_numbers))

    return process_scratchcards(cards)


file_path = 'input.txt'
result = total_scratchcards(file_path)
print("Total scratchcards including won cards:", result)
