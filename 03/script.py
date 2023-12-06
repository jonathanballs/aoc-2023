import re

schema = [line.strip() for line in open('input', 'r+')]
# schema = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".split('\n')

def is_symbol(c):
    return c not in '.0123456789'

# (0, 0) is top left
def safe_is_symbol_at_coords(x, y):
    if x < 0 or x >= len(schema[0]):
        return False
    if y < 0 or y >= len(schema):
        return False
    return is_symbol(schema[y][x])

def safe_is_symbol_in_rect(x, y, width, height):
    for i in range(x, x + width):
        for j in range(y, y+height):
            if safe_is_symbol_at_coords(i, j):
                return True
    return False

part_numbers_sum = 0
for i, line in enumerate(schema):
    for match in re.finditer(r'\d+', line):
        number = int(line[match.start(): match.end()])
        number_length = match.end() - match.start()

        is_part_number = safe_is_symbol_in_rect(match.start()-1, i-1, number_length + 2, 3)
        if is_part_number:
            part_numbers_sum += number

print("Part 1: ", part_numbers_sum)

# Part 2
number_coords = []
for y, line in enumerate(schema):
    for match in re.finditer(r'\d+', line):
        number = int(line[match.start(): match.end()])
        number_length = match.end() - match.start()
        coords = [(x, y) for x in range(match.start(), match.end())]
        number_coords.append((number, coords))

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

gear_ratio_sum = 0
for y, line in enumerate(schema):
    for x, c in enumerate(line):
        if c != '*':
            continue
        
        adjacent_nums = []

        gear_coords = (x, y)
        gear_surrounding_coords=[(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x + 1, y), (x-1, y+1), (x, y+1), (x + 1, y+1)]
        gear_numbers = []
        for number in number_coords:
            coords = number[1]
            number = number[0]
            if len(intersection(gear_surrounding_coords, coords)):
                adjacent_nums.append(number)

        if len(adjacent_nums) == 2:
            gear_ratio_sum += adjacent_nums[0] * adjacent_nums[1]

print("Part 2: ", gear_ratio_sum)


