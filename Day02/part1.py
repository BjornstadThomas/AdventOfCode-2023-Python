from Common.utils import read_lines_from_file


def is_game_possible(game_info, red, green, blue):

    max_revealed = {'red': 0, 'green': 0, 'blue': 0}

    reveals = game_info.split('; ')
    for reveal in reveals:
        #Update amount of cubes per color based on the reveal
        for part in reveal.split(', '):
            amount_of_cubes, color = part.split(' ')
            max_revealed[color] = max(max_revealed[color], int(amount_of_cubes)) #Get the max

        print("Reveal:", reveal)
        print("Current max - Red:", max_revealed['red'], "Green:", max_revealed['green'], "Blue:", max_revealed['blue'], "\n")

    #Compare max retrieved for the reveals against the max allowed for the current game
    print("Max Revealed - Red:", max_revealed['red'], "Green:", max_revealed['green'], "Blue:", max_revealed['blue'])

    return max_revealed['red'] <= red and max_revealed['green'] <= green and max_revealed['blue'] <= blue


def sum_possible_game_ids(file_path, red, green, blue):
    total_id_sum = 0
    games_info = read_lines_from_file(file_path)

    for game in games_info:
        game_id, game_info = game.split(': ')
        print("Current game id: ", game_id.split(' ')[1])
        print("Total of summed game ids is: ", total_id_sum)
        print("Current game id added to the total: ", game_id.split(' ')[1], "\n")
        if is_game_possible(game_info, red, green, blue):
            total_id_sum += int(game_id.split(' ')[1])

    return total_id_sum


file_path = 'input.txt'
result = sum_possible_game_ids(file_path, 12, 13, 14)
print("Sum of IDs of possible games:", result)
