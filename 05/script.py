# map_inputs = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""
map_inputs = open('input').read()

map_inputs = map_inputs.split('\n\n')

seeds = [int(n) for n in map_inputs[0].split(':')[1].strip().split(' ')]
map_inputs = map_inputs[1:]

def parse_map_inputs(map_input):
    map_input = map_input.strip()
    ret = []
    for line in map_input.split('\n')[1:]:
        ret.append([int(n) for n in line.split(' ')])

    return ret

maps = [parse_map_inputs(map_input) for map_input in map_inputs]

def map_value(mapping, value):
    value_offset = value - mapping[1]
    if value_offset < 0 or value_offset >= mapping[2]:
        return False

    return mapping[0] + value_offset

def get_seed_location(seed, maps):
    current_seed = seed
    for map in maps:
        for mapping in map:
            mapping_res = map_value(mapping, current_seed)
            if mapping_res is not False:
                current_seed = mapping_res
                break
    return current_seed

seed_locations = [get_seed_location(seed, maps) for seed in seeds]
print("Part 1: ", min(seed_locations))

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# This function is passed a single mapping and a single seed range. It returns
# [[...unmapped_seed_ranges], [mapped_seed_range]]
def single_map_seed_range(mapping, seed_range):
    mapping_start = mapping[1]
    mapping_end = mapping[1] + mapping[2] - 1

    seed_range_start = seed_range[0]
    seed_range_end = seed_range[0] + seed_range[1] - 1

    overlap_start = max(mapping_start, seed_range_start)
    overlap_end = min(mapping_end, seed_range_end)

    if overlap_start > overlap_end:
        # Return all as unmapped since we can't do anything
        return [[seed_range], []]

    unmapped_start = []
    unmapped_end = []

    if seed_range_start < overlap_start:
        unmapped_start = [[seed_range_start, overlap_start - seed_range_start]]

    if seed_range_end > overlap_end:
        unmapped_end = [[overlap_end + 1, seed_range_end - overlap_end]]

    mapping_offset = mapping[0] - mapping[1]
    mapped_range = [overlap_start + mapping_offset, overlap_end - overlap_start + 1]

    return [unmapped_end + unmapped_start, [mapped_range]]

# This function is passed a list of mappings and a single seed range. It returns
# the seed ranges after they have been passed through the mapping
def map_seed_range(map, seed_range):
    unmapped_ranges = [seed_range]
    mapped_ranges = []

    for mapping in map:
        new_unmapped_ranges = []
        new_mapped_ranges = []
        # Pass all unmapped ranges through the range
        for unmapped_range in unmapped_ranges:
            resp = single_map_seed_range(mapping, unmapped_range)
            new_unmapped_ranges += resp[0]
            new_mapped_ranges += resp[1]

        mapped_ranges += new_mapped_ranges
        unmapped_ranges = new_unmapped_ranges

    return unmapped_ranges + mapped_ranges

def get_seeds_location(maps, seed_ranges):
    for map in maps:
        new_seed_ranges = []
        for seed_range in seed_ranges:
            new_seed_ranges += map_seed_range(map, seed_range)
        seed_ranges = new_seed_ranges
    return seed_ranges

seed_pairs = list(chunks(seeds, 2))
location_ranges = get_seeds_location(maps, seed_pairs)
location_mins = [r[0] for r in location_ranges]
print("Part 2: ", min(location_mins))

