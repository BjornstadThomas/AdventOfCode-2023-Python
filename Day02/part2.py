from Common.utils import read_lines_from_file


def get_summed_minimum_cubes(game_info):

    max_revealed = {'red': 0, 'green': 0, 'blue': 0}

    reveals = game_info.split('; ')
    for reveal in reveals:
        #Update amount of cubes per color based on the reveal
        for part in reveal.split(', '):
            amount_of_cubes, color = part.split(' ')
            max_revealed[color] = max(max_revealed[color], int(amount_of_cubes)) #Get the max

        print("Reveal:", reveal)
        print("Current max - Red:", max_revealed['red'], "Green:", max_revealed['green'], "Blue:", max_revealed['blue'])

    #Print the max different cubes for the current game
    print("Max Revealed - Red:", max_revealed['red'], "Green:", max_revealed['green'], "Blue:", max_revealed['blue'])

    return (max_revealed['red'] * max_revealed['green'] * max_revealed['blue'])


def sum_of_power_of_games(file_path):
    total_sum_of_games = 0
    games_info = read_lines_from_file(file_path)

    for game in games_info:
        game_id, game_info = game.split(': ')
        print("\nCurrent game id: ", game_id.split(' ')[1])
        sum_of_current_game = get_summed_minimum_cubes(game_info)
        print("\nSum of current game: ", sum_of_current_game)
        total_sum_of_games += sum_of_current_game
        print("Total sum so far: ", total_sum_of_games)

    return total_sum_of_games


file_path = 'input.txt'
result = sum_of_power_of_games(file_path)
print("\nSum of IDs of possible games:", result)
