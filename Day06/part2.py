from part1 import read_input, count_ways_to_win

file_path = 'input.txt'
times, distances = read_input(file_path)
single_race_time = int("".join(map(str, times)))
single_race_distance = int("".join(map(str, distances)))

print("Single race time:", single_race_time)
print("Single race distance:", single_race_distance)

ways_to_win = count_ways_to_win(single_race_time, single_race_distance)


print("Part 2:", ways_to_win)
