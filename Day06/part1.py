def read_input(file_path):
    """Read input from a file and return the race details."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    times = [int(value) for value in lines[0].split() if value.isdigit()]
    distances = [int(value) for value in lines[1].split() if value.isdigit()]

    print("Read times:", times)
    print("Read distances:", distances)

    return times, distances


def count_ways_to_win(total_time, record_distance):
    """Calculate the number of ways to win a single race."""
    ways_to_win = 0

    # Debug: Initial values of total_time and record_distance
    print(f"Starting calculation with total_time={total_time}, record_distance={record_distance}")

    for time_held in range(total_time + 1):
        speed = time_held
        remaining_time = total_time - time_held
        distance = speed * remaining_time

        #print(f"time_held={time_held}, speed={speed}, remaining_time={remaining_time}, distance={distance}")

        if distance > record_distance:
            ways_to_win += 1
            #print(f"New way to win found, updated ways_to_win={ways_to_win}")

    print(f"Total ways to win={ways_to_win}")
    return ways_to_win


file_path = 'input.txt'
times, distances = read_input(file_path)
ways_to_win_per_race = [count_ways_to_win(time, distance) for time, distance in zip(times, distances)]
print("Amount of ways to win:", ways_to_win_per_race)

product_of_wins = 1

for ways in ways_to_win_per_race:
    product_of_wins *= ways

print("Part 1:", product_of_wins, "\n")
