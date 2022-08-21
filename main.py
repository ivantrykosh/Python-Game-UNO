import random

number_of_players = 4  # The number of player in the game
number_of_cards = 7  # The number of cards in each player

class Player:
    """Player, who plays game UNO"""
    def __init__(self, name):
        self.__cards = []
        self.__name = name

    def add_card(self, value):
        self.__cards += [value]

    def get_cards(self):
        return self.__cards

    def get_name(self):
        return self.__name


class Game:
    """Game"""
    def __init__(self, Players, Deck):
        self.__Players = Players
        self.__Current_Player = Players[0]
        self.__Deck = Deck[1:]
        self.__Garbage = []
        self.__Current_Card = Deck[0]
        self.__Winner = None

    def get_Current_Card(self):
        return self.__Current_Card

    def get_Deck(self):
        return self.__Deck

    def give_cards(self, numberw):
        cards = self.__Deck[0:number]
        self.__Deck = self.__Deck[number:]
        return cards

    def move_to_Garbage(self, card):
        self.__Garbage += [card]

    def shuffle_Deck(self):
        self.__Deck = self.__Garbage.copy()
        self.__Garbage.clear()

    def set_Current_Player(self, pos):
        self.__Current_Player = self.__Players[pos % 4]

''' List of cards '''
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
         ["red", "reverse"], ["red", "reverse"], ["red", "skip"], ["red", "skip"], ["red", "+2"],
         ["red", "+2"],
         ["blue", "reverse"], ["blue", "reverse"], ["blue", "skip"], ["blue", "skip"], ["blue", "+2"],
         ["blue", "+2"],
         ["yellow", "reverse"], ["yellow", "reverse"], ["yellow", "skip"], ["yellow", "skip"], ["yellow", "+2"],
         ["yellow", "+2"],
         ["green", "reverse"], ["green", "reverse"], ["green", "skip"], ["green", "skip"], ["green", "+2"],
         ["green", "+2"],
         ["black", "wild"], ["black", "wild"], ["black", "wild"], ["black", "wild"],
         ["black", "+4"], ["black", "+4"], ["black", "+4"], ["black", "+4"]]

random.shuffle(Cards)
Deck = Cards.copy()

players = [Player("Player " + str(i+1)) for i in range(number_of_players)]
k = 0
for i in range(0, number_of_players * number_of_cards, number_of_players):
    for j in range(number_of_players):
        players[j].add_card(Cards[k])
        Deck.pop(0)
        k += 1
for i in players:
    print(f'{i.get_name()}:', end=' ')
    for j in i.get_cards():
        print(f'{j[0]} - {j[1]}', end='; ')
    print("")
Game = Game(players, Deck)

print('====================================================================================================')
