from collections import deque
from Common.utils import read_lines_from_file

# Define pipe types and directions
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


def create_pipe_grid(lines):
    return [[c for c in line] for line in lines]


def find_start_position(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return i, j
    return None


def find_loop(grid, start):
    encountered_places = {}
    search_queue = deque([(start, 0)])

    while search_queue:
        current, distance = search_queue.popleft()

        if current in encountered_places:
            continue
        encountered_places[current] = distance

        # print(f"Visited {current}, Distance: {distance}")

        i, j = current
        for direction in pipe_types[grid[i][j]]:
            di, dj, opposite = directions[direction]
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[new_i]):
                target = grid[new_i][new_j]
                if target in pipe_types and opposite in pipe_types[target]:
                    search_queue.append(((new_i, new_j), distance + 1))

    return encountered_places


def fill_loop_interior(grid, encountered_places):
    for i, row in enumerate(grid):
        norths = 0
        for j, cell in enumerate(row):
            if (i, j) in encountered_places:
                if "n" in pipe_types[cell]:
                    norths += 1
            else:
                grid[i][j] = "I" if norths % 2 != 0 else "O"


def visualize_grid(grid):
    for row in grid:
        print(''.join(row))
    print()


lines = read_lines_from_file("input.txt")
pipe_grid = create_pipe_grid(lines)
start_position = find_start_position(pipe_grid)
encountered_places = find_loop(pipe_grid, start_position)
fill_loop_interior(pipe_grid, encountered_places)

inside_count = sum(row.count("I") for row in pipe_grid)
print("\nNumber of tiles inside the loop:", inside_count, "\n")

# Visualize the final grid
visualize_grid(pipe_grid)
