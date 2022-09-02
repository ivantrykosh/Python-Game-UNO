import random
import Deck

number_of_players = 4  # The number of player in the game
number_of_cards = 7  # The number of cards in each player

class Player:
    """
    A class used to represent a Player

    Attributes
    ----------
    __cards : list
        the list of the player`s cards (default empty)
    __name : str
        the name of the player

    Methods
    -------
    add_card(value)
        Adds the card to the list of the player`s cards
    remove_card(index)
        Removes the [index]th card from the list of the player`s cards
    get_cards()
        Returns the list of the player`s cards
    get_name()
        Returns the name of the player
    """

    def __init__(self, name):
        """
        The constructor of the class

        Parameters
        ----------
        name : str
            The name of the player
        """
        self.__cards = []
        self.__name = name

    def add_card(self, value):
        """
        The method for adding cards to the list of the player`s cards

        Parameters
        ----------
        value : list
            The card what needs to add
        """
        self.__cards += [value]
        return

    def remove_card(self, index):
        """
        The method for removing cards from the list of the player`s cards

        Parameters
        ----------
        index : int
            The index of the card to be deleted
        """
        self.__cards.pop(index)
        return

    def get_cards(self):
        """
        The method for getting the list of cards
        """
        return self.__cards

    def get_name(self):
        """
        The method for getting the player`s name
        """
        return self.__name


class Game:
    """Game"""
    def __init__(self):
        self.__Players = [Player("Player " + str(i+1)) for i in range(number_of_players)]
        self.__Current_Player = self.__Players[0]
        self.__Deck, self.__Current_Card = self.__set_Deck()
        self.__Garbage = []
        self.__Winner = None
        self.__flag_for_skip = True if (self.__Current_Card[1] != 'skip' and self.__Current_Card[1] != '+2') else False
        self.__clockwise = True if self.__Current_Card[1] != 'reverse' else False
        return

    def get_players(self):
        return self.__Players

    def get_Winner(self):
        return self.__Winner

    def get_Current_Card(self):
        return self.__Current_Card

    def get_Deck(self):
        return self.__Deck

    def get_clockwise(self):
        return self.__clockwise

    def give_cards(self, numberw):
        cards = self.__Deck[0:number]
        self.__Deck = self.__Deck[number:]
        return cards

    def move_to_Garbage(self, card):
        self.__Garbage += [card]
        return

    def shuffle_Deck(self):
        self.__Deck = self.__Garbage.copy()
        self.__Garbage.clear()
        return

    def set_Current_Player(self, pos):
        self.__Current_Player = self.__Players[pos]
        return

    def __set_Deck(self):
        deck = Deck.Cards.copy()
        random.shuffle(deck)
        for i in range(0, number_of_players * number_of_cards, number_of_players):
            for j in range(number_of_players):
                self.__Players[j].add_card(deck[0])
                deck.pop(0)
        return deck[1:], deck[0]

    def make_a_move(self):
        flag = True
        temp_flag_for_skip = self.__flag_for_skip
        for i in range(len(self.__Current_Player.get_cards())):
            if (self.__flag_for_skip and self.__check_cards(self.__Current_Card, self.__Current_Player.get_cards()[i])):
                self.__Garbage += [self.__Current_Card]
                if (self.__Garbage[-1][1] == 'wild' or self.__Garbage[-1][1] == '+4'):
                    self.__Garbage[-1][0] = 'black'
                self.__Current_Card = self.__Current_Player.get_cards()[i]
                self.__Current_Player.remove_card(i)
                if (self.__Current_Card[1] == 'wild' or self.__Current_Card[1] == '+4'):
                    self.__Current_Card[0] = ['red', 'blue', 'yellow', 'green'][random.randint(0, 3)]
                temp_flag_for_skip = True if (self.__Current_Card[1] != 'skip' and self.__Current_Card[1] != '+2') else False
                if self.__Current_Card[1] == 'reverse':
                    self.__clockwise = not self.__clockwise
                flag = False
                break
            elif (not (self.__flag_for_skip)):
                if (self.__Current_Player.get_cards()[i][1] == 'skip' or self.__Current_Player.get_cards()[i][1] == '+2'):
                    self.__Garbage += [self.__Current_Card]
                    self.__Current_Card = self.__Current_Player.get_cards()[i]
                    self.__Current_Player.remove_card(i)
                    temp_flag_for_skip = False
                    flag = False
                    break
                else:
                    temp_flag_for_skip = True
                    flag = False
        self.__flag_for_skip = temp_flag_for_skip
        if (len(self.__Deck) == 0):
            self.shuffle_Deck()
        if (flag):
            self.__Current_Player.add_card(self.__Deck[0])
            self.__Deck.pop(0)
            if (self.__check_cards(self.__Current_Card, self.__Current_Player.get_cards()[-1])):
                self.__Garbage += self.__Current_Card
                self.__Current_Card = self.__Current_Player.get_cards()[-1]
                self.__Current_Player.remove_card(-1)
                if (self.__Current_Card[1] == 'wild' or self.__Current_Card[1] == '+4'):
                    self.__Current_Card[0] = ['red', 'blue', 'yellow', 'green'][random.randint(0, 3)]
                if self.__Current_Card[1] == 'reverse':
                    self.__clockwise = not self.__clockwise
        if (len(self.__Current_Player.get_cards()) == 0):
            self.__Winner = self.__Current_Player
        if (len(self.__Deck) == 0):
            self.shuffle_Deck()
        return

    def shuffle_Deck(self):
        self.__Deck = self.__Garbage.copy()
        random.shuffle(self.__Deck)
        self.__Garbage = []
        return

    def __check_cards(self, Current_Card, Player_Card):
        flag = False
        if (Current_Card[0] == Player_Card[0] or Current_Card[1] == Player_Card[1] or Player_Card[0] == 'black'):
            flag = True
        return flag

    def pop_card(self, index):
        self.__Deck.pop(index)
        return

Game = Game()

for i in Game.get_players():
    print(f'{i.get_name()}:', end=' ')
    for j in i.get_cards():
        print(f'{j[0]} - {j[1]}', end='; ')
    print("")

print('====================================================================================================')

current_number = 0
while Game.get_Winner() == None:
    current_number %= 4
    if (Game.get_Current_Card()[1] == '+2'):
        for i in range(2):
            if (len(Game.get_Deck()) == 0):
                Game.shuffle_Deck()
            Game.get_players()[current_number].add_card(Game.get_Deck()[0])
            Game.pop_card(0)
    elif (Game.get_Current_Card()[1] == '+4'):
        for i in range(4):
            if (len(Game.get_Deck()) == 0):
                Game.shuffle_Deck()
            Game.get_players()[current_number].add_card(Game.get_Deck()[0])
            Game.pop_card(0)
    print(f'Current card: {Game.get_Current_Card()[0]} - {Game.get_Current_Card()[1]}')
    for i in Game.get_players():
        print(f'{i.get_name()}:', end=' ')
        for j in i.get_cards():
            print(f'{j[0]} - {j[1]}', end='; ')
        print("")
    Game.set_Current_Player(current_number)
    Game.make_a_move()
    if Game.get_clockwise():
        current_number += 1
    else:
        current_number -= 1

    print('====================================================================================================')

print(f'Winner: {Game.get_Winner().get_name()}')