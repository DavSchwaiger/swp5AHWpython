import random

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
colors = ["\u2660", "\u2665", "\u2663", "\u2666"]

def show_cards(deck):
    hand = []
    for card in deck[:5]:
        color = colors[card % 4]
        value = values[card % 13]
        hand.append(f"{value}{color}")
    return hand

def shuffle_deck():
    deck = list(range(52))
    random.shuffle(deck)
    return deck

def pick_and_show_cards():
    deck = shuffle_deck()
    hand = show_cards(deck)
    print(", ".join(hand))
    return deck

def pair(deck):
    value_count = [0] * 13
    for card in deck[:5]:
        value_count[card % 13] += 1

    for count in value_count:
        if count == 2:
            return True
    return False

def three_of_a_kind(deck):
    value_count = [0] * 13
    for card in deck[:5]:
        value_count[card % 13] += 1

    for count in value_count:
        if count == 3:
            return True
    return False

def four_of_a_kind(deck):
    value_count = [0] * 13
    for card in deck[:5]:
        value_count[card % 13] += 1

    for count in value_count:
        if count == 4:
            return True
    return False

def full_house(deck):
    value_count = [0] * 13
    for card in deck[:5]:
        value_count[card % 13] += 1

        if three_of_a_kind(deck) and pair(deck):
            return True
    return False

def flush(deck):
    value_count = [0] * 4
    for card in deck[:5]:
        value_count[card % 4] += 1

    for count in value_count:
        if count == 5:
            return True
    return False

def straight(deck):
    value_count = [0] * 13
    for card in deck[:5]:
        value_count[card % 13] += 1

        sorted_card_value = sorted([card % 13 for card in deck[:5]])

        for i in range(4):
            if sorted_card_value[i] + 1 != sorted_card_value[i + 1]:
                return False
        return True

def straight_flush(deck):
    value_count = [0] * 13
    for card in deck[:5]:
        value_count[card % 13] += 1

        if flush(deck) and straight(deck):
            return True
    return False
def royal_flush(deck):

    if not flush(deck):
        return False

    value_count = [0] * 13

    check_royals = (value_count[8] > 0 and
                    value_count[9] > 0 and
                    value_count[10] > 0 and
                    value_count[11] > 0 and
                    value_count[12] > 0
                    )

    for card in deck[:5]:
        value_count[card % 13] += 1

    if check_royals:
            return True
    return False

def check_combinations(deck):
    if pair(deck):
        print("Pair")
    if three_of_a_kind(deck):
        print("Three of a kind")
    if full_house(deck):
        print("Full House")
    if four_of_a_kind(deck):
        print("Four of a kind")
    if flush(deck):
        print("Flush")
    if straight(deck):
        print("Straight")
    if straight_flush(deck):
        print("Straight Flush")
    if royal_flush(deck):
        print("Royal Flush")

if __name__ == "__main__":
    for _ in range(10000):
        deck = pick_and_show_cards()
        check_combinations(deck)
