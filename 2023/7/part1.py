from collections import defaultdict
import numpy as np


def run(data):
    result = 0
    hand_types = defaultdict(list, {})
    bids = {hand: int(bid) for hand, bid in data}
    score = []
    card_strengths = list("23456789TJQKA")
    for hand, bid in data:
        counts = {card: hand.count(card) for card in hand}
        count_k = defaultdict(list, {})
        for card, count in counts.items():
            count_k[count].append(card)
        if 5 in count_k:
            hand_types["5oak"].append(hand)
        elif 4 in count_k:
            hand_types["4oak"].append(hand)
        elif 3 in count_k and 2 in count_k:
            hand_types["fh"].append(hand)
        elif 3 in count_k:
            hand_types["3oak"].append(hand)
        elif 2 in count_k and len(count_k[2]) == 2:
            hand_types["2p"].append(hand)
        elif 2 in count_k:
            hand_types["1p"].append(hand)
        else:
            hand_types["hc"].append(hand)

    for type in ["5oak", "4oak", "fh", "3oak", "2p", "1p", "hc"]:
        if type in hand_types:
            if len(hand_types[type]) > 1:
                order = sorted(hand_types[type], key=lambda word: [card_strengths.index(c) for c in word], reverse=True)
                score += order
            else:
                score += hand_types[type]
    score.reverse()
    winnings = [(i+1)*bids[hand] for i, hand in enumerate(score)]



    return np.sum(winnings)
