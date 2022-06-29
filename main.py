import random


class Player:
    def __init__(self):
        self.__cards = []

    def add_card(self, value):
        self.__cards += [value]

    def get_cards(self):
        return self.__cards


Cards = [["red", "0"], ["red", "1"], ["red", "1"], ["red", "2"], ["red", "2"], ["red", "3"], ["red", "3"], ["red", "4"],
         ["red", "4"], ["red", "5"], ["red", "5"], ["red", "6"], ["red", "6"], ["red", "7"], ["red", "7"], ["red", "8"],
         ["red", "8"], ["red", "9"], ["red", "9"],
         ["blue", "0"], ["blue", "1"], ["blue", "1"], ["blue", "2"], ["blue", "2"], ["blue", "3"], ["blue", "3"],
         ["blue", "4"], ["blue", "4"], ["blue", "5"], ["blue", "5"], ["blue", "6"], ["blue", "6"], ["blue", "7"],
         ["blue", "7"], ["blue", "8"], ["blue", "8"], ["blue", "9"], ["blue", "9"],
         ["yellow", "0"], ["yellow", "1"], ["yellow", "1"], ["yellow", "2"], ["yellow", "2"], ["yellow", "3"],
         ["yellow", "3"], ["yellow", "4"], ["yellow", "4"], ["yellow", "5"], ["yellow", "5"], ["yellow", "6"],
         ["yellow", "6"], ["yellow", "7"], ["yellow", "7"], ["yellow", "8"], ["yellow", "8"], ["yellow", "9"],
         ["yellow", "9"],
         ["green", "0"], ["green", "1"], ["green", "1"], ["green", "2"], ["green", "2"], ["green", "3"], ["green", "3"],
         ["green", "4"], ["green", "4"], ["green", "5"], ["green", "5"], ["green", "6"], ["green", "6"], ["green", "7"],
         ["green", "7"], ["green", "8"], ["green", "8"], ["green", "9"], ["green", "9"],
         ["red", "reverse"], ["red", "reverse"], ["red", "block"], ["red", "block"], ["red", "block+2"],
         ["red", "block+2"],
         ["blue", "reverse"], ["blue", "reverse"], ["blue", "block"], ["blue", "block"], ["blue", "block+2"],
         ["blue", "block+2"],
         ["yellow", "reverse"], ["yellow", "reverse"], ["yellow", "block"], ["yellow", "block"], ["yellow", "block+2"],
         ["yellow", "block+2"],
         ["green", "reverse"], ["green", "reverse"], ["green", "block"], ["green", "block"], ["green", "block+2"],
         ["green", "block+2"],
         ["black", "ch_color"], ["black", "ch_color"], ["black", "ch_color"], ["black", "ch_color"],
         ["black", "ch_color+4"], ["black", "ch_color+4"], ["black", "ch_color+4"], ["black", "ch_color+4"]]

random.shuffle(Cards)

number_of_players = 4
number_of_cards = 7
players = [Player() for i in range(number_of_players)]
k = 0
for i in range(0, number_of_players * number_of_cards, number_of_players):
    for j in range(number_of_players):
        players[j].add_card(Cards[k])
        k += 1
for i in players:
    print(i.get_cards())
