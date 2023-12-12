image_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split('\n')
image_input = open('./input', 'r+').read().strip().split('\n')

empty_rows = []
empty_cols = []

for i, row in enumerate(image_input):
    if '#' not in row:
        empty_rows.append(i)

for i in range(len(image_input)):
    col = [row[i] for row in image_input]
    if '#' not in col:
        empty_cols.append(i)

galaxies = []

for y, row in enumerate(image_input):
    for x, c in enumerate(row):
        if c != '#':
            continue

        galaxy_x = x + len([i for i in empty_cols if i < x])
        galaxy_y = y + len([i for i in empty_rows if i < y])

        galaxies.append((galaxy_x, galaxy_y))

def calculate_sum_distance(galaxies):
    sum_distance = 0
    for i, galaxy_a in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            galaxy_b = galaxies[j]

            distance = abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])
            sum_distance += distance
    return sum_distance

print("Part 1:", calculate_sum_distance(galaxies))

galaxies = []
for y, row in enumerate(image_input):
    for x, c in enumerate(row):
        if c != '#':
            continue

        galaxy_x = x + 999999*len([i for i in empty_cols if i < x])
        galaxy_y = y + 999999*len([i for i in empty_rows if i < y])

        galaxies.append((galaxy_x, galaxy_y))

print("Part 2:", calculate_sum_distance(galaxies))

