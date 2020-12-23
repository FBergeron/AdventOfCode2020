from itertools import combinations
import re
import sys

input_data_filename = "player_cards.txt"
# input_data_filename = "player_cards_short.txt"


def is_game_over():
    for cards in player_cards:
        if len(cards) == 0:
            return True
    return False


player_cards = []
cards = None
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        match = re.search("Player (\d+):", line)
        if match:
            if cards is not None and player_index is not None:
                player_cards.append(cards)

            player_index = match.group(1)
            cards = []
            continue
        
        match = re.search("(\d+)", line)
        if match:
            card = int(match.group(1))
            cards.append(card)
    if cards is not None and player_index is not None:
        player_cards.append(cards)
print(f"player_cards={player_cards}")

round = 0
while not is_game_over():

    top_cards = []
    for index, cards in enumerate(player_cards):
        top_cards.append((index, cards.pop(0)))


    print(f"top_cards={top_cards}") 
    sorted_top_cards = sorted(top_cards, key=lambda pair: pair[1], reverse=True)
    print(f"sorted_top_cards={sorted_top_cards}") 

    winner = sorted_top_cards[0][0]
    print(f"winner={winner}")

    for index, card in sorted_top_cards:
        player_cards[winner].append(card)

    round += 1

print(f"round={round}")
print(f"player_cards={player_cards}")
score = 0
for cards in player_cards:
    if len(cards) == 0:
        continue

    for index, card in enumerate(cards):
        print(f"index={index} card={card}")
        score += (len(cards) - index) * card

print(f"score={score}")

