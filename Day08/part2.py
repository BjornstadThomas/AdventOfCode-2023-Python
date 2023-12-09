import math
from Common.utils import read_lines_from_file
from part1 import parse_network_data


def navigate_from_node(instructions, connections, start_node):
    current_node = start_node
    step_count = 0
    print(f"Starting navigation from '{start_node}'.")
    while not current_node.endswith('Z'):
        direction = instructions[step_count % len(instructions)]
        next_node = connections[current_node][0 if direction == 'L' else 1]
        # print(f"Step {step_count + 1}: Current node: {current_node}, Direction: {direction}, Next node: {next_node}")
        current_node = next_node
        step_count += 1
    return step_count


lines = read_lines_from_file("input.txt")
instructions, connections = parse_network_data(lines)

total_steps = 1

for node in connections:
    if node.endswith('A'):
        print(f"\nNavigating from starting node: {node}")
        steps = navigate_from_node(instructions, connections, node)
        print(f"Steps to reach a node ending with 'Z' from {node}: {steps}")
        total_steps = math.lcm(total_steps, steps)

print("\nPart 2: Total steps for simultaneous navigation:", total_steps)
