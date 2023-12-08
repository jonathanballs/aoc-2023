import math
# direction_input = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

direction_input = open('./input', 'r+').read()

directions = direction_input.split('\n')[0].strip()

node_lines = direction_input.split('\n\n')[1].strip().split('\n')

nodes = {}
for line in node_lines:
    node = line.split(' = ')[0]
    left = line.split(' = ')[1][1:4]
    right = line.split(', ')[1][:3]

    nodes[node] = [left, right]


def part1():
    current_node = 'AAA'
    step_number = 0
    while True:
        if current_node == 'ZZZ':
            break

        next_step = directions[step_number % len(directions)]
        node = nodes[current_node]
        if next_step == 'L':
            current_node = node[0]
        elif next_step == 'R':
            current_node = node[1]
        else:
            print("Impossible step:", next_step)
            break

        step_number += 1

    print("Part 1:", step_number)

part1()

def part2():
    starting_nodes = [n for n in nodes.keys() if n.endswith('A')]
    current_nodes = starting_nodes

    end_multiples = [0] * len(starting_nodes)

    step_number = 0
    while True:

        if step_number % len(directions) == 0:
            for node_num, node in enumerate(current_nodes):
                if node.endswith('Z') and end_multiples[node_num] == 0:
                    end_multiples[node_num] = step_number

            if 0 not in end_multiples:
                break

        next_step = directions[step_number % len(directions)]

        next_nodes = []

        for current_node in current_nodes:
            node = nodes[current_node]
            if next_step == 'L':
                next_nodes.append(node[0])
            elif next_step == 'R':
                next_nodes.append(node[1])
            else:
                print("Impossible step:", next_step)
                break

        current_nodes = next_nodes
        step_number += 1

    lcm = math.lcm(*end_multiples)
    print("Part 2:", lcm)


part2()
