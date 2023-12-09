from Common.utils import read_lines_from_file


def parse_network_data(lines):
    instructions = list(lines[0])
    connections = {}

    for line in lines[1:]:
        node, linked_nodes = line.split(" = ")
        left_node, right_node = linked_nodes.strip("()").split(", ")
        connections[node.strip()] = (left_node.strip(), right_node.strip())
    return instructions, connections


def navigate_network(instructions, connections):
    current_node = 'AAA'
    step_count = 0
    print("Starting navigation from 'AAA'.")

    while current_node != 'ZZZ':
        direction = instructions[step_count % len(instructions)]
        next_node = connections[current_node][0 if direction == 'L' else 1]
        print(f"Step {step_count + 1}: Current node: {current_node}, Direction: {direction}, Next node: {next_node}")
        current_node = next_node
        step_count += 1
    return step_count


lines = read_lines_from_file("input.txt")
instructions, connections = parse_network_data(lines)
steps_to_destination = navigate_network(instructions, connections)
print("\nPart 1: Steps to reach 'ZZZ':", steps_to_destination)
