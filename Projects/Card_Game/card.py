'''
Name: Card Class
Author: Wesley Wang
Date: 11/16/2018
'''
class Card:
    '''
    A card contains a suit (Clubs[1] < Diamond[2] < Heart[3] < Spade[4])
    and a rank (number 2 to 10, J[11], Q[12], K[13], and A[14] as the highest)
    '''
    suits = ["Club", "Diamond", "Heart", "Spade"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    rank_names = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                  "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    def __init__(self, suit, rank):
        suit = suit.capitalize()
        if str(rank).isdigit():
            rank = int(rank)
        else:
            rank = rank.capitalize()
        if rank in self.rank_names:
            rank = self.ranks[self.rank_names.index(rank)]
        if suit not in self.suits or rank not in self.ranks:
            raise ValueError("Not an actual card")
        self.suit = suit
        self.rank = rank
    @property
    def suit(self):
        '''
        Return card's suit in value based on hierarchy (A>K>Q>J...)
        '''
        return self._suit
    @suit.setter
    def suit(self, suit):
        suits = self.suits
        self._suit = suits.index(suit) + 1
    @property
    def rank(self):
        '''
        Return card's rank in value, including J, Q, K, A
        '''
        return self._rank
    @rank.setter
    def rank(self, rank):
        ranks = self.ranks
        if not isinstance(rank, int):
            self._rank = ranks.index(rank) + 2
        else:
            self._rank = rank
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    def __ne__(self, other):
        return not (self.rank == other.rank and self.suit == other.suit)
    def __gt__(self, other):
        if self.rank == other.rank:
            return self.suit > other.suit
        return self.rank > other.rank
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank < other.rank
    def __ge__(self, other):
        return self.suit >= other.suit and self.rank >= other.rank
    def __le__(self, other):
        return not (self.suit >= other.suit and self.rank >= other.rank)
    def __str__(self):
        return self.rank_names[self._rank-2] + " of " + self.suits[self._suit-1] + "s"
    def __repr__(self):
        return self.rank_names[self._rank-2] + " of " + self.suits[self._suit-1] + "s"
