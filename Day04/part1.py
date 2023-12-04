from Common.utils import read_lines_from_file


def calculate_card_points(winning_numbers, scratchcard_numbers):
    """Calculate the points for a single card."""
    matches = [num for num in scratchcard_numbers if num in winning_numbers]
    if not matches:
        return 0
    return 2 ** (len(matches) - 1)  #Set amount of points (2^(n - 1)) where n is amount of matches


def total_scratchcard_points(file_path):
    """Calculate the total points from all scratchcards."""
    total_points = 0
    lines = read_lines_from_file(file_path, delimiter='|')

    for card_index, parts in enumerate(lines, start=1):
        #Remove text "Card X:" and process the numbers given
        winning_numbers = set(map(int, parts[0].split(':')[1].split()))
        scratchcard_numbers = list(map(int, parts[1].split()))
        points = calculate_card_points(winning_numbers, scratchcard_numbers)
        total_points += points

        print(f"Card {card_index}:\nWinning Numbers {winning_numbers}\nScratchcard Numbers {scratchcard_numbers}"
              f"\nPoints on this card: {points}\nPoints accrued so far: {total_points}\n")

    return total_points


file_path = 'input.txt'
result = total_scratchcard_points(file_path)
print("Total points from scratchcards:", result)
