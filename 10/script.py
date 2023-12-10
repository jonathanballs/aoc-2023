map_input = """.....
.S-7.
.|.|.
.L-J.
....."""
map_input = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

map_input = open('./input', 'r+').read()

maze = [line.strip() for line in map_input.split('\n')]

# 0, 0 is the top left corner
def find_starting_coords(maze, starting_indicator='S'):
    for y, row in enumerate(maze):
        if starting_indicator in row:
            x = row.index(starting_indicator)
            return [x, y]

def next_direction(maze, coords, direction):
    pipe = maze[coords[1]][coords[0]]

    # Just carry on
    if pipe == '|' or pipe == '-':
        return direction

    if pipe == 'L':
        if direction == [0, 1]:
            return [1, 0]
        else:
            return [0, -1]

    if pipe == '7':
        if direction == [1, 0]:
            return [0, 1]
        else:
            return [-1, 0]

    if pipe == 'J':
        if direction == [0, 1]:
            return [-1, 0]
        else:
            return [0, -1]

    if pipe == 'F':
        if direction == [0, -1]:
            return [1, 0]
        else:
            return [0, 1]

    if pipe == 'S':
        return [0, 0]

    print("failed")

coords = find_starting_coords(maze)
direction = [0, 1]
num_steps = 0

while maze[coords[1]][coords[0]] != 'S' or num_steps == 0:
    coords[0] += direction[0]
    coords[1] += direction[1]
    num_steps += 1

    direction = next_direction(maze, coords, direction)

print("Part 1:", int(num_steps / 2))

expanded_maze_width = len(maze[0]) * 3
expanded_maze_height = len(maze) * 3
expanded_maze = [['.' for x in range(expanded_maze_width)] for y in range(expanded_maze_height)]

def print_maze(expanded_maze):
    for line in expanded_maze:
        for c in line:
            print(c, end="")
        print()

coords = find_starting_coords(maze)
direction = [0, 1]
num_steps = 0

while maze[coords[1]][coords[0]] != 'S' or num_steps == 0:
    expc_x = coords[0] * 3 + 1
    expc_y = coords[1] * 3 + 1
    expanded_maze[expc_y][expc_x] = 'X'
    expanded_maze[expc_y + direction[1]][expc_x + direction[0]] = 'X'
    expanded_maze[expc_y + 2 * direction[1]][expc_x + 2 * direction[0]] = 'X'

    coords[0] += direction[0]
    coords[1] += direction[1]
    num_steps += 1

    direction = next_direction(maze, coords, direction)

search_queue = [(0, 0)]
while len(search_queue) > 0:
    queue_head = search_queue.pop()
    # Check out of bounds
    if queue_head[0] < 0 or queue_head[1] < 0:
        continue

    if queue_head[0] >= len(expanded_maze[0]):
        continue

    if queue_head[1] >= len(expanded_maze):
        continue

    queue_head_value = expanded_maze[queue_head[1]][queue_head[0]]
    if queue_head_value == '.':
        expanded_maze[queue_head[1]][queue_head[0]] = 'O'
        for x in range(-1, 2):
            for y in range(-1, 2):
                search_queue.append((queue_head[0] + x, queue_head[1] + y))


num_inside_blocks = 0
for y, row in enumerate(maze):
    for x, c in enumerate(row):
        if expanded_maze[y*3 + 1][x*3 + 1] == '.':
            expanded_maze[y*3 + 1][x*3 + 1] = 'I'
            num_inside_blocks += 1

# print_maze(expanded_maze)
print("Part 2:", num_inside_blocks)
             
