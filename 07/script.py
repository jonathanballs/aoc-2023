import itertools

puzzle_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split('\n')

puzzle_input = open('./input').read().strip().split('\n')

cards = [*"23456789TJQKA"]

# five of a kind => 6 points
# 4 of a kind -> 5 points
# Full house -> 4 points
# 3 of a kind -> 3 points
# 2 pair -> 2 points
# 1 pair -> 1 point
# high card -> 0 points

def char_frequencies(string):
    freq = {}
    for c in string:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    return freq

def score_hand(hand):
    freq = char_frequencies(hand)
    sorted_frequences = sorted(freq.values())

    # 4 - 5 of a kind
    if sorted_frequences[-1] >= 4:
        return sorted_frequences[-1] + 1

    # Full house
    if sorted_frequences[-2:] == [2, 3]:
        return 4

    # 3 of a kind
    if sorted_frequences[-1] == 3:
        return 3

    # 2 pair
    if sorted_frequences[-2:] == [2, 2]:
        return 2

    # 1 pair
    if sorted_frequences[-1] == 2:
        return 1

    return 0

def score_high_card(hand):
    score = 0

    for c in hand:
        c_score = cards.index(c)
        score *= 13
        score += c_score

    return score

def total_score(hand):
    return score_hand(hand) * pow(13, 7) + score_high_card(hand)

scored_hands = [{
    'score': total_score(hand.split()[0]),
    'hand': hand,
    'bid': int(hand.split()[1])
    } for hand in puzzle_input]

def calculate_total_winnings(scored_hands):
    sorted_hands = sorted(scored_hands, key=lambda d: d['score'])

    total_winnings = 0
    for i, d in enumerate(sorted_hands):
        total_winnings += (i+1) * d['bid']

    return total_winnings

print("Part 1:", calculate_total_winnings(scored_hands))

def score_high_card_joker(hand):
    score = 0
    joker_cards = [*"J23456789TQKA"]

    for c in hand:
        c_score = joker_cards.index(c)
        score *= 13
        score += c_score

    return score

def total_score_joker(hand):
    short_cards = hand.replace('J', '')
    numMissingJacks = 5 - len(short_cards)

    # Just use normal scoring
    if numMissingJacks == 0:
        return score_hand(hand) * pow(13, 7) + score_high_card_joker(hand)
    
    max_score = 0

    for combo in itertools.product("AKQT98765432", repeat=numMissingJacks):
        full_hand = short_cards + "".join(combo)
        full_score = score_hand(full_hand)
        if (full_score > max_score):
            max_score = full_score

    return max_score * pow(13, 7) + score_high_card_joker(hand)

scored_hands = [{
    'score': total_score_joker(hand.split()[0]),
    'hand': hand,
    'bid': int(hand.split()[1])
    } for hand in puzzle_input]

print("Part 2:", calculate_total_winnings(scored_hands))

