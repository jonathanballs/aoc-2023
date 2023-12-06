#!/bin/python

def parse_handful_totals(line):
    line = line.split(', ')

    ball_totals = dict()

    for pair in line:
        pair = pair.split(' ')
        val = pair[0]
        key = pair[1]

        if key not in ball_totals:
            ball_totals[key] = 0

        ball_totals[key] += int(val)

    return ball_totals

def merge_handfuls(handfuls):
    ball_totals = dict()
    for handful in handfuls:
        for key in handful.keys():
            if key not in ball_totals:
                ball_totals[key] = handful[key]
            elif ball_totals[key] < handful[key]:
                ball_totals[key] = handful[key]

    return ball_totals

def parse_line_totals(line):
    handfuls = line.strip().split(':')[1].strip().split('; ')
    handful_totals = [parse_handful_totals(handful) for handful in handfuls]
    ball_totals = merge_handfuls(handful_totals)

    return ball_totals

def is_subset_of_balls(ball_maxes, ball_totals):
    for key in ball_totals:
        if ball_totals[key] > ball_maxes[key]:
            return False
    return True


possible_games = []
for line in open("./input", "r+"):
    game_number = int(line.split(':')[0].split(' ')[1])
    ball_totals = parse_line_totals(line)
    ball_maxes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    if is_subset_of_balls(ball_maxes, ball_totals):
        possible_games.append(game_number)

print("Part 1: ", sum(possible_games))

def calculate_power(ball_totals):
    return ball_totals.get('green', 0) * ball_totals.get('red', 0) * ball_totals.get('blue', 0)

power_sum = 0
for line in open("./input", "r+"):
    game_number = int(line.split(':')[0].split(' ')[1])
    ball_totals = parse_line_totals(line)
    power_sum += calculate_power(ball_totals)

print("Part 2: ", power_sum)
