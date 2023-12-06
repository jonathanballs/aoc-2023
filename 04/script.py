import re

# card_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')
card_input = open('input', 'r+')

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Parse the cards
cards = []
for line in card_input:
    nums = line.split(':')[1].strip().split(' | ')

    winners = re.split(r' +', nums[0])
    players = re.split(r' +', nums[1])
    card = [winners, players]

    cards.append(card)

points_sum = 0

for card in cards:
    num_correct = len(intersection(card[1], card[0]))
    card_points = pow(2, num_correct - 1) if num_correct > 0 else 0
    points_sum += card_points

print("Part 1: ", points_sum)

card_copies = [len(intersection(card[1], card[0])) for card in cards]
num_cards = [1] * len(card_copies)

for i, card_duplications in enumerate(card_copies):
    for _ in range(num_cards[i]):
        for j in range(i, i + card_duplications):
            num_cards[j+1] += 1

print("Part 2: ", sum(num_cards))

