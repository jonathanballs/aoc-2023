import math

race_input = """Time:      7  15   30
# Distance:  9  40  200"""
race_input = open('./input', 'r+').read()

race_input_lines = race_input.split('\n')

times = [int(n) for n in race_input_lines[0].split()[1:]]
distances = [int(n) for n in race_input_lines[1].split()[1:]]

def calculate_race_distance(button_time, race_time):
    return (race_time - button_time) * button_time


all_num_win_chances = []
for race in zip(times, distances):
    num_win_chances = 0

    race_time = race[0]
    distance = race[1]

    for button_time in range(1, race_time + 1):
        race_distance = calculate_race_distance(button_time, race_time)
        if race_distance > distance:
            num_win_chances += 1

    all_num_win_chances.append(num_win_chances)


product = 1
for i in all_num_win_chances:
    product *= i

print("Part 1: ", product)

max_time = int(''.join(race_input_lines[0].split()[1:]))
distance = int(''.join(race_input_lines[1].split()[1:]))

num_win_chances = 0
for button_time in range(1, max_time + 1):
    race_distance = calculate_race_distance(button_time, max_time)

    if race_distance > distance:
        num_win_chances += 1
    elif num_win_chances > 0:
        break

print("Part 2: ", num_win_chances)
