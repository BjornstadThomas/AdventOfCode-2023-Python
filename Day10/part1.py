from collections import deque
from Common.utils import read_lines_from_file


def visualize_grid(grid, encountered_places):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) in encountered_places:
                print(f"{encountered_places[(i, j)]:>2}", end=" ")
            else:
                print(" . ", end=" ")
        print()


pipe_types = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    'S': ["n", "s", "w", "e"],
}

directions = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w"),
}

lines = read_lines_from_file("input.txt")
pipe_grid = [[c for c in line] for line in lines]

# Locate the start (S)
start = None
for i, row in enumerate(pipe_grid):
    for j, place in enumerate(row):
        if place == 'S':
            start = (i, j)
            break
    if start:
        break

encountered_places = {}
traversal_queue = deque([(start, 0)])
debug = False

while traversal_queue:
    current, distance = traversal_queue.popleft()

    if current in encountered_places:
        continue
    encountered_places[current] = distance

    if debug:
        print(f"Current position: {current}, Distance: {distance}")

    i, j = current
    available_directions = pipe_types[pipe_grid[i][j]]

    for direction in available_directions:
        di, dj, opposite = directions[direction]
        new_i, new_j = i + di, j + dj
        if not (0 <= new_i < len(pipe_grid) and 0 <= new_j < len(pipe_grid[new_i])):
            continue
        target = pipe_grid[new_i][new_j]
        if target not in pipe_types or opposite not in pipe_types[target]:
            continue
        traversal_queue.append(((new_i, new_j), distance + 1))
        if debug:
            print(f"  Moving {direction}, New position: ({new_i}, {new_j})")


max_distance = max(encountered_places.values())
print("Max Distance:", max_distance)
print("\nGrid Visualization with Distances:")
visualize_grid(pipe_grid, encountered_places)
